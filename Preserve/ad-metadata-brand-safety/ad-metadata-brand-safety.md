# Ad Metadata Brand Safety: Hygiene for Owned Feeds

## What It Is
This pattern addresses the critical need for owned-media publishers to implement an ad-metadata-integrity layer to protect their brand and audience trust. Programmatic ad insertion frequently delivers ads with incomplete or incorrect category metadata, leading to brand-safety exclusion filters failing silently. This pattern emphasizes verifying ad categories, advertiser identity, and conducting transcript-level checks to ensure unwanted or miscategorized ads are kept off owned feeds.

## Best For
Owned-media publishers utilizing programmatic ad insertion who need to proactively safeguard their brand reputation and audience trust from miscategorized or inappropriate advertisements. This is particularly relevant for podcasts, video content, and other owned channels where ad content directly impacts the user experience.

## Why It Works
Implementing an ad-metadata-integrity layer provides publisher-side control over ad content. By verifying programmatic demand's categorization and advertiser identity, publishers can prevent the degradation of their owned feed's reputation. This approach complements existing measurement-provenance efforts by not solely relying on platform- or demand-supplied metadata, ensuring a more robust brand-safety posture.

## Required Elements
*   **Ad-metadata-integrity layer:** A system or process for verifying ad categories, advertiser identity, and potentially conducting transcript-level checks.
*   **Categorization verification/audit:** Regular audits of programmatic demand to ensure accurate ad categorization.
*   **Exclusion filters:** Robust filters for unwanted ad categories, backed by verified metadata.
*   **Transcript-level checks:** For audio/video content, analyzing ad transcripts for brand-safety risks.

## Quality Bar
The quality bar for this pattern is measured by the effectiveness of preventing miscategorized or brand-unsafe ads from appearing in owned feeds. A high-quality implementation demonstrates a significant reduction in ad miscategorization incidents and a maintained level of audience trust and brand reputation.

## When Not To Use
This pattern may be less critical for owned media that does not utilize programmatic advertising or where ad content is manually vetted and inserted. However, for any owned media reliant on automated ad serving, this pattern becomes increasingly relevant.

## Riggg Score
3/5 (Medium evidence strength)

## Evidence
*   **PRIMARY / vendor release (2026-07-28):** RedCircle "Mic Check for Programmatic Ads." This report estimates ~1 in 50 programmatic ads are miscategorized, citing real cases such as gambling ads categorized as "financial planning" and sex-toy brand creative as "Shopping." The tool transcribes ad creative, scores category accuracy, verifies advertiser identity, and builds keyword lists/descriptions. It extends the 2025 host-read Mic Check, which claimed a 75% host-read error reduction. Sources: [https://podnews.net/press-release/mic-check-programmatic-ads](https://podnews.net/press-release/mic-check-programmatic-ads) (via RedCircle) + [https://podnews.net/update/ads-wrong-categories-check](https://podnews.net/update/ads-wrong-categories-check)
*   **2025 antecedent:** [https://redcircle.com/blog/introducing-mic-check-the-instant-quality-check-for-host-read-ads/](https://redcircle.com/blog/introducing-mic-check-the-instant-quality-check-for-host-read-ads/)

## Related Patterns
*   **Measurement Provenance (f267c3c3 AMP Accords / IAB v2.3):** This pattern complements measurement provenance work by emphasizing the need for trustworthy metadata and not blindly trusting platform- or demand-supplied information.