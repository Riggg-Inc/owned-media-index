"""AEO regression gates; run after mkdocs build --strict."""
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from jinja2 import Environment
from validate_aeo import Metadata, audit_aeo, summary_errors
from hooks.metadata import build_schema, page_type


class AeoTests(unittest.TestCase):
    def test_all_published_metadata(self):
        counts, errors = audit_aeo(Path("site"))
        self.assertEqual(errors, [])
        self.assertGreaterEqual(sum(counts.values()), 124)

    def test_types_are_conservative(self):
        for source, expected in [("index.md", "CollectionPage"), ("patterns/index.md", "CollectionPage"), ("framework.md", "WebPage"), ("quadrants/titles.md", "WebPage"), ("patterns/publish/canonical-episode-page.md", "Article")]:
            self.assertEqual(page_type(source), expected)

    def test_whole_graph_escapes_hostile_strings(self):
        hostile = 'Quotes " and slash \\ & </script><script>alert(1)</script> café'
        page = SimpleNamespace(file=SimpleNamespace(src_uri="patterns/quoted.md"), title=hostile,
                               content="", meta={"description": hostile}, canonical_url="https://index.riggg.com/patterns/quoted/")
        config = {"site_url": "https://index.riggg.com/", "site_name": hostile, "site_description": hostile}
        schema = build_schema(page, config, {"@type": "BreadcrumbList", "itemListElement": []})
        rendered = Environment().from_string('{{ value | tojson }}').render(value=schema)
        self.assertNotIn("</script>", rendered)
        self.assertEqual(json.loads(rendered), schema)
        self.assertEqual(schema["@graph"][-1]["headline"], hostile)
        self.assertNotIn("datePublished", rendered)
        self.assertNotIn("dateModified", rendered)

    def test_metadata_parser_preserves_duplicates(self):
        doc = Metadata('<meta name="description" content="one"><meta name="description" content="two">')
        self.assertEqual(doc.meta["description"], ["one", "two"])

    def test_summary_gate_rejects_empty_or_uncited_evidence(self):
        self.assertTrue(summary_errors("# Example\n\n## Why It Works\nDetails", True))
        body = "# Example\n\nA clear definition explaining what this pattern does and when practitioners should use it in their owned media programs.\n\n## Evidence\nAn unsupported claim."
        self.assertTrue(summary_errors(body, True))
        self.assertFalse(summary_errors(body + "\nhttps://example.org/research", True))
        self.assertFalse(summary_errors("# Collection", False))

    def test_home_cards_link_to_published_pages(self):
        import re
        html = Path("site/index.html").read_text()
        cards = re.findall(r'<h[34]><a href="([^"]+)">', html)
        self.assertGreaterEqual(len(cards), 12)
        for href in cards:
            if not href.startswith("http"):
                self.assertTrue((Path("site") / href / "index.html").is_file(), href)


if __name__ == "__main__":
    unittest.main()
