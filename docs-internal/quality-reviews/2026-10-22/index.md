# Thumbnails — substantive quality assessment
AI editorial review: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Completed: 2026-10-22T16:50:49Z
Published path: patterns/package/thumbnails/index.md
Exact body SHA256: bb386635feeec17461dfbceafee5724f77d0fa80002a1779f5a63dca07aa3516
Outcome: NEEDS_REVISION. Not human signoff.
## usefulness — pass
The five-style comparison provides a useful first choice by episode type and links directly to the corresponding patterns.
## substance — pass
The hub contains a substantial style table and concrete design checks; it is not empty filler. The specification matrix has substance but factual corrections are required.
## coherence — needs_revision
The page describes current platform constraints while relegating their obsolete snapshot status to a footer; users encounter operational instructions before the qualification.
## cross_page_consistency — pass
Style names, scores and use cases match the five sibling pages and the Package definition; no scoring redesign is needed to correct the operational specifications.
## reasonable_claims — needs_revision
The YouTube 1280x720 recommendation and universal 2 MB maximum differ from current official guidance. The Google Podcasts row conflicts with the official 2024 discontinuation announcement. Apple size range is supported, but its 10 MB limit was not established by the episode-art source. Other platform rows were not certified.
## usability — needs_revision
Dark mobile style and specification tables use near-white striped backgrounds with pale text, obscuring decisions. The wide specification table requires horizontal navigation; absence of document overflow alone is not a usability pass.
## Practitioner reader gate
Purpose pass: choose an episode thumbnail style. First action pass: match the episode to one of five concrete use cases. Example pass: the style/use-case comparison is the equivalent hub decision example. Quality Bar revise: distinguish a small-size design test from an asserted universal 120px app grid. Meaning/voice pass: retain the comparison and scores. Essential limits revise: replace obsolete active-platform specs with current sourced guidance rather than relying on the legacy disclaimer.
## Source and comparison evidence
{
  "sources": {
    "applicable": true,
    "rationale": "Read official platform guidance in context for the actual format claims; practitioner design advice does not require experimental certification.",
    "items": [
      {
        "url": "https://support.google.com/youtube/answer/72431?hl=en",
        "claim": "YouTube landscape video and podcast artwork require different output choices; a square crop is not a universal adaptation.",
        "finding": "Official image-size section recommends 16:9 videos, 9:16 Shorts and 1:1 podcast playlists. Current guidance recommends 3840x2160 video thumbnails and distinguishes 2 MB mobile from 50 MB desktop uploads. Relevant section read; fetch warned incomplete HTML, so no complete-site verification claimed.",
        "checked_at": "2026-10-22T16:46:37Z"
      },
      {
        "url": "https://podcasters.apple.com/support/5516-episode-art-template",
        "claim": "Square episode artwork should simply reuse the same text-overlay thumbnail.",
        "finding": "Apple specifies square episode artwork, 3000px preferred and RSS acceptance 1400\u20133000px; PNG/JPG without transparency. It recommends avoiding text and podcast logos because the interface already supplies titles. A square version of the text-heavy prompt needs explicit adaptation.",
        "checked_at": "2026-10-22T16:48:12Z"
      },
      {
        "url": "https://blog.youtube/news-and-events/podcast-destination-on-youtube-music/",
        "claim": "Google Podcasts remains a current destination needing episode thumbnail exports.",
        "finding": "The official September 2023 announcement says Google Podcasts will be discontinued in 2024 while users move to YouTube Music. This contradicts treating it as an ordinary active destination in a current operational table; this source is the announcement, not a fresh product test.",
        "checked_at": "2026-10-22T16:47:14Z"
      }
    ]
  },
  "comparisons": {
    "applicable": true,
    "rationale": "Read complete current framework, scoring, thumbnail hub and all five published style pages before comparing their operating guidance.",
    "items": [
      {
        "path": "framework.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Package turns source media into usable assets; each thumbnail is a packaging decision rather than a promised performance result.",
        "checked_at": "2026-10-22T16:50:49Z"
      },
      {
        "path": "scoring.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Scores are editorial judgments about fit and evidence, not numeric evidence of click-through superiority.",
        "checked_at": "2026-10-22T16:50:49Z"
      },
      {
        "path": "patterns/package/thumbnails/branded-template.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Branded Template prioritizes show recognition; distinct episode detail remains necessary, unlike source-number, expression or actual-scene choices.",
        "checked_at": "2026-10-22T16:50:49Z"
      },
      {
        "path": "patterns/package/thumbnails/data-visual.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Read full sibling: its visual mechanism and score agree with the hub; production prompts need source-specific execution inputs.",
        "checked_at": "2026-10-22T16:50:49Z"
      },
      {
        "path": "patterns/package/thumbnails/emotion-close-up.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Read full sibling: its visual mechanism and score agree with the hub; production prompts need source-specific execution inputs.",
        "checked_at": "2026-10-22T16:50:49Z"
      },
      {
        "path": "patterns/package/thumbnails/guest-headshot-text.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Read full sibling: its visual mechanism and score agree with the hub; production prompts need source-specific execution inputs.",
        "checked_at": "2026-10-22T16:50:49Z"
      },
      {
        "path": "patterns/package/thumbnails/scene-still.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Read full sibling: its visual mechanism and score agree with the hub; production prompts need source-specific execution inputs.",
        "checked_at": "2026-10-22T16:50:49Z"
      }
    ]
  }
}
## Rendered inspection and limits
Fresh live 1440/390px desktop/mobile light/dark captures retained in output/reports/omi-quality-20261022. All five dark mobile and all five light desktop screenshots visually read, plus complete Markdown and extracted article structure. No document overflow in captures. No video playback or measured click outcomes claimed. Dark prompt/table contrast is material; existing stylesheet proposal remains unapproved on 8006e12e-6551-440a-b9cc-27bce652996f. Browser-version path failure repaired using installed Chromium1243, without installation. Apple initial URL404 and search failures recovered through official-site navigation; unrelated platform rows remain unverified.
## Next action
Same package correction e050b6be-b3e8-4872-83c4-a6e8fee980f8 owns minimal full body proposals; shared CSS stays on8006e12e. No scores/framework or public bodies changed. Park until exact approved correction or changed body; nominal review date 2026-11-21T16:50:49Z. Future pass requires fresh assessment of final published body.
