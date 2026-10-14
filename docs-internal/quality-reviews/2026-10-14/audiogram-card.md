# audiogram-card — substantive post-release quality assessment

AI editorial review of complete published body, source template and current desktop/mobile light/dark render. Screenshots audiogram-card-slate-1440 and default-390 inspected; code foreground is dark red on dark in supported slate mode. No overflow; code scrolls horizontally on narrow screen. Practitioner task checks: Purpose PASS (voice must add value); First action REVISE (prompt requests text and speakers but never the source audio); Example REVISE (no worked audio selection or equivalent input/output demonstration); Quality Bar REVISE (all five bullets concern a graphic, none a playable audio asset); Meaning/voice PASS (retain short confident production guidance); Essential limits PASS in principle (poor audio/text-only alternative), but source excerpt matching and approved publication are necessary beside the audio action. Thirty words and aspect ratios are house defaults, not platform limits. No performance benchmark or named empirical claim needs external research. Related hub's static definition is imprecise for an audio-bearing derivative; do not weaken the leaf to match it. Scores untouched.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261014-audiogram-card",
  "status": "needs_revision",
  "assessed_at": "2026-10-14T16:49:17Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "e9da3fdfb491d59dff6cb369ffa74ec726dc484df16ff485610230afdc754423",
  "report_ref": "docs-internal/quality-reviews/2026-10-14/audiogram-card.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Opening clearly tells producers to select this format when recorded voice adds value and avoid it when a static quote is stronger."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "The copyable prompt only requests quote text, speaker and brand; it lacks actual source-audio input, excerpt boundaries, captions or an audio/video output example for the promised asset."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "Definition promises actual speaker voice paired with graphics but the production instructions can yield only a static graphic; this is a material mismatch between promise and process."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The related directory lists Audiogram as audio snippets with visual context, supporting the leaf definition; its generic static-assets introduction needs separate hub clarification, not removal of audio from this pattern."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Advice is openly practitioner observation and selection guidance. Word counts and aspect ratios are editorial constraints; no invented performance evidence is needed to justify them."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh rendered slate-mode prompt uses dark red text on a dark panel, reducing the readability of the primary reusable instruction. Mobile layout does not overflow but requires horizontal code scrolling."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "No material named platform limit, statistic or empirical outcome claim is made in this leaf; production guidance assessed directly rather than inventing external proof.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete related published pages and compared their actual operating guidance.",
    "items": [
      {
        "path": "patterns/package/quote-graphics/index.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Directory best-for explicitly says audio snippets with visual context, while its broad static-assets opening does not encompass audiograms correctly.",
        "checked_at": "2026-10-14T16:49:17Z"
      },
      {
        "path": "patterns/package/quote-graphics/speaker-quote.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Static speaker quote prompt appropriately asks for a headshot and exact text; copying that generic graphic structure is insufficient for an audio-bearing deliverable.",
        "checked_at": "2026-10-14T16:49:17Z"
      },
      {
        "path": "framework.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Package stage requires usable assets; a finished audiogram needs actual voice playback, not only a visual card.",
        "checked_at": "2026-10-14T16:49:17Z"
      }
    ]
  },
  "next_review_at": "2027-01-12T16:49:17Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "The audio-led pattern supplies only a generic static quote-graphic prompt; audio source, excerpt alignment and playable export checks are missing. Shared dark-mode prompt contrast also blocks usability.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
