# Article freshness implementation

## Contract

All 84 published Article pages get a muted freshness block immediately below breadcrumbs, above article content. CollectionPage/WebPage pages do not. The existing home-only breadcrumb exception, video placement and consent analytics are unchanged.

“Last updated” is the committer timestamp of the latest committed Markdown BODY transition along first-parent publication history. YAML frontmatter is excluded using the existing canonical scripts/fact_checks.py body_bytes helper; exact body bytes (including whitespace) count. Template, CSS, build, registry and frontmatter-only commits cannot advance the date. Renames preserve origin. A merge that introduces a changed body is the publication revision; an unchanged merge does not advance it. A revert is a new body transition.

Dirty/untracked bodies show “Pending commit (preview)” without dateModified. Shallow/unavailable history and future revision timestamps fail closed to “Revision history unavailable”, also without dateModified. CI already used fetch-depth: 0, retained unchanged. Dates are never derived from file mtimes, build time, YAML date fields or factual review records.

The date-only summary uses native details/summary for keyboard and tap expansion. Exact ISO UTC time is shown inside the disclosure and present in both time datetime attributes. Article dateModified comes from the identical revision object. No datePublished or inferred reviewer schema is introduced.

## Evidence records

Registry loading, hashing and record validation reuse scripts/fact_checks.py load_reviews, content_hash, body_bytes and validate_review. metadata.py imports freshness lazily to avoid the fact_checks → metadata.page_type circular dependency. No independent hash implementation exists.

Missing evidence displays **No fact-check recorded** (not a claim that no check ever happened). Valid current verified records show Last fact-checked; valid partial records explicitly show Partial fact-check and unresolved-claims wording. Details expose reviewer, method, claim-specific sources/check dates and review deadline. Invalid/future evidence, changed body hash or overdue review shows Fact-check needs review. UI honors the same 30-day high-risk / 90-day evergreen caps and seven-day partial retry validation as the canonical inventory.

This implementation does not write article content or registry records. Those remain parent-owned; measurement rewrite approval is separate.

## Verification

- Strict MkDocs build passed; final full suite: **46 tests passed** (13.206 seconds). Freshness audit: **84 Articles, zero errors**. Canonical registry validation: zero errors (83 unrecorded, one partial at test time).
- Full unittest discovery includes history fixtures for YAML/template changes, dirty/new bodies, commits/reverts, renames, future dates and shallow history; review fixtures for verified/partial/missing, overdue, hash mismatch and false future evidence; schema parity and absence on unavailable previews.
- scripts/validate_freshness.py audits all 84 generated Articles against repository provenance, visible date-only summary, exact datetime values, matching Article dateModified, review labels and breadcrumb placement; excludes metadata from non-Articles.
- CI now explicitly runs freshness and canonical fact-check validators, in addition to existing site/AEO/video and complete unittest gates.
- Existing link/AEO audits: 125 HTML pages / 8,006 internal references, zero errors; 124 canonical pages (84 Articles), zero AEO errors. Video source/public copy parity passed.
- Browser keyboard/tap/theme/mobile checks are parent-owned; no browser pass is asserted here.

Build/test logs: /tmp/omi-freshness-build.log, /tmp/omi-freshness-tests.log, /tmp/omi-freshness-validation.log. No repository staging, commit, push or deployment performed.
