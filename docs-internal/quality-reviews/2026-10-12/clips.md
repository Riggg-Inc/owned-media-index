# clips — substantive post-release quality assessment

Full body read from current f4ffead; live article and desktop/mobile dark screenshots retained as clips-* in run artifacts. Shared contrast issue reuses the original card and already-complete exact CSS proposal; no duplicate proposal or body edit needed. Scores unchanged; no human signoff.

Exact assessment record (six reasoned checks, source scope, comparisons, body hash, actual completion time and next review):

{
  "id": "quality-20261012-clips",
  "status": "needs_revision",
  "assessed_at": "2026-10-12T16:49:50Z",
  "reviewer": "Cass Reelman (AI, openai/gpt-6-astra)",
  "method": "substantive-quality-review-v1",
  "content_sha256": "bacf9c5019cb070a52b75099c077957778d566ac19c0422ae96393b56a38f2af",
  "report_ref": "docs-internal/quality-reviews/2026-10-12/clips.md",
  "dimensions": {
    "usefulness": {
      "status": "pass",
      "rationale": "The five-style comparison maps source moments to extraction choices, then supplies platform and caption workflow guidance useful to an editor exporting clips."
    },
    "substance": {
      "status": "pass",
      "rationale": "Selection table, quality tests, documented platform limits, caption references and scoped defaults provide concrete detail beyond a generic short-video recommendation."
    },
    "coherence": {
      "status": "pass",
      "rationale": "Upload maximums are distinguished from 30\u201390-second editorial defaults and standard YouTube from Shorts; crop and codec choices remain destination-dependent."
    },
    "cross_page_consistency": {
      "status": "pass",
      "rationale": "The corrected quadrant also chooses by source moment and audience fit. Data Drop and other listed style names agree with the hub taxonomy; no new universal performance ranking is asserted in operating guidance."
    },
    "reasonable_claims": {
      "status": "pass",
      "rationale": "Seven official references were read. YouTube limits, encoding and caption qualifications match; LinkedIn member/Page limits are correctly distinguished, and Meta announcement is not inflated into unlimited file-size support."
    },
    "usability": {
      "status": "needs_revision",
      "rationale": "Current live 1440/390 screenshots and article content inspected. No document overflow; however dark-mode pale striped rows erase substantive Best For text, LinkedIn/Facebook upload guidance and social caption advice, making revision necessary."
    }
  },
  "source_checks": {
    "applicable": true,
    "rationale": "Material numerical upload and caption claims checked against the seven official references; transport truncation on Google pages is recorded, relevant quoted sections were present.",
    "items": [
      {
        "url": "https://support.google.com/youtube/answer/71673?hl=en",
        "claim": "Standard YouTube maximum upload duration and file size.",
        "finding": "Official help confirms 15-minute default, longer verified uploads, and 256 GB or 12 hours maximum; relevant section present despite transport truncation warning.",
        "checked_at": "2026-10-12T16:48:58Z"
      },
      {
        "url": "https://support.google.com/youtube/answer/1722171?hl=en",
        "claim": "YouTube recommended encoding and adaptive aspect ratio.",
        "finding": "Official recommendations list MP4, H.264 and AAC options; 16:9 desktop standard with adaptation for vertical and square, not a universal format restriction.",
        "checked_at": "2026-10-12T16:48:59Z"
      },
      {
        "url": "https://www.linkedin.com/help/linkedin/answer/a548372/",
        "claim": "LinkedIn member video upload limits and aspect ratio.",
        "finding": "Member help specifies 15 minutes, 5 GB and aspect ratio 1:2.4\u20132.4:1, consistent with the public table.",
        "checked_at": "2026-10-12T16:48:59Z"
      },
      {
        "url": "https://www.linkedin.com/help/linkedin/answer/a1311816",
        "claim": "LinkedIn Page and Career Page video upload limits.",
        "finding": "Page guidance specifies 10 minutes and 5 GB, and the same aspect range; the page itself is older, so target correctly distinguishes workflow and advises confirmation.",
        "checked_at": "2026-10-12T16:49:00Z"
      },
      {
        "url": "https://about.fb.com/news/2025/06/making-it-easier-create-videos-facebook/",
        "claim": "Meta unified reels rollout and length/format announcement.",
        "finding": "Announcement says no length/format restrictions and gradual rollout; no unlimited file-size assertion appears, matching the scoped public wording.",
        "checked_at": "2026-10-12T16:49:00Z"
      },
      {
        "url": "https://support.google.com/youtube/answer/6373554?hl=en",
        "claim": "YouTube automatic captions require review and have limitations.",
        "finding": "Help explicitly warns of transcription errors, processing/language limits and requires reviewing auto captions; target accurately summarizes these caveats.",
        "checked_at": "2026-10-12T16:49:01Z"
      },
      {
        "url": "https://support.google.com/youtube/answer/2734698?hl=en",
        "claim": "YouTube supports SRT and WebVTT with format limitations.",
        "finding": "File guide supports basic UTF-8 SRT without style markup and VTT with limited styling; target acknowledges format-specific restrictions.",
        "checked_at": "2026-10-12T16:49:01Z"
      }
    ]
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read complete related published pages and compared their actual operating guidance.",
    "items": [
      {
        "path": "quadrants/clips.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Source-moment selection and audience-fit advice agree with the hub table and its editorial defaults.",
        "checked_at": "2026-10-12T16:49:50Z"
      },
      {
        "path": "patterns/package/clips/data-drop.md",
        "claim": "Compatibility with the target selection task and published framework.",
        "finding": "Statistic/context definition agrees with the Data Drop row; the separate leaf performance overclaim is recorded on its own existing correction.",
        "checked_at": "2026-10-12T16:49:50Z"
      }
    ]
  },
  "next_review_at": "2026-11-11T16:49:50Z",
  "disposition": "park",
  "retry_at": null,
  "reason": "Shared dark-mode stripe and link contrast hides material selection and upload guidance; existing exact stylesheet proposal awaits human approval.",
  "correction_card": "8006e12e-6551-440a-b9cc-27bce652996f"
}
