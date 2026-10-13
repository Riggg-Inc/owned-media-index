# problem — substantive post-release quality assessment

Full current public body and related pages read. Illustrative sample is not empirical evidence. No score redesign or private evidence access; new proposed wording requires exact human approval.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261013-problem",
  "status": "needs_revision",
  "assessed_at": "2026-10-13T16:48:20Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "ca1dd77e8800fc779eacba463b9ff68e3feff298997158a2e179135856a3c731",
  "report_ref": "docs-internal/quality-reviews/2026-10-13/problem.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Problem, credibility, learning promise and one next action provide a useful prescriptive interview writing structure."
    },
    "substance": {
      "status": "pass",
      "rationale": "Complete example, specific quality bar, exclusions and parameterized prompt enable practical application."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Four-part pattern is internally consistent, though example asks both subscribe and review despite singular CTA instruction."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "Contrasts appropriately with exploratory Big Question and concise Thesis formats while remaining within Package scope."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "Internal production data header lacks substantiating safe evidence in the article; no private evidence was consulted. First 120 characters is presented as platform truncation rather than a writing heuristic, and the named-show destination fails."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Desktop and mobile captures show material table stripe and code contrast defects obscuring named examples and the copyable prompt; Apple example link returned 404."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Checked published attribution access proportionately; fictional example explicitly labeled, so names and numbers are not treated as actual outcomes. Evidence header remains unsubstantiated, not declared false.",
    "items": [
      {
        "url": "https://podcasts.apple.com/us/podcast/marketing-against-the-grain/id1636010234",
        "claim": "Linked show supplies teardown starting evidence for this pattern.",
        "finding": "Published destination returned 404 during this review; no show or episode attribution was verified through this URL.",
        "checked_at": "2026-10-13T16:47:11Z"
      },
      {
        "url": "https://open.spotify.com/show/exit-five",
        "claim": "Exit Five link enables readers to inspect the attributed description pattern.",
        "finding": "Fetch returned only generic Spotify Web Player text, not identified show content; this is an access limitation rather than proof of attribution.",
        "checked_at": "2026-10-13T16:47:19Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete related published pages and compared their actual operating guidance.",
    "items": [
      {
        "path": "patterns/package/descriptions/thesis-takeaways-cta.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Problem-first sequence is more authority-focused than the concise thesis alternative.",
        "checked_at": "2026-10-13T16:48:20Z"
      },
      {
        "path": "patterns/package/descriptions/big-question-summary.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Exploratory alternative confirms the stated exclusion for nonprescriptive conversations.",
        "checked_at": "2026-10-13T16:48:20Z"
      },
      {
        "path": "framework.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Reusable description template fits the Package asset usability goal.",
        "checked_at": "2026-10-13T16:48:20Z"
      }
    ]
  },
  "next_review_at": "2026-11-12T16:48:20Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Repair show-reference and fixed-preview guidance, substantiate or seek approved evidence-label correction, and apply approved shared contrast fix.",
  "correction_card": "4e92936a-fd6d-4686-a204-f1e45b9fa801"
}
