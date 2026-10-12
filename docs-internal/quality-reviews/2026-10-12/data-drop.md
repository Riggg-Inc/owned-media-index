# data-drop — substantive post-release quality assessment

Full current published body read against origin/main f4ffead. Public light/dark screenshots retained in output/reports/omi-quality-20261012/data-drop*.png. No episode playback, private evidence, benchmark validation or human signoff claimed. Scores/framework unchanged. Existing Data Drop correction reused; shared CSS proposal remains on original quadrant card. This is a completed needs_revision assessment, not a pass.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261012-data-drop",
  "status": "needs_revision",
  "assessed_at": "2026-10-12T16:48:50Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "e67e1ac9a3b6003a01bf25e6f3a0eeca6609918ea901582ecb5346c9f7875f54",
  "report_ref": "docs-internal/quality-reviews/2026-10-12/data-drop.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Specific selection criteria help an editor choose a contextualized statistic rather than a decontextualized number; the exclusion cases directly support this task."
    },
    "substance": {
      "status": "pass",
      "rationale": "Four selection tests, three research starting points and a customizable extraction prompt supply concrete operating guidance without requiring additional filler."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Definition, criteria, exclusions and extraction prompt consistently focus on one contextualized number. Repeated opening definition is minor, not a material defect."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The corrected clip quadrant requires source, scope and context and selects by audience fit; Data Drop selection criteria agree with that operating advice."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "The statement that data clips perform well asserts an empirical outcome without supporting data. The prompt requests timestamps from potentially untimed text and a credible recent source without requiring verification or unavailable-data handling."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Live light and dark desktop/mobile renders were inspected at 1440 and 390. Navigation and page width work, but pale text disappears on pale striped source-table rows in dark mode; prompt and links also have weak contrast."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Publisher descriptions read for named show context; neither establishes the causal performance claim. Prof G alternate URL returned 404 and is not verified evidence.",
    "items": [
      {
        "url": "https://freakonomics.com/",
        "claim": "Freakonomics is a reasonable starting point for data-led material.",
        "finding": "The publisher presents quantified economic questions and a Radio network; this supports research relevance, not verified clip performance or an episode-level extraction.",
        "checked_at": "2026-10-12T16:47:40Z"
      },
      {
        "url": "https://a16z.com/podcasts/",
        "claim": "The a16z show is a technology and market research starting point.",
        "finding": "Publisher describes technology ideas and builders across AI, energy and genomics. No measurement of Data Drop clip performance is provided.",
        "checked_at": "2026-10-12T16:47:41Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete related published pages and compared their actual operating guidance.",
    "items": [
      {
        "path": "quadrants/clips.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "The corrected guide treats audience appeal as a planning hypothesis and requires source and context, compatible with the target selection criteria.",
        "checked_at": "2026-10-12T16:48:50Z"
      },
      {
        "path": "patterns/package/clips/index.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "The hub treats duration as an editorial starting point and retention as something to test; target 30\u201360 seconds can be guidance, not a platform restriction.",
        "checked_at": "2026-10-12T16:48:50Z"
      }
    ]
  },
  "next_review_at": "2026-11-11T16:48:50Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Qualify unsupported clip performance causality and prevent invented source/timestamps; shared dark contrast correction requires exact approval.",
  "correction_card": "e911a436-cc49-48cf-90ec-3956ccca4d5e"
}
