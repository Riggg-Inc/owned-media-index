"""Body revision provenance, separate from evidence-backed factual review.

First-parent history means a merge's publication time, not an unpublished branch
commit. Renames retain provenance. No build time or YAML date is a fallback.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import subprocess

from scripts.fact_checks import (HIGH_RISK, body_bytes, content_hash, iso,
                                load_reviews, timestamp, validate_review)


class History:
    def __init__(self, root):
        self.root = Path(root)
        self.cache = {}

    def git(self, *args):
        return subprocess.check_output(['git', '-C', str(self.root), *args], stderr=subprocess.DEVNULL)

    def revision(self, source, raw):
        if isinstance(raw, str):
            raw = raw.encode('utf-8')
        key = (source, raw)
        if key not in self.cache:
            self.cache[key] = self._revision(source, raw)
        return self.cache[key]

    def _revision(self, source, raw):
        try:
            body = body_bytes(raw)
            try:
                committed = self.git('show', 'HEAD:' + source)
            except subprocess.CalledProcessError:
                return {'state': 'pending'}
            if body_bytes(committed) != body:
                return {'state': 'pending'}
            if self.git('rev-parse', '--is-shallow-repository').strip() != b'false':
                return {'state': 'unavailable'}
            path, candidate = source, None
            for commit in self.git('rev-list', '--first-parent', 'HEAD').decode().splitlines():
                try:
                    snapshot = self.git('show', commit + ':' + path)
                except subprocess.CalledProcessError:
                    break
                if body_bytes(snapshot) != body:
                    break
                candidate = commit
                changes = self.git('diff-tree', '--first-parent', '--no-commit-id', '--name-status', '-r', '-M', commit).decode()
                for change in changes.splitlines():
                    fields = change.split('\t')
                    if len(fields) == 3 and fields[0].startswith('R') and fields[2] == path:
                        path = fields[1]
                        break
            if not candidate:
                return {'state': 'unavailable'}
            date = datetime.fromisoformat(self.git('show', '-s', '--format=%cI', candidate).decode().strip()).astimezone(timezone.utc)
            if date > datetime.now(timezone.utc):
                return {'state': 'unavailable'}
            return {'state': 'committed', 'timestamp': iso(date),
                    'date': date.strftime('%B %-d, %Y'), 'commit': candidate}
        except (subprocess.CalledProcessError, OSError, ValueError):
            return {'state': 'unavailable'}


def review_state(record, path, source, now=None):
    if record is None:
        return {'state': 'unrecorded', 'label': 'No fact-check recorded'}
    failed = {'state': 'needs-review', 'label': 'Fact-check needs review'}
    now = now or datetime.now(timezone.utc)
    if validate_review(record, now):
        return failed
    body = body_bytes(path.read_bytes())
    high = source.startswith('tools/') or bool(HIGH_RISK.search(source.replace('-', ' ') + '\n' + body.decode('utf-8')))
    checked = timestamp(record['checked_at'])
    due = min(timestamp(record['next_review_at']), checked + timedelta(days=30 if high else 90))
    if record['content_sha256'] != content_hash(path) or due <= now:
        return failed
    return {'state': record['status'],
            'label': 'Last fact-checked' if record['status'] == 'verified' else 'Partial fact-check',
            'timestamp': iso(checked), 'date': checked.strftime('%B %-d, %Y'),
            'reviewer': record['reviewer'], 'method': record['method'],
            'sources': record['sources'], 'next_review_at': iso(due)}


def page_freshness(root, source, history=None, reviews=None):
    root = Path(root)
    path = root / 'docs' / source
    history = history or History(root)
    reviews = load_reviews(root / 'data/fact-checks.json')[0] if reviews is None else reviews
    return {'revision': history.revision('docs/' + source, path.read_bytes()),
            'review': review_state(reviews.get(source), path, source)}
