# Top Business Podcasts Teardown — November 2026

## About This Analysis

We took twelve shows from this week's Apple Podcasts Business top 25 and read everything they publish in public: RSS feeds (the latest 30 episodes of each), owned websites, episode pages, and show notes. Then we checked what we saw against the Owned Media Index (OMI), Riggg's open framework of evidence-backed patterns for owned media. The question isn't who's popular. It's which of the practices that make a show an owned asset, rather than a tenant on someone else's platform, the biggest shows actually follow, and which ones even they skip.

## Shows Analyzed

- **The Prof G Pod with Scott Galloway** (#5) — Vox Media flagship; interviews interleaved with "The Week" roundups, "Office Hours" listener Q&A, and audio essays from the newsletter.
- **Morning Brew Daily** (#6) — daily news two-hander from a newsletter company; 980+ numbered episodes.
- **Financial Audit** (#8) — YouTube-native reality format; listeners apply to have their finances audited on camera.
- **Odd Lots** (#11) — Bloomberg's markets interview show; the only feed in the sample shipping transcripts in RSS.
- **How I Built This with Guy Raz** (#12) — narrative founder interviews plus an "Advice Line" call-in format.
- **Money For Couples with Ramit Sethi** (#13) — real-couple coaching sessions, cast from an application form.
- **The Clark Howard Podcast** (#16) — 2,000+ episode consumer-money show with a fixed weekday segment rotation.
- **Money Guy Show** (#18) — two-advisor financial planning show; the strongest owned website in the sample.
- **The Compound and Friends** (#20) — markets roundtable from a wealth-management firm; disclosure-heavy and survey-driven.
- **The Best One Yet** (#21) — 20-minute daily business news trio; the most distinctive title system on the chart.
- **Moonshots with Peter Diamandis** (#22) — long-form AI and tech roundtable, often recorded live.
- **Business Wars** (#24) — Audible/Wondery narrative series built on multi-part rivalry arcs.

## What the Top Shows Are Getting Right

**Produce — fixed formats beat freestyle.** The chart rewards shows with a recognizable weekly shape. Clark Howard runs a named rotation ("Ask An Advisor" on Tuesdays, "Clark Stinks" on Fridays). How I Built This alternates founder stories with "Advice Line" episodes. Prof G interleaves interviews, "The Week," and "No Mercy / No Malice." That's `produce/audience-engagement/standardized-micro-segments` scaled up to the episode level: the listener knows what they're getting before they press play.

**Package — titles are built, not written.** Every show here has a title system, and the best ones are recognizable at a glance. The Best One Yet uses emoji + quoted headline + a stacked teaser list ("🚨 'Grand Theft PTO' — GTA 6 blast radius. SNL's millennial sister tax…"), which survives truncation because the hook comes first. Money For Couples titles each episode with the couple's own words and a dollar figure ("We're worth $1.8M, but I feel guilty buying a $78 jacket"). Business Wars uses a strict `Series | Chapter | Part` structure that makes its arcs navigable. All of this maps to `package/titles/top-performing-title-styles`.

**Package — descriptions clear the floor.** Median description length runs from about 600 to about 4,400 characters. Every show writes real prose with guest and topic context, not one-liners. Money For Couples ships a "⏩ CHAPTERS" block on every episode. That's `package/descriptions/rss-feed-description-patterns` in practice.

**Publish — the newsletter is the default owned channel.** At least eight of twelve push an email list from the show notes, many on nearly every episode: Odd Lots (about 87% of episodes), The Best One Yet (about 93%), The Compound (100%), Clark Howard's daily money newsletter, and Morning Brew's daily. Prof G Media's home page is itself a newsletter. `publish/owned-channels/owned-email-newsletter` is the one OMI pattern the top of the chart has fully absorbed.

**Publish — video is assumed.** At least eight of twelve send listeners to a YouTube version, and several now treat it as the main product. How I Built This promoted "our all-new YouTube channel" in this month's notes. The audio feed is turning into the distribution copy of a video show, which raises the stakes on `publish/youtube/title-and-description-standard` and `prove/benchmarks/video-threshold-economics`.

**Publish — feed basics are clean.** All twelve declare an owner email, categories, and `itunes:type`. Business Wars correctly marks itself `serial` for its multi-part arcs. Seven of twelve attach item-level artwork to every or nearly every episode.

## What's Missing (Even at the Top)

**Canonical episode pages — mostly absent.** Nine of twelve feeds leave the episode `<link>` empty or nearly always empty. Two more point it at their hosting company's page rather than their own site. Only Money Guy links every episode to a page on its own domain. Everywhere else there's no stable URL the show controls for a given episode, so every citation, share, and AI answer points at Apple, Spotify, or YouTube. This is the core of `publish/website/canonical-episode-page`, and it's the biggest gap at the top of the chart.

**Podcasting 2.0 metadata — essentially zero.** Eleven of twelve feeds contain no `podcast:` namespace tags at all: no `podcast:guid`, no `podcast:chapters`, no `podcast:person`. Odd Lots is the lone exception, and only for transcripts. `publish/rss/feed-metadata-standard` covers this. The top shows just don't do it.

**Chapters are written, then wasted.** Money For Couples (every episode) and Financial Audit (about 83%) hand-write timestamp blocks into their descriptions. Zero of twelve publish machine-readable chapters. Same finding as September: the judgment work gets done, then stored where nothing can use it.

**Transcripts — rare, and usually not owned.** Only three of twelve make transcripts publicly available: Odd Lots in the feed via `podcast:transcript`, Money Guy as full text on its own episode pages, and Clark Howard through a link to a third-party transcript host. For answer engines, most of the chart doesn't exist as text.

**Structured data — almost none.** Only one show's website, Morning Brew Daily's, publishes `PodcastSeries` / `PodcastEpisode` structured data. `preserve/ai-optimization/geo-aeo-citation-volatility` assumes you've given answer engines something structured to cite. Most of these shows haven't.

**Video never reaches the feed.** All twelve feeds carry audio-only files, and none offers an alternate video file. The video lives only on YouTube, on rented ground. That's the gap `produce/recording/hls-video-podcast-distribution` exists to close.

**Prove — nothing public.** No show publishes audience or performance data of its own beyond chart badges. Whatever measurement happens, happens privately.

## Patterns We Don't Have Yet

Four practices cleared the bar this month: present in at least three of the twelve shows, with no existing OMI pattern and no open card. They're filed as candidates for scoring, not recommendations.

**1. Standing casting funnels (6 of 12).** The show runs a permanent, owned submission form, and the submissions *are* the episode. Money For Couples: "Apply to be coached for free on this podcast" on 27 of the last 30 episodes. Financial Audit: "We film weekdays in our studio in Austin… To apply, visit calebhammer.com/apply." Clark Howard points listeners to Ask Clark and the "Clark Stinks" submission page on every episode. How I Built This's Advice Line features "today's callers." The Best One Yet: "GET ON THE POD: Submit a shoutout or fact." Prof G's Office Hours specials answer submitted listener questions. The OMI covers in-session audience engagement, but not the intake system that turns an audience into a content supply chain and a first-party data asset. Filed as `produce/audience-casting-intake`.

**2. Live tapings as owned events (5 of 12).** Shows use ticketed or registered live tapings as tentpole episodes and audience-building events. Odd Lots: "See Odd Lots live in NYC on Dec. 9. Tickets on sale!" Morning Brew Daily promotes tickets to its Holiday Spectacular on most episodes. The Best One Yet published "LIVE from Seattle." Money For Couples drives free registrations to live sessions. Moonshots tags episodes "(recorded live)." The OMI has a simulcast standard for live streaming but nothing on in-room tapings as an owned event, where the registration list is the asset. Filed as `produce/live-taping-as-owned-event`.

**3. Listener surveys as owned research (3 of 12).** The Best One Yet links a two-minute survey on 29 of its last 30 episodes. The Compound asks listeners to "take our 2026 audience survey." Money Guy goes further and turns survey results into episodes ("We Asked 20K Americans How They Manage Money"). It's the only first-party audience measurement visible anywhere in the sample, and the OMI's Prove stage has nothing on it. Filed as `prove/listener-survey-first-party-data`.

**4. Stacked measurement redirects (9 of 12).** Nine shows send every download through two or more third-party measurement redirects before the audio file. The longest chain in the sample has eight hops, and one still includes a redirect from a measurement service that shut down in 2024. Each hop is a vendor that sees every listener request, one more point of failure, and a dependency nobody seems to audit. The OMI covers *what* to measure (`prove/measurement/amp-accords-play-standard`) but not how to govern the chain itself. Filed as `prove/enclosure-prefix-chain-governance`.

One more practice showed up but wasn't filed: owned communities (Odd Lots' Discord, Clark Howard's community forum, Financial Audit's member app). It appears in three shows, but a community is a product rather than recorded media, so it sits outside the OMI's current scope.

## One Show Worth Watching

**Money Guy Show.** It's the only show in the sample where the owned website is the episode's real home. Every one of the last 30 feed items links to a page on moneyguy.com. That page carries the full transcript with timestamps, an embedded YouTube video, an email signup, and links out to the listening apps. The feed points at the site, the site holds the text, and the text is crawlable. That's the canonical-episode-page pattern done properly at chart scale. They also turn their own listener research into content ("Are You Richer Than Your Friends? (New 2026 Data)"), which is the proprietary-data playbook running live.

What's left is cheap compared with what they've already built. The pages use a generic `Article` type instead of `PodcastEpisode`, the feed has no per-episode artwork, and the feed carries neither chapters nor a `podcast:transcript` tag, even though the transcript already exists on the page.

## Methodology

- **Chart:** Apple Podcasts US Business top 25, week of November 16–20, 2026. Apple's marketing-tools chart endpoint returned 404 this month, so the ranking comes from Apple's legacy iTunes RSS chart feed (top 10, live on November 20), cross-checked against Podshot's daily Apple Business mirror (November 20) and Media List's November 16 snapshot.
- **Sample:** 12 of the top 25. We excluded shows covered in the August and September teardowns (The Ramsey Show and its Highlights feed, The Diary Of A CEO, Planet Money, Marketplace) and sampled across formats: daily news, interview, roundtable, call-in, coaching, and narrative.
- **Data:** Publicly observable only. For each show: its RSS feed (latest 30 episodes parsed for tags, links, descriptions, and enclosures), its owned website and at least one episode page where reachable (checked for structured data, transcripts, email capture, and video embeds), and links in show notes. Some sites blocked automated requests (Bloomberg, Clark.com, iwt.com); for those we relied on feed content and partial page text. YouTube channels were noted from show-note links, not audited.
- **Framework:** OMI 5P — Produce → Package → Publish → Prove → Preserve. Percentages are the share of each show's latest 30 episodes unless noted.
