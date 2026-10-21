# twitter-thread — substantive quality review

AI editorial review, not human signoff. Complete current published Markdown and live article structure read. Scores preserved.

## Reader checks

Purpose PASS: explain a connected topic across posts. First action REVISE: supply a sourced sequence or transcript passage. Example REVISE: Coming soon is not actionable. Quality Bar REVISE: each post adds a distinct supported point, with weighted character check and one final CTA. Meaning/voice: retain confident sequence advice. Essential limits REVISE: human verify claims/quotes and link before posting.

## Rendered presentation

The central Template or Prompt Template uses dark red text against a dark background in slate mode, making executable instructions hard to read. Fresh live 1440/390 light/dark captures have no document overflow; all five dark mobile images and representative light desktop were visually inspected. Shared CSS correction remains unapproved.

Fresh evidence: output/reports/omi-quality-20261021/ per-path 1440/390 light/dark PNG and JSON. Shared CSS owner: 8006e12e-6551-440a-b9cc-27bce652996f. No playback or comprehensive accessibility certification. Body correction: e050b6be-b3e8-4872-83c4-a6e8fee980f8. Proposed fixes cannot earn a pass on unchanged public bodies.

## Six findings and provenance

~~~json
{
  "id": "quality-20261021-twitter-thread",
  "status": "needs_revision",
  "assessed_at": "2026-10-21T16:48:35Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "17d7ebba3e46c7c590b370ffd36fa32a29e59d99a2606a0f18fa27cc7d5368ce",
  "report_ref": "docs-internal/quality-reviews/2026-10-21/twitter-thread.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Use a sequence needing more room than one post and close with one clear action is a clear and useful practitioner task."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The opening/next/closing outline helps ordering but Coming soon provides no worked thread. The prompt has one insight input and lacks the actual connected source material needed to draft a faithful explanation."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "The multi-post template and single generic social-post prompt disagree about output structure. Request numbered posts with connected takeaways rather than relying on the model to invent the missing sequence."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The Thread Breakdown hub and LinkedIn Carousel sibling share an ordered explanation purpose. Preserve source context and one final action; do not import the hub unsupported algorithmic favor claim."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "The 280-character short-post drafting budget is supported by official X character-counting documentation. Weighted Unicode and 23-character links matter; the budget is not a claim that paid longer-post features do not exist."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "The central Template or Prompt Template uses dark red text against a dark background in slate mode, making executable instructions hard to read. Fresh live 1440/390 light/dark captures have no document overflow; all five dark mobile images and representative light desktop were visually inspected. Shared CSS correction remains unapproved."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "The 280-character short-post drafting budget is supported by official X character-counting documentation. Weighted Unicode and 23-character links matter; the budget is not a claim that paid longer-post features do not exist. No additional source verification or human testing is claimed.",
    "items": [
      {
        "url": "https://docs.x.com/fundamentals/counting-characters",
        "claim": "Ordinary short X posts use a 280 weighted character budget.",
        "finding": "Official documentation supports 280 weighted characters, 23 per URL and special emoji/Unicode weights. This verifies ordinary short-post scope, not absence of paid longer posts.",
        "checked_at": "2026-10-21T16:46:10Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant parent and sibling guidance plus Framework were read against the actual practitioner task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/thread-breakdown/index.md",
        "claim": "Published guidance should support a coherent usable packaging task.",
        "finding": "The Thread Breakdown hub and LinkedIn Carousel sibling share an ordered explanation purpose. Preserve source context and one final action; do not import the hub unsupported algorithmic favor claim.",
        "checked_at": "2026-10-21T16:48:35Z"
      },
      {
        "path": "patterns/package/social-posts/types/thread-breakdown/linkedin-carousel.md",
        "claim": "Published guidance should support a coherent usable packaging task.",
        "finding": "The Thread Breakdown hub and LinkedIn Carousel sibling share an ordered explanation purpose. Preserve source context and one final action; do not import the hub unsupported algorithmic favor claim.",
        "checked_at": "2026-10-21T16:48:35Z"
      },
      {
        "path": "framework.md",
        "claim": "Published guidance should support a coherent usable packaging task.",
        "finding": "Framework Package asks whether the resulting asset can be understood and reused without extra explanation; current assessment distinguishes concise routing hubs from executable leaf guidance.",
        "checked_at": "2026-10-21T16:48:35Z"
      }
    ]
  },
  "next_review_at": "2026-11-20T16:48:35Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Await exact owner approval for body guidance correction and shared dark contrast repair; unchanged pending proposals do not require duplicate research.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
~~~
