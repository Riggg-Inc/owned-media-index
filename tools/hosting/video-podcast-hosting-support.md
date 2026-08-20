# Video Podcast Hosting — Platform Support Reference

**Last updated:** 2026-08-20
**Next review due:** 2026-09-20 (monthly — Sentinel maintains this)
**Note:** This field moves fast. Verify platform docs directly before committing to a hosting decision.

## What "supported" means here

A platform is listed as Confirmed Support when it can: (1) host/serve video files, (2) output RSS with video `<enclosure>` tags or `podcast:alternateEnclosure`/HLS for compatible podcast apps, and (3) preserve audio fallback while supporting Apple/Spotify through direct or approved integrations where required.

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
| **Transistor** | Listed by Podcast Standards Project as publishing HLS video via `podcast:alternateEnclosure`; official feature page says rollout/early access is gradual — verify account availability, checked 2026-08-20 |
| **Captivate** | Listed by Podcast Standards Project as publishing HLS video via `podcast:alternateEnclosure`; official feature matrix does not surface video controls prominently — verify tenant availability, checked 2026-08-20 |
| **RSS.com** | Official docs say video episodes play on Apple Podcasts, Podcasting 2.0 apps, RSS.com pages, and YouTube; feed uses alternate enclosure, checked 2026-08-20 |
| **Omny Studio** (Triton Digital, enterprise) | Official docs support optional video podcasting; RSS feeds can include MP4 and HLS alternate enclosures, checked 2026-08-20 |
| **Flightcast** | Newer video podcast hosting platform; official site says upload video once and publish everywhere, and Podcast Standards lists HLS video in RSS, checked 2026-08-20 |
| **Podigee** | Supports audio/video podcast workflows and video minutes; Podcast Standards lists HLS video in RSS, checked 2026-08-20 |
| **Beamly** | Audio/video podcast hosting with cross-platform distribution; Podcast Standards lists HLS video in RSS, checked 2026-08-20 |
| **Fountain** | Podcast Standards lists Fountain as an HLS-in-RSS host and compatible app, checked 2026-08-20 |
| **True Fans** | Podcast Standards lists True Fans as an HLS-in-RSS host and compatible app, checked 2026-08-20 |

---

## 📱 Players / Apps (not hosting platforms — relevant for RSS video compatibility)

| App | Notes |
|---|---|
| **Apple Podcasts** | Supports video podcasts; currently relies on Apple-side HLS/API approval rather than consuming RSS alternate-enclosure HLS directly |
| **Pocket Casts** | Supports HLS video playback from RSS |
| **Fountain** | Supports HLS video playback from RSS |
| **True Fans** | Supports HLS video playback from RSS |
| **Podcast Guru** | Supports HLS video playback from RSS |
| **Podcast Addict** | Supports HLS video playback from RSS |
| **Amazon Music** | Limited HLS video playback support |
| **iHeart** | Limited HLS video playback support |
| **Spotify** | Video playback for Spotify-hosted or directly integrated shows; does not read open-RSS video |

---

## ❓ Status Unclear / Needs Verification

| Platform | Notes |
|---|---|
| **Castos** | Official docs support YouTube republishing and uploaded video passthrough to YouTube, but no HLS/RSS video enclosure support found; checked 2026-08-20 |
| **Libsyn** | Official feature page now includes audio/video hosting plus Spotify and YouTube video distribution; Apple HLS is marked "Coming Soon" and open RSS/HLS is not confirmed, checked 2026-08-20 |
| **Spreaker** | Podcast Standards says Spreaker has committed to HLS video in RSS, but current help docs still describe audio uploads only; not shipped as of 2026-08-20 |

---

## ❌ No Known Video Support / Audio-Only

| Platform | Notes |
|---|---|
| **Simplecast** (SiriusXM-owned) | Audio-focused hosting/analytics pages; no public HLS/RSS video announcement found as of 2026-08-20 |
| **Megaphone** (Spotify-owned, enterprise) | No public video announcement as of 2026-08 |

---

## Related Patterns

- `publish/rss/feed-metadata-standard.md`
- `produce/recording/hls-video-podcast-distribution.md`
