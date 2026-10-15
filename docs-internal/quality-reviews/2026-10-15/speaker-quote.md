# speaker-quote — substantive post-release quality assessment

AI editorial review, not human testing or signoff. Complete source Markdown, live rendered article, quote-graphics hub, Framework and Scoring read. Browser captures in output/reports/omi-quality-20261015/; screenshot inspection confirms dark code contrast. Reader task checks: Purpose PASS (speaker recognition); First action PASS (choose exact quote and headshot); Example PASS (fillable production template, not a claimed real campaign); Quality Bar PASS (30 words, attribution, mobile reading, two shapes); Meaning/voice PASS unchanged confident advice; Essential limits PASS audience-fit avoidance. Usability REVISE remains blocking. Optional fully worked example or rights reminder is not alone a failure. No external source certification or score redesign claimed.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261015-speaker-quote",
  "status": "needs_revision",
  "assessed_at": "2026-10-15T16:48:19Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "8e92a325db30522bec14e435540e709a872853bff198cd9f10d9312cb3e7b333",
  "report_ref": "docs-internal/quality-reviews/2026-10-15/speaker-quote.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening tells an editor to choose the portrait treatment when the speaker matters to this audience, and the avoidance rule keeps anonymous faces from overpowering a stronger quote."
    },
    "substance": {
      "status": "pass",
      "rationale": "The template requests exact words, a headshot, attribution and brand colors, with two export shapes and a mobile-legibility check; this is usable production guidance rather than filler."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The opening, use case, avoidance rule and template consistently prioritize the quote and appropriate speaker recognition; repeated definition is a minor editorial preference, not a blocking defect."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The quote-graphics parent lists the same style and score; Framework defines Package as usable derivatives and Scoring calls ratings editorial judgments. Parent performance/spec defects are not evidence that this specific template fails."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Thirty words and two output shapes are house design choices, not claimed platform limits. Recognizable speaker selection is practitioner advice, not a measured reach guarantee; most direct is ordinary editorial characterization."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Live desktop1440/mobile390 light/dark captures show organized headings and no document overflow, but dark-mode red prompt text on dark background makes the central reusable template difficult to read. Existing shared CSS correction is material."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "This is practitioner design advice, not measured performance evidence; no quoted statistic or external attribution requires certification.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete related published pages and compared their actual operating guidance.",
    "items": [
      {
        "path": "framework.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Package explicitly asks for understandable reusable assets; the concrete template serves that task.",
        "checked_at": "2026-10-15T16:48:19Z"
      },
      {
        "path": "scoring.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Scores are editorial judgments, not measured outcomes; this assessment does not redesign or certify score evidence.",
        "checked_at": "2026-10-15T16:48:19Z"
      }
    ]
  },
  "next_review_at": "2027-01-13T16:48:19Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Material low-contrast prompt text in supported dark mode prevents comfortable use; existing shared CSS correction awaits exact approval.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
