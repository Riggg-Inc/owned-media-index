# OMI Master pages — independent source audit

AI source/editorial review: openai/gpt-6-astra. Completed 2026-10-26T16:51:41.338Z.
Read the complete four assigned Markdown pages, EVIDENCE.md and docs-internal/quality-review-procedure.md in /home/production/omi-quality-review-20261026. Also read complete docs/patterns/produce/rough-cut/index.md. Scope: independent evidence check, not a six-dimension pass, rendered inspection, human signoff, or publication authorization. No source bodies, registries or cards changed.

## Actionable findings by page

### audio-mastering.md — material corrections

- **Supported:** -16 LUFS ±1 and true peak no higher than -1 dBTP are consistent with Apple's podcast recommendation [A]. The -1.5 dBTP working target is a sensible margin, not a separate universal platform mandate. 48 kHz/192 kbps stereo MP3 is a reasonable preset within Apple recommendations and specifically supported by Audacity's podcast guidance [B]. Preserve these useful defaults.

- **Incorrect export concept:** “16-bit (MP3)” confuses PCM sample precision with compressed MP3 encoding. Apple specifies resolution for WAV/FLAC but bitrate for MP3; Audacity's complete MP3 export settings expose sample rate, channels and bitrate, not PCM bit depth [A,B]. Minimal correction: “24-bit PCM WAV archive; MP3: specify bitrate, not bit depth.”

- **Unsupported cross-modality claim:** Spotify “normalized to -14” is not established for podcast episodes by Spotify's cited-type artist documentation [C]. That page explicitly describes songs/tracks/albums, playback preferences (-11/-14/-19) and device exceptions. Do not transfer a music playback rule into a podcast upload requirement. Keep the -16 podcast workflow target; remove the blanket podcast normalization assertion unless a podcast-specific primary source is supplied.

- **Unsupported as documented requirements:** YouTube -14 and Amazon -16 entries, general RSS “-16 standard,” Apple 2 GB, and the named “Spotify loudness checker” lack supporting source links here. YouTube upload encoding guidance [D] provides no numerical LUFS mandate. Absence there is not proof normalization never occurs. Replace unsupported platform mandates with clearly labeled production defaults; provide a real checker link or say “measure integrated loudness and true peak.”

- **Scope error:** Apple RSS audio is MP3 or AAC; Apple recommends AAC in MP4. “MP3, M4A, MOV” mixes audio and video/container contexts [A]. Separate RSS audio from video-podcast and subscriber upload requirements rather than claiming MOV is an RSS audio format.

- **Usability, not a demand for experimental proof:** noise floor “-50dB/-40dB” lacks reference/meter/measurement interval. Define dBFS and how measured if retaining numerical gates. Present fixed EQ/compression settings as starting points adjusted to the recording, not guaranteed standards. Re-measure final encoded output after limiting.

### export-specs.md — materially stale limits and mislabeled presets

- **Contradicted:** LinkedIn maximum 10 minutes is 15 minutes in current official help; 5 GB is supported [E].

- **Contradicted as a universal current maximum:** Facebook Reels 90 seconds. Meta's June 2025 announcement says its unified video-to-Reels flow removes length/format restrictions, with gradual rollout [F]. Do not infer unlimited file size from that statement; check destination/upload route separately.

- **Supported with scope:** YouTube 256 GB is correct but also capped at 12 hours (whichever is less), and unverified accounts default to 15 minutes [G]. Shorts up to 3 minutes for eligible square/vertical uploads and global blocking of >1-minute Shorts with active Content ID claims are supported [H]; the documentation also covers active manual copyright claims. Preserve the existing useful citation/qualification.

- **Preset versus requirement:** YouTube recommends source-matched frame rate, not a forced 30 fps; for 1080p SDR its reference bitrate is 8 Mbps at 24/25/30 fps and 12 Mbps at 48/50/60, with variable bitrate [D]. 12–15 Mbps/30fps may remain an explicitly labeled house preset for a 30fps source; it is not YouTube's mandatory setting. Same separation is needed across the table. 256 kbps AAC is a workflow choice; YouTube's stereo reference is 384 kbps, not a rejection threshold.

