# Guest Headshot Text — substantive quality assessment
AI editorial review: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Completed: 2026-10-22T16:50:48Z
Published path: patterns/package/thumbnails/guest-headshot-text.md
Exact body SHA256: d1a57e0cf579495a62e8d38c4065e7faf36a8cfac64f14cd67ddfcd435c696d7
Outcome: NEEDS_REVISION. Not human signoff.
## usefulness — pass
Recognizable guest versus topic-first selection is an actionable audience-fit decision, with an explicit case for choosing another format.
## substance — pass
The prompt supplies guest name, headshot, short topic and brand inputs; this is materially more specific than the generic sibling prompts, though a worked example would help.
## coherence — needs_revision
The opening and context request 3–5 words, while the requirements permit 5–7; the reader gets inconsistent instructions for the main text deliverable.
## cross_page_consistency — needs_revision
Scoring calls scores editorial judgments, but the unqualified most reliable thumbnail format reads as a comparative performance fact rather than a recommendation conditional on guest recognition.
## reasonable_claims — needs_revision
No comparative benchmark is provided for most reliable. Keep a confident audience-fit recommendation without inventing evidence. Apple episode art guidance contradicts a blanket square reuse of text/logo overlays.
## usability — needs_revision
Fresh dark mobile render makes the detailed prompt low contrast; light desktop is readable with a clear hierarchy and no page overflow.
## Practitioner reader gate
Purpose pass: recognition and topic choice are clear. First action pass: provide guest headshot and topic. Example revise: add one short illustrative title/layout rather than requiring readers to infer composition. Quality Bar revise: choose a consistent overlay target. Meaning/voice revise: replace only the universal reliability assertion with a scoped recommendation. Essential limits revise: use a permitted headshot and separate Apple no-text episode artwork.
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
        "checked_at": "2026-10-22T16:50:48Z"
      },
      {
        "path": "scoring.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Scores are editorial judgments about fit and evidence, not numeric evidence of click-through superiority.",
        "checked_at": "2026-10-22T16:50:48Z"
      },
      {
        "path": "patterns/package/thumbnails/branded-template.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "Branded Template prioritizes show recognition; distinct episode detail remains necessary, unlike source-number, expression or actual-scene choices.",
        "checked_at": "2026-10-22T16:50:48Z"
      },
      {
        "path": "patterns/package/thumbnails/index.md",
        "claim": "Compatibility of published selection guidance and framework roles.",
        "finding": "The hub names this style with the same score and matching use case, but its legacy platform specification matrix needs correction.",
        "checked_at": "2026-10-22T16:50:48Z"
      }
    ]
  }
}
## Rendered inspection and limits
Fresh live 1440/390px desktop/mobile light/dark captures retained in output/reports/omi-quality-20261022. All five dark mobile and all five light desktop screenshots visually read, plus complete Markdown and extracted article structure. No document overflow in captures. No video playback or measured click outcomes claimed. Dark prompt/table contrast is material; existing stylesheet proposal remains unapproved on 8006e12e-6551-440a-b9cc-27bce652996f. Browser-version path failure repaired using installed Chromium1243, without installation. Apple initial URL404 and search failures recovered through official-site navigation; unrelated platform rows remain unverified.
## Next action
Same package correction e050b6be-b3e8-4872-83c4-a6e8fee980f8 owns minimal full body proposals; shared CSS stays on8006e12e. No scores/framework or public bodies changed. Park until exact approved correction or changed body; nominal review date 2026-11-21T16:50:48Z. Future pass requires fresh assessment of final published body.
