"""Draft-only consolidation guard; no shared rejection-manifest edits."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class RecurringSegmentsTests(unittest.TestCase):
    def test_one_canonical_draft_and_archived_standalone(self):
        self.assertTrue((ROOT / 'produce/audience-engagement/standardized-micro-segments.md').is_file())
        self.assertTrue((ROOT / 'docs-internal/archive/superseded/2026-10-02/gamified-branded-segments.md').is_file())
        for folder in ('produce', 'package', 'publish', 'prove', 'preserve', 'docs'):
            self.assertEqual(list((ROOT / folder).rglob('gamified-branded-segments.md')), [])

    def test_evidence_examples_and_safety_survive_transform(self):
        draft = (ROOT / 'produce/audience-engagement/standardized-micro-segments.md').read_text()
        preview = (ROOT / 'docs-internal/reviews/recurring-show-segments-2026-10-02/publisher-preview.md').read_text()
        for text in (draft, preview):
            self.assertNotRegex(text, r'\brec[A-Za-z0-9]{14}\b')
            for required in ('Evidence level: practitioner-observation.', 'hypothetical', 'Score 3 is a provisional editorial judgment', 'No retention lift', 'purpose', 'setup', 'payoff'):
                self.assertIn(required, text)
        for heading in ('What It Is', 'Best For', 'Why It Works', 'Required Elements', 'Example Patterns', 'Quality Bar', 'When Not To Use', 'Evidence', 'Related Patterns'):
            pattern = rf'^## {heading}\n(.*?)(?=^## |\Z)'
            a = re.search(pattern, draft, re.M | re.S).group(1).strip()
            b = re.search(pattern, preview, re.M | re.S).group(1).strip()
            self.assertEqual(a, b, heading)

    def test_related_links_resolve_in_site_source(self):
        text = (ROOT / 'produce/audience-engagement/standardized-micro-segments.md').read_text()
        for url in re.findall(r'https://index\.riggg\.com/([^)]*)', text):
            self.assertTrue((ROOT / 'docs' / (url.rstrip('/') + '.md')).is_file(), url)

if __name__ == '__main__':
    unittest.main()
