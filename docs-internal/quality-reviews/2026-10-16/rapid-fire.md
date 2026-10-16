# rapid-fire — substantive quality assessment

AI editorial review, not human signoff. Full published source and fresh desktop/mobile light/dark rendered presentation assessed. Semantic/source child completed 2026-10-16T16:50:59Z; parent integrated actual render findings and completed at 2026-10-16T16:52:11Z. Parent read all five full target bodies, framework and both BTS routes, inspected ten representative screenshots from twenty captures. No score/framework/body edits or inferred approval.

## Practitioner reader checks

{
  "purpose": {
    "status": "pass",
    "finding": "Use three to five distinct quick insights; avoid nuanced five-second treatment."
  },
  "first_action": {
    "status": "pass",
    "finding": "Choose the distinct insights and target audience first."
  },
  "example": {
    "status": "revise",
    "finding": "No populated three-point example shows what qualifies as a quick insight."
  },
  "quality_bar": {
    "status": "revise",
    "finding": "Five points at eight seconds cannot meet the prompt\u2019s total; specify a feasible route."
  },
  "meaning_and_voice": {
    "status": "pass",
    "finding": "No revision applied. Keep the rapid pacing and density recommendation."
  },
  "essential_limits": {
    "status": "pass",
    "finding": "The nuanced-insight exclusion is the right essential limit; attention-clock metaphor need not become an audit paragraph."
  }
}

## Render evidence and scope

# Current live rendered review

AI editorial reviewer: Cass Reelman, openai/gpt-6-astra. Fresh October 16 desktop1440/mobile390 light/default and dark/slate captures produced by render.cjs; twenty browser snapshots, no document horizontal overflow. Ten representative screenshots visually inspected (both themes and both widths across each page). Complete source Markdown of all five targets read.

Quote Card Motion, Rapid Fire and Teaser Trailer: opening purpose, headings, Quality Bar and CTA template hierarchy are legible in light mode. Dark mode turns the essential red prompt text nearly invisible against the dark code panel. These are core working instructions, not decorative elements; usability needs_revision. Long prompt lines scroll inside code rather than overflowing the entire document; no whole-page overflow claim.

Social Posts: useful type navigation and full reference tables in light mode. In dark mode the alternating pale table rows retain near-white text, making purposes, platform values and mechanics unreadable. Material usability needs_revision. Mobile wide tables have their own horizontal content; this is not equivalent to proving every cell is immediately visible.

Behind The Scenes: intentionally short two-version navigation hub; not a complete standalone recipe. Light desktop table differentiates Instagram Story snaps from LinkedIn workflow breakdown. Dark mobile second row has nearly invisible platform and description text against pale row background, hiding the actual choice distinction. Material usability needs_revision; brevity alone is not the cause.

All five currently display Quality review pending, existing Last updated unchanged. Reuse shared contrast correction card8006e12e-6551-440a-b9cc-27bce652996f; no unapproved CSS edits, no duplicate card, no claim of repaired contrast. Semantic/source assessment is separate and will be integrated only after completion.


## Source limitations

[]

## Semantic required work and optional preferences

{
  "required": [
    {
      "id": "rapid-timing",
      "reason": "The three-slot template and total do not support all promised five-point combinations.",
      "replace": "- Each point gets 5-8 seconds max\n- Text overlays for each point\n- Pacing must be energetic\n- 20-30 seconds total",
      "with": "- For the three-point template above, give each point about 6 seconds and finish in 25 seconds\n- For four or five points, add one POINT slot per insight; allow 5\u20138 seconds per point, 2 seconds for the hook and 3 seconds for the CTA (25\u201345 seconds total)\n- Text overlays for each point\n- Pacing must be energetic; cut a point rather than rush an explanation"
    },
    {
      "id": "rapid-example",
      "reason": "Missing usable populated example.",
      "insert_after": "Prompt Template section",
      "content": "## Example\n\nIllustrative three-point reel for first-time podcast guests:\n\n- Hook: \u201cThree checks before your next recording.\u201d\n- Point 1: \u201cPut on headphones so your microphone does not pick up the other speaker.\u201d Overlay: HEADPHONES.\n- Point 2: \u201cTurn off notifications before you start.\u201d Overlay: NO INTERRUPTIONS.\n- Point 3: \u201cRecord and play back ten seconds to check your sound.\u201d Overlay: TEST FIRST.\n- CTA: \u201cSave this for your next interview.\u201d\n\nUse the 25-second template and read it aloud before editing."
    }
  ],
  "optional": [
    "Replace attention-clock metaphor only if clearer to the owner; no scientific study required."
  ],
  "scope": "Existing evidence labels/scores preserved. No framework inference or evidence-class rewrite authorized. Shared contrast owner8006e12e; package-body proposals owner e050b6be. Missing worked examples are specific reader-task gaps, not a word-count target."
}

