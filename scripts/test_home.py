"""Keep the homepage content-first."""
import unittest
from pathlib import Path

class HomeTests(unittest.TestCase):
    def test_intro_then_existing_framework(self):
        html = Path('site/index.html').read_text()
        self.assertIn('The Owned Media Index (OMI) is an open library', html)
        self.assertLess(html.index('class="omi-section omi-intro"'), html.index('id="the-framework"'))
        self.assertEqual(html.count('<h1'), 1)
        for marker in ['omi-driver', 'omi-sticky', '320vh', 'assets/imagery/', "requestAnimationFrame(update)"]:
            self.assertNotIn(marker, html)
        for stage in ['Produce', 'Package', 'Publish', 'Prove', 'Preserve']:
            self.assertIn('class="step-label">' + stage, html)
