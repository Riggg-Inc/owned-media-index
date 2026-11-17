# show-notes-for-llms whole-page quality assessment

AI editorial review. Read complete current body, all examples and prompt, not just opening caveat. Names/40-percent claim are explicitly illustrative; no real customer or experimental result inferred. Desktop/mobile light/dark captures retained; mobile slate screenshot visually inspected and code text is difficult to read. No model output experiment or empirical retrieval test performed.

Practitioner checks: Purpose PASS (usable episode notes); First action PASS (summary then questions); Example PASS (concrete and clearly illustrative); Quality Bar REVISE (minimum counts must not force unsupported claims); Meaning/voice PASS for minimal fix intent (retain four sections and confident advice); Essential limits REVISE (copy-ready prompt needs explicit source-only, omit missing facts, verify quotes/links and permission). Existing shared hub/contrast card only. Findings remain PREPARATION pending complete reconciled immutable proposal and exact owner review; no publication of rewritten body or pass date. Preserve all useful examples, but require source-checked replacements.

## Exact assessment record

{
  "id": "quality-20261117-show-notes-for-llms",
  "status": "needs_revision",
  "assessed_at": "2026-11-17T16:59:36Z",
  "reviewer": "Cass Reelman — openai/gpt-6-astra (AI editorial review)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "9d5427a091a6b06cf246ed3e14737160a3c58856ef3428842d1baea0c0f5a9fc",
  "report_ref": "docs-internal/quality-reviews/2026-11-17/show-notes-for-llms.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Four-part summary, questions, claims and resources template helps producers turn a recording into usable episode notes immediately."
    },
    "substance": {
      "status": "pass",
      "rationale": "Worked summary, three sample answers, attributed claims and a copy-ready prompt provide concrete detail; illustrative names and outcomes are explicitly labeled rather than represented as customer evidence."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "Quality Bar says every answer must be accurate and verifiable, yet the copy-ready prompt requires three to five quotable claims and resource URLs from an excerpt without instructing omission of unsupported details or human verification. This invites invented attributions when the source is insufficient."
    },
    "cross_page_consistency": {
      "status": "needs_revision",
      "rationale": "Transcript companion preserves recorded words and public-release permission; Measurement requires opening sources and retaining uncertainty. The show-notes prompt does not carry those safeguards into its copy-ready instructions and its mandatory counts may encourage filling gaps."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "Google guidance supports readable textual content without special optimizations and Microsoft supports clearer structure, but neither substantiates the page evidence label LLM retrieval testing. No test protocol/results are supplied. Present practical Q&A advice as practitioner guidance, not an undocumented empirical test claim."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh slate mobile render makes the copy-ready examples and prompt dark red on dark code backgrounds, difficult to read; essential teal links also remain low contrast. Light layout and heading sequence are useful and document overflow was false."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Relevant primary guidance checked for AI content structure claims; illustrative quotations are not treated as empirical results.",
    "items": [
      {
        "url": "https://developers.google.com/search/docs/appearance/ai-features",
        "claim": "Structured questions and answers are an empirically established special AI optimization.",
        "finding": "Google says no special optimization is necessary and recommends helpful textual content; it does not document this page claimed LLM retrieval testing.",
        "checked_at": "2026-11-17T16:51:23Z"
      },
      {
        "url": "https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/",
        "claim": "Clear headings and FAQ sections can help readers and AI systems locate information.",
        "finding": "Microsoft recommends structure and clarity, supporting practical formatting advice without establishing the page sample asset counts or claimed testing.",
        "checked_at": "2026-11-17T16:52:21Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete transcript and measurement pages read for preservation and verification standards.",
    "items": [
      {
        "path": "patterns/publish/ai-search-optimization/transcript-optimization.md",
        "claim": "Generated source summaries should preserve actual words and publication permission.",
        "finding": "Companion explicitly requires public-release clearance and preserved voice; copy-ready show-notes instructions should not fabricate quotes from insufficient excerpts.",
        "checked_at": "2026-11-17T16:59:36Z"
      },
      {
        "path": "patterns/publish/ai-search-optimization/measurement.md",
        "claim": "Citable claims need supporting sources rather than mere attribution.",
        "finding": "Measurement instructs opening citations and checking support, compatible with a human verification step missing from this prompt.",
        "checked_at": "2026-11-17T16:59:36Z"
      }
    ]
  },
  "next_review_at": "2026-12-17T16:59:36Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Copy-ready prompt needs source insufficiency and human verification safeguards, undocumented testing label needs clarification, and dark code contrast requires shared correction.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
