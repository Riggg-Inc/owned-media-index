# twitter-one-liner — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose pass: the opening identifies the post and use case. First action revise: the generic hook/body template omits source selection and audience application. Example revise: Coming soon is not an example. Quality Bar revise: stop the scroll is not an observable check; verify source fidelity and standalone meaning. Meaning/voice pass: retain confident concise guidance. Essential limits revise: require verified source wording, attribution and links in the AI prompt, without audit narration.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; representative light desktop and all five dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261020/, per-path default/slate 1440/390 PNG and JSON. Representative light desktop and all five dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261020-twitter-one-liner",
  "status": "needs_revision",
  "assessed_at": "2026-10-20T16:47:35Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "fbe568577a56f4220ab0f9dad3495422d5b005ccb696bfa58e8f2a5fb25a5d62",
  "report_ref": "docs-internal/quality-reviews/2026-10-20/twitter-one-liner.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening clearly favors a short standalone lesson and redirects context-heavy ideas to a thread."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "No worked one-liner is supplied: Coming soon plus generic hook/body/CTA fields do not show meaningful compression or checking context against the source."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "The promised one-liner conflicts with the mandatory multi-part hook/body/CTA template and requirement that a first line earn a second. A usable short statement should be modeled directly."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The parent distinguishes a punchy takeaway from the longer LinkedIn lesson; the copied generic structure erases that useful distinction."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Official X counting documentation supports 280 weighted characters and 23 per URL for standard short posts. This is appropriate drafting scope, not proof that longer paid posts do not exist. No engagement guarantee is accepted."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; representative light desktop and all five dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Official X counting documentation supports 280 weighted characters and 23 per URL for standard short posts. This is appropriate drafting scope, not proof that longer paid posts do not exist. No engagement guarantee is accepted.",
    "items": [
      {
        "url": "https://docs.x.com/fundamentals/counting-characters",
        "claim": "The short post version uses a 280 character budget including its episode URL.",
        "finding": "Official X documentation supports 280 weighted characters and 23 per URL; emoji and Unicode may count differently. This is short-post scope, not all paid longer-post features.",
        "checked_at": "2026-10-20T16:46:25Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/key-takeaway/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent distinguishes a punchy takeaway from the longer LinkedIn lesson; the copied generic structure erases that useful distinction.",
        "checked_at": "2026-10-20T16:47:35Z"
      },
      {
        "path": "patterns/package/social-posts/types/key-takeaway/linkedin-insight.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent distinguishes a punchy takeaway from the longer LinkedIn lesson; the copied generic structure erases that useful distinction.",
        "checked_at": "2026-10-20T16:47:35Z"
      },
      {
        "path": "framework.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "Framework Package asks whether an asset can be understood and used without extra explanation. A hub can route readers concisely; a leaf needs enough concrete input and examples to execute its promise.",
        "checked_at": "2026-10-20T16:47:35Z"
      }
    ]
  },
  "next_review_at": "2026-11-19T16:47:35Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Await exact owner-approved shared contrast correction and complete concrete pattern guidance correction on existing package card.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
~~~
