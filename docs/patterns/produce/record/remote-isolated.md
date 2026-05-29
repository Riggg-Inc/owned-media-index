---
description: "Remote isolated recording pattern for podcasts and webinars. Each participant captures locally with isolated video and audio tracks."
---

# Remote Isolated Recording

**Stage:** Produce → Record  
**Score:** 5  
**Evidence:** Internal production data (500+ sessions)

## What It Is

Each participant records from their own location using a platform that captures isolated video and audio tracks per person. The raw files are individual — one video file and one audio file per participant — not a mixed composite of the call.

## Why It Works

Remote isolated recording solves the core problem of distributed production: participants are in different locations, on different hardware, with different internet connections. By recording locally on each participant's machine and uploading the raw files, you bypass call compression entirely.

The result: studio-quality source material from a Zoom-like experience.

## Recommended Platforms

| Platform | Why | Link |
|---|---|---|
| **Riverside.fm** | Best combination of quality (up to 4K), reliability, and local recording. Industry standard for remote podcast recording. | [riverside.fm](https://riverside.fm) |
| **SquadCast** | Strong alternative with progressive upload (no data loss on disconnect). Owned by Descript. | [squadcast.fm](https://squadcast.fm) |

## Setup Checklist

- [ ] Participant has stable internet (wired preferred)
- [ ] Participant uses Chrome or supported browser
- [ ] External microphone connected (not laptop mic)
- [ ] Camera at eye level, good lighting
- [ ] Quiet environment, minimal background noise
- [ ] Local recording enabled in platform settings
- [ ] Test recording completed before the session
- [ ] Backup recording method identified (phone recording, secondary device)

## Quality Bar

- 1080p minimum video per participant
- 48kHz/16-bit minimum audio
- Local recording enabled (not cloud-only)
- Each participant's files downloadable as separate tracks
- Audio and video sync verified post-download

## When Not To Use

When all participants are in the same physical location — use [In-Studio Multi-Camera](in-studio-multi-camera.md) instead for higher quality and more control.

## Prompt Template

```
Create a guest preparation email for a remote isolated recording session.

Session details:
- Platform: [Riverside.fm / SquadCast]
- Date and time: [date, time, timezone]
- Expected duration: [minutes]
- Host name: [name]
- Show name: [name]

Include:
1. Platform join link and any account setup instructions
2. Technical requirements (browser, microphone, camera, internet)
3. Environment tips (lighting, background, noise)
4. What to expect during the session
5. Backup plan if technical issues arise
```
