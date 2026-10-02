#!/usr/bin/env python3
"""Read-only Article inventory and evidence-record validation, never fact attestation."""
import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from hooks.metadata import page_type

MEASUREMENT = "patterns/publish/ai-search-optimization/measurement.md"
UTC = timezone.utc
HIGH_RISK = re.compile(r"\b(?:ai|aeo|geo|llm|platform|api|specification|spec|youtube|spotify|apple|linkedin|google|chatgpt|perplexity|schema|rss|hosting|analytics)\b", re.I)


def body_bytes(raw):
    """Strip opening YAML block only; retain exact remaining UTF-8 bytes."""
    raw.decode("utf-8")
    match = re.match(br"\A---\r?\n.*?^---[^\S\r\n]*(?:\r?\n|$)", raw, re.M | re.S)
    if raw.startswith((b"---\n", b"---\r\n")) and not match:
        raise ValueError("unterminated YAML frontmatter")
    return raw[match.end():] if match else raw


def content_hash(path):
    return hashlib.sha256(body_bytes(path.read_bytes())).hexdigest()


def timestamp(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|\+00:00)", value):
        raise ValueError("expected ISO UTC timestamp (YYYY-MM-DDTHH:MM:SSZ)")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def iso(value):
    return value.isoformat().replace("+00:00", "Z")


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_review(review, now):
    errors = []
    if not isinstance(review, dict):
        return ["review must be an object"]
    required = {"checked_at", "reviewer", "method", "content_sha256", "sources", "status", "next_review_at"}
    if set(review) != required:
        errors.append("review fields must be exactly: " + ", ".join(sorted(required)))
    for key in ("reviewer", "method"):
        if not nonempty(review.get(key)):
            errors.append(key + " must name actual reviewer / describe substantive review")
    if review.get("status") not in ("verified", "partial"):
        errors.append("status must be verified or partial")
    if not isinstance(review.get("content_sha256"), str) or not re.fullmatch(r"[a-f0-9]{64}", review["content_sha256"]):
        errors.append("content_sha256 must be lowercase SHA-256")
    dates = {}
    for key in ("checked_at", "next_review_at"):
        try:
            dates[key] = timestamp(review.get(key))
        except ValueError as exc:
            errors.append(f"{key}: {exc}")
    if dates.get("checked_at", now) > now:
        errors.append("checked_at cannot be in the future")
    if len(dates) == 2:
        if dates["next_review_at"] <= dates["checked_at"]:
            errors.append("next_review_at must follow checked_at")
        if review.get("status") == "partial" and dates["next_review_at"] > dates["checked_at"] + timedelta(days=7):
            errors.append("partial retry cannot exceed seven days")
    if review.get("status") == "partial" and not re.search(r"(?:blocked|unresolved)\s*:\s*\S", str(review.get("method", "")), re.I):
        errors.append("partial method must include Blocked: or Unresolved: with reason/claims")
    sources = review.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must contain claim-specific evidence; a wholly blocked attempt is not a review")
        return errors
    for index, source in enumerate(sources):
        prefix = f"sources[{index}]"
        if not isinstance(source, dict) or set(source) != {"url", "claims", "checked_at"}:
            errors.append(prefix + ": expected url, claims, checked_at")
            continue
        try:
            url = urlsplit(source["url"])
            if not (url.scheme in ("https", "http") and url.hostname and not url.username and not url.password and not re.search(r"\s", source["url"])):
                raise ValueError()
        except (ValueError, TypeError, AttributeError):
            errors.append(prefix + ": invalid public HTTP(S) URL")
        claims = source["claims"]
        if not isinstance(claims, list) or not claims or not all(nonempty(c) for c in claims):
            errors.append(prefix + ": claims must list precise supported claims")
        try:
            checked = timestamp(source["checked_at"])
            if checked > now or checked > dates.get("checked_at", now):
                errors.append(prefix + ": source check cannot be future or after review")
        except ValueError as exc:
            errors.append(prefix + ": " + str(exc))
    return errors


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_reviews(path):
    if not path.exists():
        return {}, False
    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if not isinstance(data, dict) or set(data) != {"version", "reviews"} or type(data["version"]) is not int or data["version"] != 1 or not isinstance(data["reviews"], dict):
        raise ValueError("expected {version: 1, reviews: {docs-relative-path: review}}")
    return data["reviews"], True


