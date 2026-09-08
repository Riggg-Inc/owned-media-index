# OMI decision contract v1

Status: approved design contract; implementation pending  
Owner: IndexOps / Beacon  
Date: 2026-09-08  
Canonical store: Workboard board `owned-media-index`  
Human surface: `#team-owned-media-index` (`C0ALAP8LB26`)

This contract defines the machine-readable audit comments and the deterministic
projection used by the OMI decision digest. Workboard remains canonical. Slack
messages, buttons, and this backfill are projections; none is an independent
status store.

## 1. Marker records

A marker is the first non-empty line of a Workboard comment. The complete marker
must fit on that line. Human-readable text may follow after one blank line and is
not part of the record.

All v1 fields are required and occur in the order shown. One ASCII space (`SP`)
separates fields. Tabs, duplicate fields, unknown fields, invalid percent escapes,
and trailing spaces make the marker invalid. Parsers must reject malformed markers
rather than infer intent.

### 1.1 Grammar

The grammar is ABNF-like. Literal text is case-sensitive.

```abnf
decision-request = "DECISION-REQUEST v1"
                   SP "request=" request-id
                   SP "action=request"
                   SP "actor=" actor
                   SP "source=" request-source
                   SP "channel=" location
                   SP "message_ts=" message-ts
                   SP "timestamp=" timestamp
                   SP "card_revision=" revision

human-approve    = "HUMAN-DECISION v1"
                   SP "request=" request-id
                   SP "action=approve"
                   SP "actor=" actor
                   SP "source=" decision-source
                   SP "channel=" location
                   SP "message_ts=" message-ts
                   SP "timestamp=" timestamp
                   SP "card_revision=" revision

human-revise     = "HUMAN-DECISION v1"
                   SP "request=" request-id
                   SP "action=revise"
                   SP "actor=" actor
                   SP "source=" decision-source
                   SP "channel=" location
                   SP "message_ts=" message-ts
                   SP "timestamp=" timestamp
                   SP "card_revision=" revision
                   SP "notes=" pct-value

human-park       = "HUMAN-DECISION v1"
                   SP "request=" request-id
                   SP "action=park"
                   SP "actor=" actor
                   SP "source=" decision-source
                   SP "channel=" location
                   SP "message_ts=" message-ts
                   SP "timestamp=" timestamp
                   SP "card_revision=" revision
                   SP "reason=" pct-value
                   SP "revisit=" full-date

request-id       = "dr_" uuid
uuid             = 8HEXDIG "-" 4HEXDIG "-" 4HEXDIG "-" 4HEXDIG "-" 12HEXDIG
actor            = 1*128(A-Z / a-z / DIGIT / "." / "_" / ":" / "@" / "/" / "-")
request-source   = "workboard" / "legacy_approval_thread"
decision-source  = "slack_button" / "slack_modal" / "slack_typed" / "workboard"
location         = "-" / (ALPHA 1*(A-Z / DIGIT))
message-ts       = "-" / (10*DIGIT "." 6DIGIT)
timestamp        = full-date "T" 2DIGIT ":" 2DIGIT ":" 2DIGIT "." 3DIGIT "Z"
full-date        = 4DIGIT "-" 2DIGIT "-" 2DIGIT
revision         = 1*128(A-Z / a-z / DIGIT / "." / "_" / ":" / "-")
pct-value        = 1*(unreserved / pct-encoded)
unreserved       = A-Z / a-z / DIGIT / "-" / "." / "_" / "~"
pct-encoded      = "%" HEXDIG HEXDIG
```

UUID hexadecimal digits must be lowercase. Percent escapes must use uppercase
hexadecimal and decode to valid UTF-8. Spaces are `%20`; line breaks are `%0A`.
`notes` and `reason` must be non-empty after decoding.

### 1.2 Field semantics

| Field | Meaning |
|---|---|
| `request` | Globally unique decision opportunity. Never reuse an ID, including after revision or override. It is scoped to the containing Workboard card. |
| `action` | `request` on `DECISION-REQUEST`; exactly `approve`, `revise`, or `park` on `HUMAN-DECISION`. |
| `actor` | Principal that emitted the record. Requests use the Beacon service identity (`beacon`); Slack decisions use the immutable Slack user ID. Display names are not valid authorization identifiers. |
| `source` | Ingress path. Backfill requests use `legacy_approval_thread`; new requests use `workboard`. Human decisions record the exact button, modal, typed fallback, or direct Workboard path. |
| `channel` | Slack channel ID, normally `C0ALAP8LB26`. Use `-` only for a direct Workboard decision. Channel names are forbidden because they can change. |
| `message_ts` | Slack root/action message timestamp. A request points to its detail/approval thread; a button or modal points to its digest message; typed fallback points to the reply. Use `-` only with a direct Workboard decision. |
| `timestamp` | UTC time at which the record was created, with exactly millisecond precision. This is audit data; ordering uses the trusted Workboard comment creation time. |
| `card_revision` | Opaque immutable snapshot identifier for the approval payload. The initial adapter uses `wb_<updatedAt-ms>` captured before the request. A decision must repeat the request's value exactly. |
| `notes` | Required percent-encoded verbatim revision instruction. Only valid for `action=revise`. |
| `reason` | Required percent-encoded park reason. Only valid for `action=park`. A one-click default may use `deferred_by_approver`. |
| `revisit` | Required ISO 8601 calendar date for `action=park`. |

