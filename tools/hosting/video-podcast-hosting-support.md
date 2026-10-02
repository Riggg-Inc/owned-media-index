---
description: "Video podcast hosting and player compatibility: MP4 RSS, open HLS, Apple integrations, Spotify video, and YouTube publishing, with dated evidence."
---

# Video Podcast Hosting — Platform Support Reference

Video podcast hosting support depends on the delivery path, not just whether a service accepts a video upload. MP4 in RSS, open HLS video, Apple’s approved integration, Spotify’s native ingestion, and YouTube publishing are different capabilities. This reference separates them and identifies rollout limits and unresolved evidence.

**Documented source-review date:** 2026-10-02

**Next source review due:** 2026-11-02 (monthly; earlier when a provider changes its documentation)

**Source-review provenance and scope:** Public documentation reviewed on 2026-10-02; not an account-level upload or playback certification. Every row below has that check date. “Unknown” means not established by the cited evidence, not unsupported.

## What “supported” means here

- **MP4/file RSS:** A video file in a standard RSS `<enclosure>`. Apple still accepts MOV, MP4 and M4V video feeds; this is distinct from its integrated HLS experience. A file may stream progressively; HLS is not required for every form of video playback.
- **Open HLS RSS:** An HLS manifest/stream advertised with `podcast:alternateEnclosure` alongside the ordinary audio enclosure. The receiving app must understand that tag and stream. HLS playback alone does not prove that an app discovers it through RSS.
- **Apple HLS:** A supporting host, Apple Podcasts Connect authorization/API key and show availability are required. Apple’s HLS delivery is not automatic ingestion of the open RSS alternate enclosure. Traditional video RSS remains a separate route.
- **Spotify video:** Native Spotify for Creators/Megaphone upload or a supported direct host integration. An audio RSS listing does not prove video ingestion, and open RSS alternate enclosures are not the documented Spotify video route.
- **YouTube:** Separate channel authorization and video publishing/republishing. Audio-plus-artwork videos are not evidence of full-motion video hosting or open HLS RSS support.

**Status key:** **Live—documented** means current vendor instructions describe a usable workflow, possibly with eligibility restrictions. **Reported live** means the Podcast Standards Project (PSP) lists implementation, but this review has not independently verified the account workflow. **Announced/rollout** is not universal availability. **Unknown** is an evidence gap.

## Hosts and publishing services

All rows checked **2026-10-02**. The [PSP implementation list][psp] was itself updated September 2, 2026; its claims are attributed, not treated as fresh account tests.

