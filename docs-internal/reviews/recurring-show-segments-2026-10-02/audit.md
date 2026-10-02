# Recurring Show Segments — review handoff, 2026-10-02

Status: draft preserved for final owner review; NOT approved for publication, NOT pushed.

## Identity and disposition

- Canonical card: 7d58c975-d54b-4f8b-830e-aafc9cc247d0.
- Canonical draft: produce/audience-engagement/standardized-micro-segments.md. Keep this existing home/slug; display title is Recurring Show Segments.
- Superseded standalone: 44eb17f9-954c-45ad-94a5-b1b9514cb435. Owner authorized consolidation/retirement on 2026-10-02 21:38 UTC; that is not approval of this revised article.
- Standalone original moved byte-for-byte to docs-internal/archive/superseded/2026-10-02/gamified-branded-segments.md. Historical commits 0350a55 and ee6ccca6ff2360e28cb111e39e366711d49f710f both resolve. Card comments retain original evidence briefs and decisions.
- Isolated branch review/recurring-show-segments-20261002, based on current origin/main 260512e. No shared rejection manifest edited; no public docs/nav edits retained. No push while CTA worker 729792e7 is active.
- Original checkout's uncommitted gamified Quality Bar addition requires live facilitation/polls. It was inspected, deliberately NOT imported, and remains untouched in that checkout. It must not override this review artifact during later integration.

## Source audit

The canonical card's exact cited session was retrieved read-only from Airtable, including its full transcript lookup. The relevant discussion was read with the preceding career/interview exchange, transition, all segment questions and subsequent closing. Private source identifiers stay on the original card; no raw transcript, customer identity, or identifiers are copied into this repository.

- Setting: recorded podcast interview; two hosts and one guest. This is an activity actually performed in the recording, not a guest discussing a classroom/live-event exercise.
- 38:32–39:12: host explicitly pivots to recurring questions, describes their usual end placement, says questions are mostly reused, and announces a new question.
- 39:12–42:01: host/guest execute questions, answers and follow-ups. The newly added question is introduced at 41:31.
- 42:06–45:39: cohost adds an extended hypothetical and discussion. A rapid label therefore does not verify brevity.
- 45:46–46:02: host offers guest final word; closing answer follows.
- Observed: segment introduction and execution within this one transcript. Speaker assertion: regular recurrence across the show. Not independently verified: every-episode consistency, multiple-program validation, final edited runtime, audience response or retention lift.
- Standalone brief gives no resolvable original session locator for its reaction-test/snapshot claims. Search of local reports/vault and source history did not identify the original. These claims are not counted as verified examples. No cross-context analogy is used as evidence.

## Editorial decisions

Recommend purpose/setup/payoff plus permission to cut filler. Placement, names, length, questions and game mechanics are flexible. Three applications are explicitly hypothetical. Score 3/practitioner-observation is a provisional editorial assessment of utility and tradeoffs, not a benchmark or automatic numerical evidence cap. Previous score 4/internal-data and retention/cognitive-load/habit claims are retracted as unsupported by the checked evidence. Original customer identifier removed, not replaced with another.

## Test evidence and limits

- Publisher transform run via its exported read-only transform/scan functions; no executePlan/publication called. Draft and preview customer scans both clean; no transform warnings. Score 3 and evidence label parse correctly.
- Full section parity assertions compare draft and preview for all surviving sections; hypothetical examples and the score limitation survive removal of the Riggg Score section.
- Temporary transformed page was built at the intended canonical target, then moved out of docs before committing. Strict MkDocs build passed; site/link validator: 126 HTML pages, 8,105 internal references, zero errors. AEO validator: 125 classified pages (85 Article), zero errors.
- Preview regression run: 49/50 pass; existing freshness test hardcodes 84 articles and fails on the temporary 85th preview. Do not change that baseline expectation in this draft-only task. Final draft-only build/regression results are recorded in tests.txt.
- Publisher regressions: 114 pass / 1 fail. Failure is the existing corpus fixture requiring real-or-fake-style-segment-framing.md in the unrelated dirty checkout, where it is already deleted. Dashboard approval tests: 12 pass. No claim of all publisher tests passing; repair/reconcile that fixture before release. No unrelated test/source modifications made.
- Initial regression attempts lacked the expected site path; reran using a symlink to the built output. No resulting site files are committed.
- Related URLs resolve against existing published docs; no draft-as-public links. HTML-only checks, no live publication or browser acceptance claimed.

## Release gate

Owner must review the immutable canonical draft and authorize its exact digest before any public publication. Rebase/reconcile with active release work, rerun publication gates including the corpus-fixture check, then use the normal revision-bound publisher. This local commit is review evidence, not publication proof. Standalone done means superseded, never published. Canonical remains review.
