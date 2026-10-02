#!/usr/bin/env python3
"""Verify generated Article freshness against committed bodies and evidence."""
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hooks.freshness import History, page_freshness
from hooks.metadata import page_type
from scripts.fact_checks import load_reviews


class FreshnessHTML(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.blocks, self.revision_times, self.graphs = [], [], []
        self.script = None
        self.revision = False
        self.summary = False
        self.summary_text = ''
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'omi-freshness' in a.get('class', '').split():
            self.blocks.append(a)
        if tag == 'details' and a.get('class') == 'omi-freshness__revision':
            self.revision = True
        if tag == 'summary' and self.revision:
            self.summary = True
        if tag == 'time' and self.revision:
            self.revision_times.append(a.get('datetime'))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.script = ''

    def handle_data(self, value):
        if self.script is not None:
            self.script += value
        if self.summary:
            self.summary_text += value

    def handle_endtag(self, tag):
        if tag == 'summary':
            self.summary = False
        if tag == 'details':
            self.revision = False
        if tag == 'script' and self.script is not None:
            self.graphs.extend(json.loads(self.script).get('@graph', []))
            self.script = None


def audit(root, site):
    errors, count = [], 0
    history = History(root)
    reviews = load_reviews(root / 'data/fact-checks.json')[0]
    for path in sorted((root / 'docs').rglob('*.md')):
        source = path.relative_to(root / 'docs')
        if 'overrides' in source.parts:
            continue
        target = site / (source.with_suffix('') / 'index.html' if source.name != 'index.md' else source.with_suffix('.html'))
        if not target.exists():
            errors.append(f'{source}: missing built page')
            continue
        text = target.read_text()
        doc = FreshnessHTML(text)
        if page_type(source.as_posix()) != 'Article':
            if doc.blocks:
                errors.append(f'{source}: non-Article freshness')
            continue
        count += 1
        expected = page_freshness(root, source.as_posix(), history, reviews)
        revision, review = expected['revision'], expected['review']
        articles = [g for g in doc.graphs if g.get('@type') == 'Article']
        if len(doc.blocks) != 1 or len(articles) != 1:
            errors.append(f'{source}: expected one freshness block and Article')
            continue
        if doc.blocks[0].get('data-revision-state') != revision['state'] or doc.blocks[0].get('data-review-state') != review['state']:
            errors.append(f'{source}: freshness state mismatch')
        stamp = revision.get('timestamp')
        if articles[0].get('dateModified') != stamp:
            errors.append(f'{source}: dateModified provenance mismatch')
        if stamp:
            if doc.revision_times != [stamp, stamp] or doc.summary_text.strip() != 'Last updated: ' + revision['date']:
                errors.append(f'{source}: date-only summary/exact datetime mismatch')
        elif doc.revision_times:
            errors.append(f'{source}: invented revision timestamp')
        if review['label'] not in text:
            errors.append(f'{source}: missing review status label')
        if not text.index('aria-label="Breadcrumb"') < text.index('class="omi-freshness"') < text.index('<h1'):
            errors.append(f'{source}: metadata not under breadcrumb before article')
    return count, errors


if __name__ == '__main__':
    count, errors = audit(Path('.'), Path('site'))
    print(f'Audited freshness on {count} Articles; {len(errors)} errors.')
    print('\n'.join(errors))
    raise SystemExit(bool(errors))