| Host | Status and documented delivery | Limits / what is not established |
|---|---|---|
| **Buzzsprout** | **Live—documented:** Audio + Video plans publish video to Apple Podcasts, Spotify and YouTube; MP4/MOV upload becomes Apple HLS. [Vendor setup/FAQ][buzzsprout] | Apple API key/show approval and Spotify approval required. Vendor describes audio RSS for other apps. PSP lists open HLS RSS as **committed**, not shipped; do not infer it from Apple support. |
| **Acast** | **Live—documented:** Apple video via the Video plan or creator-network activation; audio extracted automatically. [Current launch statement][acast] | Apple authorization is separate. Older [setup documentation][acast-setup] still says limited beta; current launch statement says open to all with plan/activation requirements. Open HLS RSS, Spotify video and YouTube video are **unknown** from these sources. |
| **CoHost** | **Live—vendor claim:** Its own hosting guide says CoHost allows video publishing to Apple Podcasts. [CoHost guide][cohost] | The guide does not specify MP4 RSS versus Apple HLS/API, open alternate enclosures, or account availability. “Full video support” would overstate this evidence. |
| **Spotify for Creators** (current product name) | **Live—documented:** Video uploaded to Spotify uses its native streaming system; other listening platforms receive audio via RSS. [Spotify][spotify] | Not open-RSS video distribution. Former “Spotify for Podcasters” naming has been replaced here. |
| **Megaphone** (Spotify) | **Live—documented:** Spotify explicitly includes Megaphone video uploads in the native-video/audio-RSS workflow. [Spotify][spotify]; [Megaphone video documentation][megaphone] | Video enablement and monetization eligibility vary. This is not evidence of Apple HLS, YouTube publishing or open HLS RSS. The old “no public video announcement” classification was wrong. |
| **Podbean** | **Live—documented:** HLS video in RSS, automatic audio version and separate Apple API delivery. [Podbean technical explanation][podbean] | Enable HLS for eligible video episodes; Apple delivery and RSS delivery are distinct. Other destinations require their own verification. |
| **Transistor** | **Reported live** for open HLS RSS (PSP); **gradual rollout/early access** in its own feature page, which describes Apple-approved HLS plus Spotify/YouTube/RSS distribution. [PSP][psp]; [Transistor][transistor] | Vendor still offers a waitlist. Do not treat the destination list as generally available to every account. |
| **Captivate** | **Reported live:** PSP lists publishing HLS through alternate enclosures. [PSP][psp] | Its [public feature matrix][captivate] does not establish a video setup path. Account access, Apple/Spotify video integration and YouTube video delivery remain **unverified** in this review. |
| **RSS.com** | **Live—documented:** Max plan offers Apple HLS, Podcasting 2.0 alternate enclosures and direct YouTube video publishing. [RSS.com][rsscom] | The same page explicitly says Spotify and Amazon Music receive the **audio** feed; “publish everywhere” does not mean video everywhere. |
| **Omny Studio** (Triton Digital) | **Live—documented:** Organization-enabled video can emit both MP4 and HLS alternate enclosures; audio-first/video-first primary enclosure choices. [RSS documentation][omny] | Alternate media must be enabled/configured. Docs say Apple/Spotify ignore alternate enclosures. Apple separately named Omny an HLS launch provider. [Apple announcement][apple-launch] |
| **Flightcast** | **Reported live:** PSP lists open HLS RSS; vendor offers video publishing. [PSP][psp]; [Flightcast][flightcast] | Broad “publish everywhere” wording does not establish each destination’s ingestion method or eligibility. Confirm the required integrations before purchase. |
| **Podigee** | **Live—documented:** Video distribution to Apple, Spotify and YouTube on eligible paid plans, with quotas and platform connections. **Reported live** open HLS RSS. [Podigee][podigee]; [PSP][psp] | Audio feed distribution and video connections are explicitly separate. Confirm plan/quota and connection setup. |
| **Beamly** | **Live—vendor claim:** Audio/video hosting. **Reported live:** open HLS RSS. [Beamly][beamly]; [PSP][psp] | Its general cross-platform marketing does not independently establish Apple HLS or Spotify video integration. |
| **Fountain** | **Reported live:** Listed by PSP as both an open HLS RSS host and a compatible player. [PSP][psp] | Vendor video page did not expose readable setup documentation during this check. Host account access and proprietary destination integrations remain **unknown**. |
| **TrueFans** (listed as “True Fans” by PSP) | **Reported live:** Listed as an open HLS RSS host and compatible player. [PSP][psp] | Public site retrieval did not establish host setup/eligibility; do not infer Apple/Spotify integration from player compatibility. |
| **Blubrry** | **Live—documented:** MP4 upload generates HLS and MP3; original video, HLS and audio are published in one RSS feed. Apple workflow requires an API key and HLS enablement. [Blubrry][blubrry]; [PSP][psp] | Apple account enablement is a separate step, not automatic acceptance of RSS HLS. Added after the earlier reference omitted this PSP-listed host. |
| **Castos** | **Live—documented:** Video podcast feeds submitted to Apple, Pocket Casts and Podcast Addict; video episodes can be republished to YouTube. [Castos distribution guide][castos] | Open HLS/alternate-enclosure and Apple HLS integration are **unknown**. Separate [YouTube setup][castos-youtube] describes audio-plus-image conversion. The distribution guide’s older Spotify-only-hosting assertion is not a current ecosystem-wide rule; direct integrations now exist elsewhere. |
| **Libsyn** | **Live—vendor feature listing:** Audio/video hosting, Spotify video and YouTube video distribution. **Announced:** Apple HLS explicitly marked “Coming Soon.” [Libsyn features][libsyn] | Open HLS RSS is **unknown**. Traditional video hosting must not be conflated with the announced Apple HLS feature. |
| **Spreaker** | **Announced/committed:** PSP places it in the committed-to-shipping HLS RSS group. [PSP][psp] | [Upload documentation][spreaker] describes audio episodes (even though MP4 is among accepted containers). That does not prove video delivery. Shipped HLS status remains **unverified**, not definitively “not shipped.” |
| **Simplecast** (SiriusXM, not Spotify) | **Announced Apple HLS provider:** Apple names SiriusXM, including Simplecast, among launch supporters. [Apple announcement][apple-launch] | Its [video/YouTube help article][simplecast] could not be fully retrieved in this review. Current account rollout and open HLS RSS remain **unverified**. The earlier audio-only/no-announcement label is not defensible. |

**iHeart is listed below as a listening/distribution destination, not a demonstrated self-service video host.** Its RSS acceptance does not establish general video-hosting capability.

## Players / apps

All rows checked **2026-10-02**. Support is specific to the route and app version, not a promise that any hosted video will appear.

