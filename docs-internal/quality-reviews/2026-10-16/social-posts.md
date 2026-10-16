# social-posts — substantive quality assessment

AI editorial review, not human signoff. Full published source and fresh desktop/mobile light/dark rendered presentation assessed. Semantic/source child completed 2026-10-16T16:50:59Z; parent integrated actual render findings and completed at 2026-10-16T16:52:11Z. Parent read all five full target bodies, framework and both BTS routes, inspected ten representative screenshots from twenty captures. No score/framework/body edits or inferred approval.

## Practitioner reader checks

{
  "purpose": {
    "status": "pass",
    "finding": "Eight purposes let the reader choose the appropriate post type."
  },
  "first_action": {
    "status": "pass",
    "finding": "Choose purpose, then platform-specific version, as the opening hierarchy explains."
  },
  "example": {
    "status": "pass",
    "finding": "Quote Share versus Episode Announcement versus Behind the Scenes are concrete decision examples appropriate for a hub."
  },
  "quality_bar": {
    "status": "revise",
    "finding": "Nine-photo maximum fails the actual official twenty-photo constraint; other unsupported specifications cannot serve as verified checks."
  },
  "meaning_and_voice": {
    "status": "pass",
    "finding": "No revision applied. Preserve eight types and platform tailoring rather than deleting useful reference sections."
  },
  "essential_limits": {
    "status": "revise",
    "finding": "Do not imply external-link placement guarantees reach; distinguish editorial targets from platform limits and unknown feature scope."
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

[
  {
    "url": "https://help.x.com/en/using-x/how-to-post",
    "checked_at": "2026-10-16T16:48:02Z",
    "finding": "HTTP 403; no body verification."
  },
  {
    "url": "https://help.x.com/en/using-x/x-premium",
    "checked_at": "2026-10-16T16:48:02Z",
    "finding": "HTTP 403; no Premium feature verification."
  },
  {
    "url": "https://support.tiktok.com/en/using-tiktok/creating-videos/making-a-post",
    "checked_at": "2026-10-16T16:48:02Z",
    "finding": "Redirect produced only TikTok Support heading; no usable specifications."
  },
  {
    "url": "https://helpx.adobe.com/premiere-pro/using/auto-reframe.html",
    "checked_at": "2026-10-16T16:48:26Z",
    "finding": "HTTP 403; no fetched support for reframing. Finding relies on actual internal clip guidance and ordinary editing logic, not this blocked page."
  }
]

## Semantic required work and optional preferences

{
  "required": [
    {
      "id": "linkedin-photos",
      "reason": "Confirmed incorrect hard maximum.",
      "replace": "| LinkedIn | 9 images | 1 video |",
      "with": "| LinkedIn | Up to 20 photos | 1 video |",
      "source": "https://www.linkedin.com/help/linkedin/answer/a527229"
    },
    {
      "id": "linkedin-link-performance",
      "reason": "Unsupported causal reach claim and deterministic workaround.",
      "replace": "Links reduce organic reach; put in comments or at end",
      "with": "Place the destination where readers can find it; test inline versus comment placement against your goal"
    },
    {
      "id": "platform-matrix-scope",
      "reason": "Remaining present-tense technical matrix needs exact source verification or deliberate reclassification; do not infer updated limits from blocked sources.",
      "owner_choice": "Verify each remaining hard limit/feature row against current official documentation or actual composer, preserving supported rows; replace unresolved hard maxima with specific current-workflow checks. Do not publish a guessed refreshed table. The report does not supply a complete approved matrix replacement."
    }
  ],
  "optional": [
    "Polish repeated introductory language only if desired; not a release blocker."
  ],
  "scope": "Existing evidence labels/scores preserved. No framework inference or evidence-class rewrite authorized. Shared contrast owner8006e12e; package-body proposals owner e050b6be. Missing worked examples are specific reader-task gaps, not a word-count target."
}

## Exact completed assessment

{
  "id": "quality-20261016-social-posts",
  "status": "needs_revision",
  "assessed_at": "2026-10-16T16:52:11Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra; independent semantic/source review by same-model subagent)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "93d12811afaecc1a9316f93996593dae8d0e877be645223a00ff6f30d752222f",
  "report_ref": "docs-internal/quality-reviews/2026-10-16/social-posts.md",
  "dimensions": {
    "usefulness": {
      "status": "needs_revision",
      "rationale": "The eight-type matrix usefully distinguishes purposes, but the same page promises current platform constraints and provides a confirmed incorrect LinkedIn photo maximum. Readers cannot safely use the reference for its stated lookup task."
    },
    "substance": {
      "status": "needs_revision",
      "rationale": "Type-purpose examples are sufficient for a hub; a completed post is not necessary here. The technical reference is substantial but includes a confirmed wrong LinkedIn photo maximum, making it unsafe as a specifications lookup."
    },
    "coherence": {
      "status": "needs_revision",
      "rationale": "Types versus platform versions is clearly explained. Editorial defaults and purported hard constraints are mixed: exact truncation thresholds and link-placement advice look like universal platform rules."
    },
    "cross_page_consistency": {
      "status": "needs_revision",
      "rationale": "Its asset/distribution distinction fits owned-media.md and Package. Linked child process guidance is compatible. \u201cUnicode bold\u201d is a character substitution workaround, not native formatting; clarify the distinction instead of presenting equivalent support."
    },
    "reasonable_claims": {
      "status": "needs_revision",
      "rationale": "LinkedIn Help says twenty photos, not nine. X documentation supports ordinary 280 weighted characters and 23-character URLs, but does not establish Premium lengths, full-post visibility, or the rest of this matrix. \u201cLinks reduce organic reach\u201d is unqualified performance causality without support. The legacy snapshot note does not repair present-tense hard limits."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Fresh live desktop1440/mobile390 light/dark inspection finds pale alternating table rows with nearly white text in dark mode, obscuring the actual platform and purpose choices. Light mode is readable and there is no document horizontal overflow."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Numerical platform specifications and performance claims need proportionate credible verification.",
    "items": [
      {
        "url": "https://www.linkedin.com/help/linkedin/answer/a527229",
        "claim": "LinkedIn permits at most nine images per post.",
        "finding": "Full official Help body read. Both upload steps and multi-photo requirements explicitly allow a maximum of 20 photos. This directly contradicts the page\u2019s nine-image maximum.",
        "checked_at": "2026-10-16T16:48:02Z"
      },
      {
        "url": "https://docs.x.com/fundamentals/counting-characters",
        "claim": "Ordinary X posts allow 280 characters and links count about 23.",
        "finding": "Full official developer page read: ordinary limit is 280 weighted characters; URLs count exactly 23, emoji/CJK can count double. Does not establish Premium 25,000 length, rendering truncation or formatting support.",
        "checked_at": "2026-10-16T16:48:30Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Relevant framework, format neighbors and actual linked routes were read in full.",
    "items": [
      {
        "path": "owned-media.md",
        "claim": "Social posts remain owned assets distributed through shared platforms.",
        "finding": "Definition explicitly distinguishes content ownership from platform audience control, consistent with this hub.",
        "checked_at": "2026-10-16T16:48:09Z"
      },
      {
        "path": "patterns/package/index.md",
        "claim": "Choose social copy by purpose and platform.",
        "finding": "Package selection guide explicitly directs readers to post purpose and platform version, matching the type/version hierarchy.",
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
