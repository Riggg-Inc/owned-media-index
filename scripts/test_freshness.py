"""Offline revision/review regressions, plus generated-site schema parity."""
import copy
import os
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hooks.freshness import History, review_state, page_freshness
from hooks.metadata import build_schema, page_type
from scripts.fact_checks import content_hash, timestamp
from validate_freshness import audit, inline_metadata, FreshnessHTML


class HistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = 'docs/patterns/test.md'
        self.path = self.root / self.source
        self.path.parent.mkdir(parents=True)
        self.git('init', '-q')
        self.git('config', 'user.email', 'fixture@example.org')
        self.git('config', 'user.name', 'Fixture')
        self.path.write_text('---\nname: original\n---\n# Body\n')
        self.commit('2025-01-01T10:00:00Z')

    def git(self, *args, env=None):
        return subprocess.check_output(['git', '-C', str(self.root), *args], env=env, stderr=subprocess.DEVNULL)

    def commit(self, date):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture', env=dict(os.environ, GIT_AUTHOR_DATE=date, GIT_COMMITTER_DATE=date))

    def revision(self):
        return History(self.root).revision(self.source, self.path.read_bytes())

    def test_frontmatter_template_build_do_not_change_date(self):
        original = self.revision()
        self.path.write_text('---\nname: revised\nlast_updated: 2099-01-01\n---\n# Body\n')
        self.assertEqual(self.revision(), original)
        (self.root / 'template.html').write_text('new template')
        self.commit('2025-02-01T10:00:00Z')
        self.assertEqual(self.revision(), original)
        (self.root / 'data').mkdir()
        (self.root / 'data/quality-checks.json').write_text('{"schema_version": 1}')
        self.commit('2025-03-01T10:00:00Z')
        self.assertEqual(self.revision(), original)

    def test_body_pending_then_committed_and_revert(self):
        self.path.write_text('# Changed\n')
        self.assertEqual(self.revision(), {'state': 'pending'})
        self.commit('2025-02-01T10:00:00Z')
        self.assertEqual(self.revision()['timestamp'], '2025-02-01T10:00:00Z')
        self.path.write_text('# Body\n')
        self.commit('2025-03-01T10:00:00Z')
        self.assertEqual(self.revision()['timestamp'], '2025-03-01T10:00:00Z')

    def test_rename_preserves_body_origin(self):
        original = self.revision()
        new = self.path.with_name('renamed.md')
        self.git('mv', self.source, 'docs/patterns/renamed.md')
        self.path, self.source = new, 'docs/patterns/renamed.md'
        self.commit('2025-02-01T10:00:00Z')
        self.assertEqual(self.revision(), original)

    def test_future_and_shallow_fail_closed(self):
        self.path.write_text('# Future\n')
        self.commit('2099-01-01T10:00:00Z')
        self.assertEqual(self.revision(), {'state': 'unavailable'})
        (self.root / '.git/shallow').write_bytes(self.git('rev-parse', 'HEAD'))
        self.assertEqual(self.revision(), {'state': 'unavailable'})

    def test_untracked_pending(self):
        self.source = 'docs/patterns/new.md'
        self.path = self.root / self.source
        self.path.write_text('# New\n')
        self.assertEqual(self.revision(), {'state': 'pending'})

    def test_legacy_fact_review_states_and_canonical_hash(self):
        now = timestamp('2026-10-02T12:00:00Z')
        record = dict(checked_at='2026-10-01T12:00:00Z', reviewer='Fixture reviewer',
                      method='Compared precise claim to source.', content_sha256=content_hash(self.path),
                      sources=[dict(url='https://example.org/evidence', claims=['Precise claim'], checked_at='2026-10-01T11:00:00Z')],
                      status='verified', next_review_at='2026-10-05T12:00:00Z')
        state = lambda r: review_state(r, self.path, 'patterns/test.md', now)
        self.assertEqual(state(None)['label'], 'No fact-check recorded')
        self.assertEqual(state(record)['state'], 'verified')
        partial = dict(record, status='partial', method='Checked one claim. Blocked: another claim unresolved.')
        self.assertEqual(state(partial)['label'], 'Partial fact-check')
        for key, value in [('checked_at', '2099-01-01T00:00:00Z'), ('content_sha256', '0'*64),
                           ('next_review_at', '2026-10-02T11:00:00Z'), ('reviewer', ''), ('sources', [])]:
            self.assertEqual(state(dict(record, **{key: value}))['state'], 'needs-review')
        bad = copy.deepcopy(record)
        bad['sources'][0]['checked_at'] = '2099-01-01T00:00:00Z'
        self.assertEqual(state(bad)['state'], 'needs-review')
        self.path.write_text('---\nname: changed metadata\n---\n# Body\n')
        self.assertEqual(state(record)['state'], 'verified')
        self.path.write_text('# Body revised\n')
        self.assertEqual(state(record)['state'], 'needs-review')

    def test_quality_hook_bound_to_current_body_not_legacy_fact_record(self):
        from scripts.quality_checks import DIMENSIONS, METHOD, public_view
        from unittest.mock import patch
        source = 'patterns/test.md'
        (self.root / 'data').mkdir()
        (self.root / 'docs-internal').mkdir()
        (self.root / 'docs-internal/fixture.md').write_text('Fixture-only substantive report records why this test body is suitable.')
        now = timestamp('2026-10-07T12:00:00Z')
        self.assertEqual(public_view(self.root, source, now=now)['state'], 'pending')
        record = dict(id='fixture-quality-pass', status='pass', assessed_at='2026-10-07T10:00:00Z',
                      reviewer='Fixture only', method=METHOD, content_sha256=content_hash(self.path),
                      report_ref='docs-internal/fixture.md',
                      dimensions={d: {'status': 'pass', 'rationale': 'Fixture finding for ' + d + ' on this test page only.'} for d in DIMENSIONS},
                      source_checks={'applicable': False, 'rationale': 'Fixture body contains no external claims requiring verification.', 'items': []},
                      cross_page_comparisons={'applicable': False, 'rationale': 'Fixture repository has no related comparison pages available.', 'items': []},
                      next_review_at='2026-10-20T10:00:00Z', disposition='rolling', retry_at=None, reason=None)
        store = self.root / 'data/quality-checks.json'
        store.write_text(json.dumps({'version': 1, 'reviews': {source: [record]}}))
        self.assertEqual(public_view(self.root, source, now=now)['state'], 'passed')
        with patch('scripts.quality_checks.public_view', wraps=lambda root, src: public_view(root, src, now=now)):
            self.assertEqual(page_freshness(self.root, source)['review']['state'], 'passed')
        self.path.write_text('# A changed body invalidates the quality check')
        self.assertEqual(public_view(self.root, source, now=now)['state'], 'pending')
        self.path.write_text('# Body\n')
        record['status'] = 'needs_revision'
        record['dimensions']['substance']['status'] = 'needs_revision'
        record.update(disposition='retry', retry_at='2026-10-08T10:00:00Z',
                      reason='Fixture substance requires a concrete example before publication.')
        store.write_text(json.dumps({'version': 1, 'reviews': {source: [record]}}))
        self.assertEqual(public_view(self.root, source, now=now)['state'], 'pending')
        store.unlink()
        (self.root / 'data/fact-checks.json').write_text(json.dumps({'version': 1, 'reviews': {source: {'status': 'verified'}}}))
        self.assertEqual(public_view(self.root, source, now=now)['state'], 'pending')

    def test_schema_parity_pending_omits_date(self):
        page = SimpleNamespace(canonical_url='https://example.org/test/', file=SimpleNamespace(src_uri='patterns/test.md'),
                               content='<h1>Test</h1>', title='Test', meta={})
        config = dict(site_url='https://example.org/', site_name='Test', site_description='Test')
        for source in ['patterns/test.md', 'framework.md', 'patterns/index.md', 'index.md']:
            page.file.src_uri = source
            for revision in [self.revision(), {'state': 'pending'}, {'state': 'unavailable'}]:
                graph = build_schema(page, config, {}, {'revision': revision})['@graph']
                for item in graph:
                    if item.get('@type') in ('Article', 'WebPage', 'CollectionPage'):
                        self.assertEqual(item.get('dateModified'), revision.get('timestamp'))
                    else:
                        self.assertNotIn('dateModified', item)
                    self.assertNotIn('datePublished', item)



