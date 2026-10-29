# Whole-page quality review: patterns/produce/obs-production-standard.md
Completed 2026-10-29T16:48:28Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: afc3a17196961aa5ba50dc3d49ab92eff33238f42faa2a1c849e83aa5fd22ecd
Outcome: needs_revision; not human signoff.
## usefulness — pass
The opening makes the staffing and turnaround decision explicit: choose real-time production when someone can monitor the show, and raw capture for archival-only needs. This is useful selection guidance rather than a promise that every recording needs a live producer.
## substance — pass
Lower thirds, titles, overlays, transitions and intro/outro moments specify which decisions move upstream. The concise standard links directly to the complete scene setup and observable rough-cut checklist; repeating the definition is optional cleanup, not a material defect for this overview.
## coherence — pass
The opening, upstream production mechanism, before-mastering quality bar and exclusions agree. Producing during or immediately around recording is compatible with the rough-cut guide allowing isolated-recording assembly after a session.
## cross_page_consistency — pass
The linked Rough Cut page supplies concrete layout, audio and graphics checks; the scene template supplies implementation; Simulcast distinguishes producing a show from distributing it. The staffing and archival exclusions do not contradict these companion roles.
## reasonable_claims — pass
OBS official features support scenes, multiple text/image/video sources, transitions, preview and recording. Reducing later production work by making those choices upstream is a scoped practitioner rationale, not a quantified benchmark. Existing internal-data provenance and score were not independently certified or changed.
## usability — needs_revision
Fresh 1440px and 390px light/dark renders retain the whole readable article without horizontal overflow, but required dark-mode inline links to Rough Cut, Scene Collection and Simulcast are difficult to distinguish/read against the dark background. These links carry essential implementation detail and need the existing shared dark-link contrast correction.
## Practitioner reader gate
Purpose PASS: opening identifies staffed fast-turnaround production versus archival capture. First action PASS: decide whether live quality monitoring is available, then follow the named scene setup. Example PASS for this overview: lower thirds, overlays and intro/outro are concrete production elements; no invented case study is necessary. Quality Bar PASS in linked context: the short produced-show test is operationalized by Rough Cut’s correct-name, balanced-audio and working-intro checks. Meaning/voice PASS: no rewrite proposed; confident production advice retained. Essential limits PASS: exploratory/archival/unmonitored sessions are excluded once, at the decision. Material usability REVISE: dark links obscure the implementation routes on which the concise page relies.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Read the official OBS feature descriptions in context to check capabilities; no private production data or empirical turnaround measurements were accessed.",
    "items": [
      {
        "url": "https://obsproject.com/",
        "claim": "OBS can combine sources into scenes with transitions and preview for real-time production and recording.",
        "finding": "Official features describe image/text/browser/webcam sources, scene switching and transitions, recording, Studio Mode preview and Multiview. These support the production mechanism, not quantified time savings or Riggg internal-data provenance.",
        "checked_at": "2026-10-29T16:47:01Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read all three linked published companion Markdown documents completely to compare the selection, setup and output boundaries.",
    "items": [
      {
        "path": "patterns/produce/rough-cut/index.md",
        "claim": "The rough cut provides the output and acceptance checklist referenced by this short standard.",
        "finding": "Names layout switching, lower thirds, intros/outros and audio checks, with live or immediate post-session assembly. Supplies concrete observable checks missing from the short overview without contradicting its before-mastering boundary.",
        "checked_at": "2026-10-29T16:47:00Z"
      },
      {
        "path": "patterns/produce/obs-scene-collection-template.md",
        "claim": "The linked scene template offers a reusable setup rather than requiring raw archival sessions to use it.",
        "finding": "Detailed plugin/script installation, branding, participant setup and show-flow steps match the standard\u2019s staffed-show recommendation. Template-specific numerical counts and internal 500-session claim were read for context, not independently audited or attested in this target review.",
        "checked_at": "2026-10-29T16:47:00Z"
      },
      {
        "path": "patterns/publish/simulcast-standard.md",
        "claim": "Multiple destinations are a separate publication decision from creating a real-time rough cut.",
        "finding": "Requires destination choices, backup and replay planning, and excludes private or heavy-edit sessions. The target\u2019s contextual Simulcast link correctly separates production from broadcast distribution.",
        "checked_at": "2026-10-29T16:47:00Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261029. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Reuse the existing shared contrast candidate and owning card; no new duplicate proposal or body rewrite is warranted. Keep needs_revision and Quality review pending. After exact human approval and CSS deployment, inspect the final target again and append a real new assessment.
Nominal next review 2026-11-28T16:48:28Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.
