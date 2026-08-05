# AMP Accords Play Standard

## What It Is

The AMP (Audio Measurement Protocol) Accords represent a shift in podcast measurement from simple file downloads to more granular consumed plays and ad impressions. This pattern advocates for normalizing performance metrics across diverse platforms, ensuring owned-media scorecards differentiate between delivery-based and consumption-based audience engagement. It addresses the challenge of comparing disparate metrics (e.g., downloads vs. 30-second plays vs. YouTube views) by emphasizing transparent reporting of measurement methods and sources.

## Best For

- Owned media programs requiring accurate, comparable cross-platform performance measurement.
- Teams needing to articulate audience consumption beyond basic download figures.
- Organizations seeking to protect their analytics from inflated or inconsistent platform-specific metrics.

## Why It Works

By providing a unified framework, the AMP Accords (and patterns based on them) enable a clearer understanding of how audiences actually consume content. This reduces ambiguity and prevents misinterpretation of performance data. It helps in making informed content and distribution decisions by highlighting true engagement, rather than just content delivery. It also serves as a guardrail against platform-side ad skipping, ensuring that reported ad impressions reflect actual consumption.

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

## Riggg Score

4

## Evidence

The AMP Accords have been established as the first cross-platform measurement standard in podcasting, ratified by various industry players (platforms, advertisers, publishers, creators). Spotify has adjusted its play counts to reflect a minimum of 30 seconds of listening, aligning with the AMP's Play definition. While the IAB Tech Lab's guidelines are still evolving, the industry trend points towards more granular, consumption-based metrics. The need for this pattern is further underscored by issues like platform ad-skipping (e.g., Spotify's "Skip Ahead" test), which widen the gap between delivery and actual consumption, making verified-listen metrics crucial for fraud/quality guardrails.

## Related Patterns

- `preserve/ad-metadata-brand-safety`
- `distribute/spotify-native-upload-bypasses-rss`
- `preserve/podcasting2-transcript-namespace`
