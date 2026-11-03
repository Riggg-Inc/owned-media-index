# Whole-page quality review: patterns/produce/record/streamyard.md
Completed 2026-11-03T16:48:03Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: fa39fff7537c1b5ea56b032545adbfabfe88ee21d70b8f33c6141a90bb66dae0
Outcome: needs_revision; not human signoff.
## usefulness — pass
The opening identifies the composite-only workflow and tells the practitioner to test local-track options before participant-level editing; this is useful selection guidance, not a blanket product verdict.
## substance — pass
The output table, use and avoid lists, and two-up layout example explain the editing tradeoff concretely. This short decision reference does not need a full recording tutorial.
## coherence — pass
The opening and capability caveat scope the score to composite-only output, and the final contrast between baked layout and isolated sources follows that scope. Absolute wording about reframing should be read as recovering independent sources, not impossibility of any pixel crop.
## cross_page_consistency — needs_revision
The Record hub still describes StreamYard product-wide as mixed composite only with no isolated tracks or local recording. That contradicts this page’s explicit capability caveat and the official product page; the already-owned hub correction must resolve this shared conflict.
## reasonable_claims — pass
Official StreamYard recording information confirms local per-person audio/video and a parallel cloud recording, supporting the deliberate composite-only scope. Loss of independent source layers is a reasonable editing limitation, not an empirical performance promise. The official product page supports 1080p local output but does not fully certify every cloud-output setting; no comprehensive plan or codec certification is claimed.
## usability — needs_revision
Fresh desktop and mobile light/dark rendering shows the striped Audio output row as near-white text on a pale background in dark mode, making an essential capability comparison unreadable. Light layout and breadcrumb/section organization are usable, but the existing shared CSS defect blocks a whole-page pass.
## Practitioner reader gate
Purpose PASS: opening names composite-only selection. First action PASS: confirm plan/settings/upload with a test recording. Example PASS: two-up composite demonstrates lost independent layers. Quality Bar PASS for reference: whether the live layout is final versus needing participant-level editing is an observable decision test. Meaning/voice PASS: no rewrite or weakened production preference proposed. Essential limits REVISE: adjacent Record hub contradicts the important local-track qualification; dark Audio row conceals a key limitation. No human readability testing claimed.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Current platform capabilities matter to the composite-only scope; official product text was read rather than inferred from a citation count.",
    "items": [
      {
        "url": "https://streamyard.com/recordings",
        "claim": "StreamYard supports local separate audio and video alongside cloud recording.",
        "finding": "Official product page states each user records separate audio/video on their device and uploads in the background, while a cloud recording is also created. It describes 1080p local recordings. This supports the capability caveat; it does not certify all cloud codec/plan limits or repeat vendor quality guarantees as independent evidence.",
        "checked_at": "2026-11-03T16:48:02Z"
      },
      {
        "url": "https://support.streamyard.com/hc/en-us/articles/10725401176596-Local-Recording-of-your-Live-Stream",
        "claim": "The linked local-recording help article documents individual source tracks.",
        "finding": "Direct retrieval returned HTTP403. Indexed snippet mentions individual tracks, but complete article was not read; the accessible official recording product page supplies independent current capability context instead.",
        "checked_at": "2026-11-03T16:48:02Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read the complete recording and rough-cut hubs to compare the article\u2019s selection boundary with its adjacent production guidance.",
    "items": [
      {
        "path": "patterns/produce/record/index.md",
        "claim": "The hub should distinguish composite-only workflows from available isolated source modes.",
        "finding": "Hub tables still categorically deny StreamYard isolated tracks and local recording. This contradicts the scoped article and official current feature description. Existing hub correction remains required, not a duplicate article rewrite.",
        "checked_at": "2026-11-03T16:48:02Z"
      },
      {
        "path": "patterns/produce/rough-cut/index.md",
        "claim": "Independent sources preserve layout choice for the described OBS rough-cut workflow.",
        "finding": "The rough-cut hub calls for isolated participant feeds and multiple layouts, consistent with the article\u2019s explanation of what a baked composite cannot restore. Other hub specifications were not separately certified in this comparison.",
        "checked_at": "2026-11-03T16:48:02Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261103. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Reuse existing Record hub preparation and shared dark CSS correction on the same card. No separate StreamYard rewrite is necessary to fix these shared defects. Hub numerical reconciliation remains preparation; exact CSS/hub approval and release must precede fresh assessment. Do not alter score or publish candidate bodies.
Nominal next review 2026-12-03T16:48:03Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.
