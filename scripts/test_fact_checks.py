"""Offline tests: no network, git dates, or automatic attestations."""
import contextlib
from datetime import timedelta
import io
import json
from pathlib import Path
import tempfile
import unittest
from fact_checks import (MEASUREMENT, body_bytes, content_hash, inventory,
                         load_reviews, main, timestamp, validate_review)

NOW = timestamp("2026-10-02T12:00:00Z")


class FactCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = "patterns/prove/evergreen.md"
        self.article(self.path)

    def article(self, name, body="# Clear writing\n\nStable advice.\n"):
        path = self.root / "docs" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return path

    def review(self, path=None):
        return {"checked_at": "2026-10-01T12:00:00Z",
                "reviewer": "AI: Test reviewer (fixture only)",
                "method": "Read full source and compared each claim; report fixture.",
                "content_sha256": content_hash(self.root / "docs" / (path or self.path)),
                "sources": [{"url": "https://example.org/evidence", "claims": ["A precisely supported claim"],
                             "checked_at": "2026-10-01T11:00:00Z"}],
                "status": "verified", "next_review_at": "2026-12-30T12:00:00Z"}

    def test_unreviewed_never_uses_git_or_metadata(self):
        self.article(self.path, "---\nlast_updated: 2026-10-02\n---\n# Example\n")
        rows, errors = inventory(self.root, {}, NOW)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["state"], "unreviewed")
        self.assertIsNone(rows[0]["checked_at"])
        self.assertTrue(rows[0]["due"])

    def test_hash_excludes_only_yaml(self):
        self.assertEqual(body_bytes(b"---\na: b\n---\n\n# Body\n"), b"\n# Body\n")
        self.assertEqual(body_bytes(b"---\r\na: b\r\n---\r\n# Body\r\n"), b"# Body\r\n")
        with self.assertRaises(ValueError):
            body_bytes(b"---\na: b\n")
        path = self.article(self.path, "---\na: b\n---\n# Body\n")
        before = content_hash(path)
        path.write_text("---\na: c\n---\n# Body\n")
        self.assertEqual(before, content_hash(path))
        path.write_text("---\na: c\n---\n# Body revised\n")
        self.assertNotEqual(before, content_hash(path))

    def test_body_change_is_stale(self):
        review = self.review()
        self.article(self.path, "Changed factual claim")
        rows, errors = inventory(self.root, {self.path: review}, NOW)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["state"], "stale")
        self.assertTrue(rows[0]["due"])

    def test_invalid_dates_and_proof_fail(self):
        for field, value in [("checked_at", "2026-10-03T12:00:00Z"),
                             ("checked_at", "2026-02-30T12:00:00Z"),
                             ("checked_at", "2026-10-01"),
                             ("checked_at", "2026-10-01T12:00:00+01:00"),
                             ("next_review_at", "2026-09-01T12:00:00Z"),
                             ("content_sha256", "not-a-hash"), ("sources", []),
                             ("reviewer", ""), ("method", ""), ("status", "blocked")]:
            with self.subTest(field=field, value=value):
                review = self.review()
                review[field] = value
                self.assertTrue(validate_review(review, NOW))
        for field, value in [("url", "file:///private"), ("url", "https://user:pass@example.org"),
                             ("claims", []), ("claims", "unsupported shape"),
                             ("checked_at", "2026-10-02T11:00:00Z")]:
            review = self.review()
            review["sources"][0][field] = value
            self.assertTrue(validate_review(review, NOW))

    def test_partial_retry_is_not_fresh_and_is_bounded(self):
        review = self.review()
        review.update(status="partial", next_review_at="2026-10-05T12:00:00Z",
                      method="Compared accessible source. Blocked: remaining source unavailable; retry access.")
        rows, errors = inventory(self.root, {self.path: review}, NOW)
        self.assertFalse(errors)
        self.assertEqual(rows[0]["state"], "partial")
        self.assertTrue(rows[0]["needs_review"])
        self.assertFalse(rows[0]["due"])
        rows, _ = inventory(self.root, {self.path: review}, NOW + timedelta(days=3))
        self.assertTrue(rows[0]["due"])
        self.article(self.path, "Changed during retry window")
        rows, _ = inventory(self.root, {self.path: review}, NOW)
        self.assertTrue(rows[0]["due"])
        review["next_review_at"] = "2026-10-09T12:00:00Z"
        self.assertTrue(validate_review(review, NOW))

    def test_cadence_caps_explicit_date(self):
        self.article("tools/spec.md")
        review = self.review("tools/spec.md")
        reviews = {"tools/spec.md": review, self.path: self.review()}
        rows, errors = inventory(self.root, reviews, NOW + timedelta(days=30))
        self.assertFalse(errors)
        by_path = {r["path"]: r for r in rows}
        self.assertEqual(by_path["tools/spec.md"]["state"], "overdue")
        self.assertEqual(by_path[self.path]["state"], "current")
        rows, _ = inventory(self.root, reviews, NOW, high_days=1, evergreen_days=1)
        self.assertTrue(all(r["due"] for r in rows))

    def test_rank_measurement_then_high_risk_then_evergreen(self):
        self.article(MEASUREMENT)
        self.article("patterns/prove/platform.md", "# Platform\nGoogle analytics")
        rows, _ = inventory(self.root, {}, NOW)
        self.assertEqual([r["path"] for r in rows], [MEASUREMENT, "patterns/prove/platform.md", self.path])
        review = self.review(MEASUREMENT)
        review.update(status="partial", next_review_at="2026-10-05T12:00:00Z",
                      method="Compared accessible source. Blocked: remaining source unavailable; retry access.")
        rows, _ = inventory(self.root, {MEASUREMENT: review}, NOW)
        self.assertEqual(rows[-1]["path"], MEASUREMENT)

    def test_oldest_overdue_precedes_newer_and_partial_requires_reason(self):
        self.article("tools/old.md")
        self.article("tools/new.md")
        old = self.review("tools/old.md")
        newer = self.review("tools/new.md")
        old["next_review_at"] = "2026-10-01T13:00:00Z"
        newer["next_review_at"] = "2026-10-02T10:00:00Z"
        rows, errors = inventory(self.root, {"tools/old.md": old, "tools/new.md": newer}, NOW)
        self.assertFalse(errors)
        self.assertEqual([r["path"] for r in rows[:2]], ["tools/old.md", "tools/new.md"])
        newer["status"] = "partial"
        self.assertTrue(validate_review(newer, NOW))

    def test_every_published_page_and_unknown_target_rejected(self):
        self.article("patterns/index.md")
        self.article("framework.md")
        self.article("index.md")
        self.article("overrides/patterns/draft.md")
        (self.root / "draft.md").write_text("Not published")
        rows, errors = inventory(self.root, {"../draft.md": self.review()}, NOW)
        self.assertEqual({r["path"] for r in rows}, {self.path, "patterns/index.md", "framework.md", "index.md"})
        self.assertTrue(errors)
        rows, errors = inventory(self.root, {"framework.md": self.review("framework.md"), "index.md": self.review("index.md")}, NOW)
        self.assertFalse(errors)
        self.assertEqual({r["page_type"] for r in rows}, {"Article", "WebPage", "CollectionPage"})
        self.assertEqual({r["path"] for r in rows if r["state"] == "current"}, {"index.md", "framework.md"})

    def test_missing_empty_malformed_and_duplicate_store(self):
        path = self.root / "reviews.json"
        self.assertEqual(load_reviews(path), ({}, False))
        path.write_text('{"version":1,"reviews":{}}')
        self.assertEqual(load_reviews(path), ({}, True))
        for value in ['{}', '{"version":true,"reviews":{}}', '{"version":1,"version":1,"reviews":{}}', '{']:
            path.write_text(value)
            with self.assertRaises(ValueError):
                load_reviews(path)

    def test_cli_bounded_summary_and_validation_exit(self):
        self.article(MEASUREMENT)
        before = sorted(str(p) for p in self.root.rglob("*"))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            result = main(["due", "--root", str(self.root), "--now", "2026-10-02T12:00:00Z", "--limit", "1", "--json"])
        self.assertEqual(result, 0)
        report = json.loads(out.getvalue())
        self.assertEqual(report["summary"]["articles"], 2)
        self.assertEqual(len(report["items"]), 1)
        self.assertEqual(before, sorted(str(p) for p in self.root.rglob("*")))
        data = self.root / "bad.json"
        data.write_text('{"version":1,"reviews":{"patterns/prove/evergreen.md":null}}')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main(["validate", "--root", str(self.root), "--data", str(data), "--json"]), 1)


if __name__ == "__main__":
    unittest.main()
