"""Regression coverage for generated pages and off-nav breadcrumb hierarchy."""
import tempfile
import unittest
from pathlib import Path

from validate_site import BASE, audit

SITE = Path("site")


class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs, cls.links, cls.errors = audit(SITE)

    def trail(self, path):
        return self.docs[BASE + path][1].breadcrumbs

    def test_all_links_and_breadcrumb_schemas(self):
        self.assertGreaterEqual(len(self.docs), 124)
        self.assertEqual(self.errors, [])

    def test_off_nav_deep_leaf(self):
        trail = self.trail("patterns/package/titles/contrarian-hook/")
        self.assertEqual([c["name"] for c in trail], ["Home", "Pattern Library", "Package", "Titles", "Contrarian Hook"])

    def test_missing_intermediate_index_is_not_invented(self):
        trail = self.trail("patterns/package/social-posts/types/episode-announcement/linkedin-long-form/")
        self.assertEqual(len(trail), 6)
        self.assertNotIn("Types", [c["name"] for c in trail])
        self.assertEqual([c["name"] for c in self.trail("tools/hosting/video-podcast-hosting-support/")][:-1], ["Home", "Tools"])

    def test_home_is_not_duplicated(self):
        self.assertEqual(self.trail(""), [{"name": "Home", "href": None, "current": "page"}])

    def test_section_does_not_link_to_itself(self):
        self.assertEqual([c["name"] for c in self.trail("patterns/package/titles/")], ["Home", "Pattern Library", "Package", "Titles"])

    def test_templates_and_unapproved_drafts_are_not_published(self):
        self.assertFalse((SITE / "overrides").exists())
        # Every built content page must originate in docs/, never repository drafts.
        expected = {BASE + ("" if p.as_posix() == "index.md" else p.as_posix()[:-8] if p.name == "index.md" else p.with_suffix("").as_posix() + "/")
                    for source in Path("docs").rglob("*.md")
                    for p in [source.relative_to("docs")] if "overrides" not in p.parts}
        self.assertEqual(set(self.docs) - {BASE + "404.html"}, expected)
        self.assertFalse(any(SITE.rglob("*vertical-reel-package-standard*")))

    def test_related_patterns_use_published_equivalents(self):
        doc = self.docs[BASE + "patterns/produce/recording/hls-video-podcast-distribution/"][1]
        for url in ["../../obs-production-standard/", "../../../publish/feed-metadata-standard/", "../../../publish/youtube-title-and-description-standard/", "../../../publish/canonical-episode-page/"]:
            self.assertIn(url, doc.links)

    def test_auditor_detects_broken_raw_html_link_and_fragment(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.html").write_text('<a href="missing/">Broken</a><a href="#absent">Fragment</a>')
            _, _, errors = audit(root, breadcrumbs=False)
            self.assertEqual(len(errors), 2)
            self.assertTrue(any("missing target" in error for error in errors))
            self.assertTrue(any("missing fragment" in error for error in errors))

    def test_breadcrumb_json_is_serialized_not_interpolated(self):
        from jinja2 import Environment
        from types import SimpleNamespace
        from hooks.breadcrumbs import build_trail
        class Files:
            def documentation_pages(self):
                return files
        def page(source, title, url):
            file = SimpleNamespace(src_uri=source)
            file.page = SimpleNamespace(file=file, title=title, url=url, canonical_url=BASE + url)
            return file
        files = [page("index.md", "Home", ""), page("quoted.md", 'A "quote" & </script>', "quoted/")]
        trail = build_trail(files[-1].page, Files())
        rendered = Environment().from_string('{{ value | tojson }}').render(value=trail)
        self.assertNotIn("</script>", rendered)
        import json
        self.assertEqual(json.loads(rendered)[-1]["name"], files[-1].page.title)


if __name__ == "__main__":
    unittest.main()
