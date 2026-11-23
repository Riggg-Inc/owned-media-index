# Quality review: quadrants/recording.md
Outcome: needs_revision. AI editorial review: openai/gpt-6-astra; not human testing or approval.
Completed UTC: 2026-11-23T16:48:27Z
Exact body SHA-256: ce7dac653f471456fb0472e19c5ad63e5606981e1a7b659ad8799cf2acce9e71

usefulness: pass
The opening and location-based selection rows help producers choose a recording workflow before selecting equipment.

substance: pass
Six concrete need-to-method rows explain isolated tracks, mixed locations and meeting capture with relevant linked details.

coherence: needs_revision
The StreamYard point names the whole product while the linked pattern deliberately rates only composite-only capture; the visual comparison loses that essential scope.

cross_page_consistency: needs_revision
StreamYard guidance explicitly acknowledges isolated local tracks, whereas the quadrant comment says no isolation and the product-wide label remains unqualified.

reasonable_claims: needs_revision
The gap paragraph treats Zoom Cloud as inherently needing rescue and isolated platforms as studio quality without the microphone, room and test conditions identified in the remote recording checklist.

usability: needs_revision
Actual light and dark desktop/mobile screenshots show hover-only point names and very faint quadrant labels; dark alternating table rows render near-white text on pale backgrounds, obstructing selection.

Practitioner reader checks
Purpose PASS: choose by participant location. First action PASS: select the Remote guest interviews row. Example PASS: studio host plus remote guests maps to Hybrid. Quality Bar REVISE: source-quality promise lacks test conditions. Meaning/voice PASS for proposed targeted fixes: preserve confident isolated-track recommendation. Essential limits REVISE: label StreamYard composite-only and replace automatic rescue language.

Evidence and corrections
Read full Markdown and live article in all four captures quadrants__recording-{default,slate}-{1440,390}.png/json under /home/production/openclaw-workspace/output/reports/omi-quality-20261123. No horizontal document overflow. AI screenshot inspection actually performed. Source snapshot source-riverside.json; StreamYard help fetch returned 403, local-recording page failed extraction, blog redirected to index; no fresh vendor verification claimed for StreamYard. Cross-page scope alone establishes needed qualifier. Reuse shared card 8006e12e-6551-440a-b9cc-27bce652996f and existing contrast issue; parent owns routing. No score changes proposed. Corrections PREPARATION only; no public body edited.

{
  "source_checks": {
    "applicable": true,
    "rationale": "Fresh vendor reading checks isolated recording capability without claiming measured quality or account testing.",
    "items": [
      {
        "url": "https://riverside.fm/",
        "claim": "Remote local capture provides separate high quality source tracks.",
        "finding": "Vendor homepage explicitly advertises up to 4K video and uncompressed audio in separate tracks; this supports capability, not guaranteed studio results from any room or equipment.",
        "checked_at": "2026-11-23T16:48:26Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read full recording neighbors to compare workflow scope and practical prerequisites.",
    "items": [
      {
        "path": "patterns/produce/record/streamyard.md",
        "claim": "The plotted StreamYard score describes the named recording choice.",
        "finding": "Companion limits its score to composite-only livestream capture and explicitly recognizes local individual tracks; the quadrant product label needs that same scope.",
        "checked_at": "2026-11-23T16:48:26Z"
      },
      {
        "path": "patterns/produce/record/remote-isolated.md",
        "claim": "Isolated recording supplies studio quality with minimal setup.",
        "finding": "Companion requires external microphone, quiet room, lighting, local recording test and backup; preserve these practical conditions instead of presenting a platform guarantee.",
        "checked_at": "2026-11-23T16:48:26Z"
      },
      {
        "path": "patterns/produce/record/zoom-cloud.md",
        "claim": "Zoom Cloud is the lower flexibility choice in the selection guide.",
        "finding": "Companion supports meeting-reference use and warns against planned isolated-video edits, but its own absolute quality statements are not independent measurement evidence.",
        "checked_at": "2026-11-23T16:48:26Z"
      }
    ]
  }
}