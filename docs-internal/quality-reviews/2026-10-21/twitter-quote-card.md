# twitter-quote-card — substantive quality review

AI editorial review, not human signoff. Complete current published Markdown and live article structure read. Scores preserved.

## Reader checks

Purpose PASS: attributed graphic plus short copy. First action REVISE: choose and verify the exact source quote before drafting. Example REVISE: Coming soon supplies no usable illustration. Quality Bar REVISE: check attribution, readable image and caption rather than untestable stop-the-scroll instruction. Meaning/voice: preserve confident single-quote guidance. Essential limits REVISE: distinguish verbatim quotation from paraphrase and require public-use permission.

## Rendered presentation

The central Template or Prompt Template uses dark red text against a dark background in slate mode, making executable instructions hard to read. Fresh live 1440/390 light/dark captures have no document overflow; all five dark mobile images and representative light desktop were visually inspected. Shared CSS correction remains unapproved.

Fresh evidence: output/reports/omi-quality-20261021/ per-path 1440/390 light/dark PNG and JSON. Shared CSS owner: 8006e12e-6551-440a-b9cc-27bce652996f. No playback or comprehensive accessibility certification. Body correction: e050b6be-b3e8-4872-83c4-a6e8fee980f8. Proposed fixes cannot earn a pass on unchanged public bodies.

## Six findings and provenance

~~~json
{
  "id": "quality-20261021-twitter-quote-card",
  "status": "needs_revision",
  "assessed_at": "2026-10-21T16:48:35Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "6c88dc1f1907892805c20da6cf343a49ad9449b38769d662feee6d794a63c03c",
  "report_ref": "docs-internal/quality-reviews/2026-10-21/twitter-quote-card.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening clearly identifies an attributed quotation graphic with short supporting copy, a useful route for promoting a single episode insight."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The Example is Coming soon and the generic hook/body/CTA template never specifies the quote graphic, exact quotation or attribution layout. These are central outputs rather than optional editorial embellishments."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "The opening promises a quote-card image, but the supplied prompt requests only a social post and treats an insight and an exact quote interchangeably; it cannot reliably produce the promised asset."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "Quote Share parent explicitly pairs the quote with a graphic or clip; the LinkedIn sibling similarly requires attributed context. The Twitter leaf needs an image brief and verbatim source input to implement that shared intent."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "The 280-character budget is appropriate for ordinary short X posts, supported by official counting documentation; URLs count 23 and emoji may count two. No proof of every practitioner hook recommendation is demanded."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "The central Template or Prompt Template uses dark red text against a dark background in slate mode, making executable instructions hard to read. Fresh live 1440/390 light/dark captures have no document overflow; all five dark mobile images and representative light desktop were visually inspected. Shared CSS correction remains unapproved."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "The 280-character budget is appropriate for ordinary short X posts, supported by official counting documentation; URLs count 23 and emoji may count two. No proof of every practitioner hook recommendation is demanded. No additional source verification or human testing is claimed.",
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
        "path": "patterns/package/social-posts/types/quote-share/index.md",
        "claim": "Published guidance should support a coherent usable packaging task.",
        "finding": "Quote Share parent explicitly pairs the quote with a graphic or clip; the LinkedIn sibling similarly requires attributed context. The Twitter leaf needs an image brief and verbatim source input to implement that shared intent.",
        "checked_at": "2026-10-21T16:48:35Z"
      },
      {
        "path": "patterns/package/social-posts/types/quote-share/linkedin-quote-post.md",
        "claim": "Published guidance should support a coherent usable packaging task.",
        "finding": "Quote Share parent explicitly pairs the quote with a graphic or clip; the LinkedIn sibling similarly requires attributed context. The Twitter leaf needs an image brief and verbatim source input to implement that shared intent.",
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
