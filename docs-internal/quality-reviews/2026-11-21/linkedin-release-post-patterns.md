# linkedin-release-post-patterns whole-page quality assessment

AI editorial review: Cass Reelman, openai/gpt-6-astra. Entire current published body and comparisons read, fresh1440/390 light/dark captures; desktop-light/mobile-dark visually inspected, no horizontal overflow. No human signoff.

Reader task: Purpose PASS (episode release posts); First action REVISE (choose an angle does not explain how to draft it); Example REVISE (The Lesson and nine other names are not examples); Quality Bar REVISE (value before click is sensible but no observable grounding check); Meaning/voice PASS (retain confident advice and all ten alternatives); Essential limits PASS as advice, but proposed templates should explicitly use verified source details rather than fabricate quotations.

Next: full proposed copy with actual structures and one clearly hypothetical post; exact owner approval required. No score changes or platform-performance promises. Existing shared correction card owns this preparation and CSS.

## Exact assessment record

{
  "id": "quality-20261121-linkedin-release-post-patterns",
  "status": "needs_revision",
  "assessed_at": "2026-11-21T16:51:21Z",
  "reviewer": "Cass Reelman — openai/gpt-6-astra (AI editorial review)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "5d6fa18ce6b9a2ea184570af0b35c8966190c39aa7cd19c6999b726cd01c40a0",
  "report_ref": "docs-internal/quality-reviews/2026-11-21/linkedin-release-post-patterns.md",
  "dimensions": {
    "usefulness": {
      "status": "needs_revision",
      "rationale": "The opening promises reusable release patterns but a reader receives only ten names, with no way to turn The Tension or The Guest POV into a usable post."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "Example Patterns contains no actual examples or structures; repeating the definition in What It Is uses space without supplying the missing working model."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Value before a click, feed-native relevance and the exception for existing demand form a consistent editorial argument."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The Publish hub routes feed-native release work here and the canonical-page companion similarly asks for standalone value rather than click-only teasers."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Advice about giving a reason to care is practitioner judgment, not a claimed algorithm benefit or measured engagement guarantee; existing score is not rescored."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "The ten labels lack a first drafting action or observable source-fidelity check; dark breadcrumb links are also difficult to distinguish on the actual mobile render."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "No platform limits, numeric benchmarks or empirical mechanism claims are asserted; editorial advice does not require a controlled experiment.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Full Publish hub and canonical-page standard were read to compare routing and value-first promise.",
    "items": [
      {
        "path": "patterns/publish/index.md",
        "claim": "Hub promises post formats for launching an episode. ",
        "finding": "Ten format labels without examples underdeliver that practical promise; routing itself is correct.",
        "checked_at": "2026-11-21T16:51:21Z"
      },
      {
        "path": "patterns/publish/canonical-episode-page.md",
        "claim": "Content should provide utility before playback or subscription.",
        "finding": "Value-before-click direction agrees with the concrete independent worksheet example in the companion.",
        "checked_at": "2026-11-21T16:51:21Z"
      }
    ]
  },
  "next_review_at": "2026-12-21T16:51:21Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Supply concrete post structures and a worked hypothetical example while retaining all ten angles; shared dark navigation contrast also remains.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
