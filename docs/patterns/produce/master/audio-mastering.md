---
description: "Audio mastering standard for podcast distribution. Loudness normalization, noise reduction, EQ, and export specifications."
---

# Audio Mastering Standard

The audio mastering pass that takes the rough cut audio and produces a podcast audio master with consistent loudness and clear speech, ready for destination-specific delivery checks. Use the targets as production settings, then check destination requirements and listen to the complete result.

**Stage:** Produce → Master  
**Score:** 5  
**Evidence:** Podcast distribution standards, internal production data

## What It Is

The audio mastering pass that takes the rough cut audio and produces a podcast audio master with consistent loudness and clear speech, ready for destination-specific delivery checks.

## Target Specifications

| Parameter | Target | Tolerance |
|---|---|---|
| **Integrated loudness** | -16 LUFS | ±1 LUFS |
| **True peak** | -1.5 dBTP | Must not exceed -1.0 dBTP |
| **Noise during pauses** | No distracting noise at normal listening level | Use a digital full-scale (dBFS) meter to track changes; listen for gating artifacts |
| **Sample rate** | 48 kHz | 44.1 kHz acceptable |
| **Bit depth** | 24-bit PCM WAV for archive; MP3 uses bitrate, not PCM bit depth | — |
| **Channels** | Stereo (joint stereo for MP3) | Mono acceptable for speech-only |
| **Format** | MP3 CBR 192kbps (distribution) or WAV (archive) | MP3 128kbps minimum |

The settings below are starting points: adjust them to the voice and recording, then listen at normal speed. Keep an unprocessed copy.

## Mastering Chain

```
Raw audio tracks (per participant)
    │
    ├─ 1. Noise reduction (gate + spectral denoise)
    ├─ 2. EQ (high-pass 80Hz, presence boost 2-5kHz, de-mud 200-400Hz)
    ├─ 3. Compression (2:1-4:1 ratio, -18dB threshold, fast attack)
    ├─ 4. De-essing (if needed, 4-8kHz range)
    ├─ 5. Filler word removal (optional, via Descript or manual)
    ├─ 6. Loudness normalization (-16 LUFS integrated)
    ├─ 7. True peak limiting (-1.5 dBTP)
    └─ 8. Export
```

## Quick-Path: Automated Mastering

For faster turnaround, these tools handle most of the chain automatically:

| Tool | What It Does | When To Use |
|---|---|---|
| **Auphonic** | Loudness normalization, noise reduction, leveling — all automated | Standard episodes with clean recordings |
| **Descript Studio Sound** | One-click cleanup: noise, echo, leveling | Quick-turn episodes |
| **Adobe Podcast (Enhance)** | AI-powered voice enhancement | Problematic recordings needing rescue |

## Quality Bar

- Loudness measures -16 LUFS (±1) on integrated measurement
- No audible background noise during pauses
- No clipping or distortion
- Speaker levels balanced (no participant significantly louder than others)
- No plosives, sibilance, or mouth sounds distracting from content
- Measure integrated loudness and true peak after the final encode; listen to the entire result at normal speed
- Test the final file through the intended host or upload route before release

## Platform Requirements

For matching audio, video and image export settings by deliverable, see [Export Specifications](export-specs.md).

Use the -16 LUFS stereo target above as a production default, not a universal RSS or platform mandate. [Apple recommends approximately -16 LUFS (±1) with true peak no higher than -1 dBTP](https://podcasters.apple.com/support/893-audio-requirements). Its RSS audio guidance accepts MP3 or AAC; subscriber uploads have separate requirements.

[Audacity's MP3 guidance](https://manual.audacityteam.org/man/mp3_export_options.html) includes 192 kbps stereo CBR as a podcast preset. Keep a lossless WAV archive and make the delivery copy required by your host.

For Spotify, YouTube and Amazon destinations, check the podcast or video upload route you actually use. Spotify's [music normalization documentation](https://support.spotify.com/us/artists/article/loudness-normalization/) describes songs and albums; do not treat it as a podcast upload requirement. Measure your own finished file rather than depending on playback normalization to repair uneven speech.

_Legacy source/spec snapshot: May 2026 (date retained from the original reference; not a current fact-check). Recheck current source documentation before relying on these specifications._
