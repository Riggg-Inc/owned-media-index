# Whole-page quality review: patterns/produce/rough-cut/index.md
Completed 2026-11-05T16:50:54Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: 92d50f0ddc1b6e5fdd4a09eb070ae2222bf8f7ffae1beeffa0499384053399cd
Outcome: needs_revision; not human signoff.
## usefulness — pass
The hub tells a producer what a rough cut delivers and chooses between workflow guidance and a reusable scene template; the opening and selection guide directly serve setup decisions.
## substance — pass
Nine concrete activities include lower thirds, camera switching, screen shares and subtitle safe zones. Output sizes and the quality-bar checks provide usable detail rather than an abstract promise of efficiency.
## coherence — pass
The progression from outputs to patterns, production activities and observable checks is logical. Real-time production is clearly the selected workflow, not a claim that all editing must be live.
## cross_page_consistency — needs_revision
The hub repeats the companion template’s 157-scene claim, but the actual linked JSON has 190 scene_order entries and 226 scene-type sources among 317 sources. Repeating the companion’s inaccurate count is not consistency with the delivered artifact; both belong to the same existing template correction.
## reasonable_claims — needs_revision
The downloadable 157-scene promise does not describe the current artifact counts. Aitum’s official repository supports existence of a vertical-canvas plugin, not universal no-reformatting results. Keep the confident workflow preference but correct the concrete count and distinguish configured dual layouts from an automatic guarantee.
## usability — needs_revision
Current dark desktop/mobile rendering makes alternating table rows nearly white-on-white, obscuring vertical output requirements and template selection. Light desktop is readable and all four captures have no horizontal overflow. This is the existing shared table-contrast issue, not a new styling proposal.
## Practitioner reader gate
Purpose PASS: produce a real-time rough show. First action PASS: choose the workflow standard or scene setup from Selection Guide. Example PASS: lower thirds and 1-up through 5-up switching make the work concrete. Quality Bar PASS in meaning: check individual feeds, names, audio and both canvases; REVISE rendered readability in dark tables. Meaning/voice PASS: preserve confident real-time-production advice. Essential limits REVISE: qualify no-reformatting as dependent on configured/tested layouts and align the template count with delivered JSON, without demanding trials for practitioner preference.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Verified the concrete downloadable template counts and the primary plugin description; no private performance evidence was used.",
    "items": [
      {
        "url": "https://github.com/Aitum/obs-vertical-canvas",
        "claim": "Aitum provides an OBS plugin adding a separate vertical canvas.",
        "finding": "The official README explicitly describes a plugin for OBS Studio to add vertical canvas and supported distributions. It does not establish no reformatting for every production or all plugin compatibility.",
        "checked_at": "2026-11-05T16:50:52Z"
      },
      {
        "url": "https://index.riggg.com/assets/downloads/riggg-obs-scene-collection-v1.json",
        "claim": "The hub promises a downloadable 157-scene template.",
        "finding": "Inspected the repository\u2019s published download JSON: 190 scene_order entries, 226 scene-type source records and 317 total sources. These are distinct counts; none equals 157. No import/runtime or complete compatibility test claimed.",
        "checked_at": "2026-11-05T16:50:52Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read both full destination pages and inspected the actual published download data to evaluate the hub\u2019s choice guidance.",
    "items": [
      {
        "path": "patterns/produce/obs-production-standard.md",
        "claim": "The rough cut hub should describe the real-time workflow and its production limits.",
        "finding": "The standard recommends staffed monitoring and excludes archival-only use; the hub\u2019s concrete live-production checks are compatible, but the selection guide can retain that staffing limit.",
        "checked_at": "2026-11-05T16:50:52Z"
      },
      {
        "path": "patterns/produce/obs-scene-collection-template.md",
        "claim": "The template description and delivered scene count should agree.",
        "finding": "The companion repeats 157 scenes, specifies required plugin/script configuration and testing, while the delivered JSON exposes different scene counts. Correct the shared template/hub claim rather than treating repeated copy as evidence.",
        "checked_at": "2026-11-05T16:50:52Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261105. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Same template/hub correction ownership: full revised hub should replace 157-scene wording with an accurate scoped template description and qualify configured dual output. Full proposal remains preparation until paired template-count reconciliation and exact-version validation; no publication or owner approval inferred.
Nominal next review 2026-12-05T16:50:54Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.
