---
description: "Rough cut production patterns for owned media. Real-time show production in OBS Studio with layouts, transitions, lower thirds, and simultaneous horizontal + vertical output."
---

# Rough Cut

**Stage:** Produce → Rough Cut

The rough cut is where raw recordings become a produced show. Using OBS Studio, a real-time producer assembles the show with camera layouts, lower thirds, transitions, graphics, intros/outros, and branded overlays — either live during the session or immediately after using the isolated recordings.

This is the phase that separates Riggg's production model from traditional post-production workflows. Instead of sending raw files to an editor and waiting days, the rough cut happens in real time with broadcast-quality results.

## What the Rough Cut Produces

| Output | Format | Purpose |
|---|---|---|
| **Horizontal rough cut** | 1920×1080 (16:9) | YouTube, website, podcast video, mastering input |
| **Vertical rough cut** | 1080×1920 (9:16) | Reels, Shorts, TikTok, vertical livestream, mastering input |

Both are created simultaneously using OBS + Aitum Vertical Canvas. No separate reformatting pass needed.

## Rough Cut Patterns

| Pattern | What It Covers | Score |
|---|---|---|
| [OBS Real-Time Production Standard](../obs-production-standard.md) | Workflow and methodology for producing shows live in OBS | 5 |
| [OBS Scene Collection Template](../obs-scene-collection-template.md) | Downloadable 157-scene template with 5-participant capacity and dual output | 5 |

## What Happens in the Rough Cut

1. **Layout switching** — Cut between 1-up, 2-up, 3-up, 4-up, and 5-up participant layouts based on who is speaking
2. **Lower thirds** — Show participant names, titles, and company branding on screen
3. **Transitions** — Smooth animated transitions between layouts (Move Transition, 600ms)
4. **Graphics** — Intro sequence, outro card, branded overlays, listen-on logos
5. **Screen share integration** — When participants share screens, the layout adapts
6. **Subtitle positioning** — Subtitle safe zones configured for both horizontal and vertical
7. **Ad break cards** — Branded top roll, mid roll, and post roll cards with waveform visualizers
8. **Deliverable generation** — Quote graphics and thumbnails created during the session using live design scenes
9. **Dual output** — Horizontal and vertical versions rendered simultaneously

## Quality Bar

- All participant camera sources are isolated individual feeds (not a mixed video call)
- Lower thirds show correct name, title, and company for each participant
- Transitions are smooth and consistent (600ms Move Transition standard)
- Both horizontal and vertical outputs are rendering
- Intro and outro sequences are branded and functional
- No audio issues (levels balanced, no echo, no clipping)
- Safe zones respected for subtitle and UI overlay areas
