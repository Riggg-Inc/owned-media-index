# Quality review: tools/hosting/video-podcast-hosting-support.md
Outcome: needs_revision. AI editorial review: openai/gpt-6-astra; not human testing or approval.
Completed UTC: 2026-11-23T16:52:33Z
Exact body SHA-256: 0ed289f074a4bafadfe327682c14d60d6a038bc857ab8d40619244fa92014e40

usefulness: pass
Separating file RSS, open HLS, Apple API and native Spotify paths directly helps teams avoid buying the wrong hosting capability.

substance: pass
Twenty host/service rows and nine player rows include named sources, eligibility limits and a concrete sample-feed/test checklist; substantial reference detail is warranted.

coherence: needs_revision
All rows checked November 20 conflicts with Megaphone calling October 20 the date of this review; stale historical audit narration obscures the current decision.

cross_page_consistency: pass
HLS production guidance and feed metadata guidance support audio continuity and destination verification, not universal video reach; this reference supplies the needed route distinctions.

reasonable_claims: needs_revision
Current Megaphone documentation says monetization currently available, contradicting retained future-tense explanation. Transistor analytics coming-soon status is not in current retrieved feature text; Libsyn full-motion YouTube capability remains ambiguous behind generic video labels.

usability: needs_revision
Actual desktop/mobile dark renders make alternating host/player rows nearly unreadable. Mobile table requires horizontal navigation to see essential limits; document overflow=false does not prove all columns visible.

Practitioner reader checks
Purpose PASS: distinguish video delivery capabilities. First action PASS: ask for a sample feed and test target app. Example PASS: Buzzsprout video versus RSS.com audio-only Spotify delivery illustrates non-equivalent integration paths. Quality Bar PASS: verify primary/alternate enclosures, download behavior and approvals. Meaning/voice REVISE narrowly: remove stale review narration, retain practical route distinctions. Essential limits PASS: unknown means unestablished, not unsupported; do not erase eligibility or playback limits.

Evidence and corrections
All body read and four full live screenshots inspected; additional table viewport captures actually viewed because long full-page images shrink excessively. Evidence under /home/production/openclaw-workspace/output/reports/omi-quality-20261123/source-*.json and tools__hosting__video-podcast-hosting-support*.png/json. Eleven primary/ecosystem source documents read; no account upload/playback, private provider access or universal host audit. CoHost, Podbean, Captivate, Omny, Flightcast, Podigee, Beamly, Fountain, TrueFans, Blubrry, Castos, Spreaker and Simplecast individual vendor workflows not freshly retrieved; PSP substantiates only their attributed rows where listed. No factual-review date changed. Complete minimal proposal will target Megaphone and unresolved Transistor/Libsyn wording, not silently refresh every row. Reuse shared card and existing contrast issue; approval required before any public revision.

