# Scene Still — substantive quality assessment
AI editorial review: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Completed: 2026-10-22T16:50:49Z
Published path: patterns/package/thumbnails/scene-still.md
Exact body SHA256: 8c1de7fc947dc5a16033f316ec4a65cd915bdd6d26855a10a5b7166edcf64d42
Outcome: NEEDS_REVISION. Not human signoff.
## usefulness — pass
The reader can choose a distinctive actual recording moment and reject a visually unremarkable setup.
## substance — needs_revision
The prompt lacks an attached recording still or source time reference despite promising an actual production image; no concrete example shows which studio detail should survive the crop.
## coherence — needs_revision
Actual recording session defines the pattern, but an unconstrained create-a-thumbnail prompt can fabricate a studio. The execution needs the same provenance boundary as the definition.
## cross_page_consistency — pass
The hub distinguishes production-focused scenes from headshots and expressions, consistent with Packaging existing source media in Framework.
## reasonable_claims — needs_revision
No empirical performance promise needs experimental proof. The broad square podcast variant still requires platform adaptation; Apple recommends no text or podcast logo in episode artwork.
## usability — needs_revision
Dark mobile prompt text is materially low contrast; light desktop is readable, with useful heading navigation and no observed document overflow.
## Practitioner reader gate
Purpose pass: a distinctive real recording moment. First action revise: attach an actual cleared still before layout generation. Example revise: illustrate a host demonstrating a microphone in the actual session, not a stock studio. Quality Bar revise: check source fidelity and remove private screens. Meaning/voice pass: keep the production-focused visual recommendation. Essential limits revise: preserve real participants and equipment; do not invent a scene or reveal confidential material.
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
        "path": "patterns/package/thumbnails/index.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "The hub names this style with the same score and matching use case, but its legacy platform specification matrix needs correction.",
        "checked_at": "2026-10-22T16:50:49Z"
      }
    ]
  }
}
## Rendered inspection and limits
Fresh live 1440/390px desktop/mobile light/dark captures retained in output/reports/omi-quality-20261022. All five dark mobile and all five light desktop screenshots visually read, plus complete Markdown and extracted article structure. No document overflow in captures. No video playback or measured click outcomes claimed. Dark prompt/table contrast is material; existing stylesheet proposal remains unapproved on 8006e12e-6551-440a-b9cc-27bce652996f. Browser-version path failure repaired using installed Chromium1243, without installation. Apple initial URL404 and search failures recovered through official-site navigation; unrelated platform rows remain unverified.
## Next action
Same package correction e050b6be-b3e8-4872-83c4-a6e8fee980f8 owns minimal full body proposals; shared CSS stays on8006e12e. No scores/framework or public bodies changed. Park until exact approved correction or changed body; nominal review date 2026-11-21T16:50:49Z. Future pass requires fresh assessment of final published body.