The containing comment supplies the Workboard card ID; duplicating it in the
marker is intentionally forbidden. Button payloads may carry card ID, request,
action, and revision, but the handler must resolve and validate the canonical
comment before writing a decision.

### 1.3 Examples

```text
DECISION-REQUEST v1 request=dr_123e4567-e89b-42d3-a456-426614174000 action=request actor=beacon source=workboard channel=C0ALAP8LB26 message_ts=1788894000.123456 timestamp=2026-09-08T19:00:00.000Z card_revision=wb_1788893999000
```

```text
HUMAN-DECISION v1 request=dr_123e4567-e89b-42d3-a456-426614174000 action=approve actor=U07H4T35DR8 source=slack_button channel=C0ALAP8LB26 message_ts=1788894100.654321 timestamp=2026-09-08T19:01:40.000Z card_revision=wb_1788893999000
```

```text
HUMAN-DECISION v1 request=dr_123e4567-e89b-42d3-a456-426614174000 action=revise actor=U07GY8FRN4E source=slack_modal channel=C0ALAP8LB26 message_ts=1788894200.654321 timestamp=2026-09-08T19:03:20.000Z card_revision=wb_1788893999000 notes=Clarify%20the%20measurement%20window%20and%20name%20the%20data%20source.
```

```text
HUMAN-DECISION v1 request=dr_123e4567-e89b-42d3-a456-426614174000 action=park actor=U07H4T35DR8 source=slack_button channel=C0ALAP8LB26 message_ts=1788894300.654321 timestamp=2026-09-08T19:05:00.000Z card_revision=wb_1788893999000 reason=deferred_by_approver revisit=2026-10-08
```

### 1.4 Parsing, validity, and conflict rules

1. Read comments in trusted Workboard creation order. The supplied `timestamp`
   never controls precedence.
2. Parse only a comment whose first non-empty line begins with an exact marker
   name. Match the entire marker line against the v1 grammar. Ignore later
   human-readable lines.
3. Reject a request ID found on more than one card. Reject a human decision unless
   the same card contains an earlier valid request with matching `request` and
   `card_revision`.
4. Validate the actor/channel allowlist outside the parser. The production Slack
   handler accepts only the approved Garren/Ledge Slack IDs and channel
   `C0ALAP8LB26`; a syntactically valid unauthorized marker is not a valid decision.
5. A request is current only when it is the newest valid request for the card,
   follows the most recent transition into `ready`, and its approval payload still
   resolves to `card_revision`. A changed draft or a new `ready` cycle requires a
   new request ID and revision.
6. The first valid human decision for a current request wins. An identical retry
   by the same actor is an idempotent no-op returning the original outcome. Any
   later conflicting action is rejected and audited; it never mutates state.
7. A stale request/revision, ineligible card, wrong status, wrong channel, or
   unauthorized actor produces no Workboard mutation and no success response.
8. `APPROVAL-THREAD:` is legacy discovery metadata, not a canonical decision
   record. It is used only to seed the read-only backfill below. After launch, all
   state transitions must be backed by valid v1 markers.

## 2. Decision-state projection

### 2.1 Hard exclusions

Hard exclusions run before marker evaluation. The following are never
human-decision cards and must not appear in the digest, even if status is `ready`
or a marker was added accidentally:

- role charters: title contains the exact token `[ROLE]` or label `role-charter`;
- version/seed/epic cards: title contains a token beginning `[V0.`;
- titles containing `[AUDIT]`, `[AEO-REPORT]`, or `[BUILD]`;
- drafts in `review` or otherwise still awaiting the Auditor gate.

An excluded card with a decision marker raises a projection-integrity diagnostic;
the marker does not override the exclusion. Ordinary agent-to-agent workflow
states are never inferred to be human decisions.

### 2.2 Projection algorithm

For a non-excluded pattern, teardown, or explicitly designated framework-decision
card, select the newest current `DECISION-REQUEST`. Then select the first valid
`HUMAN-DECISION` for that request.

| Human state | Deterministic rule | Expected canonical status/effect |
|---|---|---|
| **Needs Decision** | Current request exists, no valid later human decision exists, and card status is `ready`. | Actionable and eligible for ranking in the digest. |
| **In Revision** | Winning action is `revise` and no newer request exists. | Move to `todo`, then `running`/`review` in the Scribe–Auditor loop. It remains non-actionable while in Auditor review. A new approved revision gets a new request and becomes Needs Decision. |
| **Approved** | Winning action is `approve` and publish proof is not complete. | Projection code is `approved_pending_publish`. Approval removes the item from Needs Decision but does not mark it done. Beacon queues the existing publication path. |
| **Parked** | Winning action is `park` and no newer request exists. | Move to backlog/hold and retain `reason` plus `revisit`. Reaching the revisit date prompts reassessment but never auto-approves, auto-publishes, or creates a new request. |

