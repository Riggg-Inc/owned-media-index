# Legacy factual-review evidence procedure

> Operational migration approved October 7, 2026: the recurring page-maintenance job now follows [Quality review procedure](quality-review-procedure.md), not a blanket claim-by-claim fact-certification process. This document and data/fact-checks.json preserve prior evidence and the rules for substantive source checks when appropriate. They do not create quality-check dates. The new quality registry/checklist, bootstrap coverage and rolling schedule are authoritative for public review metadata. Corrections remain in the single content-card queue; no separate digest. Historical scheduling/output instructions below are retained as history, not a second active job.

# Published-page factual review procedure

This supplements TEAM.md and the [AEO publication standard](aeo-publishing-standard.md), not the framework, scoring rubric, evidence labels, source policy, or human approval contract. Public Last updated is an editorial-change date, **not** an assertion that every claim was fact-checked. Git timestamps, builds, link checks and successful HTTP fetches never establish factual freshness.

## Read-only queue

Run from the current approved production checkout with Python 3:

~~~sh
python3 scripts/fact_checks.py due --json --limit 3
python3 scripts/fact_checks.py inventory --json --limit 100
python3 scripts/fact_checks.py validate --json --limit 3
python3 -m unittest discover -s scripts -p test_fact_checks.py -v
~~~

The stable scheduler entry point is **due --json --limit 3**. These commands perform no network requests, edits, attestations, publishing, or scheduler changes. They enumerate every published Markdown page in the approved docs/ mirror, including off-navigation Articles, CollectionPages, general WebPages and the homepage; root source drafts, template overrides and generated error pages are excluded. Schema type is not a factual-review eligibility filter. This mirrors the current publication layout, not proof that a changed local file is deployed: run against approved production, and verify source/public parity before release. If future build exclusions change, update inventory and regression coverage together.

JSON contains as_of, summary, items and errors. Each item's stable identity is its docs-relative path. A missing store or absent record means unreviewed/no content-bound record, not “fresh”; it is not a validation error. Exit 0 means structurally valid input, **not** that reviews are complete. Exit 1 means invalid store/proof/date/path input: report the blocker, do not fabricate repairs. CLI usage errors exit 2. Summary counts cover the entire inventory regardless of the row limit (default 20, allowed 1–3660). --now accepts an explicit ISO UTC time for reproducible tests, not for backdating real checks. --root and --data support isolated audit copies.

### Cadence and priority

- Default high risk: **30 days**. All tools plus AI/AEO/GEO, platform, API/spec, search engine, RSS, hosting and analytics terms in page paths/bodies are conservatively flagged by HIGH_RISK in the script. This heuristic may over-classify a passing platform reference; it never changes framework classification, evidence labels or scores.
- Default stable evergreen: **90 days**. Configure with --high-risk-days and --evergreen-days (positive day counts up to 3660); record nondefault values and rationale in the review report. Use the same flags consistently in scheduled runs. Do not silently lengthen policy.
- Effective deadline is the earlier of next_review_at and checked_at plus cadence. A body hash mismatch is immediately stale, even before its deadline. Missing/invalid records are immediately due.
- Due items sort first, with AI search measurement first, then high risk, then evergreen. Within those groups unreviewed/invalid (unknown due time) precede dated reviews, then oldest deadline, then lexical path for deterministic ties.
- A partial review is always needs_review=true, never current. Its retry deadline must be after checked_at and at most **seven days** later. Until that deadline it stays visible in inventory/summary but due=false, preventing a repeatedly blocked page from monopolizing the daily queue. A changed body overrides this deferral immediately.

## Evidence store contract

The repository store is data/fact-checks.json; the queue never creates it. Empty initialization is {"version":1,"reviews":{}}. Reviews are keyed by exact docs-relative Markdown path, without docs/ or a leading slash. Unknown targets, duplicate JSON keys, unexpected fields and malformed records fail validation.

Every record has exactly:

- checked_at: actual completed review time, ISO UTC including seconds, Z or +00:00; no future date.
- reviewer: actual human identity or AI agent/model identity, explicitly labeled, never an invented human reviewer or a generic “system”. Syntax validation cannot authenticate this assertion; the run/report supplies provenance.
- method: substantive method and durable report reference. For partial reviews include a literal Blocked: or Unresolved: marker followed by the claims, reason and next action here as well as in the report (the marker is mechanically required). Never describe an HTTP status/link crawl as claim verification.
- content_sha256: lowercase SHA-256 of the exact UTF-8 bytes after the opening YAML frontmatter block and its closing delimiter/newline. Preserve remaining whitespace and line endings; with no YAML, hash the entire file. Use content_hash() from scripts/fact_checks.py or the inventory output; do not guess hashes or normalize the body. Recompute on the final reviewed public copy. Metadata-only changes do not invalidate factual review; any body change does.
- sources: nonempty array of objects with exactly url (public HTTP(S), no embedded credentials), claims (nonempty list of precise supported claim statements), checked_at (actual source-reading UTC timestamp, not future or later than the completed review).
- status: verified only after all material checkable claims in the final body were evaluated against sufficient evidence, with caveats/observational judgments accurately labeled; otherwise partial. Neither status upgrades a framework evidence label or score.
- next_review_at: ISO UTC deadline later than checked_at; future planned dates are expected here. The cadence cap still applies.

The validator catches missing/malformed evidence, impossible/future check dates, source checks after the review, unsafe URL syntax, wrong target paths and invalid hashes. It cannot prove a source says what a claim asserts, that a person actually reviewed it, or that an apparently public URL is appropriate. Those are substantive reviewer/Auditor responsibilities. A syntactically valid record alone is **not** verified truth.

## Daily bounded source review workflow

