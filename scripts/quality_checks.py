#!/usr/bin/env python3
"""Content-bound substantive quality assessments; never automatic attestation."""
import argparse
from collections import Counter
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import urlsplit
try:
    from fact_checks import body_bytes, content_hash, timestamp, iso, unique_object, HIGH_RISK
except ModuleNotFoundError:
    from scripts.fact_checks import body_bytes, content_hash, timestamp, iso, unique_object, HIGH_RISK
ROOT = Path(__file__).resolve().parents[1]
DIMENSIONS = ("usefulness", "substance", "coherence", "cross_page_consistency", "reasonable_claims", "usability")
METHOD = "substantive-quality-review-v1"
UTC = timezone.utc


def meaningful(value):
    return isinstance(value, str) and len(value.strip()) >= 24 and len(value.split()) >= 4


def safe_path(value):
    return (isinstance(value, str) and bool(value) and "\\" not in value
            and not re.search(r"[\x00-\x1f:]", value) and not PurePosixPath(value).is_absolute()
            and all(p not in ("", ".", "..") for p in value.split("/")))


def public_paths(root):
    docs = root / "docs"
    if not docs.is_dir():
        raise ValueError("missing public docs directory")
    paths = {}
    for path in sorted(docs.rglob("*.md")):
        relative = path.relative_to(docs)
        if "overrides" in relative.parts:
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(docs.resolve()):
            raise ValueError("public page escapes docs: " + relative.as_posix())
        paths[relative.as_posix()] = path
    return paths


def load_reviews(path):
    if not path.exists():
        return {}, False
    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    if (not isinstance(data, dict) or set(data) != {"version", "reviews"}
            or type(data["version"]) is not int or data["version"] != 1 or not isinstance(data["reviews"], dict)):
        raise ValueError("expected {version: 1, reviews: {docs-relative-path: [append-only assessments]}}")
    return data["reviews"], True