| App | Status and route | Important limit |
|---|---|---|
| **Apple Podcasts** | **Live—documented:** Traditional MOV/MP4/M4V RSS video; separate integrated HLS via supporting providers and API authorization. [Video RSS][apple-rss]; [HLS setup][apple-hls] | HLS availability is rolling and region-dependent. RSS metadata remains in use, but open alternate-enclosure discovery is not the HLS delivery route. |
| **Pocket Casts** | **Live—documented:** MP4 and open-feed HLS on iOS, Android, web and desktop. [Playback documentation][pocketcasts] | HLS video cannot be downloaded as video in Pocket Casts; downloads use the standard audio file. Video exclusive to YouTube/another proprietary app will not appear. |
| **Fountain** | **Reported live:** HLS from RSS. [PSP][psp] | Current app/version and account behavior not independently playback-tested. |
| **TrueFans** | **Reported live:** HLS from RSS. [PSP][psp] | Current app/version and account behavior not independently playback-tested. |
| **Podcast Guru** | **Reported live:** HLS from RSS. [PSP][psp] | PSP attribution, not an independent playback test or claim about all clients. |
| **Podcast Addict** | **Reported live:** HLS from RSS. [PSP][psp] | PSP links its [2025.4 changelog][addict], which blocked direct retrieval in this review. Retain attributed status rather than claiming fresh vendor validation. |
| **Amazon Music** | **Beta, reported:** PSP lists HLS RSS support **in beta**. [PSP][psp] | Not general availability. For example, RSS.com still documents audio delivery to Amazon; verify show/account access. |
| **iHeart** | **Limited, reported:** PSP lists HLS RSS with **manual submission**. [PSP][psp] | Not automatic universal video ingestion and not evidence that iHeart is a general-purpose video host. |
| **Spotify** | **Live—documented:** Native video from Spotify for Creators/Megaphone and supported host integrations (e.g. Buzzsprout approval flow). [Spotify][spotify]; [Buzzsprout][buzzsprout] | Open RSS alternate enclosures are not the documented video route. RSS.com’s audio delivery and Buzzsprout’s video integration can both be true. |

## Before choosing a host

Ask for a sample feed and verify its actual primary and alternate enclosures; test the target app/version, audio fallback, and download behavior. Separately confirm Apple show/API approval, Spotify integration approval, YouTube authorization, plan quotas and rollout eligibility. “Accepts MP4,” “plays HLS,” and “publishes video everywhere” are not interchangeable guarantees.

## Related Patterns

- [Feed Metadata Standard](https://index.riggg.com/patterns/publish/feed-metadata-standard/)
- [HLS Video Podcast Distribution Standard](https://index.riggg.com/patterns/produce/recording/hls-video-podcast-distribution/)

[psp]: https://podstandards.org/2026/08/11/podcast-hosting-platforms-and-apps-that-support-hls-video-in-rss/
[buzzsprout]: https://www.buzzsprout.com/features/video-podcasting
[acast]: https://www.acast.com/en/press-room/video-on-apple-podcasts-now-open-to-all
[acast-setup]: https://learn.acast.com/en/articles/15190085-video-on-apple-podcasts-via-acast
[cohost]: https://cohostpodcasting.com/resources/best-platforms-for-video-podcast-hosting/
[spotify]: https://creators.spotify.com/features/video
[megaphone]: https://support.megaphone.fm/en/articles/12043371-video-monetization
[podbean]: https://blog.podbean.com/podbean-now-supports-hls-video-in-podcast-rss-feeds/
[transistor]: https://transistor.fm/features/video/
[captivate]: https://www.captivate.fm/features
[rsscom]: https://rss.com/features/video-podcasting/
[omny]: https://help.tritondigital.com/docs/where-is-my-rss-feed
[apple-launch]: https://www.apple.com/newsroom/2026/02/apple-introduces-a-new-video-podcast-experience-on-apple-podcasts/
[flightcast]: https://flightcast.com/
[podigee]: https://www.podigee.com/en/
[beamly]: https://beamly.com/
[blubrry]: https://blubrry.com/support/media-hosting-documentation/how-to-set-up-hls-video-podcasting-with-blubrry/
[castos]: https://support.castos.com/article/429-submit-your-video-podcast-to-podcast-directories
[castos-youtube]: https://support.castos.com/article/45-set-up-youtube-republishing-in-castos
[libsyn]: https://libsyn.com/features/
[spreaker]: https://help.spreaker.com/en/articles/3810629-what-kind-of-files-can-i-upload-to-the-platform
[simplecast]: https://help.simplecast.com/hc/en-us/articles/32469580179869-NEW-Video-Podcasts-with-YouTube-Publishing-and-Analytics
[apple-rss]: https://podcasters.apple.com/support/3684-video-podcasts
[apple-hls]: https://podcasters.apple.com/support/5593-how-to-publish-video
[pocketcasts]: https://support.pocketcasts.com/knowledge-base/video-podcasts/
[addict]: https://podcastaddict.com/changelog/2025_4#section4
