# Ad Metadata Brand Safety

## What It Is

A strategy for owned-media publishers to ensure brand safety by verifying programmatic ad categorization metadata beyond platform-provided filters. This includes auditing categories, advertiser identity, and performing transcript-level checks to prevent miscategorized or unwanted ads from appearing in owned feeds.

## Best For

- Owned media programs that rely on programmatic ad monetization.
- Publishers concerned about brand reputation and audience trust.
- Teams seeking to implement robust brand-safety controls.

## Why It Works

Programmatic ad insertion often suffers from inaccurate or incomplete categorization metadata, leading to brand-safety filter failures. Implementing an ad-metadata-integrity layer moves brand-safety decisions upstream, allowing publishers to verify ad content and context before distribution. This proactive approach protects the owned feed's brand and audience from miscategorized or inappropriate advertisements.

## Required Elements

- Ad category verification process.
- Advertiser identity verification.
- Transcript-level ad content checks.
- Exclusion filters based on verified metadata.
- Regular audits of programmatic ad performance and categorization.

## Quality Bar

The owned feed consistently avoids miscategorized or brand-unsafe programmatic advertisements, maintaining audience trust and brand reputation.

## When Not To Use

Avoid this pattern when:

- An owned media program does not monetize with programmatic ads.
- Programmatic ad partners guarantee 100% accurate ad categorization and brand safety, making verification redundant.

## Riggg Score

4

## Evidence

Evidence level: external-research.

The fundamental problem of unreliable programmatic ad metadata is corroborated by multiple sources. Barometer's episode-level brand-suitability controls, integrated across AdsWizz, Acast, and Basis DSP (2026-08-14), demonstrate an industry-wide recognition that granular, pre-bid verification is necessary to address miscategorization and brand-safety concerns in podcasts (podnews.net/press-release/basis-barometer-episode-level-brand). This aligns with the card's thesis that programmatic ad metadata cannot be taken at face value.

Further support comes from RedCircle's "Mic Check for Programmatic Ads" (2026-07-28), which estimates ~1 in 50 programmatic ads are miscategorized, citing examples of gambling, political, and adult-oriented ads appearing under incorrect categories. While these specific statistics are vendor-claimed and not independently verified, they illustrate the real-world impact of the underlying metadata unreliability problem (https://podnews.net/press-release/mic-check-programmatic-ads).

## Related Patterns

- `prove/measurement/amp-accords-play-standard.md` (Both are about not trusting demand-supplied metadata at face value.)
