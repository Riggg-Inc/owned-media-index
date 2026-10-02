# AI-Disclosure and Provenance in the Owned Asset

## What It Is

A pattern for carrying AI-disclosure and machine-readable provenance metadata inside the owned canonical asset — the RSS feed and the creator-owned website — rather than delegating it to whichever platform renders the file.

As of 2026-08-03, the EU AI Act transparency obligations (Article 50) are law. Article 50(2) requires providers of AI systems that generate synthetic audio, image, video, or text to mark those outputs "in a machine-readable format and detectable as artificially generated or manipulated." Article 50(1) requires that people be informed when they are interacting with an AI system. For owned media consumed by any EU audience, this converts AI-disclosure from an optional trust signal into a compliance obligation.

The pattern: build the disclosure and provenance into the durable, portable, platform-independent asset you control, so the signal travels with the content regardless of the destination platform.

## Best For

- Podcast and webinar programs with any EU audience (effectively any open RSS feed).
- Programs using generative AI to produce or manipulate spoken content — synthesized voice lines, generated segments, or AI-authored narration.
- Owned feeds and websites that already carry structured metadata (Podcasting 2.0 namespace tags, schema.org markup).
- Programs treating regulatory durability as a preservation concern, not a per-platform afterthought.

## Why It Works

Platforms come and go, and their disclosure UIs are inconsistent and outside your control. The one place a creator controls end-to-end is the owned asset: the RSS feed and the website. Putting machine-readable provenance there means the disclosure is:

- **Portable** — travels with the feed to every aggregator and player.
- **Durable** — survives platform UI changes and platform churn.
- **Auditable** — a single canonical source of truth for what was AI-generated.

This generalizes the Podcasting 2.0 namespace-as-metadata-carrier approach and reinforces provenance as a GEO/AEO trust signal. It also sharpens the AI-production authenticity guardrail from a nice-to-have into a disclosure requirement for generated or manipulated content.

The key scoping decision is the boundary between **generation/manipulation** (in scope) and **assistive editing** (out of scope). Article 50 carves out AI used as "an assistive function for standard editing" or that does "not substantially alter the input data ... or the semantics thereof." In practice: de-noising, repair, leveling, and standard AI editing tools are assistive and not triggering; generating whole phrases a voice never recorded, or synthesizing segments, does trigger disclosure.

## Required Elements

- A human-readable AI-disclosure statement in show notes and on the owned website.
- A machine-readable provenance label carried in the owned asset (feed item-level metadata; watch the emerging podcast-namespace provenance tag or a C2PA-style content-credentials manifest as the canonical carrier).
- A documented internal boundary defining "generation/manipulation" vs. "assistive editing" for the program's workflow, so labeling is consistent and defensible.
- Item-level granularity: disclosure applies per episode/asset, since not every item uses generative AI.
- No retroactive labeling required for content produced before the enforcement date, but a forward policy from that date.

## Quality Bar

An EU-consumed asset that uses generative AI to produce or manipulate content carries both a human-readable disclosure and a machine-readable provenance label in the owned feed/website, with a documented and consistently applied generation-vs-assistive boundary. The disclosure survives when the asset is syndicated to any platform.

## When Not To Use

- The program uses no generative AI, or uses AI only for assistive editing (de-noising, repair, leveling) that does not substantially alter semantics — disclosure is not triggered.
- No EU audience and no other jurisdiction with an equivalent obligation — the compliance driver is absent, though the trust-signal argument may still apply.
- The team cannot yet define a consistent generation-vs-assistive boundary — resolve that first; inconsistent labeling is worse than a clear, documented policy.

## Riggg Score

4

## Evidence

Evidence level: external-research.

Primary legal source: EU AI Act Article 50(2) — providers of AI generating synthetic audio/image/video/text "shall ensure that the outputs ... are marked in a machine-readable format and detectable as artificially generated or manipulated," with a carve-out where AI performs "an assistive function for standard editing" or does "not substantially alter the input data ... or the semantics thereof." Article 50(1) requires disclosure of AI interaction. Verified via web fetch on 2026-08-03 (artificialintelligenceact.eu/article/50/; machine-translation caveat noted; official text at artificialintelligenceact.eu/the-act/).

Supporting industry sources (dated 2026-08-03): Podnews, "The EU Artificial Intelligence Act becomes law." Production Expert clarifies that manipulation excludes de-noising/repair/AI editing but includes generating whole phrases a voice never recorded; no retroactive labeling for content made before the enforcement date; maximum fines cited around $40M. Public-broadcaster disclosure example: the BBC AI-usage policy.

Honest gaps: the "machine-readable" standard is not yet settled — the AI Office is expected to publish detection/labeling guidelines, and there is no canonical podcast-feed provenance tag yet. Open watch: whether a podcast-namespace provenance tag or a C2PA content-credentials manifest becomes the owned-feed carrier. This entry frames an owned-media pattern (carry provenance in the owned asset); it is not legal advice and does not set compliance thresholds.

Score rationale: external-research evidence level, cap 4 per SCORING.md. Scored 4 rather than 3 because the driver is a live legal obligation with a defined enforcement date and fine schedule, not speculation, and the owned-asset carrier approach is a clear, repeatable practice.

## Related Patterns

- `preserve/searchability/` — Podcasting 2.0 transcript/namespace tags as the machine-readable metadata carrier.
- `produce/` — AI-agentic production authenticity/quality guardrail (disclosure now mandatory for generated/manipulated content).
- GEO/AEO provenance as an AI-answer citation trust signal (Preserve).