{
  "source_checks": {
    "applicable": true,
    "rationale": "Fresh read of eleven primary or first-party ecosystem sources covers core delivery distinctions and high-impact current vendor claims; other rows remain attributed dated evidence, not freshly reverified.",
    "items": [
      {
        "url": "https://podcasters.apple.com/support/3684-video-podcasts",
        "claim": "Traditional MOV, MP4 and M4V RSS video remains supported.",
        "finding": "Apple explicitly confirms these formats and standard RSS submission separately from preferred HLS.",
        "checked_at": "2026-11-23T16:50:32.467Z"
      },
      {
        "url": "https://podcasters.apple.com/support/5593-how-to-publish-video",
        "claim": "Apple HLS needs a supporting host and API authorization.",
        "finding": "Apple documents rolling availability, show claim, API key and audio-only subscriptions; these support the reference distinctions.",
        "checked_at": "2026-11-23T16:50:32.860Z"
      },
      {
        "url": "https://podstandards.org/2026/08/11/podcast-hosting-platforms-and-apps-that-support-hls-video-in-rss/",
        "claim": "Open HLS RSS host/player statuses are attributed to PSP.",
        "finding": "September 2 list matches reported-live hosts, committed Buzzsprout/Spreaker, Amazon beta and iHeart manual submission; it is ecosystem reporting, not account tests.",
        "checked_at": "2026-11-23T16:50:33.125Z"
      },
      {
        "url": "https://support.pocketcasts.com/knowledge-base/video-podcasts/",
        "claim": "Pocket Casts streams feed video but downloads HLS episodes as audio.",
        "finding": "Official guide confirms MP4 and HLS across mobile/web/desktop and standard audio downloads; proprietary-only video is excluded.",
        "checked_at": "2026-11-23T16:50:33.907Z"
      },
      {
        "url": "https://creators.spotify.com/features/video",
        "claim": "Spotify native video differs from general RSS distribution.",
        "finding": "Official feature page explicitly says Creators or Megaphone uploads use Spotify native video and other platforms receive audio RSS.",
        "checked_at": "2026-11-23T16:50:49.147Z"
      },
      {
        "url": "https://support.megaphone.fm/en/articles/12043371-video-monetization",
        "claim": "Megaphone monetization is still described as an October 20 future launch.",
        "finding": "Current official text says currently available, not future launch; page retains an obsolete October 20 date-of-this-review sentence despite November 20 blanket row date.",
        "checked_at": "2026-11-23T16:50:49.753Z"
      },
      {
        "url": "https://www.buzzsprout.com/features/video-podcasting",
        "claim": "Buzzsprout video uses separate Apple, Spotify and YouTube connections.",
        "finding": "FAQ confirms Audio + Video plans, MP4/MOV to Apple HLS, Apple review/API key, Spotify approval and YouTube authorization.",
        "checked_at": "2026-11-23T16:50:50.068Z"
      },
      {
        "url": "https://rss.com/features/video-podcasting/",
        "claim": "RSS.com Max supports alternate enclosures but sends Spotify audio.",
        "finding": "Vendor explicitly confirms Max HLS Apple, Podcasting 2.0 alternate enclosures and YouTube; Spotify and Amazon receive audio feed.",
        "checked_at": "2026-11-23T16:50:50.272Z"
      },
      {
        "url": "https://transistor.fm/features/video/",
        "claim": "Transistor supports HLS RSS and labels unified analytics coming soon.",
        "finding": "Current page supports available video, HLS RSS and Apple hosting partnership; retrieved feature text no longer includes the cited coming-soon analytics phrase, so that specific status is unestablished.",
        "checked_at": "2026-11-23T16:51:43.012Z"
      },
      {
        "url": "https://libsyn.com/libsyn-podcast-hosting-features/",
        "claim": "Libsyn markets video publishing while Apple HLS is coming soon.",
        "finding": "Feature list confirms Apple HLS coming soon and plan-based Spotify/YouTube labels; explanatory YouTube section describes audio-to-video conversion, so full-motion YouTube transfer is not established by the same page.",
        "checked_at": "2026-11-23T16:51:43.288Z"
      },
      {
        "url": "https://www.acast.com/en/press-room/video-on-apple-podcasts-now-open-to-all",
        "claim": "Acast opens Apple video via a plan or partner manager.",
        "finding": "Launch statement explicitly describes Video plan and creator-network manager activation; it does not establish every other video destination.",
        "checked_at": "2026-11-23T16:51:43.528Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Full linked HLS distribution and feed metadata patterns were read for route scope and audio fallback.",
    "items": [
      {
        "path": "patterns/produce/recording/hls-video-podcast-distribution.md",
        "claim": "Video distribution needs destination compatibility and audio continuity.",
        "finding": "Pattern requires capable hosting, audio fallback, consent and cost check; reference complements this with host/app-specific restrictions and does not justify universal adoption.",
        "checked_at": "2026-11-23T16:52:32Z"
      },
      {
        "path": "patterns/publish/feed-metadata-standard.md",
        "claim": "Podcast feed metadata must remain useful inside listening apps.",
        "finding": "Pattern retains audio file and canonical link requirements; the reference distinguishes alternate video paths without removing audio continuity.",
        "checked_at": "2026-11-23T16:52:32Z"
      }
    ]
  }
}