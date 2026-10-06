"""Narrow guard against resurrecting explicitly rejected drafts."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
REJECTED = ('data-driven-targeted-learning', 'two-part-hook-structure', 'spaced-repetition-reflection', 'cascading-content-funnel', 'cross-format-fact-check-artifacts', 'audience-prep-networking', 'ad-metadata-brand-safety', 'focused-cohort-tracking', 'immersive-learning-exercises', 'new-bliss-closing', 'ai-disclosure-provenance-owned-asset', 'time-sequenced-messaging', 'platform-ad-skipping-monetization-resilience')

class ReconciliationTests(unittest.TestCase):
    def test_rejected_patterns_are_quarantined_not_published(self):
        for slug in REJECTED:
            with self.subTest(slug=slug):
                self.assertTrue((ROOT / "docs-internal/archive/rejected" / (slug + ".md")).is_file())
                for folder in ("produce", "package", "publish", "prove", "preserve", "docs"):
                    self.assertEqual(list((ROOT / folder).rglob(slug + ".md")), [])
                    for path in (ROOT / folder).rglob("*.md"):
                        self.assertNotIn(slug, path.read_text(), str(path))

if __name__ == "__main__":
    unittest.main()
