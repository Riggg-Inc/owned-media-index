# instagram-reel-caption — substantive quality review

AI editorial review, not human signoff. Exact current published body assessed; no draft pass.

## Reader-task check

Purpose pass: contextual caption alongside a self-contained reel. First action revise: read the actual clip, then choose the missing context. Example revise: replace Coming soon with a labelled hypothetical caption. Quality Bar revise: inspect whether the first line names the clip-specific problem and CTA destination works. Meaning/voice preserve: keep concise confident advice. Essential limits revise: do not invent quotes or results absent from the supplied clip.

## Rendered acceptance

Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved.

Fresh evidence: output/reports/omi-quality-20261017/, per-path default/slate 1440/390 PNG and JSON. Light desktop and dark mobile captures visually inspected. No comprehensive accessibility certification. Full Markdown and live article plus relevant parents/siblings, Social Posts, Framework and Scoring read. Scores and evidence policy preserved, not rescored or empirically certified. Optional naming preferences do not cause failure.

## Six findings, provenance and next action

~~~json
{
  "id": "quality-20261017-instagram-reel-caption",
  "status": "needs_revision",
  "assessed_at": "2026-10-17T16:49:20Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "26652442756485305d8a14b1165f252949c66df76e17a8882671c96a97223e65",
  "report_ref": "docs-internal/quality-reviews/2026-10-17/instagram-reel-caption.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening usefully requires a self-contained reel and a caption that adds context rather than just an episode title."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The generic hook/body/CTA skeleton is a start but the Example is Coming soon, and the prompt lacks the actual clip transcript or visual takeaway. A reader cannot see what useful added context looks like instead of repetition."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The caption format, one next action and Instagram focus agree throughout. The length is labelled a drafting target and includes a current-app preview check, so it is not presented as a freshly verified technical maximum."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The Clip Companion hub and LinkedIn sibling both call for contextual copy alongside a clip. The reel leaf keeps this scope; the shared Framework Package task supports adding the missing clip-specific input and illustration."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "The page reports no engagement result, named exemplar or quotation. Its 2200-character drafting ceiling is editorial and current-app preview is explicitly recommended. No claim of comprehensive Instagram limit verification is made by this review."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Template and Prompt Template show dark red text on the dark background in supported slate mode, making the central instructions hard to read. Fresh live Chromium captures at 1440 and 390 pixels show no document overflow; light desktop and dark mobile images were visually inspected, not just measured. Existing shared contrast proposal remains unapproved."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "The page reports no engagement result, named exemplar or quotation. Its 2200-character drafting ceiling is editorial and current-app preview is explicitly recommended. No claim of comprehensive Instagram limit verification is made by this review. No external factual-source reading is claimed for this advice-only scope; internal scores are preserved, not rescored or empirically certified.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant published parent or sibling guidance and Framework were read for the actual reader task.",
    "items": [
      {
        "path": "patterns/package/social-posts/types/clip-companion/index.md",
        "claim": "The page should implement complementary and usable packaging guidance.",
        "finding": "The Clip Companion hub and LinkedIn sibling both call for contextual copy alongside a clip. The reel leaf keeps this scope; the shared Framework Package task supports adding the missing clip-specific input and illustration.",
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
