"""Guard a superseded identifier, not general question-answer media."""
from pathlib import Path
import hashlib
import json
import unittest
ROOT = Path(__file__).resolve().parents[1]
SLUG = "non-rhetorical-anchoring"
CARD = "7c68d6ad-f05b-482f-b34f-cef03e5ba52d"
CANONICAL = "63fd804a-c90c-4f76-8282-394c56439efb"
SHA = "6ab49676b28a413b40c71e295adb4d7b5ab54d378883e758009fc011be393e68"
class AnchoringSupersessionTests(unittest.TestCase):
    def test_archive_bytes_and_provenance(self):
        archive = ROOT / "docs-internal/archive/superseded" / (SLUG + ".md")
        self.assertEqual(hashlib.sha256(archive.read_bytes()).hexdigest(), SHA)
        registry = json.loads((ROOT / "docs-internal/intake-suppressions.json").read_text())
        self.assertIn(SLUG, registry["superseded_slugs"])
        self.assertIn(CARD, registry["suppressed_card_ids"])
        self.assertNotIn(CANONICAL, registry["suppressed_card_ids"])
        self.assertEqual(registry["archive"][SLUG]["sha256"], SHA)
        self.assertEqual(registry["archive"][SLUG]["canonical_card_id"], CANONICAL)
        self.assertIn("General question-answer formats remain eligible", registry["archive"][SLUG]["decision"])
    def test_no_standalone_source_or_public_recommendation(self):
        for folder in ("produce", "package", "publish", "prove", "preserve", "docs"):
            self.assertEqual(list((ROOT / folder).rglob(SLUG + ".md")), [])
            for path in (ROOT / folder).rglob("*.md"):
                self.assertNotIn(SLUG, path.read_text(), str(path))
if __name__ == "__main__":
    unittest.main()
