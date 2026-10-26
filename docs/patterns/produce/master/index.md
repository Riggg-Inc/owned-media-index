---
description: "Mastering patterns for owned media production. Final polish for horizontal video, vertical video, and podcast audio. Tools, standards, and export specs."
---

# Master

**Stage:** Produce → Master

Mastering is the final production phase. The rough cut arrives as a produced show with layouts, graphics, and transitions already in place. The mastering editor polishes — fixing imperfections, balancing audio, color correcting, trimming dead air, and exporting to final deliverable formats.

Mastering should be fast because the rough cut did the heavy lifting. If it runs long, check whether upstream fixes would help; restoration, accessibility and creative work can legitimately need more time.

## What Mastering Produces

| Deliverable | Format | Specs | Purpose |
|---|---|---|---|
| **Mastered horizontal video** | MP4 (H.264/H.265) | 1920×1080, 30fps | YouTube, website, podcast video |
| **Mastered vertical video** | MP4 (H.264/H.265) | 1080×1920, 30fps | Reels, Shorts, TikTok, vertical social |
| **Mastered podcast audio** | MP3 or WAV | 48kHz, stereo, -16 LUFS | Apple Podcasts, Spotify, RSS distribution |
| **Mastered clips** (optional) | MP4 | H/V variants per clip | Social distribution |

## Mastering Patterns

| Pattern | What It Covers | Score |
|---|---|---|
| [Video Mastering Standard](video-mastering.md) | Final edit, color, pacing, and export for horizontal + vertical video | 5 |
| [Audio Mastering Standard](audio-mastering.md) | Loudness, noise reduction, EQ, and export for podcast audio | 5 |
| [Export Specifications](export-specs.md) | Platform-specific export settings for every distribution target | 4 |

## Mastering Tools

Choose tools by the work you need to finish. Prices and AI allowances vary by edition, billing plan and region; check the current plan before purchasing. Keep a short test project to confirm the required export and caption features.

### Video Editing / NLE

| Tool | Best For | Price | Platform |
|---|---|---|---|
| **DaVinci Resolve** | Full mastering: edit, color, audio, effects. Industry standard for color grading. | Free / paid Studio; [current edition pricing](https://www.blackmagicdesign.com/products/davinciresolve) | Win, Mac, Linux |
| **Adobe Premiere Pro** | Established NLE with broad plugin ecosystem | Check current Premiere plan | Win, Mac |
| **Final Cut Pro for Mac** | Fast rendering, native Mac optimization | $299.99 one-time Mac option; [other plans](https://www.apple.com/final-cut-pro/) | Mac only |
| **CapCut (Desktop)** | Fast, simple edits; check current auto-caption entitlement | Free / paid features | Win, Mac |
| **Descript** | Transcript-based editing, filler word removal, studio sound | [Current plans and allowances](https://www.descript.com/pricing) | Win, Mac |

### Audio Processing

| Tool | Best For | Price | Platform |
|---|---|---|---|
| **DaVinci Resolve Fairlight** | Integrated audio mastering within the NLE | Included in Resolve | Win, Mac, Linux |
| **Adobe Audition** | Dedicated audio cleanup, noise reduction, mastering | Check that your Adobe subscription includes Audition | Win, Mac |
| **Descript Studio Sound** | Audio cleanup and leveling | Plan and AI allowance dependent | Win, Mac |
| **Auphonic** | Automated loudness normalization, noise reduction, leveling | [Current credits and plans](https://auphonic.com/pricing) | Web |
| **iZotope RX** | Professional noise reduction, de-reverb, de-click | Check current RX edition and price | Win, Mac |

### Auto-Captioning

| Tool | Best For | Price |
|---|---|---|
| **CapCut** | Auto-captions and templates; check current plan | Plan-dependent |
| **Descript** | Transcript-based captions with word-level timing | [Current plans and allowances](https://www.descript.com/pricing) |
| **Premiere Pro (Speech to Text)** | Native captioning within Adobe ecosystem | Included |
| **DaVinci Resolve (Subtitle tools)** | SRT import/export and subtitle editing; check edition for automatic transcription | Edition-dependent |

## Mastering Workflow

```
Rough Cut (H + V) arrives
    │
    ├─→ Video Master
    │     ├─ Trim dead air / pauses
    │     ├─ Fix any layout errors from rough cut
    │     ├─ Color correction / grading
    │     ├─ Add burned-in captions (vertical version)
    │     ├─ Export horizontal master (1920×1080)
    │     └─ Export vertical master (1080×1920)
    │
    ├─→ Audio Master
    │     ├─ Noise reduction
    │     ├─ EQ and compression
    │     ├─ Loudness normalization (-16 LUFS)
    │     ├─ Remove filler words (optional)
    │     └─ Export podcast audio (MP3/WAV)
    │
    └─→ Clip Extraction (optional)
          ├─ Identify clip moments (Hot Take, Golden Nugget, etc.)
          ├─ Export H + V clip variants
          └─ Add burned-in captions to clips
```

## Quality Bar

- **Video:** No visible compression artifacts, consistent color, smooth transitions
- **Audio:** Loudness at -16 LUFS (±1), no distracting background noise at normal listening level, no clipping
- **Captions:** Burned-in readable captions on vertical exports so the message works without sound
- **Sync:** Audio and video perfectly synced across all exports
- **Formats:** All exports match platform-specific specs (see [Export Specifications](export-specs.md))
- **Turnaround:** Aim to keep routine mastering shorter than the rough cut; do not rush required repairs. Use same-day or next-day delivery as a planning target when the source and scope allow it.

## Selection Guide

| Need | Choose | Selection consideration |
|---|---|---|
| Finish picture and pacing | [Video Mastering](video-mastering.md) | Apply final edits and color work to video deliverables. |
| Finish sound | [Audio Mastering](audio-mastering.md) | Address loudness, noise, and EQ for podcast audio. |
| Deliver compatible files | [Export Specifications](export-specs.md) | Check the target format after finishing; export settings do not replace mastering. |
