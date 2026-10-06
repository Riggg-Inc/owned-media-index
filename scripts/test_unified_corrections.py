import hashlib
import json
from pathlib import Path
import unittest
from fact_checks import body_bytes

ROOT = Path(__file__).resolve().parents[1]

class UnifiedCorrections(unittest.TestCase):
    def test_exact_review_artifacts(self):
        manifest = json.loads((ROOT / 'docs-internal/reviews/unified-corrections-20261006/manifest.json').read_text())
        self.assertEqual(len(manifest['cards']), 3)
        self.assertEqual(manifest['auditStatus'], 'partial')
        self.assertFalse(manifest['publicationAuthorized'])
        for card in manifest['cards']:
            raw = (ROOT / card['path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), card['fullFileSha256'])
            self.assertEqual(hashlib.sha256(body_bytes(raw)).hexdigest(), card['bodySha256'])
            self.assertTrue(card['baseMatchesAuditedBytes'])
            self.assertNotIn('Evidence limitation', raw.decode())

    def test_platform_scope_and_recommendations(self):
        text = (ROOT / 'docs/patterns/package/clips/index.md').read_text()
        for term in ['15 minutes by default', 'whichever is less', 'Page/Career Page', 'gradual rollout', 'editorial export default', 'subject to language and processing limits']:
            self.assertIn(term, text)
        for term in ['80%+', 'sweet spot across all platforms', '| No limit |', 'poor quality', '240 minutes', '512 MB']:
            self.assertNotIn(term, text)

    def test_preserved_practitioner_guide(self):
        story = (ROOT / 'docs/patterns/package/clips/story-beat.md').read_text()
        pain = (ROOT / 'docs/patterns/package/descriptions/audience-pain-breakdown.md').read_text()
        for text in [story, pain]:
            self.assertIn('**Score:** 4', text)
            self.assertIn('## Prompt Template', text)
            self.assertNotIn('the better the output', text)
        self.assertIn('Fits within 60-90 seconds', story)
        self.assertIn('Verify timing and context against the recording', story)
        self.assertIn('**The Amy Porterfield Show**', pain)
        self.assertIn('**Audience Pain → Practical Breakdown → Resources**', pain)
        self.assertIn('Under 250 words', pain)
        self.assertNotIn('The SaaS Marketing Show', pain)