## Exact completed assessment

{
  "id": "quality-20261016-rapid-fire",
  "status": "needs_revision",
  "assessed_at": "2026-10-16T16:52:11Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra; independent semantic/source review by same-model subagent)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "2bbf59db469bb3447fc3458e5bf62e5b92f4cc67c2b7d83b108767afbd38dbb1",
  "report_ref": "docs-internal/quality-reviews/2026-10-16/rapid-fire.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The opening distinguishes quick standalone points from nuanced explanations and identifies when this format is appropriate."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "Three timed points and overlay instructions give an editor a usable scaffold, but there is no populated example of distinct insights, only generic placeholders. Supply one concise illustrative sequence."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "The prompt requests 3\u20135 points but only supplies three slots and a 20\u201330-second total. Five points at its permitted eight seconds need forty seconds before hook/CTA. Resolve the concrete timing conflict rather than silently dropping points."
    },
    "cross_page_consistency": {
      "status": "needs_revision",
      "rationale": "Package placement and distinct reel purposes agree with the framework and reel hub. The absolute prohibition on cropped horizontal source conflicts with the clip guide\u2019s deliberate subject-preserving reframing route. Preserve native-looking composition without excluding a usable source workflow. Evidence-label and score policy questions remain separate owner decisions, not autonomous relabeling."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "\u201cEach new point resets the attention clock\u201d is a metaphor for pacing, not a scientific model needing a study. Keep confident pacing advice; optional wording can say the new point gives viewers a reason to continue. No measured retention claim is established here."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh live desktop1440/mobile390 light/dark inspection finds the essential prompt text nearly invisible against its dark code panel. Light-mode instructions and heading structure are readable, but supported dark-mode users cannot reliably use the working template."
    }
  },
  "source_checks": {
    "applicable": false,
    "rationale": "No external source attestation is made for this production recipe. Internal timing and comparison reasoning were reviewed; unsupported comparative or paid-performance wording is explicitly unresolved rather than certified. Practical editing advice does not itself require experimental proof.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Relevant framework, format neighbors and actual linked routes were read in full.",
    "items": [
      {
        "path": "framework.md",
        "claim": "These assets belong to Package rather than an invented distribution stage.",
        "finding": "Framework Package turns source media into usable assets; these formats fit that definition.",
        "checked_at": "2026-10-16T16:48:09Z"
      },
      {
        "path": "patterns/package/clips/index.md",
        "claim": "Vertical video should never be cropped from horizontal source.",
        "finding": "Clip guidance explicitly adapts horizontal/square/vertical framing and chooses a crop preserving subject and captions. Shared reel prohibition unnecessarily excludes that legitimate production route.",
        "checked_at": "2026-10-16T16:48:22Z"
      },
      {
        "path": "evidence.md",
        "claim": "Platform observation supplies an intelligible evidence basis.",
        "finding": "Public evidence rules distinguish teardown, platform documentation and practitioner judgment; no actual platform observation is named here.",
        "checked_at": "2026-10-16T16:48:22Z"
      },
      {
        "path": "patterns/package/reels/index.md",
        "claim": "Individual pattern purpose and scope fit the collection.",
        "finding": "Hub distinguishes guest sound bites, quick lists and episode promotions consistently; shared obsolete platform specifications were not adopted as factual proof.",
        "checked_at": "2026-10-16T16:47:09Z"
      }
    ]
  },
  "next_review_at": "2026-11-15T16:52:11Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Material dark-mode readability remains unresolved on existing contrast correction; semantic corrections also need exact-artifact owner review on the existing package guidance card.",
  "correction_card": "e050b6be-b3e8-4872-83c4-a6e8fee980f8"
}
