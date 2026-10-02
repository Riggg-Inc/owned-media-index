import unittest
from pathlib import Path
from html.parser import HTMLParser

class Controls(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.inputs=[]; self.buttons=[]; self.feed(html)
    def handle_starttag(self,tag,attrs):
        if tag=='input': self.inputs.append(dict(attrs))
        if tag=='button': self.buttons.append(dict(attrs))

class ConsentTests(unittest.TestCase):
    def test_accept_is_explicit_and_reject_remains_available(self):
        controls=Controls(Path('docs/overrides/partials/consent.html').read_text())
        analytics=[i for i in controls.inputs if i.get('name')=='analytics']
        self.assertEqual(len(analytics),1)
        self.assertNotIn('checked',analytics[0])
        accept=[b for b in controls.buttons if b.get('type')=='submit']
        self.assertEqual(len(accept),1)
        self.assertEqual(accept[0].get('onclick'),'this.form.elements.analytics.checked = true')
        self.assertTrue(any(b.get('type')=='reset' for b in controls.buttons))
