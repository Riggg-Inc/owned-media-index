# instagram-caption — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose PASS: introduce an episode through its visual and one reason. First action PASS at intent level: choose episode asset and listening/viewing action. Example REVISE: Coming soon is not a usable caption. Quality Bar REVISE under substance: add an observable visual-caption match and a supplied destination, rather than only stop the scroll. Meaning/voice PASS for intended minimal correction: preserve hook/value/singular CTA and confident voice. Essential limits REVISE under substance: prompt must not invent visual details, quotations or access routes; use supplied public facts.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261018/, per-path default/slate 1440/390 PNG and JSON. Light desktop and dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261018-instagram-caption",
  "status": "needs_revision",
  "assessed_at": "2026-10-18T16:48:54Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "4c985ab19b96c937d5a8f901a293d0ee62364195bab1e6eb093d8108b30f83e5",
  "report_ref": "docs-internal/quality-reviews/2026-10-18/instagram-caption.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening clearly identifies an image-led announcement and asks for one reason to care plus a listening or viewing action. A reader can identify the task and initial episode asset."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The body repeats its opening and supplies only generic hook/body/CTA placeholders. The Example is Coming soon and the prompt never requests the actual visual or chosen listening route, despite promising a visual-first caption. A concrete worked caption and asset/route inputs are materially missing."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The introduction, When To Use, template and singular CTA form a coherent sequence. The weakness is insufficient task-specific execution, not a contradictory overall concept."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The hub promises a caption supporting the image; this page repeats that promise but its prompt requests only episode metadata, not the image. Social Posts requires added value and platform tailoring. The mismatch is captured under substance; it does not require changing the framework."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "No more than 2200 is explicitly a drafting target with current-app truncation preview, not a freshly certified universal technical maximum. Stop the scroll is aspirational advice, not a measured guarantee. No external factual claim requires verification for this editorial scope."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "No more than 2200 is explicitly a drafting target with current-app truncation preview, not a freshly certified universal technical maximum. Stop the scroll is aspirational advice, not a measured guarantee. No external factual claim requires verification for this editorial scope. No external factual-source reading is claimed for this advice-only scope; internal scores are preserved, not rescored or empirically certified.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/episode-announcement/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The hub promises a caption supporting the image; this page repeats that promise but its prompt requests only episode metadata, not the image. Social Posts requires added value and platform tailoring. The mismatch is captured under substance; it does not require changing the framework.",
        "checked_at": "2026-10-18T16:48:54Z"
      },
      {
        "path": "patterns/package/social-posts/types/episode-announcement/linkedin-long-form.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The hub promises a caption supporting the image; this page repeats that promise but its prompt requests only episode metadata, not the image. Social Posts requires added value and platform tailoring. The mismatch is captured under substance; it does not require changing the framework.",
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
