# Whole-page quality review: patterns/produce/record/zoom-cloud.md
Completed 2026-11-04T16:51:31Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: 57dca8ae4b9c41588ee631134dd00764a794c9fd0d0c01e059814b69dbe70689
Outcome: needs_revision; not human signoff.
## usefulness — pass
The opening distinguishes meeting reference and local-capture fallback from planned per-person editing. Named restricted-device and webinar scenarios help readers choose a recording route.
## substance — needs_revision
The output table and use cases give real detail, but the cloud fallback lacks the first setup/test action and treats automatic transcripts as an unconditional output. A short permission/settings/test instruction is needed for its recommended fallback.
## coherence — needs_revision
When To Use allows content-led webinars, while When Not To Use rejects any planned webinar and any mastering workflow. These instructions conflict for exactly the reader considering the documented fallback.
## cross_page_consistency — needs_revision
Produce explicitly offers cloud recording as fallback or backup, whereas this page excludes any planned production. Record hub also imposes universal separate video and uncompressed audio despite listing Zoom fallback paths; shared hub correction remains necessary.
## reasonable_claims — needs_revision
Official Zoom resolution documentation lists 360p, 720p and 1080p conditions for cloud recordings, contradicting the unqualified 720p table. Cloud settings support distinct speaker/gallery/screen files and optional per-person M4A audio/transcripts. No read source establishes universally lower audio quality caused by cloud processing; retain production preference without that asserted comparison.
## usability — needs_revision
Current desktop/mobile light presentation has useful headings and breadcrumbs, but mobile dark captures make gallery and transcript rows pale text on pale backgrounds. Important output guidance is unreadable. Shared CSS correction remains unapproved; no new public quality date is justified.
## Practitioner reader gate
Purpose PASS: opening explains meeting/fallback use. First action REVISE: no cloud-settings or test-recording step. Example PASS: restricted devices and content-led webinar are concrete selection examples. Quality Bar REVISE: fixed 720p and unconditional transcript do not tell readers how to check actual files. Meaning/voice REVISE narrowly: preserve isolated-video preference, not universal audio inferiority. Essential limits REVISE: mention host/account permission and consent at the test step; avoid generic evidence disclaimers.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Material resolution, file layout, audio and transcription claims checked against full rendered official support articles, not snippets or loading shells.",
    "items": [
      {
        "url": "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066421",
        "claim": "Cloud recording always produces the listed 720p video output.",
        "finding": "Official table includes 360p without HD, 720p with meeting HD, 1080p with full HD, and separate screen-sharing conditions. Fixed 720p description is materially incomplete.",
        "checked_at": "2026-11-04T16:51:29.770Z"
      },
      {
        "url": "https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0064676",
        "claim": "Cloud video is mixed, separate audio is possible, and transcript is generated.",
        "finding": "Standard settings can create separate active-speaker/gallery/shared-screen views, not general independent video per participant. Separate M4A audio is optional up to 200 speakers, phone callers merged; transcript requires setting. No universal local-versus-cloud audio quality test is supplied.",
        "checked_at": "2026-11-04T16:51:29.770Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read the complete Produce and Record hubs and local-recording sibling, comparing the actual choice and quality instructions.",
    "items": [
      {
        "path": "patterns/produce/index.md",
        "claim": "Recording selection and downstream editing guidance should remain compatible.",
        "finding": "Cloud is described as fallback or backup, not an exclusion from all planned production; target absolute refusal needs narrowing.",
        "checked_at": "2026-11-04T16:51:29.770Z"
      },
      {
        "path": "patterns/produce/record/index.md",
        "claim": "Recording selection and downstream editing guidance should remain compatible.",
        "finding": "Hub lists Zoom fallback yet forbids mixed/compressed sources universally; existing owning hub correction remains preparation.",
        "checked_at": "2026-11-04T16:51:29.770Z"
      },
      {
        "path": "patterns/produce/record/zoom-local.md",
        "claim": "Recording selection and downstream editing guidance should remain compatible.",
        "finding": "Local sibling sensibly prioritizes audio-first fallback and separate audio; cloud superiority claims cannot be inferred from sibling recommendations.",
        "checked_at": "2026-11-04T16:51:29.770Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261104. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Prepare a complete minimal cloud correction on the SAME owning card, keep existing hub/CSS ownership and human approval gate. No body or score changes in this record-only release.
Nominal next review 2026-12-04T16:51:31Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.
