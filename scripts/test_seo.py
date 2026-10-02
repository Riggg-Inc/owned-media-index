"""Release gates for metadata, discovery and optional analytics."""
import gzip
import importlib.util
import json
import os
import re
import unittest
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import xml.etree.ElementTree as ET

spec = importlib.util.spec_from_file_location('seo', 'hooks/seo.py')
seo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seo)

class Metadata(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.descriptions, self.canonicals = [], []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name') == 'description': self.descriptions.append(attrs.get('content'))
        if tag == 'link' and attrs.get('rel') == 'canonical': self.canonicals.append(attrs.get('href'))

class SEOTests(unittest.TestCase):
    def test_all_published_metadata(self):
        descriptions = []
        for p in Path('site').rglob('index.html'):
            with self.subTest(page=str(p)):
                html = p.read_text()
                meta = Metadata(html)
                self.assertEqual(len(meta.descriptions), 1)
                self.assertTrue(meta.descriptions[0])
                descriptions.extend(meta.descriptions)
                self.assertEqual(len(meta.canonicals), 1)
                self.assertTrue(meta.canonicals[0].startswith('https://index.riggg.com/'))
                blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
                self.assertEqual(len(blocks), 1)
                graph = json.loads(blocks[0])['@graph']
                if p == Path('site/index.html'):
                    self.assertNotIn('BreadcrumbList', [item['@type'] for item in graph])
                else:
                    self.assertIn('BreadcrumbList', [item['@type'] for item in graph])
                for item in graph:
                    self.assertNotIn('datePublished', item)
                    self.assertNotIn('dateModified', item)
        self.assertGreaterEqual(len(descriptions), 124)
        self.assertEqual([text for text, count in Counter(descriptions).items() if count > 1], [])

    def test_sitemap(self):
        raw = Path('site/sitemap.xml').read_bytes()
        tree = ET.fromstring(raw)
        ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in tree.findall('s:url/s:loc', ns)]
        self.assertEqual(len(urls), len(list(Path('site').rglob('index.html'))))
        self.assertTrue(all(u.startswith('https://index.riggg.com/') for u in urls))
        self.assertNotIn(b'<lastmod>', raw)
        self.assertEqual(gzip.decompress(Path('site/sitemap.xml.gz').read_bytes()), raw)
        self.assertIn('Sitemap: https://index.riggg.com/sitemap.xml', Path('site/robots.txt').read_text())

    def test_analytics_requires_valid_id_and_privacy(self):
        for env in [{'OMI_GA_MEASUREMENT_ID': 'bad'}, {'OMI_GA_MEASUREMENT_ID': 'G-TEST123', 'OMI_PRIVACY_URL': ''}]:
            with patch.dict(os.environ, env, clear=True), self.assertRaises(ValueError):
                seo.on_config(SimpleNamespace(extra={}, copyright=''))

    def test_analytics_disabled_by_default(self):
        with patch.dict(os.environ, {}, clear=True):
            config = seo.on_config(SimpleNamespace(extra={}, copyright=''))
            self.assertNotIn('analytics', config.extra)

    def test_analytics_opt_in(self):
        with patch.dict(os.environ, {'OMI_GA_MEASUREMENT_ID': 'G-TEST123', 'OMI_PRIVACY_URL': 'https://example.com/privacy'}, clear=True):
            config = seo.on_config(SimpleNamespace(extra={}, copyright=''))
            self.assertFalse(config.extra['consent']['cookies']['analytics']['checked'])
            self.assertIn('reject', config.extra['consent']['actions'])
            self.assertIn('href="#__consent"', config.copyright)
            self.assertNotIn('__md_displayConsent', config.copyright)

    def test_json_serialization_handles_quotes(self):
        page = SimpleNamespace(canonical_url='https://index.riggg.com/test/', file=SimpleNamespace(src_uri='patterns/test.md'), title='A "quoted" title', meta={'description': 'A "quoted" answer'})
        result = seo.on_page_context({}, page, SimpleNamespace(site_url='https://index.riggg.com/', site_name='Owned Media Index'), None)
        self.assertEqual(json.loads(json.dumps(result['seo_schema']))['@graph'][-1]['headline'], page.title)
