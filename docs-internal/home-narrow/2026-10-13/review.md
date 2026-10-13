# Homepage — narrow factual correction, October 13

Status: INTERNAL REVIEW ONLY. Supersedes the paired homepage draft at `9bc305cca18145c94372b9303d1755e2ed6e33c4`; historical artifacts remain intact. No approval or publication implied.

Card: `42dce931-c8d7-47b5-82a0-ce1c6a3c603e`. Current page: https://index.riggg.com/ . Base: `42ddb64b5dfe341004f70111178c5e159893f5e6` (fresh origin/main). Original current homepage sources at Oct7 proposal commit are byte-identical to this base; no subsequent homepage edits were reset. Live homepage retrieved HTTP200 October13 20:11UTC; its reviewed copy agrees with base.

## What stays

“Everything You Need”, “Open Source. Opinionated.”, “Opinionated. Sourced. Specific.”, broadcast-quality aspirations (both occurrences), the anti-generic/vendor-pitched positioning, evidence-focused editorial voice, community CTA, and full Riggg service pitch remain. Owner confirmed every submission is reviewed by the team October13 20:10UTC; that statement is retained verbatim. No added benefits companion, repeated disclaimers, score redesign, article/navigation/privacy/tracking changes, or layout changes.

## Exact before → after (only actual changes)

### `docs/index.md`

**Before:** Everything in this index maps to five stages of the owned media operating system.

**After:** The pattern library maps to five stages of the owned media operating system.

**Why:** Framework introduction: policy/contribution pages are not individual stage entries. Keeps the five-stage marketing framework intact in both representations.

**Before:** What's coming next and how the index evolves quarterly

**After:** What's coming next, including a proposed quarterly issue

**Why:** Roadmap calls its quarterly issue proposed, not an established publishing cadence.

**Before:** Entries are scored and sourced. Nothing earns a 5 without evidence.

**After:** Entries are scored and sourced. A 5 means recommended default, with strong evidence and broad usefulness.

**Why:** Matches the existing published scoring definition; no scores or scoring rules change.

### `docs/overrides/home.html`

**Before:** Every entry in the index maps to one of five stages of the owned media operating system.

**After:** The pattern library maps to five stages of the owned media operating system.

**Why:** Same framework correction as Markdown; not a redesign.

**Before:** Top-performing title styles,

**After:** Editorially ranked title styles,

**Why:** Title rankings are editorial recommendations, not a measured performance leaderboard.

**Before:** >Performance Benchmarks</a>

**After:** >Performance Measurement</a>

**Why:** The linked Prove hub explicitly has its Benchmarks section marked “more coming”; measurement accurately names what is available. This heading change is a factual inventory correction, not an objection to marketing headings.

**Before:** the numbers that prove owned media works.

**After:** the numbers that show how your owned media is working.

**Why:** The metrics help assess results; they do not predetermine a positive outcome. Keeps the active, useful pitch.

**Before:** how to make every session findable forever.

**After:** how to make sessions easier to find and reuse.

**Why:** Removes the literal permanence guarantee while keeping the findability/reuse benefit.

**Before:** Every pattern earns a 1–5 score based on evidence, reliability, and real-world production results. Nothing gets a 5 without proof.

**After:** Patterns earn an editorial 1–5 score based on usefulness, evidence, repeatability, and fit for real production. A 5 means recommended default, with strong evidence and broad usefulness.

**Why:** Uses current policy’s editorial criteria and score-5 meaning, without adding limitations boilerplate.

**Before:** Every entry in the index follows the same structure.

**After:** Patterns in the index follow a shared structure.

**Why:** The shared structure applies to patterns, not every policy, hub or contribution page.

**Before:** A 5 means industry standard with production data behind it.

**After:** A 5 means recommended default, with strong evidence and broad usefulness.

**Why:** Corrects the explicit score-5 contradiction: recommended default, not industry standard or mandatory production data.

**Before:** Get simulcast standards, repurposing pipelines, and performance benchmarks.

**After:** Get simulcast standards, repurposing pipelines, and performance scorecards.