- **Unresolved, not certified:** TikTok 10-minute maximum is contradicted by an official search excerpt distinguishing recording up to 10 minutes from uploads up to 60, but the fetched page returned only a shell [I]. Obtain readable full documentation before substituting a definitive value. Instagram 90s/4GB, TikTok 4GB, Facebook 10GB, X universal 512MB, and generic video-podcast 2GB were not established by accessible primary text in this audit. Do not treat them as checked. X help access was blocked. Use destination-specific links/route labels or omit unverified maxima pending review.
- Do not discard the practical presets or image examples simply because limits need revision. Smallest useful change: split “recommended production settings” from “upload limits,” retain supported values with their conditions, and avoid “every major distribution platform” completeness promises.

### index.md — software inclusion and audience statistic

- **Unsupported measured audience claim:** “80%+ watched without sound” gives no source, date, platform, population or denominator and generalizes to all vertical video. No primary study establishing this was retrieved; searches partly failed. This is NOT a verified false percentage, but an unsupported cross-platform behavioral claim. Minimal correction: “Burn in readable captions on vertical exports so the message works without sound.” Keep the action, remove the unsupported number.

- **High-priority unresolved inclusion claim:** “Adobe Audition — Included with Premiere” must not stand without a specific qualifying bundle. Ordinary Premiere single-app ownership should not be conflated with an all-app subscription. All attempted official Adobe product/plan/FAQ routes returned 403 [L]; therefore this run does not certify current price or bundle contents. Minimal safe correction pending a readable plan check: “Separate Adobe app; check your subscription includes Audition.” Do not claim a fully source-verified contradiction from inaccessible pages.

- **Supported/qualified pricing:** Resolve has a free edition, integrated Fairlight and Mac/Windows/Linux support [J]. Its page currently displays Studio “Was $295 Now $236,” so $295 is supported as the reference price, not the current promotional checkout amount. Avoid hardcoding a temporary sale; label list price/date or link pricing.

- **Partially supported, scope correction:** Final Cut Pro $299.99 one-time is explicitly confirmed [K]. “Mac only” is correct only if the row is specifically the one-time Mac edition: the product also exists on iPad, and the same page offers Creator Studio subscriptions. Label “Final Cut Pro for Mac” rather than presenting all Final Cut Pro as Mac-only.

- **Unresolved inclusion/price details:** Descript primary pricing confirms Free plus paid plans, Studio Sound/filler-word tools and per-plan AI/media allowances, but extraction omits paid dollar amounts [M]. Auphonic page confirms credit billing and differing plan features, but extraction omits usable price/allowance cells [N]. Do not certify $24+, $11/month or free 2h/month from those extracts. CapCut free auto-caption entitlement, RX $129+, Premiere $22.99 and Resolve automatic transcription entitlement need version/tier-specific checks. “Included” must distinguish ordinary subtitle import/editing from AI automatic transcription; the retrieved general Resolve overview alone is not sufficient proof that all automatic features are free.

- House delivery presets agree across Master/audio/export; keep them as workflow defaults. The rough-cut neighbor explicitly supplies simultaneous horizontal/vertical prepared outputs, supporting the described handoff. “If mastering takes longer ... something went wrong upstream” is an overabsolute diagnosis, not demonstrated internal data: repair work, accessibility and creative complexity can legitimately lengthen mastering. Minimal change: “Aim to keep mastering shorter than the rough cut; if it runs long, check whether upstream fixes would help.”

### video-mastering.md — mostly useful practitioner guidance, limited empirical claims
The edit/color/sync checklist is concrete practitioner advice, not something requiring a study for every bullet. No external factual defect comparable to the other three pages was established. Preserve it. Two practical clarifications merit parent review: “center 80%” is a house heuristic, not a verified universal UI safe zone; preview against destination UI. A full 1.5x watch can aid pacing review but is not sufficient on its own to judge real-time audio defects or one-frame sync: add normal-speed checks of sync, transitions and audible defects. Three-second dead-air trimming should preserve intentional pauses. “Internal production data” is asserted but no dataset/outcome is shown; do not invent one. Rough-cut/master handoff is coherent with the neighboring page. Parent must decide six-dimension/rendered outcome independently.

## Primary-source retrieval ledger (actual UTC)

Times below are web_fetch fetchedAt values unless explicitly an unsuccessful attempt/search. A successful retrieval does not imply all claims on that domain were checked.


- **[A]** https://podcasters.apple.com/support/893-audio-requirements — 2026-10-26T16:47:44.450Z. Complete extracted audio requirements read: RSS MP3/AAC, subscriber WAV/FLAC/MP3 distinctions; PCM resolution versus MP3 bitrate; -16 ±1 and true peak -1 recommendation.

