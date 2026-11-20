# feed-metadata-standard whole-page quality assessment

AI editorial review by Cass Reelman, openai/gpt-6-astra. Entire published Markdown and complete rendered article read. Full parent Publish and Canonical Episode Page compared. Apple primary documentation read live at its recorded time. No private data or human signoff.

Practitioner gate: Purpose PASS (episode checklist for app clarity); First action PASS (fill episode title/description); Example REVISE (none demonstrates usable metadata); Quality Bar REVISE (understandability alone cannot check a well-formed feed, no GUID/enclosure/validation checks); Meaning/voice PASS (confident bounded advice should be retained, no rewrite published); Essential limits PASS (no performance guarantee or private example). Material gaps map to substance/consistency/usability. Score 5 remains unchanged; this review does not rescore.

Fresh live Chromium captures at 1440/390 widths, light/dark, no overflow. Desktop-light and mobile-dark screenshots visually inspected. Dark breadcrumb/footer links remain hard to read; no table defect invented. Public label pending and September 30 revision date observed. Source checks do not establish all platform requirements.

Outcome NEEDS_REVISION. Same shared correction card; full proposal preparation must preserve useful fields, supply a hypothetical example and distinguish editorial checks from host-generated technical checks. No permission to publish body edits.

## Exact assessment record

{
  "id": "quality-20261120-feed-metadata-standard",
  "status": "needs_revision",
  "assessed_at": "2026-11-20T16:47:14Z",
  "reviewer": "Cass Reelman — openai/gpt-6-astra (AI editorial review)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "b1d9380b79e52e4153cb7cb8a0b623877225e7b1919175906b902d5b619be986",
  "report_ref": "docs-internal/quality-reviews/2026-11-20/feed-metadata-standard.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The episode-field checklist gives producers a recognizable pre-publication task and keeps the canonical website link in scope."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "A feed standard promising distribution quality offers only field names: no worked metadata example, stable GUID or enclosure checks, or actual validation step. This is materially short of the parent hub promise of a complete well-formed feed."
    },
    "coherence": {
      "status": "pass",
      "rationale": "The opening, field list and app-understandability quality bar consistently address episode metadata rather than an unrelated publishing workflow. Repeated introductory wording is minor."
    },
    "cross_page_consistency": {
      "status": "needs_revision",
      "rationale": "The Publish hub promises a complete well-formed RSS feed, but this page is only an editorial episode checklist and omits technical identity and enclosure requirements. Canonical Episode Page linkage is otherwise compatible."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Discoverability support is bounded rather than guaranteed. Required Fields is reasonably an editorial standard, not an explicit exhaustive Apple specification; the material completeness gap is recorded under substance and cross-page consistency, not a fabricated false statistic."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh desktop and mobile light/dark renders have no horizontal overflow, but dark-mode breadcrumb and footer links are very low contrast against the navy background. The sparse quality bar also lacks an example or feed-validation action."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Official Apple RSS requirements were read to assess technical completeness of the advertised feed standard, not to demand experiments for editorial advice.",
    "items": [
      {
        "url": "https://podcasters.apple.com/support/823-podcast-requirements",
        "claim": "The page presents a feed metadata standard supporting distribution quality.",
        "finding": "Apple requires permanent episode GUIDs and unique enclosures with URL, length and type, plus feed validation requirements. The page omits these actionable checks; its general editorial field advice remains useful.",
        "checked_at": "2026-11-20T16:46:42Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read the full parent publishing hub and canonical episode companion to compare the actual promise and website relationship.",
    "items": [
      {
        "path": "patterns/publish/index.md",
        "claim": "The parent describes this destination as a complete well-formed RSS feed standard.",
        "finding": "The target lacks technical identity, enclosure and validation guidance necessary to fulfill that broader promise.",
        "checked_at": "2026-11-20T16:47:14Z"
      },
      {
        "path": "patterns/publish/canonical-episode-page.md",
        "claim": "The canonical website home complements rather than duplicates the RSS description.",
        "finding": "The target retains a website link and makes episode metadata understandable in-app, compatible with the companion standalone website utility.",
        "checked_at": "2026-11-20T16:47:14Z"
      }
    ]
  },
  "next_review_at": "2026-12-20T16:47:14Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Complete the feed-standard example and technical validation guidance under exact owner approval; shared dark-link contrast remains on the existing owning correction card.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
