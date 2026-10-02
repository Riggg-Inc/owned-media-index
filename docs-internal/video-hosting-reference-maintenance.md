# Video hosting reference maintenance contract

Scope: factual maintenance of the existing video-hosting reference, not pattern approval, scores, strategy, or scheduler configuration. Preserve existing human/exact-revision approval gates for any work outside that standing maintenance scope. Never publish the separate Spotify/HLS candidate pattern as part of this task.

## Monthly run and event-driven correction

1. Fetch origin and work in an isolated clean worktree of current origin/main. Do not reset, stash, commit or publish the dirty operational checkout's unrelated changes.
2. Canonical editable source: `tools/hosting/video-podcast-hosting-support.md`. Published input: `docs/tools/hosting/video-podcast-hosting-support.md`. MkDocs deploys **docs**, not the root tools directory. Maintain byte-identical files, including description, introductory answer and dates. This fixes the former Aug20-source/Aug11-public divergence.
3. Read current primary vendor technical/setup sources in full context. Follow source links in the reference. Use PSP as an attributed implementation report, not proof of each tenant's access. Distinguish file RSS, open alternate-enclosure HLS, Apple approval/API, Spotify native/direct integration and YouTube publishing. Check product names/ownership, plans, beta/rollout status and audio fallback. A blocked page or missing evidence means unknown, never unsupported. Explicitly record conflicting documentation.
4. Advance the review date only after real review; retain uncertainty and citations. Set next review one calendar month ahead. A successful no-change review is valid, but a mere scheduled execution is not a review.
5. Run `python scripts/check_video_reference.py --sync` after reviewing source changes; the non-mutating default check must pass. CI rejects parity drift **before** building; it never silently copies content or advances dates. This is a narrow parity guard, not an automated factual verifier or scheduler.
6. Run strict MkDocs build, `scripts/validate_site.py`, `scripts/validate_aeo.py`, and `python -m unittest discover -s scripts -p 'test_*.py' -v`. Inspect scoped diff and customer-data/secret safety; commit only authorized files. If publication requires additional approval, stage and report the exact blocker instead of bypassing it.
7. Push only scoped maintenance on current main under the existing authorization. Verify GitHub Pages build/deployment and fetch https://index.riggg.com/tools/hosting/video-podcast-hosting-support/. Confirm updated dates, corrected rows, citations, canonical URL and no raw metadata. Report commit, tests and live proof; distinguish HTML verification from browser/app playback testing. A commit or successful push alone is not completion.

## Initial refresh evidence (2026-10-02)

Reviewed current Apple RSS and HLS setup, Spotify native-video description, Buzzsprout, Acast (conflicting older beta docs/current launch), CoHost, Podbean, Transistor, Captivate feature matrix, RSS.com, Omny, Flightcast, Podigee, Beamly, Blubrry, Castos, Libsyn, Spreaker and Pocket Casts documentation, plus PSP's September 2 implementation list. Full claim-level source URLs remain beside public rows. Simplecast help and Podcast Addict changelog blocked retrieval; Fountain/TrueFans pages did not yield usable host setup docs. Their rows retain attributed evidence/uncertainty. No customer accounts or video playback were tested.

This contract intentionally does not install or modify a schedule; the scheduler owner should reference this path and retain completion/failure reporting.
