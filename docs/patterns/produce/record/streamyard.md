---
description: "This StreamYard pattern evaluates a composite-only livestream workflow: recording the finished layout rather than editable per-person sources."
---

# StreamYard

This StreamYard pattern evaluates a composite-only livestream workflow: recording the finished layout rather than editable per-person sources. Use a composite-only workflow when the live layout is the final product; verify local-track options when participant-level editing is required.

**Stage:** Produce → Record  
**Score:** 2  
**Evidence:** Platform documentation, practitioner observation

**Capability caveat:** StreamYard’s [local-recording documentation](https://support.streamyard.com/hc/en-us/articles/10725401176596-Local-Recording-of-your-Live-Stream) describes individual video and audio tracks. Its indexed official documentation contradicts a product-wide “no isolated tracks” claim. The score and rationale below are retained for the composite-only workflow, not as an assessment of every current recording mode. Confirm current plan, settings, and upload completion with a test recording.

## What It Is

StreamYard is a browser-based live streaming and recording platform. In the composite-only workflow evaluated here, the recording contains the participant layout, branding, and overlays baked into one video.

## Why It Gets a 2

The composite-only workflow produces a **single mixed composite** — that file alone does not isolate participants for post-production. The video has StreamYard's layout baked in, which means you cannot reframe, re-layout, or produce the show differently after the fact.

It is included in the Index because many teams use it and need to understand its limitations.

## What You Get

| Output | Quality | Isolated? |
|---|---|---|
| Video (composite) | Up to 1080p | ❌ Single mixed file with layout baked in |
| Audio | Compressed, mixed | ❌ No separate tracks |

## When To Use

- Quick livestreams where production quality is secondary to going live fast
- Shows where the StreamYard layout is the final product (no post-production)
- Teams with zero technical capability for OBS or dedicated recording platforms

## When Not To Use

- Any show that requires post-production editing of individual participants
- Any show that needs per-person framing for clips, reels, or thumbnails
- Any production workflow that feeds into a rough cut stage
- When you need separate audio tracks for podcast mastering
- When you need both horizontal and vertical output

## The Core Limitation

A StreamYard composite records what the audience sees. If you stream a 2-up layout, that is the only view available from the composite file unless separate tracks were also captured. You cannot go back and create a 1-up close-up of the guest, extract a vertical clip with different framing, or add different lower thirds. The production decisions are permanent at the moment of recording.

This is the fundamental difference between StreamYard and the isolated recording + OBS rough cut workflow: **A composite-only recording locks layout decisions at capture time. Isolated recording keeps them open.**
