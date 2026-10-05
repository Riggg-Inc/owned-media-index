# All-page freshness implementation — 2026-10-02

## Scope and semantics

Every published interior Markdown page receives one shared freshness block, including Articles, CollectionPage hubs and ordinary WebPages. The homepage (`docs/index.md`, `/`) is the sole published-content display exception: never render Last updated or fact-check status there. Enforce this in the shared partial, homepage template and release validator. Keep homepage source provenance/schema and review inventory intact; the exception is display-only. The generated 404 still has no freshness block. Preserve this rule in every future publishing/maintenance cycle.

Last updated remains the true committed Markdown-body revision from History: frontmatter/template-only commits do not advance it; uncommitted bodies show Pending commit (preview), unavailable/shallow/future history fails closed. All relevant Article, WebPage and CollectionPage entities use the identical timestamp as the visible revision; pending/unavailable states omit dateModified. No datePublished, build-time fallback or fabricated fact-check dates are introduced.

### Homepage limitation requiring explicit acceptance

home.html contains separately maintained visible homepage content and bypasses docs/index.md's rendered body. The homepage has no visible freshness block. Its retained schema provenance is the Markdown source-content revision; presentation changes independently. It dates docs/index.md, not home.html. This is accurate source provenance, not a claim that all visible template content changed on that date. A future template-content provenance model or migration to a single content source should be a separate deliberate change; this implementation does not manufacture a historical template-body date or review attestation. Existing registry hashes continue to bind Markdown bodies only, including the homepage, so a homepage review must explicitly disclose its scope rather than imply template-wide verification.

## Inventory and review compatibility

fact_checks.py now inventories all published Markdown pages and accepts review records for any of them. Version-1 review records and canonical body hashes are unchanged. Inventory rows add page_type; summaries expose pages, page_types and the actual Article subset through articles. Missing records remain unreviewed / No fact-check recorded; no automatic attestations. Existing cadence, claim-specific evidence and due-queue rules remain intact.

## Enforcement

- Freshness audit derives the entire inventory dynamically, requires one freshness block, verifies revision/review status and timestamp parity, and checks all relevant schema entities.
- Independent tests explicitly require homepage, hub, informational WebPage and tool Article coverage; none assume a fixed 84/85 Article count.
- Audit detects missing output and unexpected built HTML, with generated 404 exempt from page freshness.
- Legacy standalone Last updated / Last verified / Last fact-checked stamps are rejected in source and rendered paragraphs; explanatory prose, fenced examples, Source snapshot lines and claim-table dates remain allowed.
- Date-only visible summaries retain exact UTC machine datetimes and disclosure details. Homepage breadcrumb and freshness-display absence are independently asserted; all interior content pages must retain one freshness block.
- Existing CI already runs strict build, all tests, site/AEO/freshness validation and registry validation with full Git history; no workflow changes are necessary.

## Verification

Integrated verification passed: mkdocs build --strict; all 50 unit/regression tests; validate_site.py (126 HTML pages including 404, 8,110 references, zero errors); validate_aeo.py (125 content pages: 85 Articles, 28 CollectionPages, 12 WebPages); validate_freshness.py (125 pages, zero errors); fact_checks.py validate (zero errors); and check_video_reference.py. Inventory reports 124 unreviewed pages and one partial review, not 125 fact-checked pages. Homepage source-body revision resolves to 2026-09-30T20:41:14Z, commit e96a7035d08d579ce417196fae37dee7cf383001. Working-tree content edits correctly remain pending until committed. No commit, push or deployment was performed by this implementation task.
