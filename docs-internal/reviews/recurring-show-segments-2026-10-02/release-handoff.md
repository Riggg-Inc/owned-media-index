# Recurring Show Segments — approved release preparation

Owner approved the full inline article on 2026-10-02 21:55 UTC. Reviewed commit: `2465e715a0a21d47f1a8366b05450b4836bb8e18`. Draft SHA-256: `903164dd9a05e2ae387b670d5646d791a93bab1d749d903b08b435140fb534ed`. The historical audit and preview remain unchanged; their “not approved” statements describe that earlier snapshot, not the subsequent owner decision.

Source bytes unchanged. Canonical public target is `docs/patterns/produce/standardized-micro-segments.md`; display title Recurring Show Segments, score 3. Public article exactly equals the previously reviewed publisher preview; only stage-index discovery is added. No deep nav or unrelated article changes. Archived standalone remains byte-for-byte reversible outside docs; tests forbid its path and references in active trees.

## Test repairs

- Freshness expected Article count derives from the current docs source inventory using the canonical classifier, not a hardcoded 84 or a count of generated output. Empty inventory fails. Full audit still checks every source page and non-Article exclusion. Added missing-build negative ensures an absent output cannot pass.
- Publisher corpus failure came from an unrelated dirty checkout with a deleted historical draft, not scanner behavior. Isolated test copy supports `OMI_TEST_CONTENT_REPO`; real complete current-origin release corpus runs all 115 tests, zero skips. Production publisher code unchanged. Patch and logs retained at `/home/production/omi-recurring-gates-20261002/`; apply test-only patch through normal workspace review if desired. No fake source fixtures or ignored missing files.

## Mandatory serialized handoff

Do not push until parent confirms the CTA writer relinquished or explicitly serializes integration. No such confirmation received during preparation. Fetch/rebase only owned release commits onto then-current origin; preserve CTA files, all dirty main work, and unapproved website-hub commit cfa49f7. Recheck full diff and all gates.

Canonical card remains open. Independent Auditor must pass. Parent must bind its trusted authenticated owner-turn provenance to the exact digest using workspace `docs/omi-dashboard-approval.md`: DASHBOARD-AUDIT, ready cycle, DECISION-REQUEST, DASHBOARD-APPROVAL-EVIDENCE, HUMAN-DECISION. Existing prose approval is real authorization but does not itself satisfy the executable marker gate. Do not synthesize markers from untrusted quoted identity.

Publisher requires clean main equal to origin with no unpushed commits. In the serialized window, integrate and push only reviewed preparatory source/archive/test changes, then use a fresh clean main clone and `planPublish`/`executePlan` to generate the page and index with description from publisher-preview and section `Rough Cut / Real-Time Production`. A separate candidate commit holds the public preview for exact comparison; do not pre-push the preview page and bypass the publisher. Use installed absolute MkDocs path. Do not inject fake git/preflight/validation success.

After publisher verified remote push, verify GitHub Pages deployment and live canonical page (title, score, all substantive sections, metadata, privacy, links, desktop/mobile). Record verified publication proof and only then mark canonical done. No Slack required.
