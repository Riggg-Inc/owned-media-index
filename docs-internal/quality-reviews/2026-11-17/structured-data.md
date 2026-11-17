# structured-data whole-page quality assessment

AI editorial review. Complete current body, JSON snippets and prompt read; relevant primary vocabulary properties inspected and direct guest URL returned404. No full Schema.org validation service or Google Rich Results interactive test claimed. Captured desktop1440/mobile390 light/slate; inspected mobile slate. No horizontal document overflow.

Practitioner checks: Purpose PASS (describe episode metadata); First action PASS (customize example); Example REVISE (unsupported guest property in copy-ready code); Quality Bar REVISE (vocabulary validator separate from Google feature test, scoped types); Meaning/voice PASS for minimal correction intent (preserve useful schema examples and no-guarantee introduction); Essential limits PASS in opening/placeholder note, but implementation contradictions require repair. Same existing shared hub/contrast card. Findings PREPARATION until full reconciled proposed files, immutable hash/diff and independent review; exact human approval required for bodies. Park, no public quality date.

## Exact assessment record

{
  "id": "quality-20261117-structured-data",
  "status": "needs_revision",
  "assessed_at": "2026-11-17T17:00:49Z",
  "reviewer": "Cass Reelman — openai/gpt-6-astra (AI editorial review)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "4b28e27d3cdb8c80c681654964c35ec76f416916d41a724ed469cdbe16d9a1ae",
  "report_ref": "docs-internal/quality-reviews/2026-11-17/structured-data.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "Explains episode identity and offers JSON-LD examples and a prompt, giving site implementers a concrete starting point."
    },
    "substance": {
      "status": "pass",
      "rationale": "PodcastEpisode, FAQPage and VideoObject examples contain useful fields, media URL distinctions and placeholder warnings; correction should retain these substantive examples."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "The introduction says use applicable types and no universal AI requirement, while Required Schema Types and every episode must have PodcastEpisode imply a universal prescription. Quality Bar validation only via Google Rich Results Test conflicts with the prose instruction to validate vocabulary separately."
    },
    "cross_page_consistency": {
      "status": "needs_revision",
      "rationale": "Measurement correctly separates valid markup from citation evidence and framework covers webinars as well as podcasts. Every episode PodcastEpisode framing needs scope to podcast episodes and a real vocabulary validation path."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "PodcastEpisode primary property listing inspected includes author, associatedMedia, episodeNumber and partOfSeries, but not guest; schema.org/guest returns404. The copy-ready example and Quality Bar require this unsupported property. Universal AI recency and no-benefit-from-omission claims are not justified by the checked Google documentation."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Long JSON examples are structured and document overflow is false, but slate mobile renders show poor contrast in syntax and especially the dark red prompt on navy. Shared dark-link contrast also affects the validation destination."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Vocabulary and Google policy sources checked for copy-ready implementation correctness, without claiming full rich-result testing.",
    "items": [
      {
        "url": "https://schema.org/PodcastEpisode",
        "claim": "The example guest property is supported PodcastEpisode vocabulary.",
        "finding": "Relevant Episode and CreativeWork property listings inspected: episodeNumber, partOfSeries, associatedMedia, author and contributor are documented; guest was absent. Full unrelated inherited property corpus not audited.",
        "checked_at": "2026-11-17T16:53:41Z"
      },
      {
        "url": "https://schema.org/guest",
        "claim": "The required guest field resolves to a defined Schema.org property.",
        "finding": "Direct primary vocabulary URL returned404, reinforcing the missing-property problem rather than validating the copy-ready example.",
        "checked_at": "2026-11-17T16:54:42Z"
      },
      {
        "url": "https://developers.google.com/search/docs/appearance/structured-data/sd-policies",
        "claim": "Valid syntax alone guarantees correctness or search display.",
        "finding": "Complete guidelines distinguish content quality from technical testing, require visible accurate content and explicitly deny guaranteed display even after Rich Results Test.",
        "checked_at": "2026-11-17T16:54:59Z"
      },
      {
        "url": "https://developers.google.com/search/docs/appearance/ai-features",
        "claim": "All AI discovery requires a specific schema or extra markup.",
        "finding": "Google explicitly requires no special schema; advice must be scoped to applicable episode metadata rather than universal AI eligibility.",
        "checked_at": "2026-11-17T16:51:23Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Framework and Measurement compared for content scope and validation meaning.",
    "items": [
      {
        "path": "framework.md",
        "claim": "Owned media includes more formats than podcast episodes.",
        "finding": "Framework includes webinars, live production and reusable media; PodcastEpisode should not be presented as mandatory for every format.",
        "checked_at": "2026-11-17T17:00:49Z"
      },
      {
        "path": "patterns/publish/ai-search-optimization/measurement.md",
        "claim": "Markup validation is not evidence of successful AI citation.",
        "finding": "Measurement explicitly distinguishes technical checks from attribution and observed citations, agreeing with this page introduction but not categorical prescriptions.",
        "checked_at": "2026-11-17T17:00:49Z"
      }
    ]
  },
  "next_review_at": "2026-12-17T17:00:49Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Unsupported guest schema property and contradictory universal validation requirements need exact correction; dark examples remain difficult to read.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