class QualityTemplateTests(unittest.TestCase):
    def render(self, review, source='patterns/test.md'):
        from jinja2 import Environment, FileSystemLoader, select_autoescape
        env = Environment(loader=FileSystemLoader('docs/overrides'), autoescape=select_autoescape())
        return env.get_template('partials/freshness.html').render(
            page=SimpleNamespace(file=SimpleNamespace(src_uri=source)),
            page_freshness={'revision': {'state': 'committed', 'date': 'January 1, 2025',
                                       'timestamp': '2025-01-01T10:00:00Z'}, 'review': review})

    def test_passed_quality_is_only_compact_semantic_date(self):
        review = {'state': 'passed', 'timestamp': '2026-10-07T12:00:00Z',
                  'date': 'October 7, 2026', 'reviewer': 'PRIVATE REVIEWER',
                  'method': 'PRIVATE METHOD', 'sources': ['PRIVATE CLAIM LOG']}
        text = self.render(review)
        doc = FreshnessHTML(text)
        self.assertEqual(doc.quality_lines, ['Last quality checked on October 7, 2026'])
        self.assertEqual(doc.review_times, [review['timestamp']])
        self.assertEqual(doc.review_disclosures, 0)
        self.assertEqual(text.count('<details'), 1)
        self.assertNotIn('PRIVATE', text)
        self.assertLess(text.index('omi-freshness__revision'), text.index('omi-freshness__quality'))

    def test_missing_needs_revision_stale_and_nonpass_never_show_dates(self):
        for state in ['pending', 'needs_revision', 'stale', 'partial', 'verified', 'unrecorded']:
            with self.subTest(state=state):
                text = self.render({'state': state, 'timestamp': '2026-10-07T12:00:00Z',
                                    'date': 'October 7, 2026'})
                doc = FreshnessHTML(text)
                self.assertEqual(doc.quality_lines, ['Quality review pending'])
                self.assertEqual(doc.review_times, [])
                self.assertNotIn('Last quality checked on', text)
        self.assertEqual(FreshnessHTML(self.render({'state': 'passed'})).quality_lines,
                         ['Quality review pending'])

    def test_home_never_renders_even_with_current_pass(self):
        self.assertEqual(self.render({'state': 'passed', 'timestamp': '2026-10-07T12:00:00Z',
                                      'date': 'October 7, 2026'}, 'index.md').strip(), '')


