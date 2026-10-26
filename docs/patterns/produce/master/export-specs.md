---
description: "Export specifications for owned media deliverables. Platform-specific video, audio, and image export settings."
---

# Export Specifications

Working export presets for common video, audio and image deliverables. Start with the destination and aspect ratio; distinguish workflow presets from platform upload limits.

**Stage:** Produce → Master  
**Score:** 4  
**Evidence:** Platform documentation

## What It Is

Working export presets for common video, audio and image deliverables. Choose a preset, check the current destination limits and test a representative export before rendering the whole batch.

## Video Export Specs

Resolution, codec and bitrate below are starting presets, not platform mandates. The 30fps examples assume a 30fps source; keep the source frame rate unless your delivery brief requires a conversion. Maximum size and duration depend on the account and upload route.

### Horizontal (16:9)

| Platform | Resolution | Codec | Bitrate | Frame Rate | Container | Max Size |
|---|---|---|---|---|---|---|
| YouTube | 1920×1080 | H.264 | 12-15 Mbps | 30fps | MP4 | 256 GB or 12 hours, whichever is less |
| LinkedIn | 1920×1080 | H.264 | 10-15 Mbps | 30fps | MP4 | 5 GB |
| Facebook | 1920×1080 | H.264 | 10-15 Mbps | 30fps | MP4 | Check current upload route |
| Twitter/X | 1920×1080 | H.264 | 6-10 Mbps | 30fps | MP4 | Check account/upload route |
| Website | 1920×1080 | H.264/H.265 | 8-12 Mbps | 30fps | MP4 | Host-dependent |
| Podcast (video) | 1920×1080 | H.264 | 8-12 Mbps | 30fps | MP4/MOV | Check podcast host |

### Vertical (9:16)

| Platform | Resolution | Codec | Max Duration | Frame Rate | Max Size |
|---|---|---|---|---|---|
| Instagram Reels | 1080×1920 | H.264 | Check current account/upload route | 30fps | Check current upload route |
| YouTube Shorts | 1080×1920 | H.264 | 3min (eligible square/vertical uploads) | 30fps | N/A |
| TikTok | 1080×1920 | H.264 | Check recording versus upload route | 30fps | Check current upload route |
| LinkedIn | 1080×1920 | H.264 | 15min | 30fps | 5 GB |
| Facebook Reels | 1080×1920 | H.264 | No universal 90s cap in the new unified video flow | 30fps | Check current upload route |

[YouTube documents Shorts up to three minutes](https://support.google.com/youtube/answer/15424877) for eligible square or vertical uploads. Shorts over one minute with an active Content ID claim are blocked globally. Other platform limits in this table still require destination-specific revalidation.

### Check the destination before batch export

- [YouTube upload limits](https://support.google.com/youtube/answer/71673): 256 GB or 12 hours, whichever is less; accounts need verification for videos longer than 15 minutes. [Encoding recommendations](https://support.google.com/youtube/answer/1722171) use the source frame rate and suggested variable bitrates. The higher-bitrate examples here are working presets, not upload requirements.
- [LinkedIn video requirements](https://www.linkedin.com/help/linkedin/answer/a548377): up to 15 minutes and 5 GB. Check the same upload route you will use for release.
- [Meta's unified Facebook video/Reels flow](https://about.fb.com/news/2025/06/making-it-easier-create-videos-facebook/) removes length/format restrictions as it rolls out. That is not a promise of unlimited file size.
- For Instagram, TikTok, X and podcast hosts, verify current limits in the target account before committing to the full render. Record the destination, account/route, date checked and one successful sample upload. Do not substitute a filming limit for an upload limit.

## Audio Export Specs

| Deliverable | Format | Bitrate | Sample Rate | Channels | Loudness |
|---|---|---|---|---|---|
| Podcast (RSS) | MP3 CBR | 192 kbps | 48 kHz | Stereo | -16 LUFS |
| Podcast (archive) | WAV | Lossless | 48 kHz | Stereo | -16 LUFS |
| Video embedded | AAC | 256 kbps | 48 kHz | Stereo | -16 LUFS |
| Audiogram | MP3/AAC | 192 kbps | 48 kHz | Stereo | -16 LUFS |

## Image Export Specs

| Deliverable | Size | Format | Color Space |
|---|---|---|---|
| YouTube thumbnail | 1280×720 | JPEG/PNG | sRGB |
| Podcast app thumbnail | 3000×3000 | JPEG/PNG | sRGB |
| Quote graphic (square) | 1080×1080 | PNG | sRGB |
| Quote graphic (landscape) | 1920×1080 | PNG | sRGB |
| Quote graphic (story) | 1080×1920 | PNG | sRGB |
| OG image | 1200×630 | JPEG/PNG | sRGB |

## Recommended Export Presets

### DaVinci Resolve

```
Horizontal Master:
  Format: MP4
  Codec: H.264
  Resolution: 1920×1080
  Frame Rate: 30fps
  Quality: Restrict to 15,000 kbps
  Audio: AAC 256kbps

Vertical Master:
  Format: MP4
  Codec: H.264
  Resolution: 1080×1920
  Frame Rate: 30fps
  Quality: Restrict to 12,000 kbps
  Audio: AAC 256kbps

Podcast Audio:
  Format: MP3
  Bitrate: 192 kbps CBR
  Sample Rate: 48,000 Hz
```

### Adobe Premiere Pro

```
Horizontal Master:
  Preset: H.264 → YouTube 1080p HD
  Adjust: CBR 15 Mbps, Audio AAC 256kbps

Vertical Master:
  Preset: H.264 → Custom
  Resolution: 1080×1920
  Adjust: CBR 12 Mbps, Audio AAC 256kbps
```

_Legacy source/spec snapshot: May 2026 (date retained from the original reference; not a current fact-check). Platform specs change — verify before relying on edge cases._
