"""Website-hub supersession guard; no shared release files mutated."""
from pathlib import Path
import hashlib
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "docs-internal/archive/superseded"
SOURCE = "publish/website/canonical-episode-page.md"
DOCS = "docs/patterns/publish/canonical-episode-page.md"
OLD = "Canonical control and portability belong to the separate website-format-hub guidance (currently an unpublished draft), rather than being repeated here."
NEW = "Site control and continuity are covered below."

def section(text, heading):
    return text.split("## " + heading + "\n", 1)[1].split("\n## ", 1)[0].strip()

class WebsiteHubSupersessionTests(unittest.TestCase):
    def test_archive_and_no_duplicate(self):
        manifest = json.loads((ARCHIVE / "website-hub-disposition.json").read_text())
        for name, digest in manifest["archives"].items():
            self.assertEqual(hashlib.sha256((ARCHIVE / name).read_bytes()).hexdigest(), digest)
        for folder in ("produce", "package", "publish", "prove", "preserve", "docs"):
            self.assertEqual(list((ROOT / folder).rglob("*owned-website-as-format-hub*.md")), [])

    def test_score_and_new_section_parity(self):
        source, docs = [(ROOT / p).read_text() for p in (SOURCE, DOCS)]
        self.assertEqual(section(source, "Riggg Score"), "3")
        self.assertIn("**Score:** 3", docs)
        normalize = lambda s: re.sub(r"\[Owned Media Library\]\([^)]*\)", "Owned Media Library", s)
        self.assertEqual(normalize(section(source, "Site Control, Navigation And Continuity")), normalize(section(docs, "Site Control, Navigation And Continuity")))
        for p in (SOURCE, DOCS):
            for link in re.findall(r"\]\(([^)]+\.md)\)", (ROOT / p).read_text()):
                self.assertTrue((ROOT / p).parent.joinpath(link).resolve().is_file(), link)

    def test_approved_cta_preserved_except_superseded_pointer(self):
        for p in (SOURCE, DOCS):
            approved = json.loads((ARCHIVE / "website-hub-disposition.json").read_text())["approvedCanonicalBaseline"][p]
            current = (ROOT / p).read_text()
            self.assertEqual(section(current, "Standalone Utility And Optional Next Actions"), section(approved, "Standalone Utility And Optional Next Actions").replace(OLD, NEW))
            self.assertEqual(section(current, "Required Elements"), section(approved, "Required Elements"))

if __name__ == "__main__":
    unittest.main()
