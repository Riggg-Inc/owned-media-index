#!/usr/bin/env python3
"""Fail-closed research selection. No network, publication or Workboard mutations."""
import argparse, copy, datetime as dt, json, os, pathlib, sys
TRACKS = {'research-queued', 'research-active', 'owner-hold', 'closed'}
DISPOSITIONS = {'draft', 'consolidate', 'retire'}
def date(s): return dt.date.fromisoformat(s)
def validate(state):
    assert state['schema_version'] == 1 and state['max_active_topics'] == 3
    assert state['remaining_triage_due'] == '2026-10-21'
    seen = set()
    for t in state['topics']:
        assert t['track'] in TRACKS
        for k in ('owner','question','next_action','canonical_relationship','authorization'): assert t[k]
        for c in [t['card_id']] + t['canonical_relationship']['aliases']:
            assert c not in seen, 'duplicate canonical/alias card'; seen.add(c)
        assert t['extension_count'] in (0,1)
        if t['track'].startswith('research-'):
            date(t['due_date']); assert t['owner'] == 'orrin-deepforge'
        if t['track'] == 'research-queued':
            assert t['due_date'] <= state['remaining_triage_due'], 'finite triage deadline exceeded'
        if t['track'] == 'research-active':
            assert 0 <= (date(t['due_date'])-date(t['started_date'])).days <= 7*(1+t['extension_count'])
        if t['extension_count']:
            assert all(t['source_blocker'].get(k) for k in ('source','retrieval_action','decision_impact'))
        if t['track'] == 'closed':
            assert t['final_disposition'] in DISPOSITIONS and t['outcome_artifact'] and t['completed_date']
    assert sum(t['track']=='research-active' for t in state['topics']) <= 3, 'WIP exceeds three topics'
    return True

def reconcile(state, board, today, now=None):
    validate(state)
    now = now or dt.datetime.now(dt.timezone.utc)
    captured = dt.datetime.fromisoformat(board['captured_at'].replace('Z','+00:00'))
    assert 0 <= (now-captured).total_seconds() <= 1800, 'snapshot stale/future; refresh native board reads'
    cards = {c['id']:c for c in board['cards']}
    assert len(cards)==len(board['cards']), 'duplicate snapshot cards'
    errors=[]
    for t in state['topics']:
        for cid in [t['card_id']]+t['canonical_relationship']['aliases']:
            c=cards.get(cid)
            if c is None: errors.append(cid+': missing current card'); continue
            if cid != t['card_id']:
                if c['status'] not in ('done','backlog'): errors.append(cid+': alias independently active')
                continue
            if t['track'].startswith('research-'):
                required={t['track'],'no-auto-draft','due:'+t['due_date']}
                if not required.issubset(set(c.get('labels',[]))): errors.append(cid+': control labels drift')
                if c.get('agentId')!=t['owner']: errors.append(cid+': assignee drift')
                if c['status'] not in ('backlog','running'): errors.append(cid+': unsafe research status')
                if t['track']=='research-queued' and c['status']=='running': errors.append(cid+': queued card running')
                if t['track']=='research-active' and any(x in c.get('labels',[]) for x in ('owner-held','cleanup-hold','research-hold')): errors.append(cid+': unreleased hold')
            if t['track']=='owner-hold' and c['status'] not in ('backlog','blocked'): errors.append(cid+': owner hold advanced')
            if t['track']=='closed' and t['final_disposition']!='draft' and c['status'] not in ('done','backlog'): errors.append(cid+': closed research unexpectedly active')
    assert not errors, '; '.join(errors)
    return cards

def plan(state, board, today, now=None):
    cards=reconcile(state,board,today,now)
    active=[t for t in state['topics'] if t['track']=='research-active']
    queued=[t for t in state['topics'] if t['track']=='research-queued']
    return {'active_topics':len(active),'free_slots':3-len(active),
      'research_assignments':[t['card_id'] for t in sorted(active,key=lambda t:(t['due_date'],t['topic_id'])) if t['due_date']>=today and cards[t['card_id']]['status']=='backlog'],
      'overdue':[t['card_id'] for t in active+queued if t['due_date']<today],
      'triage_due':[t['card_id'] for t in queued if t['due_date']<=today],
      'queued_topics':len(queued),'owner_held_topics':sum(t['track']=='owner-hold' for t in state['topics']),
      'completed_outcomes':{d:sum(t['track']=='closed' and t['final_disposition']==d for t in state['topics']) for d in DISPOSITIONS}}

