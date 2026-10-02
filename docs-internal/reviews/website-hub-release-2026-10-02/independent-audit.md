# Independent website-hub release audit — PASS

Audited 2026-10-02. Worktree: `/home/production/omi-hub-approved-release-20261002`. HEAD and observed origin/main: `43cca3ceb28452ae5d7347f34307b187cc78a899`. Scope is content/integration readiness, not deployment certification. Owner exact-text approval supplied in assignment: October 2 22:40 UTC, card `4df042ae-7b97-4270-a2aa-c6c99f3ba8da`, comment `6d981347-d1f6-496b-95c3-233fde6994a8`; this child did not independently query dashboard authentication.

## Exact content proof

Both entire canonical files are byte-identical to immutable additive review commit `e9015672b4f737112d8b9ca755a564371ce8f47a`, not merely keyword/heading matches. Full approved CTA and Site Control prose also compares byte-for-byte with review.md section text, allowing only its explicitly documented source/docs library-link target difference and section-delimiter newlines.

- Source `publish/website/canonical-episode-page.md` SHA256: `ec0765577d0f1882e9c3e8a3705825fbc041d06506c7750349dd21b22d6dda64`
- Docs `docs/patterns/publish/canonical-episode-page.md` SHA256: `3fed7476710d70e4783454c71aaeff0cdc4e7c42afd42af05e35102455dd64e1`
- Immutable review.md SHA256: `6245dfe2224562edac1d425876111ed6dc44c3fdb8eff539bc052d46ecff53ee`

Scoped diff changes only the approved hub-pointer sentence and adds Site Control, Navigation And Continuity in source/docs. Score remains 3 in both; Required Elements, other CTA consent/measurement wording, introduction and evidence remain unchanged. No old prerequisite snapshot replay is visible in the resulting diff.

## Archives and retirement guards

- Original archive SHA256 `3d28a7b0adffb8c9af2580509160cb843daabf4814f11f0368f686514a9ac147`: byte-identical to current HEAD original draft and add3e58 archive.
- Dirty/local score-3 archive SHA256 `0ec744ea62bbe359abdb60623439954b4819e1a035e6f200a3461c02d5eb287c`: byte-identical to immutable add3e58 archive and manifest digest. Historical dirty checkout was not mutated or independently resnapshotted.
- Active standalone source is removed; archival copies live outside docs. No standalone public page or redirect is introduced.
- Current shared `scripts/test_reconciliation.py`, reconciliation JSON, rejected README and every tracked rejected archive file are byte-identical to current HEAD/origin. The 12 existing rejected-slug guards remain intact. New hub regression is separate.

## Links and newsletter

Source library link resolves to `preserve/vector-memory/content-memory-standard.md`; docs link resolves to existing `docs/patterns/preserve/content-memory-standard.md`. Generated canonical HTML links to `../../preserve/content-memory-standard/`, the public library route, not a repository-only draft.

Both newsletter source/docs are entirely unchanged versus current origin. Each retains the known code-formatted unpublished-hub path (source line 48, docs line 54), explicitly described as not a public destination. This is nonclickable stale editorial text, not a publication blocker under the assigned scope. Proposed separate exact-review repair: replace that related-pattern entry with Canonical Episode Page and its appropriate source/public link. No authority to perform that repair was inferred.

## Guarded existing-page release

Reviewed content-repo `docs-internal/aeo-publishing-standard.md`, workspace `docs/omi-publisher-aeo-gate.md`, and actual `scripts/omi-publish.mjs` add-only guard. The publisher explicitly never overwrites an existing page; its existing-page/no-op outcome cannot deliver this revision and must not be treated as update success. Use the separately authorized content-repo manual release: isolated current-origin base; exact approval/digest evidence; customer-data scan; only scoped changes staged; no unrelated commits; fresh strict build, site/AEO validation and full regressions; then commit/push and independently verify deployment plus live canonical prose/score/links. Preserve add-only safeguards; do not add an overwrite bypass or mark standalone published.

Parent owns tests and publication. This audit inspected generated HTML but does not attest a fresh full-suite run, remote push or live browser deployment. Historical archive/review text that says approval is pending is immutable provenance; the later supplied approval and release proof should be recorded separately rather than silently rewriting history.

**Verdict: PASS for the inspected exact-content release scope. No content blocker found. Final test, customer-data, approval-authentication and deployment gates remain parent-owned.**
