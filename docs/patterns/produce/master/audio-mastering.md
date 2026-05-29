---
description: "Audio mastering standard for podcast distribution. Loudness normalization, noise reduction, EQ, and export specifications."
---

# Audio Mastering Standard

**Stage:** Produce → Master  
**Score:** 5  
**Evidence:** Podcast distribution standards, internal production data

## What It Is

The audio mastering pass that takes the rough cut audio and produces a distribution-ready podcast audio file meeting loudness, noise, and quality standards for Apple Podcasts, Spotify, and all major platforms.

## Target Specifications

| Parameter | Target | Tolerance |
|---|---|---|
| **Integrated loudness** | -16 LUFS | ±1 LUFS |
| **True peak** | -1.5 dBTP | Must not exceed -1.0 dBTP |
| **Noise floor** | Below -50dB | Below -40dB minimum |
| **Sample rate** | 48 kHz | 44.1 kHz acceptable |
| **Bit depth** | 16-bit (MP3) or 24-bit (WAV) | — |
| **Channels** | Stereo (joint stereo for MP3) | Mono acceptable for speech-only |
| **Format** | MP3 CBR 192kbps (distribution) or WAV (archive) | MP3 128kbps minimum |

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
- File validates on Spotify loudness checker and Apple Podcasts requirements

## Platform Requirements

| Platform | Loudness | Format | Max File Size |
|---|---|---|---|
| Apple Podcasts | -16 LUFS recommended | MP3, M4A, MOV | 2 GB |
| Spotify | -14 to -16 LUFS (normalized to -14) | MP3, OGG (converted) | Via RSS |
| YouTube (audio) | -14 LUFS (normalized) | Extracted from video | N/A |
| Amazon Music | -16 LUFS | MP3 | Via RSS |
| RSS (general) | -16 LUFS standard | MP3 CBR preferred | Host-dependent |

_Last verified: May 2026._