The operational plan is one daily published-page source-review run, maximum **three existing pages**. Scheduling/activation belongs to the operator; this document and CLI install no cron, timer, or job. This is separate from monthly AEO visibility measurement, quarterly lifecycle/scoring reviews and new-draft approval. It must not duplicate their publication jobs.

1. Read TEAM.md, the AEO publication standard and this procedure. Inspect current production, scoped worktree state and the due JSON. Keep unrelated drafts/files intact. Select at most three due paths; if a wholly blocked page has already been attempted, consult the run ledger and use a larger read-only queue window to select another eligible page rather than repeatedly retrying or inventing an attestation.
2. Read the **entire page** and source context. Inventory material factual claims, including numbers, dates, platform features, tool specifications, current availability and asserted causal outcomes. Separate recommendations, examples, practitioner observations and measured findings. Prioritize primary official documentation; credible methodology-disclosed research remains governed by TEAM.md. Do not use private customer material or unapproved/login-only sources.
3. Open/read each relevant source and compare the exact claim, population, timeframe, modality and limitations. Record source excerpts/locations and the actual UTC check time. A page title, search snippet, fetched status code, homepage link or citation count is insufficient evidence. Record contradictory/obsolete evidence, not just supporting passages. Inaccessible content is blocked, not “confirmed”.
4. Produce a durable source-to-claim report (repository internal report or canonical work item) containing: article path and reviewed body hash; actual reviewer identity; start/end UTC; each claim's exact text/section; source URL, source excerpt/section and check time; support/contradiction/uncertainty verdict and rationale; limitations; corrections/diff; unsupported claims; approval blockers; next owner/action and next review/retry date. Preserve the report and earlier review history through version control/audit records, not only the latest JSON record.
5. Apply only authorized corrections to existing public material, keeping canonical source/public copies aligned where required. Do not reclassify framework stages, silently change scores/evidence labels, ingest unrelated drafts, weaken analytics/consent/privacy gates or invent conversions/citations. Review-only/no-change work may update evidence records but must not bump public Last updated as though an editorial edit occurred.
6. Record verified only for completed substantive review. If some claims were supported but others remain blocked, record partial with truthful supported sources, gaps in method/report and a retry within seven days. If **nothing** was substantively verified, emit a blocked report with failed sources, reason, owner and retry plan; do not create a review or change checked_at. Carry that attempt in the operational ledger so another due page can be selected. Do not overwrite a prior valid review with an empty proof record.
7. Validate the store and rerun due inventory. Preserve existing Scribe → Auditor → Beacon and applicable exact-revision human approval gates; AI factual review is not human publication approval. New candidates/drafts still use their existing approval process. Source-policy/framework changes still need the existing signoffs. A correction outside authorization becomes a review proposal, not an automatic ship.
8. Before any authorized release, follow the AEO publication standard: isolated clean production checkout, strict build, both generated-site validators, regressions, source/public parity, customer-data checks and scoped diff/commit safeguards. Publication/date provenance and visible/schema parity checks remain mandatory. Beacon verifies deployed canonical pages and records deployment/commit evidence. Never claim “updated” or “fact-checked” without the path/report and verifiable evidence; report partial/blocked work plainly.

A scheduled run reports reviewed/changed/partial/blocked paths, sources and claim verdicts, remaining due counts and next actions. It must not call an unchanged fetched page “fact-checked”, treat unavailability as zero, or describe the entire archive as reviewed because one page passed.

## Owner-authorized operational schedule

The daily published-page source-review job is distinct from draft approval, quarterly scoring and monthly AEO performance reporting. It evaluates up to three due pages at 16:45 UTC and delivers a summary to the requesting owner conversation. A complete no-change source review may publish only its body-bound evidence record and audit through normal validation/deployment acceptance; it must name the actual AI reviewer and must not imply human signoff. Substantive article corrections remain staged for review of that exact artifact. A partial record is not a pass. Missing records mean no content-bound record has been captured, not proof that nobody ever checked a page.

Job identity: cfa8f525-f4ac-434d-bbef-8c0054c0f6ff. Scheduler enablement and scheduled-run acceptance must be verified separately after release. Before modifying any scheduler configuration, inspect and preserve the existing job definition. Do not create duplicate article-review jobs.

## Site-wide freshness presentation

Every published interior page has one shared Last updated display and explicit factual-review status, including hubs, comparison pages and references. The homepage alone must never show either freshness display; preserve both its no-breadcrumb and no-freshness-display exceptions. Keep the homepage in the review inventory and retain its provenance/schema. The generated 404 is not a reviewed content page. Standalone hand-written Last updated/Last verified labels are not substitutes for the shared metadata: remove redundant revision labels, and qualify legacy verification dates as historical source/spec snapshots without silently advancing or erasing them. Keep row-level source observation dates and instructional examples when their scope is clear. A historical date-only assertion must not become an exact-time verified registry record without supporting audit provenance.

The source-review queue includes this whole publication registry; existing job cfa8f525-f4ac-434d-bbef-8c0054c0f6ff continues using due --json --limit 3. Older article-only wording does not exclude hub/reference/homepage rows returned by the current queue. Expanding UI/inventory coverage does not constitute substantive fact-check completion. Run the complete generated-site freshness audit and live per-page parity after any coverage change.

## Reader-facing review language

Owner clarification, October6: use the shared fact-check run metadata instead of inserting a stock Evidence limitation paragraph into each article about retained scores, internal-data labels or editorial advice not being proven facts. Practitioner guidance may remain practitioner guidance. Keep audit details and unresolved evidence gaps in the review record; retain specific context or qualifications needed to make individual claims accurate. Do not upgrade partial records to verified merely because the generic disclaimer was removed.
