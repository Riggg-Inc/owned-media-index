# linkedin-process-post — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose pass: a production lesson for professionals. First action revise: identify one decision and the constraint that drove it. Example revise: Coming soon fails to demonstrate an actual process lesson. Quality Bar revise: require a decision, reason and reusable lesson. Meaning/voice preserve: do not turn practical advice into a caveat-heavy audit. Essential limits revise: use only approved production details and no confidential screens.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261017/, per-path default/slate 1440/390 PNG and JSON. Light desktop and dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261017-linkedin-process-post",
  "status": "needs_revision",
  "assessed_at": "2026-10-17T16:49:20Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "138f2c46982eb8c1a28beda54b0f6f666fd3b0a231e24b666f5bf3486c148d83",
  "report_ref": "docs-internal/quality-reviews/2026-10-17/linkedin-process-post.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The professional-audience opening gives a useful reason to share a production decision rather than a recording announcement."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The page repeats its opening, offers a generic hook/body/CTA skeleton and explicitly has no worked example. Its prompt asks for guest and quote but not the actual decision, alternatives or observable lesson, so it does not yet teach the promised process breakdown."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The purpose and platform remain internally consistent; the 1300-character instruction is clearly an editorial target, not a hard technical constraint."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The parent correctly distinguishes a LinkedIn workflow breakdown from Instagram production snaps. The current leaf agrees in its opening but needs process-specific inputs to deliver that distinction; Framework Package asks for usable assets without extra explanation."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "No measured production benefit or performance guarantee is claimed. The length target explicitly disclaims a limit or proven optimum. Generic hook advice can remain confident practitioner guidance; the gap is execution detail rather than missing experiments."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "No measured production benefit or performance guarantee is claimed. The length target explicitly disclaims a limit or proven optimum. Generic hook advice can remain confident practitioner guidance; the gap is execution detail rather than missing experiments. No external factual-source reading is claimed for this advice-only scope; internal scores are preserved, not rescored or empirically certified.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/behind-the-scenes/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The parent correctly distinguishes a LinkedIn workflow breakdown from Instagram production snaps. The current leaf agrees in its opening but needs process-specific inputs to deliver that distinction; Framework Package asks for usable assets without extra explanation.",
        "checked_at": "2026-10-17T16:49:20Z"
      },
      {
        "path": "framework.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "Framework Package asks whether an asset can be understood and used without extra explanation. A hub can route readers concisely; a leaf needs enough concrete input and examples to execute its promise.",
        "checked_at": "2026-10-17T16:49:20Z"
      }
    ]
  },
  "next_review_at": "2026-11-16T16:49:20Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Await exact owner-approved shared contrast correction and complete concrete pattern guidance correction on existing package card.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
~~~
