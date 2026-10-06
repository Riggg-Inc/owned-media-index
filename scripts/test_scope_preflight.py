"""Controlled synthetic replay; no search, network, or real cards created."""
import copy
import hashlib
import json
import unittest
from scope_preflight import ROOT, SCHEMA, validate

BASE = {k: 'Synthetic fixture context, not research evidence' for k,r in SCHEMA['properties'].items() if r.get('type') == 'string'}
BASE.update(slug='recurring-recorded-segment', asset='Recorded B2B educational episode', source_locator='offline synthetic full passage', source_context='Host asks every guest the same closing question, records the answer, and edits it into each published episode. The topic is workplace training; no learners are routed.', modality='recorded interview', participants='host, guest and episode editor', observed_action='Host records recurring question; editor preserves segment', demonstrates='Recurring recorded format; no measured retention lift', interviewed_topic='B2B workplace learning', audience_outcome='Repeatable segment navigation; retention lift unknown', outcome_stage_link='Produce: consistent episode structure', mechanism='recorded-production', stage='Produce', full_context_read=True, medium_practice=True, semantic_duplicate_found=False, register_checked=True, existing_cards_checked=True, related_card_ids=[], scope_decision='eligible')

class ScopeTests(unittest.TestCase):
    def test_positive_medium_examples(self):
        for name, mechanism, stage in [('recurring-recorded-segment','recorded-production','Produce'), ('ai-assisted-episode-naming','media-packaging','Package'), ('owned-recording-library','owned-preservation','Preserve'), ('b2b-educational-episode','recorded-production','Produce'), ('owned-episode-newsletter','owned-distribution','Publish'), ('recorded-guest-preparation','recording-guest-preparation','Produce')]:
            with self.subTest(name=name):
                r=dict(BASE,slug=name,mechanism=mechanism,stage=stage)
                self.assertEqual(validate(r), [])
    def test_training_topic_is_not_media_practice(self):
        r=dict(BASE,slug='renamed-owned-learning',source_context='Guest describes surveying learners, routing low recognition scores to a recognition track, then measuring learner improvement. Host interviews guest about training; no recording workflow is demonstrated.', observed_action='Trainer routes learners by baseline survey deficits', demonstrates='Training program design', mechanism='cohort-routing',medium_practice=False)
        self.assertTrue(validate(r))
    def test_all_explicit_blocked_mechanisms(self):
        reg=json.loads((ROOT/'docs-internal/intake-suppressions.json').read_text())
        for mechanism in reg['blocked_mechanisms']:
            self.assertTrue(validate(dict(BASE,mechanism=mechanism)))
    def test_missing_each_field(self):
        for key in SCHEMA['required']:
            r=copy.deepcopy(BASE); del r[key]
            self.assertTrue(validate(r), key)
    def test_snippet_counts_and_semantic_duplicate_do_not_pass(self):
        for change in [dict(full_context_read=False), dict(semantic_duplicate_found=True), dict(register_checked=False),dict(medium_practice=False),dict(full_context_read=1),dict(scope_decision='borderline')]:
            self.assertTrue(validate(dict(BASE,**change)))
    def test_retired_slug_and_duplicate_ids(self):
        reg=json.loads((ROOT/'docs-internal/intake-suppressions.json').read_text())
        for slug in reg['retired_slugs']+reg['superseded_slugs']:
            self.assertTrue(validate(dict(BASE,slug='Produce/'+slug+'.md')))
        for id in reg['suppressed_card_ids']:
            self.assertTrue(validate(dict(BASE,related_card_ids=[id])))
    def test_actual_retired_source_mechanism(self):
        source=(ROOT/'docs-internal/archive/rejected/data-driven-targeted-learning.md').read_text()
        self.assertIn('Routing individuals into specific learning tracks', source)
        self.assertIn('baseline engagement survey metrics', source)
        self.assertTrue(validate(dict(BASE,source_context=source,mechanism='cohort-routing',medium_practice=False)))
    def test_facilitated_peer_retirement_and_duplicate(self):
        source=(ROOT/'docs-internal/archive/rejected/facilitated-peer-connection.md').read_text()
        self.assertIn('audience is encouraged to connect with one another', source)
        self.assertTrue(validate(dict(BASE,slug='facilitated-peer-connection')))
        for card in ['a34ea862-3aa4-4873-bb71-e7dd9d8fe107', '73075383-ed4a-4389-8873-493ea2150b70']:
            self.assertTrue(validate(dict(BASE,slug='renamed-peer-networking',related_card_ids=[card])))
        self.assertTrue(validate(dict(BASE,slug='renamed-peer-networking',source_context=source,mechanism='keynote-facilitation',medium_practice=False)))
    def test_real_recurring_draft_not_suppressed(self):
        source=(ROOT/'produce/audience-engagement/standardized-micro-segments.md').read_text()
        self.assertIn('purpose', source)
        self.assertIn('payoff', source)
        self.assertEqual(validate(dict(BASE,slug='standardized-micro-segments',source_context=source)), [])
    def test_archive_hash(self):
        reg=json.loads((ROOT/'docs-internal/intake-suppressions.json').read_text())
        for slug, provenance in reg['archive'].items():
            self.assertEqual(hashlib.sha256((ROOT/'docs-internal/archive/rejected'/ (slug+'.md')).read_bytes()).hexdigest(), provenance['sha256'])

if __name__ == '__main__':
    unittest.main()
