# branded-template — substantive quality review

AI editorial review, not human signoff. Complete current published Markdown and live article structure read. Scores preserved.

## Reader checks

Purpose PASS: recognizable series art with episode differentiation. First action PASS: choose fixed layout/colors/fonts and episode-specific visual. Example PASS at basic task level: prompt inputs define concrete text, topic, visual and colors; an optional visual example alone would not fail. Quality Bar PASS: shrink-preview legibility, contrast and short text are observable. Meaning/voice: preserve confident template advice. Essential limits REVISE: do not diagnose CTR decline as template fatigue; clarify ordinary video versus square show-art scope.

## Rendered presentation

The central Template or Prompt Template uses dark red text against a dark background in slate mode, making executable instructions hard to read. Fresh live 1440/390 light/dark captures have no document overflow; all five dark mobile images and representative light desktop were visually inspected. Shared CSS correction remains unapproved.

Fresh evidence: output/reports/omi-quality-20261021/ per-path 1440/390 light/dark PNG and JSON. Shared CSS owner: 8006e12e-6551-440a-b9cc-27bce652996f. No playback or comprehensive accessibility certification. Body correction: e050b6be-b3e8-4872-83c4-a6e8fee980f8. Proposed fixes cannot earn a pass on unchanged public bodies.

## Six findings and provenance

~~~json
{
  "id": "quality-20261021-branded-template",
  "status": "needs_revision",
  "assessed_at": "2026-10-21T16:48:35Z",
  "reviewer": "Cass Reelman (AI editorial review; openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "15f8d41d59f6f55522affb816a1ee51745ca654edc62136f97e704f652ff00fe",
  "report_ref": "docs-internal/quality-reviews/2026-10-21/branded-template.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening makes a clear tradeoff: use repeatable brand layout for recognition while keeping episode-specific detail so releases remain distinguishable."
    },
    "substance": {
      "status": "pass",
      "rationale": "Concrete constraints\u2014short overlay, contrast, brand colors and a fill-in design prompt\u2014are enough to start a usable template; a visual example would help but its absence alone is not a material failure."
    },
    "coherence": {
      "status": "pass",
      "rationale": "What It Is prioritizes recognition while the introduction warns against interchangeable episodes; these are compatible design goals rather than a contradiction."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The Thumbnails hub places this style under series consistency and show recognition, matching the leaf. Framework Package requires an understandable asset. Hub legacy specifications are explicitly historical and not freshly certified by this review."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "YouTube documentation supports 16:9 for ordinary video thumbnails and Apple supports square show art; neither proves a universal causal template-fatigue CTR decline. The When Not To Use sentence attributes a drop to fatigue without evidence. Reframe as an observable indistinguishability check, not a measured diagnosis. 120-pixel and 5\u20137-word checks are editorial heuristics here."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "The central Template or Prompt Template uses dark red text against a dark background in slate mode, making executable instructions hard to read. Fresh live 1440/390 light/dark captures have no document overflow; all five dark mobile images and representative light desktop were visually inspected. Shared CSS correction remains unapproved."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "YouTube documentation supports 16:9 for ordinary video thumbnails and Apple supports square show art; neither proves a universal causal template-fatigue CTR decline. The When Not To Use sentence attributes a drop to fatigue without evidence. Reframe as an observable indistinguishability check, not a measured diagnosis. 120-pixel and 5\u20137-word checks are editorial heuristics here. No additional source verification or human testing is claimed.",
    "items": [
      {
        "url": "https://support.google.com/youtube/answer/72431?hl=en",
        "claim": "The template recommends 16:9 for ordinary YouTube video thumbnails.",
        "finding": "Retrieved best-practices section explicitly recommends 16:9 for videos, 9:16 for Shorts and 1:1 for podcast playlists. Fetch warned incomplete overall response; relevant section was readable. No causal template-fatigue finding is supplied.",
        "checked_at": "2026-10-21T16:46:50Z"
      },
      {
        "url": "https://podcasters.apple.com/support/5514-show-cover-template",
        "claim": "Square artwork is appropriate for podcast show covers.",
        "finding": "Apple describes square show art at 3000 by 3000 with legible recognizable title and high contrast. Scope is show cover, not every episode-art surface or app.",
        "checked_at": "2026-10-21T16:46:50Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Complete relevant parent and sibling guidance plus Framework were read against the actual practitioner task.",
    "items": [
      {
        "path": "patterns/package/thumbnails/index.md",
        "claim": "Published guidance should support a coherent usable packaging task.",
        "finding": "The Thumbnails hub places this style under series consistency and show recognition, matching the leaf. Framework Package requires an understandable asset. Hub legacy specifications are explicitly historical and not freshly certified by this review.",
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
