# linkedin-long-form — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose PASS: make a new episode professionally relevant. First action PASS at intent level: choose an insight beyond the title. Example REVISE: Coming soon offers no standalone professional lesson. Quality Bar REVISE under substance: add an observable useful application supported by the episode. Meaning/voice PASS for narrow correction: retain professional framing and singular CTA, not a legalistic rewrite. Essential limits REVISE under substance: prompt needs actual audience/application facts and must not invent guest claims.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261018/, per-path default/slate 1440/390 PNG and JSON. Light desktop and dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261018-linkedin-long-form",
  "status": "needs_revision",
  "assessed_at": "2026-10-18T16:48:54Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "4d8c17072132e45bafc7172d3875d3bf89b4d12191eca166e4148ac983985c90",
  "report_ref": "docs-internal/quality-reviews/2026-10-18/linkedin-long-form.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening explains professional relevance before a viewing invitation and tells readers to make the post valuable without a click. That is a useful release-post task, not a generic announcement."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The template and prompt ask for value/context but never show how to turn an episode insight into a professional application. Coming soon replaces the only example. The promised standalone professional value needs one concrete worked post and audience/use-case inputs, not more introductory repetition."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The long-form context and approximately1300-character editorial target are compatible with the introduction. Hook, body and one CTA are a sensible progression; naming capitalization is only optional polish."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The parent describes thought-leadership framing, and the Instagram/X siblings distinguish visual support and short promises. This page maintains those roles; Framework Package expects independently usable assets, which the missing worked example should demonstrate."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "The page explicitly labels1300characters an editorial target, not a platform limit or engagement optimum. Neither professional relevance nor stop-the-scroll advice asserts empirical results. No research certification is required for those recommendations."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "The page explicitly labels1300characters an editorial target, not a platform limit or engagement optimum. Neither professional relevance nor stop-the-scroll advice asserts empirical results. No research certification is required for those recommendations. No external factual-source reading is claimed for this advice-only scope; internal scores are preserved, not rescored or empirically certified.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/episode-announcement/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent describes thought-leadership framing, and the Instagram/X siblings distinguish visual support and short promises. This page maintains those roles; Framework Package expects independently usable assets, which the missing worked example should demonstrate.",
        "checked_at": "2026-10-18T16:48:54Z"
      },
      {
        "path": "patterns/package/social-posts/types/episode-announcement/instagram-caption.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent describes thought-leadership framing, and the Instagram/X siblings distinguish visual support and short promises. This page maintains those roles; Framework Package expects independently usable assets, which the missing worked example should demonstrate.",
        "checked_at": "2026-10-18T16:48:54Z"
      },
      {
        "path": "framework.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "Framework Package asks whether an asset can be understood and used without extra explanation. A hub can route readers concisely; a leaf needs enough concrete input and examples to execute its promise.",
        "checked_at": "2026-10-18T16:48:54Z"
      }
    ]
  },
  "next_review_at": "2026-11-17T16:48:54Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Await exact owner-approved shared contrast correction and complete concrete pattern guidance correction on existing package card.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
~~~
