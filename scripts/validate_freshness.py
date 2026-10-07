#!/usr/bin/env python3
"""Audit every published Markdown page's provenance, review state and schema."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hooks.freshness import History, page_freshness
from hooks.metadata import page_type
from scripts.fact_checks import body_bytes


def inline_metadata(text):
    """Reject standalone legacy page stamps, not prose, examples or claim dates."""
    errors, fence = [], None
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        # Fenced examples are documentation, not page metadata.
        if stripped.startswith(('~~~', chr(96) * 3)):
            char = stripped[0]
            if fence is None:
                fence = char
            elif fence == char:
                fence = None
            continue
        if fence or line.startswith(('    ', '	')):
            continue
        plain = re.sub(r'<[^>]+>', '', stripped)
        plain = plain.replace('**', '').replace('__', '').strip('*_ ')
        plain = re.sub(r'^[-+]\s+', '', plain)
        if re.match(r'^(?:(?:Last updated|Last verified|Last fact-checked)\s*:|Last quality checked on\s+|Quality review pending$)', plain, re.I):
            errors.append(number)
    return errors


class FreshnessHTML(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.blocks, self.revision_times, self.review_times, self.graphs = [], [], [], []
        self.script = None
        self.paragraph = None
        self.legacy_metadata = []
        self.code_depth = 0
        self.freshness_depth = 0
        self.section = None
        self.summary = False
        self.summary_text = ''
        self.review_summary = ''
        self.quality_lines = []
        self.quality_text = None
        self.review_disclosures = 0
        self.quality_extra_tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.quality_text is not None and tag != 'time':
            self.quality_extra_tags.append(tag)
        if tag in ('pre', 'code'):
            self.code_depth += 1
        if self.freshness_depth and tag == 'div':
            self.freshness_depth += 1
        if tag == 'p' and not self.freshness_depth and not self.code_depth:
            self.paragraph = ''
        if 'omi-freshness' in a.get('class', '').split():
            self.blocks.append(a)
            self.freshness_depth = 1
        if tag == 'details' and a.get('class', '').startswith('omi-freshness__'):
            self.section = a['class'].split('__')[-1]
        if tag == 'details' and self.section == 'review':
            self.review_disclosures += 1
        if tag == 'p' and 'omi-freshness__quality' in a.get('class', '').split():
            self.quality_text = ''
        if tag == 'summary' and self.section:
            self.summary = True
        if tag == 'time' and self.section == 'revision':
            self.revision_times.append(a.get('datetime'))
        if tag == 'time' and self.quality_text is not None:
            self.review_times.append(a.get('datetime'))
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.script = ''

    def handle_data(self, value):
        if self.quality_text is not None:
            self.quality_text += value
        if self.paragraph is not None and not self.code_depth:
            self.paragraph += value
        if self.script is not None:
            self.script += value
        if self.summary and self.section == 'revision':
            self.summary_text += value
        if self.summary and self.section == 'review':
            self.review_summary += value

    def handle_endtag(self, tag):
        if tag == 'p' and self.quality_text is not None:
            self.quality_lines.append(self.quality_text.strip())
            self.quality_text = None
        if tag == 'p' and self.paragraph is not None:
            if inline_metadata(self.paragraph):
                self.legacy_metadata.append(self.paragraph)
            self.paragraph = None
        if tag in ('pre', 'code'):
            self.code_depth = max(0, self.code_depth - 1)
        if tag == 'div' and self.freshness_depth:
            self.freshness_depth -= 1
        if tag == 'summary':
            self.summary = False
        if tag == 'details':
            self.section = None
        if tag == 'script' and self.script is not None:
            self.graphs.extend(json.loads(self.script).get('@graph', []))
            self.script = None


def audit(root, site):
    errors, count, targets = [], 0, set()
    history = History(root)
    for path in sorted((root / 'docs').rglob('*.md')):
        source = path.relative_to(root / 'docs')
        if 'overrides' in source.parts:
            continue
        for line in inline_metadata(body_bytes(path.read_bytes()).decode()):
            errors.append(f'{source}:{line}: duplicate standalone freshness metadata')
        target = site / (source.with_suffix('') / 'index.html' if source.name != 'index.md' else source.with_suffix('.html'))
        targets.add(target)
        if not target.exists():
            errors.append(f'{source}: missing built page')
            continue
        count += 1
        text = target.read_text()
        doc = FreshnessHTML(text)
        if doc.legacy_metadata:
            errors.append(f'{source}: rendered duplicate standalone freshness metadata')
        expected = page_freshness(root, source.as_posix(), history)
        revision, review = expected['revision'], expected['review']
        kind = page_type(source.as_posix())
        entities = [g for g in doc.graphs if g.get('@type') in ('Article', 'WebPage', 'CollectionPage')]
        expected_types = ['WebPage', 'Article'] if kind == 'Article' else [kind]
        if source.as_posix() == 'index.md':
            if doc.blocks or doc.revision_times or doc.review_times or any(label in text for label in ('Last updated:', 'Last fact-checked', 'No fact-check recorded', 'Last quality checked on', 'Quality review pending', 'omi-freshness__quality')):
                errors.append(f'{source}: homepage must never display freshness metadata')
            if [g.get('@type') for g in entities] != expected_types or any(g.get('dateModified') != revision.get('timestamp') for g in entities):
                errors.append(f'{source}: homepage schema provenance mismatch')
            if 'aria-label="Breadcrumb"' in text or any(g.get('@type') == 'BreadcrumbList' for g in doc.graphs):
                errors.append(f'{source}: homepage breadcrumb exception lost')
            continue
        if len(doc.blocks) != 1 or [g.get('@type') for g in entities] != expected_types:
            errors.append(f'{source}: expected one freshness block and correct page entities')
            continue
        if doc.blocks[0].get('data-revision-state') != revision['state'] or doc.blocks[0].get('data-review-state') != review['state']:
            errors.append(f'{source}: freshness state mismatch')
        stamp = revision.get('timestamp')
        if any(g.get('dateModified') != stamp for g in entities):
            errors.append(f'{source}: dateModified provenance mismatch')
        if stamp:
            if doc.revision_times != [stamp, stamp] or doc.summary_text.strip() != 'Last updated: ' + revision['date']:
                errors.append(f'{source}: date-only summary/exact datetime mismatch')
        elif doc.revision_times:
            errors.append(f'{source}: invented revision timestamp')
        passed = review['state'] == 'passed'
        label = 'Last quality checked on ' + review['date'] if passed else 'Quality review pending'
        if doc.quality_extra_tags:
            errors.append(f'{source}: quality line must contain only text and semantic time')
        if doc.quality_lines != [label]:
            errors.append(f'{source}: expected exactly one compact quality line')
        if doc.review_times != ([review['timestamp']] if passed else []):
            errors.append(f'{source}: quality-check timestamp mismatch')
        if doc.review_disclosures or any(old in text for old in ('Last fact-checked', 'Partial fact-check', 'No fact-check recorded', 'Fact-check needs review', 'omi-freshness__review')):
            errors.append(f'{source}: legacy public factual-review UI remains')
        if text.find('omi-freshness__quality') < text.find('omi-freshness__revision'):
            errors.append(f'{source}: quality line must follow Last updated')
        block_at = text.find('class="omi-freshness"')
        if not 0 <= text.find('aria-label="Breadcrumb"') < block_at < text.find('<h1'):
            errors.append(f'{source}: metadata not under breadcrumb before content')
    for target in set(site.rglob('*.html')) - targets:
        if target == site / '404.html':
            if FreshnessHTML(target.read_text()).blocks:
                errors.append('404.html: generated error page must not claim freshness')
        else:
            errors.append(f'{target}: built HTML page outside Markdown inventory')
    return count, errors


if __name__ == '__main__':
    count, errors = audit(Path('.'), Path('site'))
    print(f'Audited freshness on {count} published pages; {len(errors)} errors.')
    print('\n'.join(errors))
    raise SystemExit(bool(errors))
