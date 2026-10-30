# Whole-page quality review: patterns/produce/obs-scene-collection-template.md
Completed 2026-10-30T16:49:30Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: 4e46b254e00eb797188e5ffb3dcee44a7aed7f70877621f575f091d9d2a1094a
Outcome: needs_revision; not human signoff.
## usefulness — pass
The opening identifies staffed video shows, five participants, horizontal/vertical layouts and exclusions. The actual downloadable collection and ordered branding/participant workflow serve a specific producer task.
## substance — pass
Named camera-box variants, participant fields, show-flow sequence and concrete rehearsal checks provide substantial usable detail. This is a real 2,318,677-byte downloadable collection, not a generic promise.
## coherence — needs_revision
The setup promises a production-ready import and exactly 157 scenes, but the linked current artifact has 190 scene_order entries and 226 scene-typed source objects. Neither matches the undocumented count; the version and counting convention must be reconciled before operators can reliably verify the import.
## cross_page_consistency — pass
The OBS Production Standard positions real-time production as a rough edit before final mastering. The template is a concrete implementation with a staffed-production opening and rehearsal gate. The Record hub explains why isolated capture is useful; a scene collection is not represented here as a substitute for isolated source recording. This comparison does not certify every separate platform table in the hub.
## reasonable_claims — needs_revision
Primary plugin documentation supports vertical-canvas and moving-source capabilities, and the Lua implementation supports mutually exclusive visibility within configured groups. The public artifact confirms 317 sources and 1920x1080 base resolution, but not the claimed 157-scene count. The blanket 15 required plugins and OBS 30.0+ compatibility statement lack a version/platform test matrix; Stream Deck and Logitech hardware entries do not establish universal import dependencies. The 500+ session assertion is not verified by public artifact inspection or allowed evidence read in this run. Do not certify that outcome or change the underlying score.
## usability — needs_revision
Fresh desktop/mobile light/dark renders show working document hierarchy, download and no page-wide overflow, but dark-mode pale table cells with light inherited text make the dependency/architecture tables unreadable. Required setup also omits re-linking exported local media/script paths and checking the configured Scenes and Groups list after importing; the Lua code only toggles named configured groups. Installation alone does not establish a working collection on a different machine.
## Practitioner reader gate
Purpose PASS: opening gives staffed-show use and exclusions. First action REVISE: plugin installation/import sequence does not explain relinking local exported assets and validating configured script groups. Example PASS: concrete @Text_ParticipantX and show-flow names make implementation tangible. Quality Bar REVISE: add independent preview/listen-back of both recorded outputs and a portable-asset check, not just absence of warning triangles. Meaning/voice PASS for the current practical structure; retain useful tables, examples and confident rehearsal advice in the minimal correction. Essential limits REVISE: do not present 15 listed integrations as universal requirements or imply a tested OBS/plugin compatibility matrix. Existing participant/1080p exclusions remain valuable. AI editorial review, not human usability testing.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Check downloadable configuration and official capability documentation, not private customer evidence or runtime compatibility inferred from a link.",
    "items": [
      {
        "url": "https://index.riggg.com/assets/downloads/riggg-obs-scene-collection-v1.json",
        "claim": "Download size, scene/source counts and reusable configuration match the guide.",
        "finding": "Live download is byte-identical to current repository artifact, SHA256 ae13d26640aec83ce0a76ed90f81b4564d32210e63e1fbe1a83382f816a8c19a. It has 317 sources, 226 scene-typed objects, 190 scene_order entries and 1920x1080 base resolution. It retains a local script path and explicit toggler group settings; no OBS runtime import was performed.",
        "checked_at": "2026-10-30T16:48:26Z"
      },
      {
        "url": "https://github.com/Aitum/obs-vertical-canvas",
        "claim": "Aitum adds a vertical canvas to OBS Studio.",
        "finding": "Maintainer README explicitly describes a vertical canvas plugin. It does not prove this exported collection records both canvases without configuration or is compatible with every current plugin version.",
        "checked_at": "2026-10-30T16:48:26Z"
      },
      {
        "url": "https://github.com/exeldro/obs-move-transition",
        "claim": "Move Transition can animate sources during transitions.",
        "finding": "Maintainer README describes moving sources to new positions during scene transitions. No playback or exported-collection compatibility was tested.",
        "checked_at": "2026-10-30T16:48:26Z"
      },
      {
        "url": "https://raw.githubusercontent.com/exeldro/obs-lua/master/source-toggler.lua",
        "claim": "Source toggler makes configured scene/group children mutually exclusive.",
        "finding": "Read complete Lua: script_properties exposes Scenes and Groups; script_update and source_load attach item_visible callbacks by configured source name. Callback hides other visible children. This supports the mechanism but requires configured group names; merely downloading the script is insufficient.",
        "checked_at": "2026-10-30T16:48:26Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete current OBS standard and recording hub to check capture versus live rough-production scope.",
    "items": [
      {
        "path": "patterns/produce/obs-production-standard.md",
        "claim": "This collection implements the staffed real-time rough-production approach.",
        "finding": "The standard explicitly places overlays/layouts before final mastering and warns against unmonitored use. Template opening and rehearsal checks support the same audience and workflow.",
        "checked_at": "2026-10-30T16:48:26Z"
      },
      {
        "path": "patterns/produce/record/index.md",
        "claim": "Live scene output and isolated source capture serve different editing needs.",
        "finding": "The hub advocates isolated participant files for later reframing. Template describes composite show layouts rather than promising isolated capture; no direct contradiction established. Hub platform specifications were not independently certified in this comparison.",
        "checked_at": "2026-10-30T16:48:26Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261030. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Reuse shared contrast candidate on existing card. Prepare an exact full-content correction of count convention, portable-import setup and tested dependency scope; do not publish body changes or alter scores. Session-volume assertion needs authorized substantiation or removal of the unsupported numeric qualifier in the proposed revision. No import/runtime verification or complete plugin compatibility claim. Keep any unfinished correction preparation explicit.
Nominal next review 2026-11-29T16:49:30Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.
