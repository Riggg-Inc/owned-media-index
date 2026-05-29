---
description: "Recording methods for owned media production. Remote recording platforms, in-studio capture, isolated tracks, and source quality standards."
---

# Record

**Stage:** Produce → Record

Recording is the capture phase — getting the raw source material from each participant in the highest quality possible. The recording method determines the ceiling for everything downstream. You cannot fix a bad recording in the rough cut or master.

## Two Recording Models

### Remote Recording

Each participant records from their own location. The platform captures **isolated video and audio tracks per person** — not a single mixed video call recording.

This is the dominant model for podcasts, webinars, and distributed expert interviews.

| Method | What It Captures | Quality Ceiling |
|---|---|---|
| **Riverside.fm** | Isolated video + audio per participant, local recording, up to 4K | High — local recording avoids compression artifacts |
| **SquadCast** | Isolated audio + video per participant, progressive upload | High — progressive upload prevents data loss |
| **Zoom (local recording)** | Separate audio tracks per participant, gallery/speaker video | Medium — video is compressed, audio is usable |
| **Zoom (cloud recording)** | Mixed video + separate audio | Low-Medium — cloud video is heavily compressed |
| **StreamYard** | Mixed composite video only | Low — no isolated tracks, limited post-production flexibility |
| **Google Meet / Teams** | Single mixed recording | Low — no isolation, compressed, limited control |

### In-Studio Recording

All participants are physically present. Capture happens via cameras, audio interfaces, and local recording hardware.

| Method | What It Captures | Quality Ceiling |
|---|---|---|
| **Multi-camera + audio interface** | Individual camera feeds per person + isolated XLR audio | Highest — full control over every source |
| **Single camera (wide shot)** | One video with all participants in frame | Medium — no per-person framing, limits post-production layouts |
| **Single camera + separate audio** | One wide video + isolated audio per person via mixer/interface | Medium-High — audio is flexible, video is fixed |

## Why Isolated Tracks Matter

If you record a single mixed video (like a Zoom gallery view), the rough cut editor cannot:

- Switch between speaker close-ups
- Create 1-up, 2-up, or multi-camera layouts
- Crop or reframe individual participants
- Create vertical versions with per-person framing
- Generate headshot-based thumbnails or quote graphics

**Isolated tracks per participant = full creative control in the rough cut.** This is non-negotiable for broadcast-quality production.

## Recording Patterns

| Pattern | Best For | Score |
|---|---|---|
| [Remote Isolated Recording](remote-isolated.md) | Distributed teams, guest interviews, most podcast/webinar use cases | 5 |
| [In-Studio Multi-Camera](in-studio-multi-camera.md) | High-production shows, recurring studio programs | 5 |
| [Hybrid Recording](hybrid-recording.md) | Host in-studio + remote guests, mixed environments | 4 |

## Quality Bar

- **Video:** Minimum 1080p per participant. 4K preferred for crop flexibility.
- **Audio:** Minimum 48kHz/16-bit WAV or equivalent. No compressed-only formats.
- **Isolation:** One video file AND one audio file per participant. No mixed recordings.
- **Backup:** Platform must support local recording or progressive upload as a safety net.
- **Sync:** All tracks must be sync-able via timecode, clap, or platform-native sync.

## Platform Constraints

| Platform | Isolated Video | Isolated Audio | Max Resolution | Local Recording | Max Participants |
|---|---|---|---|---|---|
| Riverside.fm | ✅ | ✅ | 4K | ✅ | 10 |
| SquadCast | ✅ | ✅ | 1080p | ✅ (progressive) | 10 |
| Zoom (local) | ❌ (gallery only) | ✅ (separate tracks) | 1080p | ✅ | 1000 |
| StreamYard | ❌ | ❌ | 1080p | ❌ | 10 |
| Zencastr | ✅ | ✅ | 1080p | ✅ | 15 |
| Remotely.fm | ✅ | ✅ | 4K | ✅ | 8 |

_Last verified: May 2026._
