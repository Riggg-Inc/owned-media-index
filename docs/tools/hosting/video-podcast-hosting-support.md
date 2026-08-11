# Video Podcast Hosting — Platform Support Reference

**Last updated:** 2026-08-11
**Next review due:** 2026-09-20 (monthly — Sentinel maintains this)
**Note:** This field moves fast. Verify platform docs directly before committing to a hosting decision.

## What "supported" means here

A platform is listed as Confirmed Support when it can: (1) host/serve video files, (2) output RSS with video `<enclosure>` tags or `podcast:alternateEnclosure`, and (3) that feed is accepted by major apps (Apple Podcasts, Pocket Casts, Spotify open RSS).

---

## ✅ Confirmed Support

| Platform | Notes |
|---|---|
| **Buzzsprout** | Added video hosting + RSS video enclosure, 2026 |
| **Acast** | Expanded video distribution with RSS support, 2026. Weekly-session uplift claim is vendor self-report — no third-party benchmark |
| **CoHost** | Added full video support, 2026 |
| **iHeart** | Added RSS/HLS video support, 2026 |
| **Spotify for Podcasters** (formerly Anchor) | Native video in Spotify app since ~2024–25; RSS video enclosure for third-party apps is partial/limited — feeds Spotify-side playback better than open ecosystem |
| **Podbean** | Long-standing video hosting; one of the earlier adopters pre-2024 |

---

## 📱 Players / Apps (not hosting platforms — relevant for RSS video compatibility)

| App | Notes |
|---|---|
| **Apple Podcasts** | Supports video podcast spec; expanded 2024 |
| **Pocket Casts** | Expanded RSS/HLS video playback, 2026 |
| **Spotify** | Video playback for Spotify-hosted shows (not open RSS) |

---

## ❓ Status Unclear / Needs Verification

| Platform | Notes |
|---|---|
| **Transistor** | Audio-first; no public video announcement as of 2026-08 |
| **Captivate** | Expressed interest; no shipping date announced |
| **Castos** | WordPress-integrated host; no known video roadmap |
| **RSS.com** | Unverified; needs direct documentation check |
| **Spreaker** | Not tracked yet |

---

## ❌ No Known Video Support / Audio-Only

| Platform | Notes |
|---|---|
| **Simplecast** (Spotify-owned) | Audio-focused; no public announcement as of 2026-08 |
| **Libsyn** | Traditional audio; no known video push as of 2026-08 |
| **Megaphone** (Spotify-owned, enterprise) | No public video announcement as of 2026-08 |
| **Omny Studio** (Triton Digital, enterprise) | No known video capability as of 2026-08 |

---

## Related Patterns

- `publish/rss/feed-metadata-standard.md`
- `produce/recording/hls-video-podcast-distribution.md`
