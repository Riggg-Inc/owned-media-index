# Proposed shared dark-mode readability correction

Status: exact-version proposal, NOT approved or deployed. Owning card: 8006e12e-6551-440a-b9cc-27bce652996f.

## Current pages and defect
https://index.riggg.com/patterns/ and https://index.riggg.com/patterns/package/clips/debate-moment/ demonstrate a shared problem also seen on Golden Nugget, Hot Take and Story Beat. Supported slate mode inherits pale text onto mint table stripes and dark burgundy code text. Content links also have weak contrast. Light-mode content and guidance do not require rewriting.

## Complete proposed implementation
The full revised file is docs/stylesheets/extra.css in this proposal commit. Only three slate-scoped CSS overrides are added: lighten content links to #67ddd5; change alternating table cell backgrounds to #253447; give code #f0bdc7 text on #253447. The original default palette, content, dates, score/framework, consent and analytics are unchanged. The commit diff is the meaningful exact change set.

## Check evidence and limitations
Playwright loaded current public Pattern Library and Debate Moment at 1440 and 390 widths, dismissed consent via ordinary Reject, selected dark mode via its visible theme toggle, then injected the full proposed stylesheet locally. Verified all striped table cells use rgb(37,52,71), existing pale foreground, and no horizontal page overflow. Screenshots inspected before and after: source/selection text and code become readable. This is a candidate CSS preview, not deployed correction or a full accessibility certification. Initial attempts targeted the hidden palette input and then encountered the consent overlay; corrected harness uses Reject before visible toggle.

Evidence files are retained in workspace output/reports/omi-quality-20261011/contrast-proposal-results.json, contrast-proposal.cjs and contrast-proposed-*.png. Production record-only builds and all109 tests passed independently; those do not certify this proposed stylesheet. After exact human approval, integrate against then-current origin/main, strict build and all validators/regressions/privacy checks, deploy, verify real desktop/mobile dark and light presentation, and append genuine final quality outcomes. Existing needs_revision history must remain unchanged.

## Decision
Approve this exact stylesheet revision, request changes, or park via the existing next-card flow. No further article-body edits or scoring changes are requested. This proposal is not publication authority.
