# Whole-page quality review: patterns/produce/record/in-studio-multi-camera.md
Completed 2026-10-30T16:51:59Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: e20cf62b8afe73d21127c213fd9ac5b08891ed7498fca61d7f409a43f50c2d42
Outcome: needs_revision; not human signoff.
## usefulness — pass
Clearly serves co-located producers needing lighting, sound and framing control. Starter/professional equipment examples and isolated-feed quality checks provide concrete planning help.
## substance — pass
Two equipment tables distinguish entry and professional setups, with camera, mic, interface, capture, lighting and acoustics roles. Individual-feed and lighting checks are useful detail, not fluff.
## coherence — needs_revision
The professional table offers 2-3 cameras and 2-5 microphones, but the definition and Quality Bar require an individual camera feed per participant. Those quantities only support that requirement for some group sizes; size the example per participant or explicitly describe the two-person-plus-wide baseline.
## cross_page_consistency — pass
The recording hub advocates isolated participant feeds and remote guide directs co-located participants to studio capture. This page links back to remote for distributed guests and rough cut for composition, preserving the intended stage boundary.
## reasonable_claims — needs_revision
Control over the room is a valid recommendation, but no latency and no technical variability are categorical claims contradicted by real capture/sync considerations; OBS documents render delay specifically for audio/video synchronization. RODE confirms four combo inputs and multitrack recording for Pro II, supporting that example but not five wired XLR microphones on four inputs. A noise floor below -50dB lacks a reference/measurement method and is not an actionable universal acoustic-treatment guarantee.
## usability — needs_revision
Fresh desktop/mobile/light/dark renders show useful equipment hierarchy and no page-wide overflow, but pale striped table rows have light text in dark mode, hiding equipment guidance. The unqualified noise-floor check and per-participant equipment ambiguity also prevent reliable self-checking. Existing shared CSS plus small body clarifications are needed.
## Practitioner reader gate
Purpose PASS: control shared-room production. First action PASS: select a starter or professional setup with per-person capture. Example REVISE: clarify equipment counts per participant rather than implying 2-3 cameras cover five required individual feeds. Quality Bar REVISE: replace unreferenced -50dB requirement with a recorded speech/silence listening check or define a validated measurement. Meaning/voice PASS: preserve strong room-control advice and actual equipment examples. Essential limits REVISE: no zero-latency/no-variability promise; verify all isolated feeds and sync before session. Shared dark contrast blocks table use.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Use primary manufacturer specifications and official capture documentation proportionately; no bench testing or product purchasing.",
    "items": [
      {
        "url": "https://rode.com/en-au/products/rodecaster-pro-ii",
        "claim": "RODECaster Pro II provides multichannel microphone inputs and isolated recording options.",
        "finding": "Current manufacturer page states four Neutrik combo inputs, multitrack/stereo recording and four headphone outputs. This supports a four-input example, not five wired XLR mic inputs without another route.",
        "checked_at": "2026-10-30T16:51:57Z"
      },
      {
        "url": "https://obsproject.com/kb/filters-guide",
        "claim": "Studio video/audio processing may need synchronization, not a universal no-latency claim.",
        "finding": "Official filter guide explicitly describes Render Delay as delaying source rendering to help audio/video sync. It supports retaining a sync check rather than promising zero delay. Focusrite latency help returned 403; no inaccessible source is claimed read.",
        "checked_at": "2026-10-30T16:51:57Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read full Record hub, hybrid and remote pages to distinguish studio control from location/routing guarantees.",
    "items": [
      {
        "path": "patterns/produce/record/index.md",
        "claim": "Studio production should retain separate source feeds for editing.",
        "finding": "Hub identifies multi-camera plus interface as per-person camera and audio capture; studio Quality Bar matches that aim but equipment counts need clearer scaling.",
        "checked_at": "2026-10-30T16:51:57Z"
      },
      {
        "path": "patterns/produce/record/hybrid-recording.md",
        "claim": "Mixed-location sessions require a hybrid option.",
        "finding": "Hybrid guide adds headphones and a sync point to connect studio and remote participants; studio page correctly redirects distributed guests rather than claiming one setup fits all.",
        "checked_at": "2026-10-30T16:51:57Z"
      },
      {
        "path": "patterns/produce/record/remote-isolated.md",
        "claim": "Location-based route should preserve separate downloadable tracks.",
        "finding": "Remote guide emphasizes isolated files and verification; studio guide uses the same editing objective with local equipment. Comparison does not verify its session-count claim.",
        "checked_at": "2026-10-30T16:51:57Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261030. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Prepare smallest full-content revision clarifying camera/input sizing, replacing absolute technical promises and making audio checks observable. Reuse existing shared CSS correction; no scores/framework change, no body publication before approval.
Nominal next review 2026-11-29T16:51:59Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.