Publication closes an Approved item only when canonical publish proof exists (a
`PUBLISHED:` record with artifact and commit) and the Workboard card is `done`.
Until both are true, it remains `approved_pending_publish`; a failed publish is an
operational error, not a new human decision. Once both are true the card is
`published` and leaves the active four-state decision projection.

Status/marker disagreements do not get guessed into a state. Preserve the last
valid marker-derived state, add a drift diagnostic, and require the owning worker
to repair the canonical status.

## 3. Read-only legacy backfill (2026-09-08)

Method: list `ready` cards on `owned-media-index`, then read each card and retain
only live `APPROVAL-THREAD:` comments. The result is nine cards: eight candidate
patterns and the August teardown. Two ready candidates without an approval thread
(`podcasting2-transcript-namespace` and
`platform-ad-skipping-monetization-resilience`) are excluded. The unrelated ready
teardown is included because it has a live approval thread and teardown reports
are eligible human decisions.

Age is whole elapsed UTC days from the legacy Slack thread timestamp to
2026-09-08T19:26:33Z. Request IDs are reserved now and must be preserved if the
handler later persists this backfill. No source card was commented, moved, or
otherwise mutated, and no Slack message was posted.

| Card ID | Request ID | Slug | Thread ts | Age |
|---|---|---|---:|---:|
| `02c84b08-f036-413f-a71d-cedcf7733c8d` | `dr_7a4f6689-c477-42b7-84d4-05416ea1e465` | `teardown-2026-08` | `1787231209.328659` | 19d |
| `322075f9-810d-416d-bc89-0acce751e698` | `dr_69cdfddc-b1d8-4b68-83ec-2ab23c5fdbd8` | `preserve/ai-disclosure-provenance-owned-asset` | `1787403706.266599` | 17d |
| `4df042ae-7b97-4270-a2aa-c6c99f3ba8da` | `dr_b9d5acc8-d390-4201-8f8d-098f746c191a` | `owned-website-as-format-hub` | `1787576496.637079` | 15d |
| `54b74531-2d42-48b7-b1ed-35bb8a364348` | `dr_75ab9682-399e-40cd-bc4f-62606e87fef1` | `publish/owned-email-newsletter` | `1787749287.304979` | 13d |
| `9c6cf292-bf3b-4a6d-8ffb-35b9e85302cb` | `dr_6d21a77b-c76c-4747-a7d6-e84210817ff5` | `video-threshold-economics` | `1787922069.154899` | 11d |
| `b348d523-b4a3-4b75-88fa-12340767eca9` | `dr_ed48993e-bb07-4d37-a027-5adf5335b763` | `webinar-platform-consolidation-risk` | `1788094909.482169` | 9d |
| `71d51a9c-48cf-4dc4-824f-fb5073778226` | `dr_2e2ebdaf-9a89-475a-b240-ba37fd9b0bd6` | `spotify-native-upload-bypasses-rss` | `1788267700.515879` | 7d |
| `f267c3c3-9e5d-4927-85ab-2ac4bdcb5510` | `dr_47e5887c-702d-47b8-b669-bdc1059a8ea4` | `amp-accords-play-standard` | `1788440500.213019` | 5d |
| `a5b59382-f752-43eb-849d-c5da3d2dc480` | `dr_9a261a80-b7aa-4ab0-8f82-686a79544c9f` | `geo-aeo-citation-volatility` | `1788613274.871269` | 3d |

### 3.1 DECISION-REQUEST projection entries

These are projection records only; they have not been appended to the cards.

```text
DECISION-REQUEST v1 request=dr_7a4f6689-c477-42b7-84d4-05416ea1e465 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1787231209.328659 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1787231219752
DECISION-REQUEST v1 request=dr_69cdfddc-b1d8-4b68-83ec-2ab23c5fdbd8 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1787403706.266599 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1787403713889
DECISION-REQUEST v1 request=dr_b9d5acc8-d390-4201-8f8d-098f746c191a action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1787576496.637079 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1787576504189
DECISION-REQUEST v1 request=dr_75ab9682-399e-40cd-bc4f-62606e87fef1 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1787749287.304979 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1787749292908
DECISION-REQUEST v1 request=dr_6d21a77b-c76c-4747-a7d6-e84210817ff5 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1787922069.154899 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1787922077754
DECISION-REQUEST v1 request=dr_ed48993e-bb07-4d37-a027-5adf5335b763 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1788094909.482169 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1788094914468
DECISION-REQUEST v1 request=dr_2e2ebdaf-9a89-475a-b240-ba37fd9b0bd6 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1788267700.515879 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1788267709389
DECISION-REQUEST v1 request=dr_47e5887c-702d-47b8-b669-bdc1059a8ea4 action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1788440500.213019 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1788440507415
DECISION-REQUEST v1 request=dr_9a261a80-b7aa-4ab0-8f82-686a79544c9f action=request actor=beacon source=legacy_approval_thread channel=C0ALAP8LB26 message_ts=1788613274.871269 timestamp=2026-09-08T19:26:33.000Z card_revision=wb_1788613279697
```
