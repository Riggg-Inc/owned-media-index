# linkedin-quote-post — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose pass: the opening identifies the post and use case. First action revise: the generic hook/body template omits source selection and audience application. Example revise: Coming soon is not an example. Quality Bar revise: stop the scroll is not an observable check; verify source fidelity and standalone meaning. Meaning/voice pass: retain confident concise guidance. Essential limits revise: require verified source wording, attribution and links in the AI prompt, without audit narration.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; representative light desktop and all five dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261020/, per-path default/slate 1440/390 PNG and JSON. Representative light desktop and all five dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261020-linkedin-quote-post",
  "status": "needs_revision",
  "assessed_at": "2026-10-20T16:47:35Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "cfad3ebd8bd83b5a44243948ce228476782cfc18c98566152083f27f9347b227",
  "report_ref": "docs-internal/quality-reviews/2026-10-20/linkedin-quote-post.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening explains sharing an attributed quotation with a relevant professional interpretation rather than repeating the quote."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "Neither the template nor Coming soon demonstrates an attributed quotation followed by interpretation. The AI input accepts an insight or quote interchangeably and supplies no source excerpt for verification."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Quote, context and singular action form a sensible post; the generic hook/body scaffold is incomplete rather than an inherent logical contradiction."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "Twitter Quote Card explicitly requires clear attribution; this page promises attribution but its operational prompt does not require exact wording or speaker/source verification."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "The editorial length target is appropriately qualified. However the AI quotation workflow can turn a paraphrased insight into attributed speech without an exact-quote/source check; this is a material accuracy risk, not a demand for experimental proof of advice."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; representative light desktop and all five dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "The editorial length target is appropriately qualified. However the AI quotation workflow can turn a paraphrased insight into attributed speech without an exact-quote/source check; this is a material accuracy risk, not a demand for experimental proof of advice. No external factual-source reading is claimed for this advice-only scope; internal scores are preserved, not rescored or empirically certified.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/quote-share/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "Twitter Quote Card explicitly requires clear attribution; this page promises attribution but its operational prompt does not require exact wording or speaker/source verification.",
        "checked_at": "2026-10-20T16:47:35Z"
      },
      {
        "path": "patterns/package/social-posts/types/quote-share/twitter-quote-card.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "Twitter Quote Card explicitly requires clear attribution; this page promises attribution but its operational prompt does not require exact wording or speaker/source verification.",
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
