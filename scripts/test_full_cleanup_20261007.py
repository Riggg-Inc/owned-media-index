"""Owner-authorized legacy cleanup regression; no network or publication."""
import hashlib,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class CleanupTests(unittest.TestCase):
    def test_archive_bytes_and_no_active_source(self):
        for item in json.loads((ROOT/'docs-internal/archive/rejected/full-cleanup-20261007.json').read_text()):
            self.assertEqual(hashlib.sha256((ROOT/item['archive']).read_bytes()).hexdigest(),item['sha256'])
            if not item['source'].startswith('/'):
                self.assertFalse((ROOT/item['source']).exists())
    def test_suppressed_topics_absent_from_publication_inputs(self):
        reg=json.loads((ROOT/'docs-internal/intake-suppressions.json').read_text())
        slugs=['track-specific-surveying','transparent-preframing-virtual-logistics','lanyard-sponsorship-dominance','flipped-asynchronous-baseline','live-attendance-gating','kinesthetic-audience-reset','strategic-pause-engagement','platform-monetization-eligibility-risk','host-adserver-self-preferencing','ad-loudness-parity']
        for slug in slugs:
            self.assertIn(slug,reg['retired_slugs'])
            for folder in ['produce','package','publish','prove','preserve','docs']:
                self.assertEqual(list((ROOT/folder).rglob(slug+'.md')),[])
                for p in (ROOT/folder).rglob('*.md'):
                    self.assertNotIn(slug,p.read_text(),str(p))
    def test_no_manufactured_training_survey_archive(self):
        self.assertFalse((ROOT/'docs-internal/archive/rejected/track-specific-surveying.md').exists())
if __name__=='__main__':unittest.main()
