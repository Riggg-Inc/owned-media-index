"""Truthful metadata for published docs; optional, consent-gated measurement."""
import gzip
import os
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


class Paragraphs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items, self.current = [], None
    def handle_starttag(self, tag, attrs):
        if tag == 'p': self.current = []
    def handle_data(self, data):
        if self.current is not None: self.current.append(data)
    def handle_endtag(self, tag):
        if tag == 'p' and self.current is not None:
            self.items.append(' '.join(''.join(self.current).split()))
            self.current = None


def on_config(config):
    measurement = os.getenv('OMI_GA_MEASUREMENT_ID', '').strip()
    privacy = os.getenv('OMI_PRIVACY_URL', '').strip()
    if measurement:
        if not re.fullmatch(r'G-[A-Z0-9]+', measurement):
            raise ValueError('OMI_GA_MEASUREMENT_ID must be a GA4 measurement ID')
        parsed = urlparse(privacy)
        if parsed.scheme != 'https' or not parsed.netloc or any(c in privacy for c in '"<>'):
            raise ValueError('Analytics activation requires an approved HTTPS OMI_PRIVACY_URL')
        config.extra['analytics'] = {'provider': 'google', 'property': measurement}
        config.extra['consent'] = {
            'title': 'Optional analytics',
            'description': 'With your permission, we use Google Analytics to understand which resources are useful. You can reject optional analytics. <a href="' + privacy + '">Privacy policy</a>.',
            'actions': ['accept', 'reject', 'manage'],
            'cookies': {'analytics': {'name': 'Google Analytics', 'checked': False}, 'github': False},
        }
        config.copyright += ' &nbsp;·&nbsp; <a href="#" onclick="__md_displayConsent(); return false">Analytics preferences</a>'
    return config


def on_page_content(html, page, config, files):
    if not page.meta.get('description'):
        parser = Paragraphs()
        parser.feed(html)
        candidates = [p for p in parser.items if len(p) >= 65 and not re.match(r'^(Stage|Score|Evidence|Status|Last updated|Source):', p)]
        text = candidates[0] if candidates else 'Explore ' + page.title + ' in the Owned Media Index: practical patterns, tools, and standards curated by Riggg.'
        if len(text) > 180:
            text = text[:177].rsplit(' ', 1)[0].rstrip('.,;:') + '…'
        page.meta['description'] = text
    return html


def on_page_context(context, page, config, nav):
    canonical = page.canonical_url
    source = page.file.src_uri
    kind = 'CollectionPage' if source.endswith('/index.md') else 'WebPage'
    if source.startswith('patterns/') and not source.endswith('/index.md'):
        kind = 'TechArticle'
    org = {'@type': 'Organization', '@id': 'https://riggg.com/#organization', 'name': 'Riggg Inc.', 'url': 'https://riggg.com'}
    graph = [org, {'@type': 'WebSite', '@id': config.site_url + '#website', 'name': config.site_name, 'url': config.site_url, 'publisher': {'@id': org['@id']}},
             {'@type': kind, '@id': canonical + '#content', 'url': canonical, 'name': page.title, 'description': page.meta['description'], 'isPartOf': {'@id': config.site_url + '#website'}, 'publisher': {'@id': org['@id']}}]
    if kind == 'TechArticle':
        graph[-1]['headline'] = page.title
        graph[-1]['mainEntityOfPage'] = canonical
    if context.get('breadcrumb_schema'):
        graph.append(context['breadcrumb_schema'])
    # Omit unknown editorial dates rather than claim build time is a revision.
    context['seo_schema'] = {'@context': 'https://schema.org', '@graph': graph}
    return context


def on_post_build(config):
    sitemap = Path(config.site_dir) / 'sitemap.xml'
    text = re.sub(r'\s*<lastmod>.*?</lastmod>', '', sitemap.read_text())
    sitemap.write_text(text)
    with gzip.open(str(sitemap) + '.gz', 'wb') as handle:
        handle.write(text.encode())