class BuiltFreshnessTests(unittest.TestCase):
    def test_every_published_page_including_home_hubs_and_webpages(self):
        count, errors = audit(Path('.'), Path('site'))
        sources = [p.relative_to('docs').as_posix() for p in Path('docs').rglob('*.md') if 'overrides' not in p.relative_to('docs').parts]
        self.assertEqual(count, len(sources))
        self.assertEqual({page_type(s) for s in sources}, {'Article', 'CollectionPage', 'WebPage'})
        for source, kind in [('index.md', 'CollectionPage'), ('patterns/index.md', 'CollectionPage'), ('framework.md', 'WebPage'), ('tools/hosting/video-podcast-hosting-support.md', 'Article')]:
            self.assertIn(source, sources)
            self.assertEqual(page_type(source), kind)
        home = Path('site/index.html').read_text()
        self.assertEqual(len(FreshnessHTML(home).blocks), 0)
        self.assertNotIn('Homepage source-content revision', home)
        self.assertNotIn('Last updated:', home)
        self.assertNotIn('Last fact-checked', home)
        self.assertNotIn('Last quality checked on', home)
        self.assertNotIn('Quality review pending', home)
        self.assertNotIn('aria-label="Breadcrumb"', home)
        self.assertEqual(len(FreshnessHTML(Path('site/404.html').read_text()).blocks), 0)
        self.assertEqual(errors, [])

    def test_missing_build_fails_closed(self):
        with tempfile.TemporaryDirectory() as missing:
            count, errors = audit(Path('.'), Path(missing))
        self.assertEqual(count, 0)
        self.assertTrue(errors)
        self.assertTrue(all('missing built page' in error for error in errors))


class InlineMetadataTests(unittest.TestCase):
    def test_rendered_template_duplicates_rejected_but_prose_allowed(self):
        doc = FreshnessHTML('<p><strong>Last verified:</strong> 2026-10-02</p><p>Source snapshot: 2026-10-02</p><p>The Last updated: label describes revisions.</p><pre><code>Last updated: example</code></pre>')
        self.assertEqual(doc.legacy_metadata, ['Last verified: 2026-10-02'])
        shared = FreshnessHTML('<div class="omi-freshness"><p>Last updated: Pending commit (preview)</p></div>')
        self.assertEqual(shared.legacy_metadata, [])

    def test_legacy_standalone_stamps_are_rejected(self):
        for text in ['Last updated: 2026-10-02', '**Last verified:** 2026-10-02', '*Last updated: September 2026*', '- **Last verified:** yesterday', '<p>Last updated: today</p>', 'Last quality checked on October 7, 2026', 'Quality review pending']:
            with self.subTest(text=text):
                self.assertEqual(inline_metadata(text), [1])

    def test_source_snapshots_claim_dates_and_examples_remain(self):
        text = "Source snapshot: 2026-10-02\n| Claim | Last verified |\n| A | 2026-10-02 |\nThe Last updated: label describes body revision.\n~~~text\nLast updated: example\n~~~\n    Last verified: code example\n"
        self.assertEqual(inline_metadata(text), [])


if __name__ == '__main__':
    unittest.main()
