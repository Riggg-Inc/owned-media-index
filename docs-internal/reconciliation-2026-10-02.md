# Repository / Workboard reconciliation — 2026-10-02

Owner authorized safe duplicate cleanup, not editorial approval. Base `177f1107feb4267e85f5b0c832e142af9f300b62` (origin/main at isolated-worktree creation). No push/deployment by this pass. Dirty local main and all other worktrees preserved. Library release card b348d523, Content Memory source/docs, Preserve hub, and published AI audience guidance untouched.

## Completed

- Read 112 full Workboard tool objects, including notes, comments, artifacts, approvals and claims. Stored raw snapshots outside repo under `/tmp/omi-board-full.json` and `/tmp/omi-board-final.json`; no private card prose copied into public docs.
- Three exact duplicate tasks closed as **superseded, NOT published**, with reciprocal canonical comments. No cards deleted; expired claims released only on the two redundant claimed cards.

| Closed redundant | Canonical retained | Evidence |
|---|---|---|
| 83c11644-d19c-4e09-b49e-e9861d41242f | 047c5c2d-ef27-4db9-adc6-7740fb4e21dd | Identical targeted-learning evidence brief; Sept30 explicit duplicate finding; draft at 41840f8. |
| c28ddb78-e85e-4909-9c03-66d64117b9dd | 8ad3af51-07a0-4848-927e-5549d86f7112 | Identical in-app brief/task; ed5963d redundant draft; canonical 789dd1a has substantive evidence paragraph. |
| 73075383-ed4a-4389-8873-493ea2150b70 | a34ea862-3aa4-4873-bb71-e7dd9d8fe107 | Identical peer-connection brief; redundant has no separate draft/revision; canonical 2f8764d. |

Canonical draft paths, none public on this base:
- `produce/data-driven-targeted-learning/data-driven-targeted-learning.md` (local-main history).
- `publish/in-app-thought-leadership-retention/embedding-thought-leadership-in-product-interface.md` (local-main history; original card misreported filename).
- `produce/audience-engagement/facilitated-peer-connection.md` (local-main history).

Rejected two-part-hook draft moved byte-for-byte to `docs-internal/archive/rejected/`, outside MkDocs and root drafting directories. Removed one stale recommendation from the immersive-learning root draft. Both September30 rejection cards remain done and unchanged. Existing CI unittest discovery now tests against rejected-slug resurrection; it does not prevent a separate external automation from writing a draft before CI runs.

## Inventory and non-duplicates

Machine manifest `reconciliation-2026-10-02.json`: 176 source/docs representations with hashes, card matches and inferred public routes. Mirrors are intentional, not duplicates. 141 card path references: 90 current, 21 external workspace, 16 moved/history candidates, 9 local-main-only, 2 corrected historical filenames, 1 intentional negative test, 2 unresolved. All 98 extracted commit mentions resolve across OMI and openclaw-workspace; none warrants a fabrication claim.

No docs page lacked both a Markdown inbound link and nav entry. Built-site validator checked 8,035 internal link/resource references across 125 HTML pages: zero errors. This is not semantic proof that every article belongs or every graph node is reachable from the homepage.

Distinct rescore/revision/retirement tasks remain open. In-app retirement card `3333b5c0` is an implementation task, not another duplicate editorial card. Its redundant draft is present only in dirty/local main, absent from origin/main; this branch cannot remove that file without importing unpublished commits. Preserve those changes for separately serialized reconciliation.

## Decisions / evidence blockers still open

- `e64c4314` versus `1e068e6a`: asynchronous baseline re-grounding versus existing blocked-safety revision; overlapping source but not an identical revision task. Keep both pending editorial evidence reconciliation.
- `a3af20c0` versus `1ad7cc9f`: kinesthetic re-grounding has different source context; historical draft c38af5e0 actually exists in **openclaw-workspace**, current OMI alternative is c87e004. Corrected old missing/fabrication implication on 1ad7cc9f; do not close merely by slug.
- `b6643937`: event-content draft/hash ec19b1e9 exists in **openclaw-workspace**. Commented location correction; no automatic public import.
- Canonical targeted-learning and facilitated-peer cards received explicit source-context/scope review findings; remain review, not approved. Other live-facilitation-adjacent drafts (immersive learning, warmup, strategic pause, asynchronous baseline, networking) need full-context editorial judgment, not blanket rejection.
- Two unresolved references: Scribe charter `schemas/pattern.schema.md` (actual schema directory needs owner/maintainer reconciliation), and ad-metadata card b2058cc8 referring to `prove/measurement-provenance/amp-accords-iab-v2.3.md` (likely obsolete reference; do not invent a target).

## Verification and final board

Strict build passed; site links/breadcrumb validator: 125 HTML pages, 8,035 references, 0 errors. AEO: 124 pages (12 WebPage, 28 CollectionPage, 84 Article), 0 errors. Video source/public parity passed. All 28 regression tests passed. No public-page takedown, score change, Workshop/scheduler edit, Slack post or deployment.

Final live board: **112 cards = 27 backlog + 40 todo + 15 ready + 6 running + 5 review + 1 blocked + 18 done**. Done includes rejected/superseded, not just published. Changed cards: three closed above; canonical three commented; 1ad7cc9f and b6643937 history correction comments. No other statuses changed.

Coverage limits: tool returns bounded card objects; extraction is heuristic, links are mechanically inferred and no external source transcripts were re-audited. No external live HTTP/deployment/browser verification in this isolated pass. The manifest retains the pre-cleanup article hashes, with quarantine disposition attached, not a perpetually synchronized registry. No global automation behavior changed.

Integration: parent waits for library release completion, fetches current origin/main, cherry-picks cleanup commit in a clean integration worktree, reruns strict build/site/AEO/video/tests, inspects scoped diff and protected files, then serializes push/deploy and verifies live site. Do not push dirty main or import its unpublished drafts.

## Follow-up owner rejection (20:57 UTC)

Parent independently closed spaced-repetition-reflection card `8ad7a074` as rejected. Full card reread confirmed explicit clinical-training source rationale and no-resurfacing direction. Moved its root draft byte-for-byte into the rejected archive and extended the regression. Cascading-content-funnel card/source remain untouched during owner discussion. Earlier board totals above are superseded by this fresh live snapshot: {"backlog":27,"todo":41,"ready":14,"running":6,"review":5,"blocked":1,"done":18} (112 total). No additional card mutation by this follow-up.
