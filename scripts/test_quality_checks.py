"""Offline fixtures, never real assessment evidence."""
import contextlib
import copy
from datetime import timedelta
import io
import json
from pathlib import Path
import tempfile
import unittest
from quality_checks import (DIMENSIONS, METHOD, content_hash, inventory, iso, load_reviews,
                            main, public_view, timestamp, validate_assessment)
NOW = timestamp("2040-03-12T12:00:00Z")


class QualityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.page("index.md")
        (self.root / "docs-internal").mkdir()
        (self.root / "docs-internal/report.md").write_text("Fixture only: actual test report with substantive explanatory text.")
        (self.root / "data").mkdir()

    def page(self, path, body="# Guide\n\nPractical evergreen advice.\n"):
        file = self.root / "docs" / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(body)

    def record(self, path="index.md", status="pass", ago=1):
        at = NOW - timedelta(days=ago)
        record = {"id": path.replace("/", "-") + "-" + str(ago), "status": status,
                  "assessed_at": iso(at), "reviewer": "Fixture reviewer only", "method": METHOD,
                  "content_sha256": content_hash(self.root / "docs" / path), "report_ref": "docs-internal/report.md",
                  "dimensions": {d: {"status": "pass", "rationale": "Fixture finding explaining specific page fitness for " + d} for d in DIMENSIONS},
                  "source_checks": {"applicable": False, "rationale": "Pure guidance fixture makes no material externally verifiable assertions.", "items": []},
                  "cross_page_comparisons": {"applicable": False, "rationale": "Standalone test fixture has no relevant neighboring guidance pages.", "items": []},
                  "next_review_at": iso(at + timedelta(days=90)), "disposition": "rolling", "retry_at": None, "reason": None}
        if status != "pass":
            record.update(disposition="park", reason="Fixture correction requires exact human approval before body changes.")
            if status == "aborted":
                record["dimensions"] = {}
            else:
                record["dimensions"]["substance"]["status"] = "needs_revision"
        return record

    def save(self, reviews):
        (self.root / "data/quality-checks.json").write_text(json.dumps({"version": 1, "reviews": reviews}))

    def cli(self, command="due", now=NOW, extra=None):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = main([command, "--root", str(self.root), "--now", iso(now), "--json"] + (extra or []))
        return code, json.loads(out.getvalue())

    def test_empty_bootstrap_homepage_and_no_fact_uplift(self):
        (self.root / "data/fact-checks.json").write_text('{"version":1,"reviews":{"index.md":{"status":"verified"}}}')
        code, report = self.cli()
        self.assertEqual(code, 0)
        self.assertEqual(report["summary"]["phase"], "bootstrap")
        self.assertEqual(report["items"][0]["path"], "index.md")
        self.assertIsNone(public_view(self.root, "index.md", now=NOW)["date"])

    def test_needs_revision_completes_first_pass_and_rolling(self):
        self.save({"index.md": [self.record(status="needs_revision")]})
        code, report = self.cli()
        self.assertEqual(code, 0)
        self.assertEqual(report["summary"]["phase"], "rolling")
        self.assertEqual(report["items"], [])
        self.assertEqual(public_view(self.root, "index.md", now=NOW)["state"], "pending")

    def test_aborted_not_first_pass_and_untouched_first(self):
        self.page("z.md")
        aborted = self.record(status="aborted", ago=10)
        aborted.update(disposition="retry", retry_at=iso(NOW - timedelta(days=1)))
        rows, errors = inventory(self.root, {"index.md": [aborted]}, NOW)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["path"], "z.md")
        self.assertFalse(rows[1]["first_pass_completed"])

    def test_current_pass_dirty_body_and_frontmatter(self):
        self.save({"index.md": [self.record()]})
        view = public_view(self.root, "index.md", now=NOW)
        self.assertEqual(view["state"], "passed")
        self.assertEqual(view["date"], iso(NOW - timedelta(days=1))[:10])
        self.assertEqual(public_view(self.root, "index.md", body_hash="0" * 64, now=NOW)["state"], "pending")
        self.page("index.md", "---\nupdated: today\n---\n# Guide\n\nPractical evergreen advice.\n")
        self.assertEqual(public_view(self.root, "index.md", now=NOW)["state"], "passed")
        self.page("index.md", "Changed published body")
        self.assertIsNone(public_view(self.root, "index.md", now=NOW)["date"])

    def test_latest_revision_not_historical_pass(self):
        history = [self.record(ago=3), self.record(status="needs_revision", ago=1)]
        self.save({"index.md": history})
        self.assertEqual(public_view(self.root, "index.md", now=NOW)["state"], "pending")
        loaded, _ = load_reviews(self.root / "data/quality-checks.json")
        self.assertEqual(loaded["index.md"], history)

    def test_cadence_rolls_30_90_and_no_forced_work(self):
        self.page("tools/api.md")
        reviews = {p: [self.record(p)] for p in ("index.md", "tools/api.md")}
        self.save(reviews)
        self.assertEqual(self.cli()[1]["items"], [])
        rows, errors = inventory(self.root, reviews, NOW + timedelta(days=30))
        self.assertFalse(errors)
        self.assertEqual({r["path"]: r["state"] for r in rows}, {"index.md": "current", "tools/api.md": "overdue"})
        overdue_view = public_view(self.root, "tools/api.md", now=NOW + timedelta(days=30))
        self.assertEqual(overdue_view["state"], "passed")
        self.assertEqual(overdue_view["date"], reviews["tools/api.md"][0]["assessed_at"][:10])
        self.assertTrue(next(r for r in rows if r["path"] == "tools/api.md")["due"])
        self.assertTrue(all(r["due"] for r in inventory(self.root, reviews, NOW + timedelta(days=90))[0]))
        self.page("new.md")
        self.assertEqual(self.cli()[1]["summary"]["phase"], "bootstrap")

    def test_daily_cap_across_reruns_utc_reset(self):
        reviews = {}
        for i in range(7):
            path = f"p{i}.md"
            self.page(path)
            if i < 5:
                reviews[path] = [self.record(path, status="aborted" if i == 0 else "needs_revision", ago=0)]
        self.save(reviews)
        for _ in range(2):
            code, report = self.cli(extra=["--limit", "99"])
            self.assertEqual(code, 0)
            self.assertEqual(report["summary"]["assessed_today"], 5)
            self.assertEqual(report["summary"]["remaining_today"], 0)
            self.assertEqual(report["items"], [])
        self.assertEqual(self.cli(now=NOW + timedelta(days=1))[1]["summary"]["remaining_today"], 5)

    def test_retry_park_changed_body_and_queue_age(self):
        self.page("a.md")
        old = self.record("index.md", status="needs_revision", ago=10)
        old.update(disposition="retry", retry_at=iso(NOW - timedelta(days=1)))
        recent = self.record("a.md", status="needs_revision", ago=3)
        recent.update(disposition="retry", retry_at=iso(NOW - timedelta(days=1)))
        rows, errors = inventory(self.root, {"index.md": [old], "a.md": [recent]}, NOW)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["path"], "index.md")
        old["retry_at"] = iso(NOW + timedelta(days=2))
        rows, _ = inventory(self.root, {"index.md": [old], "a.md": [recent]}, NOW)
        self.assertEqual(rows[0]["path"], "a.md")
        self.page("index.md", "Updated published body now needs reassessment")
        rows, _ = inventory(self.root, {"index.md": [old], "a.md": [recent]}, NOW)
        self.assertEqual(rows[0]["state"], "stale")

    def test_strict_invalid_records_fail_closed(self):
        for field, value in [("status", "verified"), ("assessed_at", "2099-01-01T00:00:00Z"),
                             ("content_sha256", "bad"), ("report_ref", "../secret.md"), ("report_ref", "docs-internal/missing.md"),
                             ("method", "factcheck"), ("dimensions", {}), ("reviewer", ""), ("next_review_at", "2000-01-01T00:00:00Z")]:
            with self.subTest(field=field, value=value):
                record = self.record()
                record[field] = value
                self.assertTrue(validate_assessment(record, NOW, self.root))
                self.save({"index.md": [record]})
                self.assertEqual(public_view(self.root, "index.md", now=NOW)["state"], "pending")
                self.assertEqual(self.cli()[0], 1)
        bad = self.record()
        bad["dimensions"]["coherence"]["rationale"] = "good"
        self.assertTrue(validate_assessment(bad, NOW))

    def test_sources_not_url_count_and_cross_page_checks(self):
        record = self.record()
        self.assertFalse(validate_assessment(record, NOW, self.root))
        record["source_checks"] = {"applicable": True, "rationale": "Specific platform claim requires checking primary evidence in context.", "items": []}
        self.assertTrue(validate_assessment(record, NOW))
        record["source_checks"]["items"] = [{"url": "https://example.org", "claim": "Specific material assertion that must be checked.",
                                            "finding": "Source does not establish the claimed universal outcome.", "checked_at": record["assessed_at"]}]
        record["status"] = "needs_revision"
        record["dimensions"]["reasonable_claims"]["status"] = "needs_revision"
        record.update(disposition="park", reason="Specific unsupported claim needs approved correction before publication.")
        self.assertFalse(validate_assessment(record, NOW))
        self.save({"index.md": [record]})
        self.assertEqual(public_view(self.root, "index.md", now=NOW)["state"], "pending")
        record["source_checks"]["items"][0]["checked_at"] = iso(NOW)
        self.assertTrue(validate_assessment(record, NOW))

    def test_cross_page_reference_and_pass_dimension_guard(self):
        self.page("neighbor.md")
        record = self.record()
        record["cross_page_comparisons"] = {"applicable": True, "rationale": "Neighboring guidance shares terminology requiring a direct comparison.",
            "items": [{"path": "neighbor.md", "claim": "Both pages should define the intended audience consistently.",
                       "finding": "The fixture pages contain no conflicting audience definitions.", "checked_at": record["assessed_at"]}]}
        self.assertFalse(validate_assessment(record, NOW, self.root, {"index.md", "neighbor.md"}))
        record["cross_page_comparisons"]["items"][0]["path"] = "missing.md"
        self.assertTrue(validate_assessment(record, NOW, self.root, {"index.md", "neighbor.md"}))
        record = self.record()
        record["dimensions"]["usability"]["status"] = "needs_revision"
        self.assertTrue(validate_assessment(record, NOW))

    def test_malformed_nested_values_are_errors_not_attestations(self):
        for field, value in [("dimensions", {d: None for d in DIMENSIONS}), ("source_checks", []),
                             ("cross_page_comparisons", {"applicable": True, "rationale": "Valid length rationale containing several specific words.", "items": [None]}),
                             ("report_ref", "docs-internal/invalid\x00.md"), ("status", {})]:
            record = self.record()
            record[field] = value
            self.assertTrue(validate_assessment(record, NOW, self.root))

    def test_schema_duplicate_keys_paths_history(self):
        file = self.root / "data/quality-checks.json"
        file.write_text('{"version":1,"version":1,"reviews":{}}')
        with self.assertRaises(ValueError):
            load_reviews(file)
        record = self.record()
        for reviews in ({"../index.md": [record]}, {"index.md": record}, {"index.md": [record, copy.deepcopy(record)]}):
            self.assertTrue(inventory(self.root, reviews, NOW)[1])
        self.page("overrides/template.md")
        self.assertEqual(len(inventory(self.root, {}, NOW)[0]), 1)


if __name__ == "__main__":
    unittest.main()
