# linkedin-insight — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose pass: the opening identifies the post and use case. First action revise: the generic hook/body template omits source selection and audience application. Example revise: Coming soon is not an example. Quality Bar revise: stop the scroll is not an observable check; verify source fidelity and standalone meaning. Meaning/voice pass: retain confident concise guidance. Essential limits revise: require verified source wording, attribution and links in the AI prompt, without audit narration.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; representative light desktop and all five dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261020/, per-path default/slate 1440/390 PNG and JSON. Representative light desktop and all five dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261020-linkedin-insight",
  "status": "needs_revision",
  "assessed_at": "2026-10-20T16:47:35Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "ffc1f8b195c261d91c37c95db2739f2598cb70dc55de99c217a60161a64f9ee2",
  "report_ref": "docs-internal/quality-reviews/2026-10-20/linkedin-insight.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening usefully tells professionals to develop one episode insight instead of summarizing every topic."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The repeated hook/body/CTA skeleton and Coming soon example never demonstrate turning an actual lesson into a professional action. The prompt lacks supporting source context and a specific reader application."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Choosing one idea, adding context and inviting one action is logically sound; repeated introductory sentences are minor."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The parent promises actionable standalone value; this page preserves that intent but generic instructions do not fully operationalize it. Quote Share correctly differs by foregrounding an attributed quotation."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Advice is framed as practitioner observation, not measured lift. The 1300-character LinkedIn target explicitly disclaims a platform limit or optimum. Existing editorial scores are not empirical certification and are not changed."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; representative light desktop and all five dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "Advice is framed as practitioner observation, not measured lift. The 1300-character LinkedIn target explicitly disclaims a platform limit or optimum. Existing editorial scores are not empirical certification and are not changed. No external factual-source reading is claimed for this advice-only scope; internal scores are preserved, not rescored or empirically certified.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/key-takeaway/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent promises actionable standalone value; this page preserves that intent but generic instructions do not fully operationalize it. Quote Share correctly differs by foregrounding an attributed quotation.",
        "checked_at": "2026-10-20T16:47:35Z"
      },
      {
        "path": "patterns/package/social-posts/types/quote-share/linkedin-quote-post.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent promises actionable standalone value; this page preserves that intent but generic instructions do not fully operationalize it. Quote Share correctly differs by foregrounding an attributed quotation.",
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
