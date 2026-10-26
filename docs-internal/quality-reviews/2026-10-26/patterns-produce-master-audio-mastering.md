# Whole-page quality review: patterns/produce/master/audio-mastering.md
Completed 2026-10-26T16:59:42Z
Reviewer: Cass Reelman (AI editorial review, openai/gpt-6-astra)
Exact published body SHA256: ade45fa03bffe6a950dcbaeb01ccf96298462f7904f03776284cbbac46ca1fbd
Outcome: needs_revision; not human signoff.
## usefulness — needs_revision
The chain and targets help a producer finish speech audio, but the platform-requirements table and unlinked Spotify loudness-checker acceptance step can send readers toward incorrect requirements; those are material to the promised distribution-ready result.
## substance — pass
Eight processing steps, integrated loudness/peak targets, tool options and audible acceptance checks provide real operational substance. The repeated definition is minor, not a reason to rewrite the entire guide.
## coherence — pass
Noise reduction through EQ/compression to normalization, limiting and export is a coherent suggested order. It should remain a starting chain adjusted by listening rather than a mandatory preset for every voice.
## cross_page_consistency — pass
The Master hub and Export Specifications use the same -16 LUFS stereo and 48 kHz workflow baseline. Those working presets can be consistent without proving every platform row is a requirement; distinguish prescribed workflow targets from external ingest limits.
## reasonable_claims — needs_revision
Platform normalization assertions, all-major-platform scope, MP3 bit-depth wording and a Spotify loudness checker are insufficiently scoped or supported. A legacy snapshot disclaimer does not turn a requirements table into verified current guidance; retain useful working targets while correcting these precise claims.
## usability — needs_revision
Fresh light desktop is usable, but mobile dark pale stripes obscure peak, sample-rate and platform rows and dark code obscures the mastering chain. This is a task-critical readability failure, not an optional visual preference.
## Practitioner reader gate
Purpose PASS: finish podcast audio. First action PASS: work from isolated tracks and address noise. Example PASS: the ordered chain and suggested settings make an executable starting example. Quality Bar REVISE: replace unverified Spotify checker gate with integrated/true-peak measurement plus full listening and destination ingest checks. Meaning/voice PASS with precise fixes: retain decisive working targets. Essential limits REVISE: identify presets versus platform requirements and adjust processing by ear.
## Sources and comparisons
{
  "source_checks": {
    "applicable": true,
    "rationale": "Independent same-model AI read primary sources in context; parent read and synthesized retained source report. Inaccessible or partial sources are explicit limitations, not verified facts. Full ledger retained in independent-source-audit.md.",
    "items": [
      {
        "url": "https://podcasters.apple.com/support/893-audio-requirements",
        "claim": "Apple podcast loudness, formats and MP3 bit depth requirements.",
        "finding": "Independent AI read complete extracted requirements: -16 LUFS plus/minus1 and true peak no higher than -1dBTP supported; RSS accepts MP3/AAC, PCM resolution applies to WAV/FLAC rather than MP3. No universal Apple2GB audio limit established.",
        "checked_at": "2026-10-26T16:47:44.450Z"
      },
      {
        "url": "https://support.spotify.com/us/artists/article/loudness-normalization/",
        "claim": "Spotify normalizes podcast episodes to minus14 LUFS.",
        "finding": "Independent AI read complete music artist documentation about tracks and albums, variable listening settings and device exceptions. It does not establish podcast-episode normalization or a podcast upload mandate; no cross-modality inference accepted.",
        "checked_at": "2026-10-26T16:47:44.266Z"
      },
      {
        "url": "https://manual.audacityteam.org/man/mp3_export_options.html",
        "claim": "MP3 exports specify sixteen-bit depth and a192kbps podcast preset.",
        "finding": "Complete export documentation reviewed independently: MP3 uses bitrate, channels and sample rate rather than PCM bit-depth;192kbps stereo CBR is a supported podcast working preset.",
        "checked_at": "2026-10-26T16:48:39.837Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Parent read complete current Master hub and both audio/video/export guides, plus Rough Cut and framework, to compare the actual finishing handoff and shared settings.",
    "items": [
      {
        "path": "patterns/produce/rough-cut/index.md",
        "claim": "Finishing receives an already assembled horizontal and vertical show.",
        "finding": "Rough Cut describes layouts, graphics, transitions and dual output, supporting the finishing handoff without proving that every episode can finish faster than its rough cut.",
        "checked_at": "2026-10-26T16:58:52.138Z"
      },
      {
        "path": "patterns/produce/master/export-specs.md",
        "claim": "Sibling pages use consistent audio finishing targets.",
        "finding": "Both reference48kHz stereo MP3 at192kbps and minus16LUFS as working settings; cross-page agreement is coherent but cannot certify external platform requirements or unavailable source evidence.",
        "checked_at": "2026-10-26T16:58:52.138Z"
      }
    ]
  }
}
## Rendered acceptance
Complete Markdown and current rendered article read. Fresh 1440/390 light/dark captures retained in output/reports/omi-quality-20261026. Desktop-light and mobile-dark screenshots visually inspected. Screenshot text at reduced scale is not claimed as complete reading; complete source/extraction supplies that. No private customer evidence, playback, measured outcomes or human testing claimed.
## Next action
Retain exact claim-specific recommendations in independent-source-audit.md on the SAME existing correction card. Material body changes remain preparation until complete source-scoped revised pages and independent review are ready; no numerical rescoring, framework change or public edits. Existing CSS8ba3927 already covers dark links/tables/code and awaits human approval.
Nominal next review 2026-11-25T16:58:52Z. Parked correction requires exact human approval and fresh post-release assessment; no public pass date.

Initial new uncommitted record failed seconds-versus-milliseconds timestamp validation. Rejected record retained in run audit; finalized at actual correction completion above. All pre-existing production objects unchanged.
