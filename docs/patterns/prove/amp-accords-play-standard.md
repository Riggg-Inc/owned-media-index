---
description: "The AMP Accords Play Standard pattern separates delivered downloads from consumed plays and ad impressions in cross-platform reporting."
---

# AMP Accords Play Standard

The AMP Accords Play Standard pattern separates delivered downloads from consumed plays and ad impressions in cross-platform reporting. Use explicit metric definitions, collection methods, and source platforms rather than adding unlike audience measures together.

**Stage:** Prove
**Score:** 4

## What It Is

The AMP (Alliance for Measurement in Podcasting) Accords represent a shift in podcast measurement from simple file downloads to more granular consumed plays and ad impressions. This pattern advocates for normalizing performance metrics across diverse platforms, ensuring owned-media scorecards differentiate between delivery-based and consumption-based audience engagement. It addresses the challenge of comparing disparate metrics (e.g., downloads vs. 30-second plays vs. YouTube views) by emphasizing transparent reporting of measurement methods and sources.

## Best For

- Owned media programs requiring accurate, comparable cross-platform performance measurement.
- Teams needing to articulate audience consumption beyond basic download figures.
- Organizations seeking to protect their analytics from inflated or inconsistent platform-specific metrics.

## Why It Works

By providing a unified framework, the AMP Accords (and patterns based on them) enable a clearer understanding of how audiences actually consume content. This reduces ambiguity and prevents misinterpretation of performance data. It helps in making informed content and distribution decisions by highlighting true engagement, rather than just content delivery. Separating delivery from consumption makes reporting limitations clearer; it does not itself prevent ad skipping or prove that an impression was consumed.

## Required Elements

- **Metric Definition:** Clearly state the definition of each metric reported (e.g., "play" as 30 seconds of listen time).
- **Measurement Method:** Specify how each metric is collected (e.g., server logs, client-side tracking).
- **Source Platform:** Identify the origin of the data (e.g., Spotify, Apple Podcasts, IAB-compliant hosting).
- **Consumption Type:** Categorize metrics as either delivery-based (e.g., downloads) or consumption-based (e.g., plays, ad impressions).
- **Metric Glossary:** Include a glossary of all reported metrics and their definitions in client-facing scorecards.

## Quality Bar

Scorecards should clearly distinguish and define all reported metrics and their sources, avoiding any implicit assumptions of comparability. Where possible, adhere to AMP Accords definitions for "Play," "Audience," "Ad Impression," and "Ad Audience." Metrics should accurately reflect audience consumption rather than just content delivery.

## When Not To Use

This pattern may be less critical for programs solely focused on content archival or those with very limited distribution channels that already provide uniform metrics. However, as the podcast ecosystem matures and diversifies, the principles of transparent and normalized measurement become increasingly relevant for virtually all owned-media efforts.

## Evidence

The [Alliance for Measurement in Podcasting’s official site](https://www.ampaccords.com/) describes the Accords as a cross-platform measurement standard ratified by twelve operators spanning platforms, advertisers, publishers, and creators. Its “first” claim is the organization’s own characterization, not an independently established comparison.

The public landing page does not substantiate all detailed metric definitions. The full white paper requires a form submission and was not reviewed in this pass. Treat the 30-second play example as illustrative until checked against the current standard and the reporting platform’s own documentation. Spotify alignment and anti-ad-skipping effects are not established by this source. The existing score is retained pending the normal evidence review; a source link alone does not validate it.

## Related Patterns

- `preserve/ad-metadata-brand-safety/ad-metadata-brand-safety.md`
- `publish/syndication/spotify-native-upload-bypasses-rss.md`
- `preserve/podcasting2-transcript-namespace.md` — NOT YET WRITTEN (Workboard card f2ca608a, in todo)
