---
description: "Export specifications for owned media deliverables. Platform-specific video, audio, and image export settings."
---

# Export Specifications

**Stage:** Produce → Master  
**Score:** 4  
**Evidence:** Platform documentation

## What It Is

A reference table of export settings for every deliverable format across every major distribution platform. Use this to ensure your mastered files meet platform requirements on the first export.

## Video Export Specs

### Horizontal (16:9)

| Platform | Resolution | Codec | Bitrate | Frame Rate | Container | Max Size |
|---|---|---|---|---|---|---|
| YouTube | 1920×1080 | H.264 | 12-15 Mbps | 30fps | MP4 | 256 GB |
| LinkedIn | 1920×1080 | H.264 | 10-15 Mbps | 30fps | MP4 | 5 GB |
| Facebook | 1920×1080 | H.264 | 10-15 Mbps | 30fps | MP4 | 10 GB |
| Twitter/X | 1920×1080 | H.264 | 6-10 Mbps | 30fps | MP4 | 512 MB |
| Website | 1920×1080 | H.264/H.265 | 8-12 Mbps | 30fps | MP4 | Host-dependent |
| Podcast (video) | 1920×1080 | H.264 | 8-12 Mbps | 30fps | MP4/MOV | 2 GB |

### Vertical (9:16)

| Platform | Resolution | Codec | Max Duration | Frame Rate | Max Size |
|---|---|---|---|---|---|
| Instagram Reels | 1080×1920 | H.264 | 90s | 30fps | 4 GB |
| YouTube Shorts | 1080×1920 | H.264 | 60s | 30fps | N/A |
| TikTok | 1080×1920 | H.264 | 10min | 30fps | 4 GB |
| LinkedIn | 1080×1920 | H.264 | 10min | 30fps | 5 GB |
| Facebook Reels | 1080×1920 | H.264 | 90s | 30fps | 4 GB |

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

_Last verified: May 2026. Platform specs change — verify before relying on edge cases._