**Why:** Current Prove hub offers a scorecard, not a completed benchmark collection.

**Before:** Prove ROI with benchmarks and attribution models.

**After:** Measure ROI with scorecards and attribution models.

**Why:** Keeps the ROI objective and active voice, without claiming measurement guarantees positive ROI or offering a completed benchmark collection.

**Before:** >Top Performing Title Styles</a>

**After:** >Riggg-Ranked Title Styles</a>

**Why:** Closes the second measured-ranking implication. Link target and existing explanatory paragraph remain unchanged.

**Before:** The complete guide to simultaneous live streaming across LinkedIn, YouTube, Facebook, and vertical social platforms.

**After:** Plan your simulcast: destinations, horizontal and vertical outputs, promotion, recording backup, and replay.

**Why:** The destination is a short decision checklist, not complete platform-by-platform instructions. Names its actual decisions; keeps the imperative pitch and adds no access/legal disclaimer.

**Before:** Ranked description styles that improve discoverability across Apple Podcasts, Spotify, and podcast directories.

**After:** Ranked description styles designed to help listeners find and choose your episodes across Apple Podcasts, Spotify, and podcast directories.

**Why:** Keeps the discoverability benefit as design intent rather than an established cross-platform performance result.

## Context and choices

This is a bounded correction, not a new full-site quality judgment. Brand aspirations and the owner-confirmed review workflow are not being treated as suspect factual claims. The changed measurement heading and simulcast teaser are the two inventory choices that might otherwise look like tone editing: their linked destinations demonstrably do not contain the promised benchmark collection or complete platform guide. Other original marketing headings remain untouched.

Sources: current `docs/scoring.md`, `SCORING.md`, `docs/roadmap.md`, `docs/patterns/prove/index.md`, `docs/patterns/package/titles/index.md`, `docs/patterns/package/descriptions/index.md`, `docs/patterns/publish/simulcast-standard.md`, and the owner’s contribution-review confirmation on this card. The Markdown and custom template have different coverage by design; their shared framework, scoring meaning, and service pitch agree.

Content Creation Lab lens retrieved: internal “Hook Building and Hook Templates” synthesis (sections2–3, swipe files versus measured studies; clarity without losing expert meaning). Applied only as plain-language editing judgment for a B2B library, not as evidence of homepage conversion performance. No borrowed viral-result claims.

## Draft checks / release boundary

Current strict build, video-reference parity, site/AEO/freshness validators, fact-check registry validation, and complete regression suite are recorded in `validation.txt`. Independent contextual draft review is in `independent-review.md`. Structural/source checks in `scope-checks.txt` verify layout/CSS/links and owner-protected copy preserved. These are draft checks only; no published quality assessment, review timestamp, registry record, quota bypass, public release or approval. Normal exact-pair owner approval and current release/live gates remain required. Rendered checks are HTML-only; no browser visual acceptance claimed.

## Exact full-file SHA-256

- `docs/index.md`: `ec19dabfb35900a0cde4da5cc07f09375ee36884885a3ed1424780c73ebefded`
- `docs/overrides/home.html`: `1a4d80e1b11234fbd0e89d331dc633681fda1417019cd51ca604d6070e7fe801`

### Independent-review disposition

The independent review recommends this exact pair for owner review, with no blocking defect. Its optional observations are deliberately visible, not silently applied: the anatomy paragraph's “every entry” is read within the “How Patterns Work” section as patterns; vector-database wording describes one supported searchable-library approach rather than a required first step; ROI remains an audience objective rather than a guaranteed positive return or a claim that the scorecard alone computes financial ROI. These are reasonable editorial choices for the owner, not grounds to resume the rejected broad stripping of marketing copy. The full independent note is retained alongside the draft.

### Verified technical outcome

All gates passed on October 13: video-reference parity; strict build; site validator (128 HTML pages / 8,376 resource references, zero errors); AEO validator (127 pages, zero errors); freshness validator (127 pages, zero errors); fact-check registry schema/content validation (zero errors); 109 regression tests passed. Existing registry reports partial/unreviewed records rather than fresh verification: intentionally unchanged. No live page or quality record was updated.
