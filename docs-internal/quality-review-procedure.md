# Substantive quality review

This is a separate editorial assessment, not a renamed fact check and not a new quality score. Existing data/fact-checks.json and its history remain unchanged. No factual record is imported as a quality pass. The quality store starts empty; only actual completed work may be added.

## Standard

Read the entire published Markdown body and its rendered presentation. Judge whether it is fit for publication, not perfect, universally persuasive, or proof of every opinion. Record page-specific findings in six dimensions:

- usefulness: useful to the intended reader and intended task;
- substance: enough concrete detail and examples to support the promise;
- coherence: clear internal logic, scope and structure;
- cross_page_consistency: compatible with relevant definitions, patterns and linked guidance elsewhere;
- reasonable_claims: proportional claims, scoped recommendations and supported material factual assertions;
- usability: understandable, actionable, navigable and usable in its published presentation.

All six must pass for overall pass. Material defects mean needs_revision, not an invented pass. Specific material factual claims need proportionate credible sources read in context. Pure guidance may legitimately need no external citation; explain why. Never fabricate citations, source reads, comparisons, dates, reviewer identity or findings. A URL count is not evidence of truth. The validator checks structure, not editorial truth; human/agent review of report substance remains mandatory.

## Stable API and storage contract

scripts.quality_checks.public_view(root, src, body_hash=None, now=None) returns exactly state, label, date, timestamp, reviewer, method. src is docs-relative. The latest completed pass on the exact current body yields state passed, label Last quality checked on, and its actual assessment date, even when its review cadence has expired. This is a truthful historical event, not certification that a review is currently fresh; an expired unchanged pass remains due in the queue. Otherwise state pending, label Quality review pending, and null date/timestamp/reviewer/method. Supplied body_hash must also match disk. New bodies, later needs_revision/aborted records and malformed registries fail closed; cadence expiry alone does not erase the historical date. The homepage is included in inventory; its existing public freshness/display exception remains a presentation-layer exception.

Store: data/quality-checks.json, top-level exactly {"version": 1, "reviews": {}}. Each reviews key is a published docs-relative Markdown path; each value is a nonempty chronological **append-only list** of assessment objects. Preserve all prior objects verbatim and retain reports. Never rewrite old timestamps, hashes or findings when correcting/reassessing. Git history supplies durable publication audit; publication review must compare the previous store prefix to ensure history was not edited. This CLI is read-only and never generates or mutates assessments.

Every assessment has exactly these required fields, plus optional correction_card:

- id: globally unique stable identifier (3–128 ASCII alphanumeric/dot/underscore/hyphen characters; initial alphanumeric).
- status: pass, needs_revision, or aborted. Only first two mean completed substantive assessment.
- assessed_at: actual completion/abort time in ISO UTC (seconds; Z or +00:00), not future.
- reviewer: actual reviewer identity, including AI identity where applicable.
- method: substantive-quality-review-v1.
- content_sha256: lowercase SHA-256 of exact UTF-8 published body bytes, removing only opening YAML frontmatter (use content_hash).
- report_ref: existing repository-relative docs-internal/*.md report containing the actual findings.
- dimensions: exactly the six names above, each {"status": "pass" or "needs_revision", "rationale": "page-specific substantive explanation"}. For aborted only, empty {}.
- source_checks and cross_page_comparisons: each {"applicable": boolean, "rationale": "meaningful scope or nonapplicability explanation", "items": []}. Applicable requires at least one actual item; not applicable requires none. Source items contain exactly url, claim, finding, checked_at. Comparison items contain exactly path (published docs-relative Markdown), claim, finding, checked_at. Each finding says what was actually learned, including limitations. Times cannot follow assessed_at. Claims/findings/rationales require at least 24 characters and four words; this is a placeholder guard, not an automatic substantive score.
- next_review_at: ISO UTC after assessed_at; effective due date is capped by 30/90-day cadence.
- disposition: rolling for pass; retry or park for needs_revision/aborted.
- retry_at: null for rolling/park; ISO UTC strictly after assessed_at and no more than 30 days later for retry.
- reason: null for pass; meaningful explanation of blocking correction/access issue for retry/park.
- correction_card (optional): existing shared review-queue card ID or reference, never a fabricated card.

## Deterministic queue and daily operation

Run python3 scripts/quality_checks.py due --json --limit 5. Also available: inventory and validate, --root, --data, --now YYYY-MM-DDTHH:MM:SSZ. Validation failures exit nonzero and due refuses to select work from an invalid store. inventory/validate summarize all published docs/**/*.md except template overrides, including homepage, landing pages and reference pages; repo drafts are excluded.

Bootstrap persists until every currently published page has at least one completed substantive assessment (pass OR needs_revision). Aborted attempts do not count. New published pages restore bootstrap. Prioritize untouched/never-completed pages, then changed-body pages, then ordinary due work. Within classes use oldest prior attempt then due date then path; no permanently privileged page or fixed high-risk subset. Retried aborts follow untouched pages. Parked/retry-delayed pages do not monopolize selection. A changed body overrides a parked/delayed old-body disposition and requires reassessment.

Maximum five distinct pages per UTC day, including aborted attempts. summary exposes assessed_today, remaining_today, daily_limit, first_pass_completed and phase. Re-running after records are appended cannot grant another five slots. Read-only selection is not a reservation: execute batches serially under the existing single worker, persist each attempt promptly, and reload due before more work. Concurrent unrecorded runs are not safe. Do not invent an aborted record just to reserve a slot.

After first pass, automatically use rolling cadence: 30 days for tools and volatile/platform/AI/API-related content; 90 for evergreen. The deterministic conservative classifier is shared with the existing risk vocabulary, but no prior factual review data is consulted. If nothing is due, do nothing. Pending corrections require explicit park (until change/reassessment) or dated retry, not endless immediate retries. An oldest-attempt ordering allows overdue work to advance after each retried page; unbounded arrivals can naturally keep bootstrap active.

## Complete workflow and approval boundaries

1. Select remaining daily work; capture current body hash and full published page. Read and compare relevant neighboring pages, check applicable claims and rendered usability.
2. Write a real report with six findings, sources/comparisons or explicit nonapplicability, outcome, reviewer/time and exact body hash. If work could not be completed, append aborted and explain the retry/park disposition; do not attest six completed findings.
3. Append the assessment, preserving history. Completed needs_revision counts toward bootstrap but never grants a public date. Link its exact corrections into the **same existing shared review-card queue**, not a second queue. Reuse an existing card where applicable.
4. A real pass on the unchanged already-published body allows automatic **record-only publication** of report/store and derived quality metadata, subject to normal build/validation and deployment verification. This authority does not authorize substantive body corrections. No git/body-modification date may be relabeled as review time.
5. Proposed body corrections require explicit approval of the exact changes via the existing approval workflow/card. Do not treat approval of this quality-review program as approval of future edits. Apply only approved changes, reassess the resulting published body, append a new record, validate/build/publish, verify live, then close the same card with evidence.
6. Run registry regression tests and validate_freshness/build checks before publication. Preserve old fact-check records and all assessment history. No new numerical quality score, scheduler, board, or approval bypass is introduced here.
