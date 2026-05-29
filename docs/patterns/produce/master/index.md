---
description: "Mastering patterns for owned media production. Final polish for horizontal video, vertical video, and podcast audio. Tools, standards, and export specs."
---

# Master

**Stage:** Produce → Master

Mastering is the final production phase. The rough cut arrives as a produced show with layouts, graphics, and transitions already in place. The mastering editor polishes — fixing imperfections, balancing audio, color correcting, trimming dead air, and exporting to final deliverable formats.

Mastering should be fast because the rough cut did the heavy lifting. If mastering takes longer than the rough cut, something went wrong upstream.

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

### Video Editing / NLE

| Tool | Best For | Price | Platform |
|---|---|---|---|
| **DaVinci Resolve** | Full mastering: edit, color, audio, effects. Industry standard for color grading. | Free / $295 (Studio) | Win, Mac, Linux |
| **Adobe Premiere Pro** | Established NLE with broad plugin ecosystem | $22.99/mo | Win, Mac |
| **Final Cut Pro** | Fast rendering, native Mac optimization | $299.99 (one-time) | Mac only |
| **CapCut (Desktop)** | Fast, simple edits with good auto-caption support | Free | Win, Mac |
| **Descript** | Transcript-based editing, filler word removal, studio sound | $24/mo+ | Win, Mac |

### Audio Processing

| Tool | Best For | Price | Platform |
|---|---|---|---|
| **DaVinci Resolve Fairlight** | Integrated audio mastering within the NLE | Included in Resolve | Win, Mac, Linux |
| **Adobe Audition** | Dedicated audio cleanup, noise reduction, mastering | Included with Premiere | Win, Mac |
| **Descript Studio Sound** | One-click audio cleanup and leveling | Included with Descript | Win, Mac |
| **Auphonic** | Automated loudness normalization, noise reduction, leveling | Free (2hrs/mo) / $11/mo | Web |
| **iZotope RX** | Professional noise reduction, de-reverb, de-click | $129+ | Win, Mac |

### Auto-Captioning

| Tool | Best For | Price |
|---|---|---|
| **CapCut** | Fast auto-captions with style templates | Free |
| **Descript** | Transcript-based captions with word-level timing | $24/mo+ |
| **Premiere Pro (Speech to Text)** | Native captioning within Adobe ecosystem | Included |
| **DaVinci Resolve (Subtitle tools)** | SRT import/export, manual and auto | Included |

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
- **Audio:** Loudness at -16 LUFS (±1), noise floor below -50dB, no clipping
- **Captions:** Burned-in captions on all vertical video (80%+ watched without sound)
- **Sync:** Audio and video perfectly synced across all exports
- **Formats:** All exports match platform-specific specs (see [Export Specifications](export-specs.md))
- **Turnaround:** Mastering should take less time than the rough cut. Target: same day or next day.