def inventory(root, reviews, now, high_days=30, evergreen_days=90):
    """docs/ is the approved public mirror; repo source/drafts stay excluded."""
    docs = root / "docs"
    if not docs.is_dir():
        raise ValueError("missing public docs directory")
    rows, errors, paths = [], [], {}
    for path in sorted(docs.rglob("*.md")):
        relative = path.relative_to(docs).as_posix()
        if "overrides" not in path.relative_to(docs).parts and page_type(relative) == "Article":
            paths[relative] = path
    for key in reviews:
        if key not in paths:
            errors.append(f"{key}: target is not a published Article in docs/")
    for relative, path in paths.items():
        body = body_bytes(path.read_bytes())
        digest = hashlib.sha256(body).hexdigest()
        high = relative.startswith("tools/") or bool(HIGH_RISK.search(relative.replace("-", " ") + "\n" + body.decode("utf-8")))
        cadence = high_days if high else evergreen_days
        review = reviews.get(relative)
        reasons, due_at, checked_at = [], None, None
        if relative not in reviews:
            state = "unreviewed"
            reasons.append("no content-bound evidence review record")
        else:
            invalid = validate_review(review, now)
            errors.extend(f"{relative}: {error}" for error in invalid)
            if invalid:
                state = "invalid"
                reasons.extend(invalid)
            else:
                checked_at = review["checked_at"]
                checked = timestamp(checked_at)
                due_at = min(timestamp(review["next_review_at"]), checked + timedelta(days=cadence))
                changed = review["content_sha256"] != digest
                if changed:
                    reasons.append("body hash changed since review")
                if review["status"] == "partial":
                    reasons.append("partial review; unresolved claims remain")
                if due_at <= now:
                    reasons.append("review cadence expired")
                state = "stale" if changed else "partial" if review["status"] == "partial" else "overdue" if due_at <= now else "current"
        # Partial is never fresh, but a short retry window prevents queue starvation.
        due = state != "current" and not (state == "partial" and due_at > now)
        rows.append({"path": relative, "risk": "high" if high else "evergreen", "cadence_days": cadence,
                     "state": state, "needs_review": state != "current", "due": due,
                     "checked_at": checked_at, "due_at": iso(due_at) if due_at else None,
                     "content_sha256": digest, "reasons": reasons})
    rows.sort(key=lambda r: (not r["due"], r["path"] != MEASUREMENT, r["risk"] != "high", r["due_at"] or "", r["path"]))
    return rows, errors


def positive(value):
    number = int(value)
    if not 1 <= number <= 3660:
        raise argparse.ArgumentTypeError("must be between 1 and 3660")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inventory", "due", "validate"), nargs="?", default="due")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--data", type=Path, help="default ROOT/data/fact-checks.json")
    parser.add_argument("--now", help="explicit UTC evaluation time for reproducible reports")
    parser.add_argument("--high-risk-days", type=positive, default=30)
    parser.add_argument("--evergreen-days", type=positive, default=90)
    parser.add_argument("--limit", type=positive, default=20, help="maximum rows; summary remains complete")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        now = timestamp(args.now) if args.now else datetime.now(UTC)
        reviews, present = load_reviews(args.data or args.root / "data/fact-checks.json")
        rows, errors = inventory(args.root, reviews, now, args.high_risk_days, args.evergreen_days)
        selected = [r for r in rows if r["due"]] if args.command == "due" else rows
        summary = {"articles": len(rows), "needs_review": sum(r["needs_review"] for r in rows),
                   "due": sum(r["due"] for r in rows), "states": dict(Counter(r["state"] for r in rows)),
                   "record_file_present": present, "errors": len(errors), "selected": len(selected),
                   "shown": min(len(selected), args.limit)}
        report = {"as_of": iso(now), "summary": summary, "items": selected[:args.limit], "errors": errors}
    except (ValueError, OSError) as exc:
        report = {"errors": [str(exc)]}
        errors = report["errors"]
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(json.dumps(report.get("summary", {}), sort_keys=True))
        for row in report.get("items", []):
            print(f"{row['state']:10} {row['risk']:9} {row['path']} — {'; '.join(row['reasons']) or 'evidence record current'}")
        for error in errors:
            print("ERROR: " + error)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
