"""Narrow guard against resurrecting an explicitly rejected draft."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReconciliationTests(unittest.TestCase):
    def test_rejected_pattern_is_quarantined_not_published(self):
        name = "two-part-hook-structure.md"
        self.assertTrue((ROOT / "docs-internal/archive/rejected" / name).is_file())
        for folder in ("produce", "package", "publish", "prove", "preserve", "docs"):
            self.assertEqual(list((ROOT / folder).rglob(name)), [])
            for path in (ROOT / folder).rglob("*.md"):
                self.assertNotIn("two-part-hook-structure", path.read_text(), str(path))

if __name__ == "__main__":
    unittest.main()
