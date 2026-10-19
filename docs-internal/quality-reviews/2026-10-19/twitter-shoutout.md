# twitter-shoutout — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose PASS: The introduction asks for specific appreciation, appropriate tagging and a reason to follow the conversation, giving a recognizable short-post task. First action PASS: introduction identifies the specific moment/lesson to select. Example REVISE: Coming soon supplies no usable model. Quality Bar REVISE: generic stop-the-scroll advice lacks the specific observable checks identified in substance. Meaning/voice PASS: keep useful confident introduction and narrow purpose. Essential limits PASS: do not invent guest words, current relevance or reach results; a proposed example must be clearly fictional.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261019/, per-path default/slate 1440/390 PNG and JSON. Light desktop and dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261019-twitter-shoutout",
  "status": "needs_revision",
  "assessed_at": "2026-10-19T16:48:07Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "7f55e29eeeaf583f0e99dba44f8f5e1071d4a7c963de191418db2be5fe3c09f5",
  "report_ref": "docs-internal/quality-reviews/2026-10-19/twitter-shoutout.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The introduction asks for specific appreciation, appropriate tagging and a reason to follow the conversation, giving a recognizable short-post task."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "Coming soon is not a worked shoutout. Generic guest name and insight fields omit verified handle and the exact contribution to acknowledge; a concise illustrative post is needed."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Recognition and directing readers to the conversation are consistent; short format and single CTA remain sensible constraints."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "LinkedIn Gratitude similarly prioritizes the guest contribution rather than a tag. The hub automatic reach wording should be corrected at its source."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Official X documentation supports 280 weighted characters for the short post and 23 per URL, with new mentions counted. No reach increase follows merely from tagging."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Official X documentation supports 280 weighted characters for the short post and 23 per URL, with new mentions counted. No reach increase follows merely from tagging.",
    "items": [
      {
        "url": "https://docs.x.com/fundamentals/counting-characters",
        "claim": "The short post version uses a 280 character budget including its episode URL.",
        "finding": "Official X documentation supports 280 weighted characters and 23 per URL; emoji and Unicode may count differently. This is short-post scope, not all paid longer-post features.",
        "checked_at": "2026-10-19T16:46:25Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/guest-tag/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "LinkedIn Gratitude similarly prioritizes the guest contribution rather than a tag. The hub automatic reach wording should be corrected at its source.",
        "checked_at": "2026-10-19T16:48:07Z"
      },
      {
        "path": "patterns/package/social-posts/types/guest-tag/linkedin-gratitude.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "LinkedIn Gratitude similarly prioritizes the guest contribution rather than a tag. The hub automatic reach wording should be corrected at its source.",
        "checked_at": "2026-10-19T16:48:07Z"
      },
      {
        "path": "framework.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "Framework Package asks whether an asset can be understood and used without extra explanation. A hub can route readers concisely; a leaf needs enough concrete input and examples to execute its promise.",
        "checked_at": "2026-10-19T16:48:07Z"
      }
    ]
  },
  "next_review_at": "2026-11-18T16:48:07Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Await exact owner-approved shared contrast correction and complete concrete pattern guidance correction on existing package card.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
~~~
