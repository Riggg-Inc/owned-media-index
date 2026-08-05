# Webinar Platform Consolidation Risk

## What It Is

A strategy for mitigating portability and lock-in risks for owned webinar content, especially in light of platform consolidation events. This pattern emphasizes maintaining an export-first posture for raw recordings, transcripts, and registrant data to ensure content ownership and flexibility, rather than relying solely on vendor-native engagement features.

## Best For

- Owned media programs that treat webinars as core assets.
- Content teams with significant webinar libraries.
- Organizations concerned about vendor lock-in or future platform changes.
- Teams prioritizing long-term content portability and data control.

## Why It Works

Platform consolidation, such as the Cvent–ON24 acquisition, can alter pricing, features, and roadmaps, potentially impacting the accessibility and utility of owned webinar content. By establishing a clear portability and export discipline, teams can safeguard their content and audience data, ensuring continued access and the ability to migrate to alternative platforms without loss. This reduces dependence on single-vendor ecosystems and preserves the value of content assets.

## Required Elements

- **Raw Recording Archive:** A process for capturing and archiving raw, unbranded webinar recordings in a neutral, accessible format (e.g., MP4).
- **Transcript Export:** Routine export of high-quality transcripts, ensuring they are stored and managed independently.
- **Registrant Data Ownership:** Clear protocols for exporting and owning all registrant and attendance data, independent of the webinar platform's CRM.
- **Platform-Agnostic Content Strategy:** Develop content that is not overly reliant on proprietary platform features that may not be transferable.
- **Regular Export Audits:** Periodic review of export processes to ensure data integrity and completeness.

## Quality Bar

Webinar content, including raw media and associated data, should be fully reconstructible and portable to a new platform with minimal effort and no loss of fidelity or information. The content should retain its core value and functionality even outside the original vendor's ecosystem.

## When Not To Use

Avoid excessive focus on this pattern when:

- Webinars are solely used for ephemeral, live-only events with no long-term content value.
- The program has minimal investment in webinars and portability is a low priority.
- The current vendor has a proven, stable history of open data practices and no foreseeable acquisition/merger risk.

## Riggg Score

4

## Evidence

Evidence level: external-research.

Based on primary vendor M&A announcements (Cvent acquires ON24), industry analysis of platform consolidation trends, and the stated "deeper platform gravity" in post-acquisition vendor messaging, which directly highlights increased lock-in risks.

## Related Patterns

- `preserve/data-portability-standard.md`
- `distribute/rss-feed-canonical.md`
- `preserve/ai-disclosure-provenance-owned-asset.md` (for long-term asset integrity)
