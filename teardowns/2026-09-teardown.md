# Top Business Podcasts Teardown — September 2026

## About This Analysis

Each month we pull the Apple Podcasts Business chart, sample twelve shows, and study what they actually ship — feeds, sites, structured data — against the Owned Media Index (OMI), a five-stage framework (Produce → Package → Publish → Prove → Preserve) for building media assets you own instead of renting. Last month we sampled the top of the chart: network flagships, public-radio operations, established interview franchises. This month the chart itself had rotated hard, and we deliberately sampled the other cohort — the independent and mid-tier operators who climbed into the top 25 in 2026. Fourteen of the current top 25 had never been analyzed. We took twelve of them.

The result is the most useful teardown we could have run, because it separates two things that last month's sample conflated: what a *well-resourced* show does, and what the *chart* actually rewards. The answer is uncomfortable. The chart rewards almost none of this.

## Shows Analyzed

- **Unblinded with Sean Callagy** (#3) — new, fast-rising influence/communication show; 20 episodes deep.
- **Coffeez with Joe Shalaby** (#6) — high-cadence founder interview show with the most disciplined title schema in the sample.
- **The Vault Unlocked** (#7) — founder-lessons interview show; newsletter- and LinkedIn-forward.
- **Proven Podcast** (#8) — operator interview show; the only show in the sample with 100% consistency on anything.
- **The Level Up Podcast w/ Paul Alex** (#9) — extreme-cadence solo/interview hybrid; 1,182 episodes.
- **the bossbabe podcast** (#10) — established women's entrepreneurship brand; the most aggressive owned-email operation here.
- **We Fixed It, You're Welcome** (#14) — business-strategy case-study show with a genuine narrative format.
- **The Code To Winning** (#15) — YouTube-native interview show; audio feed is downstream of the channel.
- **The Home Service Expert** (#19) — niche B2B trades show; 511 episodes and the deepest owned canonical layer in the sample.
- **Founder's Story** (#20) — network-produced founder interview show; strongest title craft of the group.
- **Creators Inc. Podcast** (#22) — creator-economy interview show; new, platform-native.
- **BILFPOD** (#24) — culture/business crossover interview show; strong per-episode packaging.

## What the Top Shows Are Getting Right

**Package — per-episode artwork is close to universal, and it's the one visual they actually own.** Nine of twelve ship a distinct item-level `itunes:image` on effectively every episode: Unblinded, Coffeez, The Vault Unlocked, Proven, and The Code To Winning at 100%, We Fixed It at 90%, bossbabe at 89%, BILFPOD at 81%. This is more disciplined than last month's cohort and it's the right instinct. Inside an audio app there is no thumbnail and no title card — the item artwork *is* the packaging, and unlike a YouTube thumbnail it travels through RSS to every downstream surface and survives a host migration.

**Package — titles are structured records, not headlines.** The best title work in this sample is structural. Coffeez runs a fixed slot schema on 93% of episodes (`Hook | Guest Name | Coffeez with Joe Shalaby Ep. 317`). Founder's Story runs the sharpest variant in either month's sample: a role label plus a verbatim pull-quote plus a stable ID plus the guest — `Estate Attorney: "I'm Giving Away What My Industry Charges Thousands For" | Ep. 445 with Atty. William Funk`. The Code To Winning uses double-pipe delimiters with a zero-padded episode number on 100% of episodes. These titles survive being torn out of the feed, which is the only environment that matters once an answer engine or a Slack paste gets hold of them.

**Package — descriptions carry real link and CTA architecture.** bossbabe puts a subscribe or connect CTA in 90% of descriptions, BILFPOD 85%, We Fixed It 74%, The Vault Unlocked 70%. These are long, structured bodies — 1,400 to 3,900 characters on average — consistent with `package/descriptions/rss-feed-description-patterns`. The floor established last month holds here.

**Publish — the owned email channel is alive where it's taken seriously.** bossbabe is the standout: newsletter and subscribe language appears 579 times across its feed, with live email capture on the owned site. The Vault Unlocked (78 mentions) and Founder's Story (116) also run real list-building through the feed. Where operators have thought about owned channels at all, email is the one they picked — which is the `publish/owned-channels/owned-email-newsletter` thesis validated by behavior.

**Package — episode segmentation work is genuinely being done.** Proven Podcast writes a topic-timestamp index into 100% of its 84 episodes. Unblinded does it on 70%. bossbabe, The Home Service Expert, BILFPOD, and The Code To Winning do it on a meaningful minority. Somebody is listening back and marking topic boundaries — the expensive part of the job.

## What's Missing (Even at the Top)

**Preserve — transcripts are at zero. Not low. Zero.** Across 3,068 episodes in twelve feeds, there is not one `podcast:transcript` tag. Last month's sample had three shows shipping transcripts; this cohort has none. The same is true of `podcast:chapters` — zero of twelve — and of `podcast:person`, `podcast:funding`, `podcast:value`, and `podcast:socialInteract`, all zero. The Podcasting 2.0 namespace is, in this cohort, entirely theoretical. Transcripts remain the single highest-leverage AEO asset a show controls and the one thing that turns an audio file into a retrievable, citable document. This is exactly the gap `preserve/transcripts` and candidate `f2ca608a` exist to close, and the top of the Business chart is not closing it.

**Publish — the canonical episode page has collapsed as a practice.** This is the month's real finding. Only **two of twelve** shows publish unique per-episode pages on a domain they own: The Home Service Expert (511 of 511) and Proven Podcast (roughly 80% of its catalog, the rest falling back to host URLs). Of the remaining ten: five point every episode at a host-controlled subdomain or a platform profile page; one points its entire catalog at a network's domain; one points 334 episodes at its own homepage and gives 162 episodes no link at all; one points all 86 episodes at a single YouTube channel URL; and one ships no episode links whatsoever. Last month ten of twelve had real owned episode pages. The difference is not that these shows are worse — it's that the chart does not require it. If you believe `publish/website/canonical-episode-page` and `preserve/owned-website-as-format-hub` matter, you have to be honest that ranking is not the mechanism that will force it.

**Publish — four shows have no owned web presence at the channel level either.** Three point their feed's `<link>` at a hosting platform's default profile page; one points it at a YouTube channel. There is no owned domain in the chain at all. Every asset — archive, discovery, subscriber relationship — sits on infrastructure the show does not control. This is `preserve/third-party-archive-is-a-tenancy` (candidate `6e5affc9`) described from the inside.

**Publish — RSS-native video remains at zero.** Not one `podcast:alternateEnclosure` in the sample. Every enclosure is `audio/mpeg`, with a single stray `video/mp4`. Video in this cohort means YouTube, and YouTube means the walled garden. Last month exactly one show shipped HLS through its own feed; this month, none. `produce/hls-video-podcast-distribution` remains a pattern with almost no adoption outside shows whose host does it automatically.

**Preserve — episode-level structured data is nearly absent.** Two of the ten reachable sites emit `PodcastEpisode` schema. Most carry `Organization` and `WebSite` markup and stop, and several render as near-empty JavaScript shells to a plain fetch, surfacing no structured data at all. One site serves proper `PodcastSeries` and `Person` schema but has no episode-level markup underneath it. For a cohort betting its growth on discovery, the retrieval plumbing is simply not built.

**Prove — nothing is publicly provable.** As last month, no show in the sample surfaces performance data publicly. This stage stays dark by design, and we will not pretend otherwise.

## Patterns We Don't Have Yet

Three practices cleared the bar — present in 3+ of the twelve shows, with no existing OMI pattern and no open card. Filed as candidates for scoring, not as recommendations.

**1. Per-episode feed artwork as a portable owned asset (9 of 12).** Nine shows ship unique item-level `itunes:image` at 81–100% of episodes. The OMI's `package/thumbnails/thumbnail-hook-patterns` scopes explicitly to YouTube, webinar replays, and website pages — platform-rendered surfaces. It says nothing about the feed-level image, which is the only visual that travels with the RSS and the only one visible at the moment of choice in an audio app. Notably, the three non-adopters are the three largest catalogs in the sample (379, 511, and 1,182 episodes), which suggests a volume cliff worth investigating rather than pure neglect. Filed as `package/per-episode-feed-artwork`.

**2. Show-name stamping in the episode title (6 of 12).** Six shows repeat their own brand inside each episode title — Coffeez at 89% of episodes, The Level Up Podcast 59%, The Code To Winning 41%, The Home Service Expert 40%, Founder's Story 40%, The Vault Unlocked 34% — usually via a pipe-delimited composite with a fixed slot order. It is redundant inside a podcast app, which is the point: it is there for every surface that strips channel context, including AI answer corpora. The OMI documents title *styles*, not the title as a self-attributing portable record. This one comes with a real cost — it burns characters in a slot that truncates hard, and the sample's best hook-writers deliberately spend the whole title on the hook instead — so it needs a truncation-budget rule, not a blanket endorsement. Filed as `package/show-name-stamped-in-episode-title`.

**3. Hand-built timestamp indexes with no machine-readable equivalent (6 of 12).** Six shows write topic-timestamp blocks into description text — Proven at 100% of episodes, Unblinded at 70% — while zero of twelve emit `podcast:chapters`. This is the sharpest waste in the sample: the expensive human judgment about where topics begin and end is already being performed, then written into prose where nothing can address, query, or deep-link it. The `package/chapters/` directory in this repo exists and is empty. Filed as `package/chapter-timestamp-index-in-description`.

## One Show Worth Watching

**The Home Service Expert.** It is the least glamorous show in the sample — a trades and home-services B2B interview show sitting at #19 — and it has built the one thing almost nobody else here has: a complete owned canonical layer. All 511 episodes resolve to 511 unique URLs on `homeserviceexpert.com`, sustained across roughly eight years and multiple format shifts. Not a host subdomain, not a network page, not a homepage dump. Every episode has an address the show owns, which means every episode is a permanent, migratable, linkable asset rather than a row in someone else's database.

What makes it instructive rather than just admirable is the asymmetry. It is the most committed show here on Publish and among the weakest on Package — 1 of 511 episodes carries per-episode artwork, descriptions run the shortest in the sample at ~917 characters, and there are no transcripts or chapters. It also returns a 403 to a plain scripted fetch of those episode pages; whether AI crawlers are allowlisted is not determinable from outside, but it is worth flagging against candidate `5b348762` that infrastructure defaults can quietly gate the retrievability of the exact asset you spent eight years building.

The lesson is that the owned canonical layer is a choice available to a niche B2B operator with no network behind it, and that having it is not the same as having filled it. The Home Service Expert has built 511 front doors. The next move is putting something machine-readable behind each one.

## Methodology

- **Source:** Apple Podcasts Business chart (U.S.), September 2026, top 25 via the iTunes top-podcasts feed (genre 1321), retrieved 2026-09-20.
- **Sample:** 12 shows, all twelve new to this teardown series — selected from the fourteen top-25 shows not covered in the August 2026 sweep, spanning #3 to #24 and 20 to 1,182 episodes. Sample skews independent and mid-tier by construction; comparisons to August are cohort comparisons, not time-series.
- **Data:** Publicly observable only — RSS feeds (3,068 episodes parsed), public websites, rendered structured data, public YouTube and social links. No private analytics, no paywalled data.
- **Framework:** OMI 5P (Produce → Package → Publish → Prove → Preserve). Gap bar for a teardown-candidate: a practice present in 3+ of the 12 shows with no existing OMI pattern and no open Workboard card.
- **Caveats:** Single snapshot. Two sites (`provenpodcast.com`, `seancallagy.com`) were unreachable from our fetcher and are excluded from site-level counts; one returned 403 to scripted requests. JS-heavy sites may render structured data client-side that a plain fetch does not see, so schema counts are a floor, not a ceiling. One intended sample show was swapped for The Code To Winning after its feed host blocked automated retrieval. Prove-stage findings are intentionally thin — public performance data effectively does not exist for this cohort.