- **[B]** https://manual.audacityteam.org/man/mp3_export_options.html — 2026-10-26T16:48:39.837Z. Complete extracted export documentation read; sample rate/channels/bitrate modes, podcast CBR presets including 192 kbps stereo, lossless working-copy recommendation.

- **[C]** https://support.spotify.com/us/artists/article/loudness-normalization/ — 2026-10-26T16:47:44.266Z. Complete extract read; explicitly music tracks/albums, variable playback settings/device exceptions. Not podcast-specific evidence.

- **[D]** https://support.google.com/youtube/answer/1722171 — 2026-10-26T16:47:55.399Z. Encoding guidance read: source frame rate, VBR, SDR/HDR bitrate distinctions, MP4/H.264, 48kHz and stereo 384 kbps. No LUFS target in retrieved guidance.

- **[E]** https://www.linkedin.com/help/linkedin/answer/a548377 — 2026-10-26T16:48:13.974Z. Video requirements: 5GB, 15min, 10–60fps and wide resolution/aspect-ratio ranges.

- **[F]** https://about.fb.com/news/2025/06/making-it-easier-create-videos-facebook/ — 2026-10-26T16:48:40.613Z. Complete announcement read, including rollout and audience settings; no length/format restrictions in new unified flow, not a file-size specification.

- **[G]** https://support.google.com/youtube/answer/71673 — 2026-10-26T16:47:55.313Z. Complete extracted guidance read: 256GB or 12h, unverified 15min.

- **[H]** https://support.google.com/youtube/answer/15424877 — 2026-10-26T16:47:55.218Z. Extracted eligibility, copyright and FAQ sections read. Transport warned incomplete large HTML; substantive sections available: square/vertical up to 3min, channel/date distinctions, >1min active-claim blocking.

- **[I]** https://support.tiktok.com/en/using-tiktok/creating-videos/camera-tools — 2026-10-26T16:48:14.179Z fetched shell only. Official search excerpt retrieved 2026-10-26T16:48:34.081Z says recording 10min/upload 60min. Explicitly limited evidence, not full-context verification.

- **[J]** https://www.blackmagicdesign.com/products/davinciresolve — 2026-10-26T16:48:13.881Z. Relevant overview, Fairlight, free/Studio and pricing sections read (long extract truncated in peripheral hardware listings). Free edition and Studio reference $295/promotional $236 shown. https://www.blackmagicdesign.com/products/davinciresolve/edit retrieved 2026-10-26T16:48:40.166Z; reviewed editing/subtitle introduction, not sufficient entitlement matrix for automatic transcription.

- **[K]** https://www.apple.com/final-cut-pro/ — 2026-10-26T16:48:41.116Z. Product FAQ read: Mac/iPad, $299.99 one-time Mac option, Creator Studio $12.99/mo or $129/year and subscription-specific content.

- **[L]** Adobe access failures: https://www.adobe.com/products/audition.html at 2026-10-26T16:47:44.390Z; https://www.adobe.com/creativecloud/plans.html at 2026-10-26T16:48:13.526Z; https://helpx.adobe.com/audition/faq.html at 2026-10-26T16:48:39.510Z; https://www.adobe.com/products/audition/pricing-info.html at 2026-10-26T16:48:57.087Z; https://www.adobe.com/products/premiere/plans.html at 2026-10-26T16:48:57.139Z. All 403; no retrieved contents used as evidence.

- **[M]** https://www.descript.com/pricing — 2026-10-26T16:48:40.423Z. Complete extracted text read, paid dollar amounts absent; plan/AI allowance distinctions visible.

- **[N]** https://auphonic.com/pricing — 2026-10-26T16:48:14.118Z. Complete extract read; dynamic price cells absent, credit mechanics and feature differences visible.

- **[O]** https://help.x.com/en/using-x/x-videos — failed 403 attempt 2026-10-26T16:48:13.593Z; no current X limits certified.

## Minimal correction priority
1. Fix MP3 bit depth and stop applying Spotify music normalization as a podcast requirement.
2. Correct LinkedIn/Facebook maxima and separate all presets from platform requirements.
3. Remove unsupported silent-watch percentage; qualify Adobe inclusion and tool tiers rather than inventing current prices.
4. Retain usable mastering checklists; clarify real-time QC, measurement references and destination safe-zone checks without turning reader pages into audit reports.

No whole-page pass is granted by this report; unresolved rows are explicitly not verified.
