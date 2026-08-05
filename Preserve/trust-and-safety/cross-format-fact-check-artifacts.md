# Cross-Format Fact-Check Artifacts

## What It Is

A standard for ensuring that fact-checks, corrections, and scientific-context notes for owned media (especially podcasts) are linked and accessible across all audience surfaces. This includes RSS show notes, episode transcripts, owned episode web pages, video descriptions, and on-screen overlays in video formats. The core principle is that trust artifacts, such as corrections or clarifications, must not be limited to a single modality or platform.

## Best For

- Podcasts or media programs addressing high-stakes claims (e.g., health, science, finance, public safety).
- Shows that integrate video and audio formats.
- Programs where factual accuracy and audience trust are paramount.
- Content intended for syndication across multiple platforms and consumption methods (audio-only, video, text).

## Why It Works

Trust and provenance work fails if a correction or fact-check exists only in one modality (e.g., a video overlay) or on a single platform. When fact-checks are consistently linked across all formats, it enhances transparency, audience understanding, and the long-term durability of trust artifacts. This prevents situations where audio-only listeners or AI-indexed answer engines miss critical context or corrections. It establishes a canonical, owned source for trust information.

## Required Elements

- **Stable Owned URL:** Every fact-check or correction artifact must have a stable, dereferenceable URL on an owned property (e.g., the program's website).
- **Timestamps and Transcript Anchors:** When applicable, fact-checks should include timestamps for audio/video references and be anchored to specific points in the transcript.
- **RSS Show Notes Link:** A clear link to the owned URL of the fact-check should be included in the RSS feed's episode notes.
- **Owned Episode Page Integration:** The owned episode web page must clearly display or link to the fact-check artifact.
- **Video Description Link:** For video formats, the video description should contain a prominent link to the fact-check.
- **On-Screen Overlays (when used):** If on-screen overlays are used for real-time fact-checking, they must complement, not replace, the persistent, cross-format links to the owned artifact.

## Quality Bar

Fact-check artifacts are easily discoverable and accessible regardless of how the audience consumes the content (audio, video, text). The owned URL serves as the authoritative source.

## When Not To Use

- When fact-checking is not performed or is outside the scope of the content. This pattern applies *when* fact-checks are created, not to mandate their creation.
- For low-stakes content where a formal fact-check process is not required or feasible.

## Riggg Score

3

## Evidence

Evidence level: external-research.

Based on podcast-industry case analysis, publisher public material, and news investigations, highlighting the challenges of trust preservation when fact-checks are modality-locked. Specifically, observations from a single high-profile case (Diary of a CEO) where on-screen fact-checking in video was not accessible to audio listeners and linked resources were problematic. While a significant case, this is not yet a broad market study, limiting the score to a "Viable" pattern.

## Related Patterns

- `preserve/provenance/ai-disclosure-provenance-owned-asset.md` (for broader AI provenance)
- `prove/trust/canonical-source-for-corrections.md` (potential future pattern for a centralized correction system)
