# stat-callout — substantive post-release quality assessment

AI editorial review by current model, not human signoff. Full source and live article plus Speaker Quote, Quote Graphics hub, Framework and Scoring read. Purpose PASS (highlight credible number); First action PASS (select number/source/context); Example PASS (specific fillable visual brief rather than invented data); Quality Bar PASS with optional quote-to-stat tailoring (source visible, mobile-readable); Meaning/voice PASS (unchanged useful guidance); Essential limits PASS (reject heavy context or unreliable source). Dark-mode usability REVISE on existing CSS card only; do not create a new body correction for optional preference. Screenshots at1440/390 light/dark retained; no full-site accessibility certification.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261015-stat-callout",
  "status": "needs_revision",
  "assessed_at": "2026-10-15T16:48:40Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "52d45672da103e88638187cbcafb4cd39bdd5cf978e5a931113025b47fd96e4c",
  "report_ref": "docs-internal/quality-reviews/2026-10-15/stat-callout.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening makes a credible context-bearing number the selection test, and the prompt tells the designer to make that number visually dominant with a visible source."
    },
    "substance": {
      "status": "pass",
      "rationale": "Number, context line, source, optional speaker and colors are concrete production inputs; clear context and attribution requirements support an actual export rather than abstract advice."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The generic Quality Bar mentions quotes and mandatory speaker attribution while the statistic-specific template makes the speaker optional. This deserves a small optional tailoring, but the opening and explicit source requirement resolve the task without a materially misleading instruction."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "Speaker Quote uses the same mobile-reading and brand rules; Quote Graphics lists Stat Callout for data and benchmarks. Framework Package is served by retaining context; no platform-size claim in this page is treated as a hard limit."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "There are no sample statistics to certify and no empirical performance promise. Credible sourcing and avoiding context-heavy numbers are sound editorial decision rules; suggested shapes are design output choices."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Light desktop is readable and mobile has no document overflow. In dark mode the core prompt is low-contrast red on a dark panel, and link contrast is weak, materially impeding the actual copy-and-customize task."
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
        "checked_at": "2026-10-15T16:48:40Z"
      },
      {
        "path": "scoring.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Scores are editorial judgments, not measured outcomes; this assessment does not redesign or certify score evidence.",
        "checked_at": "2026-10-15T16:48:40Z"
      }
    ]
  },
  "next_review_at": "2027-01-13T16:48:40Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Material low-contrast prompt text in supported dark mode prevents comfortable use; existing shared CSS correction awaits exact approval.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