def validate_assessment(record, now, root=None, paths=None):
    errors = []
    required = {"id", "status", "assessed_at", "reviewer", "method", "content_sha256", "report_ref", "dimensions",
                "source_checks", "cross_page_comparisons", "next_review_at", "disposition", "retry_at", "reason"}
    if not isinstance(record, dict):
        return ["assessment must be an object"]
    if not required <= set(record) or set(record) - required - {"correction_card"}:
        errors.append("assessment fields must match documented schema")
    if not isinstance(record.get("id"), str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{2,127}", record["id"]):
        errors.append("id must be a stable unique assessment identifier")
    status = record.get("status")
    if status not in ("pass", "needs_revision", "aborted"):
        errors.append("status must be pass, needs_revision or aborted")
    if not isinstance(record.get("reviewer"), str) or not record["reviewer"].strip():
        errors.append("reviewer must name actual reviewer")
    if record.get("method") != METHOD:
        errors.append("method must be " + METHOD)
    if not isinstance(record.get("content_sha256"), str) or not re.fullmatch(r"[a-f0-9]{64}", record["content_sha256"]):
        errors.append("content_sha256 must be lowercase SHA-256")
    ref = record.get("report_ref")
    if not safe_path(ref) or not ref.startswith("docs-internal/") or not ref.endswith(".md"):
        errors.append("report_ref must name a repository-relative docs-internal Markdown report")
    elif root is not None:
        report = root / ref
        if not report.is_file() or not report.resolve().is_relative_to(root.resolve()):
            errors.append("report_ref must resolve to an existing local report")
        elif not meaningful(report.read_text(encoding="utf-8")):
            errors.append("report_ref report must contain substantive findings")
    dates = {}
    for field in ("assessed_at", "next_review_at"):
        try:
            dates[field] = timestamp(record.get(field))
        except (ValueError, TypeError) as exc:
            errors.append(field + ": " + str(exc))
    assessed = dates.get("assessed_at", now)
    if assessed > now:
        errors.append("assessed_at cannot be in the future")
    if dates.get("next_review_at", assessed) <= assessed:
        errors.append("next_review_at must follow assessed_at")
    disposition = record.get("disposition")
    if status == "pass":
        if disposition != "rolling" or record.get("retry_at") is not None or record.get("reason") is not None:
            errors.append("pass requires rolling disposition and null retry_at/reason")
    else:
        if disposition not in ("retry", "park") or not meaningful(record.get("reason")):
            errors.append("non-pass requires explicit retry/park and meaningful reason")
        if disposition == "park" and record.get("retry_at") is not None:
            errors.append("park requires null retry_at")
        if disposition == "retry":
            try:
                retry = timestamp(record.get("retry_at"))
                if not assessed < retry <= assessed + timedelta(days=30):
                    errors.append("retry_at must follow assessment by at most 30 days")
            except (ValueError, TypeError) as exc:
                errors.append("retry_at: " + str(exc))
    if "correction_card" in record and (not isinstance(record["correction_card"], str) or not record["correction_card"].strip()):
        errors.append("correction_card must name the existing queue card")
    dims = record.get("dimensions")
    if status == "aborted":
        if dims != {}:
            errors.append("aborted attempt must have empty dimensions")
    elif not isinstance(dims, dict) or set(dims) != set(DIMENSIONS):
        errors.append("completed assessment requires all six named dimensions")
    else:
        for name, finding in dims.items():
            if (not isinstance(finding, dict) or set(finding) != {"status", "rationale"}
                    or finding.get("status") not in ("pass", "needs_revision") or not meaningful(finding.get("rationale"))):
                errors.append(name + ": require status and meaningful page-specific rationale")
        outcomes = [f.get("status") for f in dims.values() if isinstance(f, dict)]
        if status == "pass" and any(s != "pass" for s in outcomes):
            errors.append("overall pass requires all dimensions fit for publication")
        if status == "needs_revision" and "needs_revision" not in outcomes:
            errors.append("needs_revision must identify a failing dimension")
    for field in ("source_checks", "cross_page_comparisons"):
        evidence = record.get(field)
        if not isinstance(evidence, dict) or set(evidence) != {"applicable", "rationale", "items"}:
            errors.append(field + ": require applicable, rationale, items")
            continue
        if type(evidence["applicable"]) is not bool or not meaningful(evidence["rationale"]) or not isinstance(evidence["items"], list):
            errors.append(field + ": invalid applicability/rationale/items")
            continue
        if evidence["applicable"] != bool(evidence["items"]):
            errors.append(field + ": applicable evidence requires items; nonapplicable requires none")
        for item in evidence["items"]:
            target = "url" if field == "source_checks" else "path"
            if not isinstance(item, dict) or set(item) != {target, "claim", "finding", "checked_at"}:
                errors.append(field + ": invalid evidence item schema")
                continue
            if not meaningful(item["claim"]) or not meaningful(item["finding"]):
                errors.append(field + ": claim and finding must be substantive")
            try:
                checked = timestamp(item["checked_at"])
                if checked > assessed or checked > now:
                    errors.append(field + ": check cannot follow assessment or be in future")
            except (ValueError, TypeError):
                errors.append(field + ": invalid checked_at")
            if target == "url":
                try:
                    url = urlsplit(item[target])
                    if url.scheme not in ("http", "https") or not url.hostname or url.username or url.password or re.search(r"\s", item[target]):
                        raise ValueError()
                except (TypeError, ValueError, AttributeError):
                    errors.append(field + ": invalid public HTTP(S) URL")
            elif not safe_path(item[target]) or (paths is not None and item[target] not in paths):
                errors.append(field + ": comparison must name a published page")
    return errors


def inventory(root, reviews, now):
    root = Path(root)
    paths = public_paths(root)
    errors, rows, ids = [], [], set()
    for key in reviews:
        if not safe_path(key) or key not in paths:
            errors.append(str(key) + ": not a published Markdown page")
    for name, path in paths.items():
        body = body_bytes(path.read_bytes())
        digest = content_hash(path)
        volatile = name.startswith("tools/") or bool(HIGH_RISK.search(name.replace("-", " ") + "\n" + body.decode("utf-8")))
        cadence = 30 if volatile else 90
        history = reviews.get(name, [])
        invalid, valid, previous = [], [], None
        if not isinstance(history, list) or (name in reviews and not history):
            invalid.append("history must be a nonempty append-only assessment list")
            history = []
        for record in history:
            faults = validate_assessment(record, now, root, paths)
            if not faults:
                at = timestamp(record["assessed_at"])
                if previous is not None and at <= previous:
                    faults.append("assessment history must have strictly increasing timestamps")
                previous = at
                if record["id"] in ids:
                    faults.append("assessment id must be globally unique")
                ids.add(record["id"])
            invalid.extend(faults)
            if not faults:
                valid.append(record)
        errors.extend(name + ": " + e for e in invalid)
        latest = valid[-1] if valid else None
        completed = [r for r in valid if r["status"] in ("pass", "needs_revision")]
        first_pass = bool(completed) and not invalid
        at = latest["assessed_at"] if latest else None
        due_at = None
        state, due = "unreviewed", True
        if invalid:
            state = "invalid"
        elif latest:
            due_at = min(timestamp(latest["next_review_at"]), timestamp(at) + timedelta(days=cadence))
            changed = latest["content_sha256"] != digest
            if changed:
                state = "stale"
            elif latest["status"] == "pass":
                state, due = ("overdue", True) if due_at <= now else ("current", False)
            else:
                state = latest["status"]
                due = latest["disposition"] == "retry" and timestamp(latest["retry_at"]) <= now
                due_at = timestamp(latest["retry_at"]) if latest["disposition"] == "retry" else None
        rows.append({"path": name, "risk": "volatile" if volatile else "evergreen", "cadence_days": cadence,
                     "state": state, "due": due, "needs_review": state != "current", "first_pass_completed": first_pass,
                     "assessed_at": at, "due_at": iso(due_at) if due_at else None, "content_sha256": digest,
                     "disposition": latest["disposition"] if latest else None})
    # Untouched pages precede repeated aborts; oldest attempt wins within classes.
    rows.sort(key=lambda r: (not r["due"], r["first_pass_completed"],
                            bool(r["assessed_at"]) if not r["first_pass_completed"] else r["state"] != "stale",
                            r["assessed_at"] or "", r["due_at"] or "", r["path"]))
    return rows, errors


def public_view(root, src, body_hash=None, now=None):
    pending = {"state": "pending", "label": "Quality review pending", "date": None,
               "timestamp": None, "reviewer": None, "method": None}
    try:
        root = Path(root)
        now = timestamp(now) if isinstance(now, str) else now or datetime.now(UTC)
        src = str(src)
        reviews, _ = load_reviews(root / "data/quality-checks.json")
        rows, errors = inventory(root, reviews, now)
        if errors:
            return pending
        row = next((r for r in rows if r["path"] == src), None)
        if row is None or row["state"] not in ("current", "overdue") or (body_hash is not None and body_hash != row["content_sha256"]):
            return pending
        record = reviews[src][-1]
        return {"state": "passed", "label": "Last quality checked on", "date": record["assessed_at"][:10],
                "timestamp": record["assessed_at"], "reviewer": record["reviewer"], "method": record["method"]}
    except (ValueError, OSError, TypeError, KeyError):
        return pending


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inventory", "due", "validate"), nargs="?", default="due")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--data", type=Path)
    parser.add_argument("--now")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args(argv)
    if args.limit < 1:
        parser.error("--limit must be positive")
    try:
        now = timestamp(args.now) if args.now else datetime.now(UTC)
        reviews, present = load_reviews(args.data or args.root / "data/quality-checks.json")
        rows, errors = inventory(args.root, reviews, now)
        phase = "rolling" if all(r["first_pass_completed"] for r in rows) else "bootstrap"
        today = {name for name, history in reviews.items() if isinstance(history, list) and any(
            isinstance(r, dict) and isinstance(r.get("assessed_at"), str) and r["assessed_at"][:10] == iso(now)[:10] for r in history)}
        budget = max(0, 5 - len(today))
        selected = [r for r in rows if r["due"] and r["path"] not in today] if args.command == "due" else rows
        limit = min(args.limit, budget) if args.command == "due" else args.limit
        if errors and args.command == "due":
            selected = []
        report = {"as_of": iso(now), "summary": {"pages": len(rows), "phase": phase,
                  "first_pass_completed": sum(r["first_pass_completed"] for r in rows), "due": sum(r["due"] for r in rows),
                  "states": dict(Counter(r["state"] for r in rows)), "daily_limit": 5, "assessed_today": len(today), "remaining_today": budget,
                  "record_file_present": present, "errors": len(errors), "selected": len(selected), "shown": min(limit, len(selected))},
                  "items": selected[:limit], "errors": errors}
    except (OSError, ValueError, TypeError) as exc:
        errors = [str(exc)]
        report = {"errors": errors}
    print(json.dumps(report, indent=2 if args.json else None))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