def transition(state, topic, action, today, payload):
    result=copy.deepcopy(state); t=next(t for t in result['topics'] if t['topic_id']==topic)
    assert t['track']!='owner-hold', 'explicit owner holds cannot be changed here'
    if action=='activate':
        assert t['track']=='research-queued' and today<=t['due_date'], 'queued triage expired'
        assert payload.get('scope_evidence') and payload.get('scope_passed') is True and payload.get('semantic_review') is True
        assert t['authorization']=='owner-2026-10-07T21:15Z'
        t.update(track='research-active',started_date=today,due_date=(date(today)+dt.timedelta(days=7)).isoformat(),scope_evidence=payload['scope_evidence'])
    elif action=='extend':
        assert t['track']=='research-active' and t['extension_count']==0
        assert all(payload.get(k) for k in ('source','retrieval_action','decision_impact'))
        assert date(today)<=date(t['due_date'])+dt.timedelta(days=1), 'late escalation is not an extension'
        assert date(t['due_date'])<date(payload['due_date'])<=date(t['due_date'])+dt.timedelta(days=7)
        t.update(extension_count=1,source_blocker={k:payload[k] for k in ('source','retrieval_action','decision_impact')},due_date=payload['due_date'])
    elif action=='close':
        assert t['track'] in ('research-active','research-queued')
        d=payload['disposition']; assert d in DISPOSITIONS and payload.get('artifact') and payload.get('reason')
        if d in ('draft','consolidate'):
            assert payload.get('scope_evidence') and payload.get('scope_passed') is True and payload.get('semantic_review') is True and payload.get('sources'), 'no sources is not a supported outcome'
        if d=='draft': assert t['track']=='research-active', 'draft requires active topic'
        if d=='consolidate': assert payload.get('target') and payload['target']!=t['card_id']
        if d=='retire': assert payload.get('reversible') is True and payload.get('reason') in ('research-not-supported','out-of-scope','duplicate')
        t.update(track='closed',final_disposition=d,outcome_artifact=payload['artifact'],completed_date=today,scope_evidence=payload.get('scope_evidence'),drafting_released=d=='draft' and payload.get('drafting_released') is True)
        t['outcome_details']=payload
    else: raise AssertionError('unknown transition')
    result['history'].append({'date':today,'topic_id':topic,'action':action,'details':payload})
    validate(result); return result

def eligible(state, board, today, card, now=None):
    reconcile(state,board,today,now)
    t=next((t for t in state['topics'] if card==t['card_id'] or card in t['canonical_relationship']['aliases']),None)
    return {'eligible':bool(t and card==t['card_id'] and t['track']=='closed' and t['final_disposition']=='draft' and t['drafting_released'] and t['scope_evidence']), 'reason':'research release only; scope and editorial/publication gates still apply' if t else 'untracked: use existing correction/ops gates; not research authorization'}

def main():
    p=argparse.ArgumentParser(); p.add_argument('command',choices=['validate','plan','eligible','transition']);p.add_argument('--state',required=True);p.add_argument('--board');p.add_argument('--today',default=dt.datetime.now(dt.timezone.utc).date().isoformat());p.add_argument('--card');p.add_argument('--topic');p.add_argument('--action');p.add_argument('--payload');p.add_argument('--output')
    a=p.parse_args();s=json.loads(pathlib.Path(a.state).read_text());date(a.today)
    if a.command=='validate': out={'valid':validate(s)}
    else:
        b=json.loads(pathlib.Path(a.board).read_text())
        if a.command=='plan':out=plan(s,b,a.today)
        elif a.command=='eligible':out=eligible(s,b,a.today,a.card)
        else:
            reconcile(s,b,a.today)
            assert a.output and pathlib.Path(a.output).resolve()!=pathlib.Path(a.state).resolve(), 'write reviewed transition to separate file; no blind state overwrite'
            out=transition(s,a.topic,a.action,a.today,json.loads(pathlib.Path(a.payload).read_text()))
            pathlib.Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':
    try: main()
    except (AssertionError,KeyError,ValueError,TypeError,StopIteration) as e:
        print(json.dumps({'eligible':False,'error':str(e) or 'invalid control state'}));sys.exit(2)
