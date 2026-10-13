# Draft validation — 2026-10-13

Internal owner-review artifact only. No approval, publication, runtime adoption, score change or new quality assessment.

Base: 94c7bbd228c41b1dbd02e15b83cba475ea1b7af9, also remote main when checked. Exported this tracked tree to isolated /tmp/omi-practitioner-final-XSTMW6, then overlaid exactly revised/docs/owned-media.md, revised/OWNED-MEDIA.md and revised/FRAMEWORK.md. No maintenance branch changes included.

All commands exited successfully (full output: validation.log):

- python scripts/check_video_reference.py
- mkdocs build --strict
- python scripts/validate_site.py — 128 HTML pages, 8,248 link/resource references, zero errors
- python scripts/validate_aeo.py — 127 pages, zero errors
- python scripts/validate_freshness.py — 127 pages, zero errors
- python scripts/fact_checks.py validate — zero errors
- python scripts/quality_checks.py validate — zero errors
- python -m unittest discover -s scripts -p "test_*.py" -v — 109 tests PASS, 8.395 seconds

Used existing /home/production/owned-asset-media-index/.venv/bin tools; installed nothing. Preview export has no Git history: provenance is not a release-date certification. Existing registry records were not rewritten to certify candidate bytes.

SHA256SUMS verified for all three revised files. Baseline snapshots exactly match the three tracked base files. Public article body exactly contained in root copy; expected Related/footer retained. Framework diff changes only asset-definition bullet. PESO primary-source link and explicit licence/ownership distinction retained; retired benefits heading absent. Independent AI scoped draft review PASS is in independent-review.md, not owner approval.

Recovery finding: prior /tmp/omi-practitioner-tests.log ran in the maintenance tree without a generated site and failed (5 failures, 8 errors). Prior preview did not overlay root/framework. Neither was used as final proof; the isolated synchronized run above supersedes them.

Release still requires authenticated exact-revision owner decision on all three files together, fresh current-base integration, rendered desktop/mobile acceptance, deployment and live parity. No such publication is authorized by this artifact.
