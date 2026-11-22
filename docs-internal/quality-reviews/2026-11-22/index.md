# index — whole-page quality assessment

Complete current Markdown and rendered article read. AI editorial review, not human testing or signoff.
## Practitioner reader gate
Purpose PASS: opening identifies the decision. First action PASS: choose by source/audience/task before tools or format. Example PASS: concrete named choices and decision mappings are appropriate to a comparison page. Quality Bar REVISE: essential selection alternatives must remain readable in dark mode. Meaning/voice REVISE: retain practical shortlist while correcting the specific factual/interaction claims described above. Essential limits REVISE: distinguish editorial rankings from measured guarantees and platform/feed control where relevant.
## Render evidence
Fresh public Chromium 1440/390 light/dark captures examined; desktop-light and mobile-dark screenshots visually inspected. No horizontal overflow. Pale alternating table rows retain near-white text in dark mode, hiding decision guidance; essential teal links also lose contrast. Reuse existing shared CSS correction, not a duplicate.
Artifacts: output/reports/omi-quality-20261122/quadrants__index-{default,slate}-{1440,390}.{png,json}. Desktop-light/mobile-dark screenshots visually inspected.
## Next action
Reuse same shared correction card/CSS proposal. Preserve scores/axes/positions. Prose proposals remain preparation until immutable complete handoff, independent review and exact approval. Park until approved change or explicit retry; no public pass date.
## Six reasoned checks and exact record
{
  "id": "quality-20261122-quadrants-index",
  "status": "needs_revision",
  "assessed_at": "2026-11-22T17:08:34Z",
  "reviewer": "Cass Reelman — openai/gpt-6-astra (AI editorial review)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "0542d41e9071a127e0f532447d7f4b48163c2b8432b1b7941ddaa1f4325db78e",
  "report_ref": "docs-internal/quality-reviews/2026-11-22/index.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The hub quickly routes readers to the right comparison category and names each decision axis."
    },
    "substance": {
      "status": "pass",
      "rationale": "Six concise links with axes and plotted inventory are sufficient substance for this routing page; another long tutorial would add friction."
    },
    "coherence": {
      "status": "pass",
      "rationale": "One opening, an interaction explanation and one inventory table form a coherent small navigation hub."
    },
    "cross_page_consistency": {
      "status": "needs_revision",
      "rationale": "Recording Methods actually plots eight dots, not the six claimed in Patterns Plotted. Distribution uses non-link divs, contradicting the hub instruction that dots click to full pattern pages; Mastering links mostly to a shared guide rather than individual tool pages."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "The count and universal click-through claims are directly falsified by the actual linked source markup, not a matter of editorial preference. Other inventories match: 11 titles, six descriptions, five clips, nine tools and 13 platforms."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh public Chromium 1440/390 light/dark captures examined; desktop-light and mobile-dark screenshots visually inspected. No horizontal overflow. Pale alternating table rows retain near-white text in dark mode, hiding decision guidance; essential teal links also lose contrast. Reuse existing shared CSS correction, not a duplicate. The table is the central task interface; Description, Recording and Distribution axes/counts are almost invisible in dark mode."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "This comparison uses editorial selection guidance and directly inspected internal inventory, not external numerical outcomes or attributed examples.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant companion pages and framework/scoring definitions read to compare actual meaning, not keyword overlap.",
    "items": [
      {
        "path": "quadrants/recording.md",
        "claim": "Current document assertion or comparison: Recording inventory count",
        "finding": "Read full source: eight plotted entries, including Riverside and SquadCast separately, not the six claimed by the hub.",
        "checked_at": "2026-11-22T17:08:34Z"
      },
      {
        "path": "quadrants/distribution-platforms.md",
        "claim": "Current document assertion or comparison: Click-through interaction",
        "finding": "All thirteen platform dots are div elements, not linked pattern destinations; universal click-through instruction is false.",
        "checked_at": "2026-11-22T17:08:34Z"
      },
      {
        "path": "quadrants/mastering-tools.md",
        "claim": "Current document assertion or comparison: Tool chart inventory",
        "finding": "Nine plotted tools match the count; most link to the common mastering guide rather than individual pattern pages.",
        "checked_at": "2026-11-22T17:08:34Z"
      }
    ]
  },
  "next_review_at": "2027-02-20T17:08:34Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Material readable-selection failure in current dark presentation; additional page-specific factual or consistency corrections are identified in the six findings.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
