"""Offline revision/review regressions, plus generated-site schema parity."""
import copy
import os
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from hooks.freshness import History, review_state
from hooks.metadata import build_schema
from scripts.fact_checks import content_hash, timestamp
from validate_freshness import audit


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

    def test_review_states_and_canonical_hash(self):
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

    def test_schema_parity_pending_omits_date(self):
        page = SimpleNamespace(canonical_url='https://example.org/test/', file=SimpleNamespace(src_uri='patterns/test.md'),
                               content='<h1>Test</h1>', title='Test', meta={})
        config = dict(site_url='https://example.org/', site_name='Test', site_description='Test')
        for revision in [self.revision(), {'state': 'pending'}, {'state': 'unavailable'}]:
            article = build_schema(page, config, {}, {'revision': revision})['@graph'][-1]
            self.assertEqual(article.get('dateModified'), revision.get('timestamp'))
            self.assertNotIn('datePublished', article)


class BuiltFreshnessTests(unittest.TestCase):
    def test_all_85_articles_and_nonarticle_exclusion(self):
        count, errors = audit(Path('.'), Path('site'))
        self.assertEqual(count, 85)
        self.assertEqual(errors, [])


if __name__ == '__main__':
    unittest.main()
