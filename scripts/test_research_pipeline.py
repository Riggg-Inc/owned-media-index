import copy, datetime as dt, json, pathlib, unittest
import research_pipeline as r
ROOT=pathlib.Path(__file__).resolve().parents[1]
class ResearchTests(unittest.TestCase):
 def setUp(self):
  self.s=json.loads((ROOT/'docs-internal/research-pipeline.json').read_text()); self.now=dt.datetime(2026,10,7,22,tzinfo=dt.timezone.utc)
  cards=[]
  for t in self.s['topics']:
   cards.append({'id':t['card_id'],'status':'backlog','agentId':t['owner'],'labels':[t['track'],'no-auto-draft','due:'+str(t['due_date'])]})
   cards.extend({'id':a,'status':'done'} for a in t['canonical_relationship']['aliases'])
  self.b={'captured_at':self.now.isoformat(),'cards':cards}
 def plan(self,day='2026-10-07'):return r.plan(self.s,self.b,day,self.now)
 def test_three_topic_slots(self):self.assertEqual(self.plan()['active_topics'],3);self.assertEqual(self.plan()['free_slots'],0)
 def test_aliases_do_not_add_slots(self):self.assertEqual(len(self.plan()['research_assignments']),3)
 def test_expired_not_assigned(self):self.assertEqual(self.plan('2026-10-15')['research_assignments'],[]);self.assertGreaterEqual(len(self.plan('2026-10-15')['overdue']),3)
 def test_queue_finite(self):self.assertEqual(self.plan()['queued_topics'],20);self.assertTrue(all(t['due_date']<='2026-10-21' for t in self.s['topics'] if t['track']=='research-queued'))
 def test_holds_excluded(self):self.assertEqual(self.plan()['owner_held_topics'],23)
 def test_owner_hold_cannot_retire(self):
  with self.assertRaises(AssertionError):r.transition(self.s,next(t['topic_id'] for t in self.s['topics'] if t['track']=='owner-hold'),'close','2026-10-14',{'disposition':'retire','artifact':'note','reason':'research-not-supported','reversible':True})
 def test_one_extension(self):
  p={'source':'https://primary/source','retrieval_action':'retrieve dated notice','decision_impact':'verifies current access','due_date':'2026-10-21'}
  s=r.transition(self.s,'8ad3af51','extend','2026-10-14',p)
  with self.assertRaises(AssertionError):r.transition(s,'8ad3af51','extend','2026-10-21',{**p,'due_date':'2026-10-28'})
 def test_extension_requires_source(self):
  with self.assertRaises(AssertionError):r.transition(self.s,'8ad3af51','extend','2026-10-14',{'due_date':'2026-10-21'})
 def test_duplicate_rejected(self):
  self.s['topics'][1]['canonical_relationship']['aliases'].append(self.s['topics'][0]['card_id'])
  with self.assertRaises(AssertionError):self.plan()
 def test_todo_promotion_rejected(self):
  self.b['cards'][0]['status']='todo'
  with self.assertRaises(AssertionError):self.plan()
 def test_missing_card_fail_closed(self):
  self.b['cards'].pop()
  with self.assertRaises(AssertionError):self.plan()
 def test_stale_snapshot_fail_closed(self):
  self.b['captured_at']='2026-10-06T00:00:00+00:00'
  with self.assertRaises(AssertionError):self.plan()
 def test_no_source_not_supported_draft(self):
  with self.assertRaises(AssertionError):r.transition(self.s,'8ad3af51','close','2026-10-14',{'disposition':'draft','artifact':'memo','reason':'looks good'})
 def test_reversible_unsupported_not_false(self):
  s=r.transition(self.s,'8ad3af51','close','2026-10-14',{'disposition':'retire','artifact':'attempt ledger','reason':'research-not-supported','reversible':True})
  self.assertFalse(s['topics'][0]['drafting_released']);self.assertEqual(s['topics'][0]['outcome_details']['reason'],'research-not-supported')
 def test_active_not_scribe_eligible(self):self.assertFalse(r.eligible(self.s,self.b,'2026-10-07',self.s['topics'][0]['card_id'],self.now)['eligible'])
 def test_fourth_topic_blocked(self):
  t=next(t for t in self.s['topics'] if t['track']=='research-queued')
  with self.assertRaises(AssertionError):r.transition(self.s,t['topic_id'],'activate','2026-10-07',{'scope_evidence':'scope.json','scope_passed':True,'semantic_review':True})
 def test_free_slot_replenishes_only_scoped_queue(self):
  s=r.transition(self.s,'8ad3af51','close','2026-10-08',{'disposition':'retire','artifact':'attempt ledger','reason':'research-not-supported','reversible':True})
  q=next(t for t in s['topics'] if t['track']=='research-queued')
  with self.assertRaises(AssertionError):r.transition(s,q['topic_id'],'activate','2026-10-08',{})
  s=r.transition(s,q['topic_id'],'activate','2026-10-08',{'scope_evidence':'scope.json','scope_passed':True,'semantic_review':True})
  self.assertEqual(sum(t['track']=='research-active' for t in s['topics']),3)
 def test_independent_alias_running_fails(self):
  alias=self.s['topics'][0]['canonical_relationship']['aliases'][0]
  next(c for c in self.b['cards'] if c['id']==alias)['status']='running'
  with self.assertRaises(AssertionError):self.plan()
 def test_supported_proposal_requires_explicit_drafting_release(self):
  p={'disposition':'draft','artifact':'complete-proposal.md','reason':'supported narrow practice','scope_evidence':'scope.json','scope_passed':True,'semantic_review':True,'sources':['primary']}
  s=r.transition(self.s,'8ad3af51','close','2026-10-14',p)
  self.assertFalse(r.eligible(s,self.b,'2026-10-14',s['topics'][0]['card_id'],self.now)['eligible'])
  s=r.transition(self.s,'8ad3af51','close','2026-10-14',{**p,'drafting_released':True})
  self.assertTrue(r.eligible(s,self.b,'2026-10-14',s['topics'][0]['card_id'],self.now)['eligible'])
 def test_no_unknown_auto_release(self):self.assertFalse(r.eligible(self.s,self.b,'2026-10-07','unknown',self.now)['eligible'])
if __name__=='__main__':unittest.main()
