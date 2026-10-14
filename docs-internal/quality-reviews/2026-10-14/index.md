# index — substantive post-release quality assessment

AI editorial review of complete hub, all five linked leaf bodies, current1440/390 light/dark presentation. Dark desktop and light mobile screenshots inspected: pale striped table cells with pale text hide best-for/spec guidance. No page overflow; wide spec table scrolls within mobile viewport. Practitioner gate: Purpose PASS—choose among five graphics formats. First action PASS—best-for links route to individual patterns. Example PASS—table maps expert insight/data/dialogue/series/audio to concrete formats. Quality Bar REVISE—point sizes at1080width do not assure mobile readability; use actual output preview, as W3C explains image-editor point-size variability. Meaning/voice PASS for retained design advice; only unsupported performance and universal platform claims need narrowing. Essential limits REVISE—May2026 snapshot caveat is honest but not a cure for current-looking unscoped limits and works-everywhere guarantee. W3C normal endpoint and X returned403; W3C first-party source retrieved through official GitHub repository, not access-control circumvention. Pinterest ad-spec scope explicitly distinguished from organic creation guidance. No complete certification of Instagram/LinkedIn/Facebook/X specifications asserted. Preserve original snapshot date and historical records; proposed current practical guidance must not silently redatestamp legacy values.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261014-index",
  "status": "needs_revision",
  "assessed_at": "2026-10-14T16:51:37Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "0e56543f9ec80dce7dacafb202b61969268a6964cf5758bcce9d134f547d3c3c",
  "report_ref": "docs-internal/quality-reviews/2026-10-14/index.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Five-style best-for comparison and direct leaf links make this a useful selection hub for producers repackaging expert conversations."
    },
    "substance": {
      "status": "pass",
      "rationale": "The format comparison, attribution/length requirements, platform table and legibility checks contain concrete operational detail rather than fluff; retain useful examples while fixing specifics."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "Opening defines all quote graphics as static assets while listing audio-bearing Audiogram Card. A square default claimed to work everywhere also conflicts with recommended vertical story and Pinterest formats."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "Scores and best-for labels match the five linked leaves, and stand-alone attribution guidance fits their quality bars. Audio-definition inconsistency is localized to this hub rather than an excuse to rewrite useful siblings."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "Highest-performing has no comparative evidence and platform-agnostic/works everywhere overstates portability. Pinterest official specs distinguish desktop20MB and app32MB for standard ads, so a universal20MB row lacks scope. W3C supports contrast targets but warns image-editor point sizes do not ensure rendered size."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh supported dark-mode render hides text in alternating pale table rows, including format selection and specifications. Mobile contained scrolling avoids page overflow but does not resolve contrast or too-small typography guidance."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Checked proportionate primary references for material contrast and Pinterest size claims; inaccessible X and unverified platform rows remain explicit limitations, not certified source checks.",
    "items": [
      {
        "url": "https://help.pinterest.com/en/business/article/pinterest-product-specs",
        "claim": "Pinterest standard image file size and recommended aspect ratio are correctly scoped.",
        "finding": "Official ad guide recommends2:3/1000x1500 and says desktop20MB versus in-app32MB for standard image ads; this is ad-format guidance, not a universal organic-Pin limit. The hub leaves those distinctions unstated.",
        "checked_at": "2026-10-14T16:49:33Z"
      },
      {
        "url": "https://help.pinterest.com/en/article/create-a-pin-from-an-image-or-video",
        "claim": "Organic publishing workflow is distinct from ad format specifications.",
        "finding": "Official creation instructions describe separate image/video upload and aspect-ratio editing, but do not establish the hub universal20MB claim. No organic size limit inferred from absence.",
        "checked_at": "2026-10-14T16:50:49Z"
      },
      {
        "url": "https://raw.githubusercontent.com/w3c/wcag/main/understanding/20/contrast-minimum.html",
        "claim": "Contrast and image text sizing guidance must reflect actual rendered readability.",
        "finding": "Official W3C source discusses4.5:1 normal and3:1 large-text thresholds, images of text and unreliable point-size settings across image-editing resolutions. Supports contrast advice, not a guarantee from18\u201324pt at1080pixels.",
        "checked_at": "2026-10-14T16:50:49Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete related published pages and compared their actual operating guidance.",
    "items": [
      {
        "path": "patterns/package/quote-graphics/audiogram-card.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Audiogram uses actual voice paired with a graphic, so the directory static-only definition is incomplete.",
        "checked_at": "2026-10-14T16:51:37Z"
      },
      {
        "path": "patterns/package/quote-graphics/branded-pull-quote.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Series-consistency use case and score4 match; leaf makes no highest-performing empirical assertion.",
        "checked_at": "2026-10-14T16:51:37Z"
      },
      {
        "path": "patterns/package/quote-graphics/conversation-exchange.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Dialogue selection and score4 match; brief stand-alone exchange guidance remains useful.",
        "checked_at": "2026-10-14T16:51:37Z"
      },
      {
        "path": "patterns/package/quote-graphics/speaker-quote.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Portrait-plus-quote description and score5 match directory; no score redesign authorized by this assessment.",
        "checked_at": "2026-10-14T16:51:37Z"
      },
      {
        "path": "patterns/package/quote-graphics/stat-callout.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Credible number with context/source attribution supports data-point use case; do not strip that meaningful source requirement.",
        "checked_at": "2026-10-14T16:51:37Z"
      }
    ]
  },
  "next_review_at": "2026-11-13T16:51:37Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Unsupported highest-performing/universal-format assertions, insufficiently scoped platform limits and static-only definition need targeted correction; shared dark-mode stripes hide comparison cells.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
