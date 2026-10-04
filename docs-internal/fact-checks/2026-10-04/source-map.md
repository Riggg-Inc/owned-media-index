# Primary source excerpts and verdicts

Read with report-v1.md for exact article claims and limits. These are actual retrieved passages, not HTTP-based verification.

## google-ai
URL: https://developers.google.com/search/docs/appearance/ai-features
Observed: 2026-10-04T16:47:07.503Z
Extraction truncated: false
Verdict: Supported: Google AI features aggregate in Search Console Web; technical eligibility is not citation proof.

overall search traffic in
 [Search Console](https://search.google.com/search-console/about).
 In particular, they're reported on in the [Performance report](https://support.google.com/webmasters/answer/7576553),
 within the ["Web" search type](https://support.google.com/webmasters/answer/7576553#by_search_type).
 Learn more about how [AI Overviews](https://support.google.com/webmasters/answer/7042828#ai-overviews&zippy=%2Ct%2Cai-overviews)
 and [AI Mode](https://support.google.com/webmasters/answer/7042828#ai-mode&zippy=%2Ct%2Cai-mode) are counted
 towards the overall data in Search Console, how to
 [analyze traffic changes](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops)
 overall, and how to [combine Search Console and Analytics data](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console).

 In addition to Search Console, you could also track conversions and time spent on your site in
 other tools, such as Google Analytics. We've seen that when people click from search results
 pages with AI Overviews, these clicks are higher quality (meaning, users are more likely to spend
 more time on the site).

## Contr

## bing
URL: https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/
Observed: 2026-10-04T16:47:07.067Z
Extraction truncated: false
Verdict: Supported: native report metrics and sampled grounding; current property access uncertain.

Total Citations

Shows the total number of citations that are displayed as sources in AI-generated answers during the selected time frame. This highlights how often your content is referenced by AI systems, without indicating placement or presentation within a specific answer.

Average Cited Pages

Shows the average number of unique pages from your site that are displayed as sources in AI-generated answers per day over the selected time range. Because the data is aggregated across supported AI surfaces, average cited pages reflect overall citation patterns and does not indicate ranking, authority, or the role of any page within an individual answer.

Grounding queries

Shows the key phrases the AI used when retrieving content that was referenced in AI-generated answers. The data shown represents a sample of overall citation activity. We will continue to refine this metric as additional data is processed.

Page-level citation activity

Shows citation counts for specific URLs from your site, making it easy to see which individual pages are most often referenced across AI-generated answers during the selected date range. This reflects how often pages are cited, not page importance, ra

## channels
URL: https://support.google.com/analytics/answer/9756891?hl=en
Observed: 2026-10-04T16:47:07.696Z
Extraction truncated: true
Verdict: Supported: AI Assistant excludes Google AI Overviews/Mode.

AI Assistant
 AI Assistant is the channel by which users arrive at your site from sources like ChatGPT, Gemini, Deepseek, Copilot, or Grok. It excludes Google’s [AI Overviews and AI Mode](https://blog.google/products/search/ai-mode-search/).

 Audio
 Audio is the channel by which users arrive at your site/app via ads on audio platforms (e.g., podcast platforms).

 Cross-network
 Cross-network is the channel by which users arrive at your site/app via ads that appear on a variety of networks (e.g., Search and Display).

 Direct
 Direct is the channel by which users arrive at your site/app via a saved link or by entering your URL.

 Display
 Display is the channel by which users arrive at your site/app via display ads, including ads on the Google Display Network.

 Email
 Email is the channel by which users arrive at your site/app via links in email.

 Mobile Push Notifications
 Mobile Push Notifications is the channel by which users arrive at your site/app via links in mobile-device messages when they're not actively using the app.

 Organic Search
 Organic Search is the channel by which users arrive at your site/app via non-ad links in organic-search results, including Google’s [AI

## chatgpt
URL: https://help.openai.com/en/articles/9237897-chatgpt-search
Observed: 2026-10-04T16:47:58.685Z
Extraction truncated: false
Verdict: Supported: query rewriting, location and memory affect context.

typically rewrites your query into one or more targeted queries that it sends those providers. For instance, if a biotech researcher asked ChatGPT, “what’s the latest on the development of drugs that target CCR8 for cancer?” ChatGPT might initially query a search partner using “CCR8 immunotherapy drug development 2025.” After reviewing the initial results, ChatGPT search may send additional, more specific queries to other search providers, like “CHS-114 conference 2025.” ChatGPT also collects general location information based on your IP address and may share that general location with third-party search providers to improve the accuracy of your results. For example, if you type into ChatGPT “What are some good restaurants near me?” and ChatGPT determines from your IP address that you are in the San Francisco area, ChatGPT may rewrite your prompt into the search query “top restaurants San Francisco.” ChatGPT does not share the IP address itself, or any of your ChatGPT account information, with third-party search providers in order to run the search.
For more information about how search providers may process queries, review their privacy policies:

- [Microsoft privacy statement](h

## utm
URL: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
Observed: 2026-10-04T16:47:58.193Z
Extraction truncated: false
Verdict: Supported: documented ChatGPT UTM; not universal arriving medium.

automatically includes the UTM parameter utm_source=chatgpt.com in referral URLs, enabling clear tracking and analysis of inbound traffic from ChatGPT search results.

### Does ChatGPT Atlas train on my web page content?
Publishers should disallow the [GPTBot user-agent](https://openai.com/bot/) from sites and pages they wish to exclude from potential training. We respect this signal for content acquired via users’ interactions in Atlas.
Note: if users opt-in to training, webpages that opt out of GPTBot will not be trained on.

## Developer FAQs

### What can I do to improve my website performance with ChatGPT agent in Atlas?
Making your website more accessible helps ChatGPT Agent in Atlas understand it better.
ChatGPT Atlas uses ARIA tags—the same labels and roles that support screen readers—to interpret page structure and interactive elements. To improve compatibility, follow[WAI-ARIA best practices](https://www.w3.org/WAI/ARIA/apg/) by adding descriptive roles, labels, and states to interactive elements like buttons, menus, and forms. This helps ChatGPT recognize what each element does and interact with your site more accurately.

### How do apps built with the Apps SDK work in

## acquisition
URL: https://support.google.com/analytics/answer/12923437?hl=en
Observed: 2026-10-04T16:47:59.369Z
Extraction truncated: true
Verdict: Supported: session source/medium dimension.

Session source / medium
 The source and medium associated with a new session.
 To learn how to populate this dimension, see [Traffic-source dimensions, manual tagging, and auto-tagging](https://support.google.com/analytics/answer/11242870).

 Session source platform

 The platform where you manage buying activity (i.e., where budgets and targeting criteria are set).

 Examples include:

- 'DV360' (traffic from Display & Video 360 marketing activity)

- 'Google Ads' (traffic from Google Ads marketing activity)

- 'Manual' (traffic that isn't from Google media marketing activity)

- 'SA360' (traffic from Search Ads 360 marketing activity)

- 'SFMC' (traffic from Salesforce Marketing Cloud marketing activity)

- 'Shopping Free Listings' (traffic from Google Merchant Center marketing activity)

 To learn how to populate this dimension, see [Traffic-source dimensions, manual tagging, and auto-tagging](https://support.google.com/analytics/answer/11242870).

## Metrics in the report

The report includes the following [metrics](https://support.google.com/analytics/answer/9355664). If you are an [Editor or Administrator](https://support.google.com/analytics/answer/9305587#zippy=%2Cgoogle-an

## direct
URL: https://support.google.com/analytics/answer/15258820?hl=en
Observed: 2026-10-04T16:47:59.272Z
Extraction truncated: true
Verdict: Supported: Direct has no clear referral source; source can be lost.

represents website traffic that doesn't have a clear referral source. Understanding your (direct) / (none) traffic helps you:

- Determine if your campaigns are effectively driving traffic.

- Ensure accurate crediting of traffic sources for better decision-making.

- Address technical issues that may lead to more accurate data and a smoother user journey.

## Reasons for (direct) / (none)

### Missing traffic information

- When links to your site lack UTM parameters or your site isn't integrated with marketing and advertising platforms, traffic source information is lost.

- Redirects (for example, from one site to another or from a secure site (https) to a non-secure site (http)) can strip UTM parameters from the URL.

- Using URL shorteners like bit.ly can also strip away referral details.

If this applies to you, check your marketing links, email campaigns, and social media posts to confirm they include correct UTM tags. You should ensure these tracking parameters remain intact when visitors arrive at your website.

### Users accessing your website directly or through offline documents

Traffic coming from users who visit your website by entering the URL directly into their br

## inspection
URL: https://support.google.com/webmasters/answer/9012289?hl=en
Observed: 2026-10-04T16:47:59.084Z
Extraction truncated: true
Verdict: Supported: indexed status not guarantee of appearance.

doesn't actually guarantee that your page will appear in Search results. The report [doesn't check all conditions](https://support.google.com/webmasters/answer/9012289?hl=en#not_tested) for appearing on Google. For a definitive test of whether your URL is appearing, search for the page URL on Google.

- If the URL redirects to another URL, the results reflect the tested URL in the index, not the redirect target in the index. To see the indexing results for the canonical of a redirected page, click the INSPECT button in the Page indexing > [Indexing](https://support.google.com/webmasters/answer/7645831) section.

#### Understanding the results

- Read the [overall page status](https://support.google.com/webmasters/answer/9012289?hl=en#presence_google) at the top of the tool to see whether or not the URL is eligible to appear in Google Search results: URL is on Google means that the URL is eligible to appear in Search results, but is not guaranteed to be there. URL is not on Google means that the URL can't appear in Search results.

- Expand the [Page indexing](https://support.google.com/webmasters/answer/9012289?hl=en#index_coverage) or [Video indexing](https://support.google.com/we

## schema
URL: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
Observed: 2026-10-04T16:47:58.686Z
Extraction truncated: true
Verdict: Supported: automated technical checks cannot establish quality.

These quality guidelines are not easily testable using an automated tool.
 Violating a quality guideline can prevent syntactically correct structured data from being
 displayed as a rich result in Google Search, or possibly cause it
 to be [marked as spam](https://support.google.com/webmasters/answer/3498001).

### Content

- Follow the [spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies).

- Provide up-to-date information. We won't show a rich result for time-sensitive
 content that is no longer relevant.

- Provide original content that you or your users have generated.

- Don't mark up content that is not visible to readers of the page. For example, if the JSON-LD
 markup describes a performer, the HTML body must describe that same performer.

- Don't mark up irrelevant or misleading content, such as fake reviews or content
 unrelated to the focus of a page.

- Don't use structured data to deceive or mislead users. Don't impersonate any person or
 organization, or misrepresent your ownership, affiliation, or primary purpose.

- Content in structured data must also follow the additional content guidelines or policies, as
 docum

## site
URL: https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site
Observed: 2026-10-04T16:47:58.444Z
Extraction truncated: false
Verdict: Supported: site operator is incomplete.

doesn't necessarily return all the URLs that are indexed
 under the prefix specified in the query. Keep this in mind if you want to use the
 site: operator for tasks like identifying how many URLs are indexed and serving
 under a prefix.

- A site: operator without a query (for example site:example.com)
 doesn't rank the results. It will generally show the shortest URL for the prefix at the top,
 but otherwise the results are relatively random.

 Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

 Last updated 2025-12-10 UTC.
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="a775ed3eaa40ca2c">>>

## recrawl
URL: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
Observed: 2026-10-04T16:47:58.275Z
Extraction truncated: false
Verdict: Supported: days-to-weeks crawl, no 48-hour SLA.

Crawling can take anywhere from a few days to a few weeks. Be patient and monitor progress
 using either the
 [Index Status report](https://support.google.com/webmasters/answer/7440203)
 or the
 [URL Inspection tool](https://support.google.com/webmasters/answer/9012289).

## Use the URL Inspection tool (just a few URLs)

 To request a crawl of individual URLs, use the
 [URL Inspection tool](https://support.google.com/webmasters/answer/9012289#request_indexing).
 You must be an
 [owner or full user of the Search Console property](https://support.google.com/webmasters/answer/7687615)
 to be able to request indexing in the URL Inspection tool.

 Keep in mind that there's a quota for submitting individual URLs and requesting a recrawl
 multiple times for the same URL won't get it crawled any faster.

## Submit a sitemap (many URLs at once)

 If you have large numbers of URLs, submit a sitemap. A sitemap is an important way for Google
 to discover URLs on your site. It can be very helpful if you just launched your site or
 recently performed a
 [site move](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes). A sitemap
 can also include additional meta

## ahrefs
URL: https://ahrefs.com/brand-radar
Observed: 2026-10-04T16:47:57.703Z
Extraction truncated: true
Verdict: Supported as vendor description only; accuracy uncertain.

Every prompt is modeled from real user searches in Ahrefs’ keyword database.
448
M+

Total monthly prompts

IndexPrompts

AI Overviews

313,747,187

ChatGPT

30,587,601

Gemini

30,584,294

Perplexity

30,364,765

Copilot

30,216,088

AI Mode

12,893,994

### Track your brand mentions across AI answers and see how often you show up in the conversations that matter.

### Benchmark your brand against competitors in AI search and spot the big players.

### Find valuable AI citations and secure new mentions to boost your visibility in LLM answers.

### Preview your AI visibility for free

For example,

3
AI Analytics

## See which pages AI sends traffic and bots to

AI traffic

### Find the pages AI search already sends traffic to, then create more of what’s working.

Bot visits

### Watch AI crawlers in real time: when they read your pages and which ones they visit most.

4
AI Sources

## Track the offsite sources that influence AI visibility

## Used by 3,000+ companies

Before Brand Radar, I was testing scripts and manually extracting AI responses from ChatGPT, AI Overviews, all the main AI-search platforms. With Brand Radar, it’s now just a few clicks to identify what I need, and e

## copyright-html
URL: https://www.copyright.gov/what-is-copyright/
Observed: 2026-10-04T16:48:16.584Z
Extraction truncated: false
Verdict: Contradicted: creating an asset ALWAYS gives its creator ownership. US scope.

Companies, organizations, and other people besides the work’s creator can also be copyright owners. Copyright law allows ownership through “works made for hire,” which establishes that works created by an employee within the scope of employment are owned by the employer. The work made for hire doctrine also applies to certain independent contractor relationships, for certain types of commissioned works.

 Copyright ownership can also come from contracts like assignments or from other types of transfers like wills and bequests.

## What rights does copyright provide?

 U.S. copyright law provides copyright owners with the following exclusive rights:

- Reproduce the work in copies or [phonorecords](https://www.copyright.gov/title17/92chap1.html).

- Prepare derivative works based upon the work.

- Distribute copies or phonorecords of the work to the public by sale or other transfer of ownership or by rental, lease, or lending.

- Perform the work publicly if it is a literary, musical, dramatic, or choreographic work; a [pantomime](https://www.copyright.gov/circs/circ52.pdf); or a motion picture or other audiovisual work.

- Display the work publicly if it is a literary, musical, dra

## transistor
URL: https://transistor.fm/terms/
Observed: 2026-10-04T16:47:58.040Z
Extraction truncated: true
Verdict: Contradicted: a hosted account cannot lose access / loses nothing on provider loss.

Account suspension and deletion
The Owner reserves the right, at its sole discretion, to suspend or delete at any time and without notice, User accounts which it deems inappropriate, offensive or in violation of these Terms.
The suspension or deletion of User accounts shall not entitle Users to any claims for compensation, damages or reimbursement.
The suspension or deletion of accounts due to causes attributable to the User does not exempt the User from paying any applicable fees or prices.

### Content on this Application
Unless where otherwise specified or clearly recognizable, all content available on this Application is owned or provided by the Owner or its licensors.
The Owner undertakes its utmost effort to ensure that the content provided on this Application infringes no applicable legal provisions or third-party rights. However, it may not always be possible to achieve such a result.
In such cases, without prejudice to any legal prerogatives of Users to enforce their rights, Users are kindly asked to preferably report related complaints using the contact details provided in this document.
Rights regarding content on this Application - “Some-rights-reserved”
Unless where ex

## youtube-terms
URL: https://www.youtube.com/static?template=terms
Observed: 2026-10-04T16:47:06.755Z
Extraction truncated: true
Verdict: Supported with rights caveats: platform license distinct from ownership.

You retain ownership rights in your Content. However, we do require you to grant certain rights to YouTube and other users of the Service, as described below.

License to YouTube

By providing Content to the Service, you grant to YouTube a worldwide, non-exclusive, royalty-free, sublicensable and transferable license to use that Content (including to reproduce, distribute, prepare derivative works, display and perform it) in connection with the Service and YouTube’s (and its successors' and Affiliates') business, including for the purpose of promoting and redistributing part or all of the Service.

License to Other Users

You also grant each other user of the Service a worldwide, non-exclusive, royalty-free license to access your Content through the Service, and to use that Content, including to reproduce, distribute, prepare derivative works, display, and perform it, only as enabled by a feature of the Service (such as video playback or embeds). For clarity, this license does not grant any rights or permissions for a user to make use of your Content independent of the Service.

Duration of License

The licenses granted by you continue for a commercially reasonable period of time a

## freakonomics
URL: https://freakonomics.com/about/
Observed: 2026-10-04T16:47:07.126Z
Extraction truncated: false
Verdict: Supported: show/topic identity. Uncertain: recurring data mechanism or performance.

Freakonomics Radio](https://freakonomics.com/series/freakonomics-radio): Stephen Dubner explores things you always thought you knew (but didn’t) and things you never thought you wanted to know (but do). Some of our most popular episodes are about the economics of sleep and how to become great at just about anything, plus the true stories of rent control, minimum wage, and the gender pay gap.

[No Stupid Questions](https://freakonomics.com/series/nsq/): Research psychologist Angela Duckworth (author of Grit) and tech and sports executive Mike Maughan really like to ask people questions, and they believe there’s no such thing as a stupid one. So they have a podcast where they can ask each other as many “stupid questions” as they want. No Stupid Questions is a production of the Freakonomics Radio Network.

[People I (Mostly) Admire](https://freakonomics.com/series/people-i-mostly-admire): Steven Levitt, the unorthodox University of Chicago economist and co-author of the Freakonomics books, tracks down other high achievers — from sports superstars to Nobel Prize winners — and asks questions that only he would think to ask.

[The Economics of Everyday Things](https://freakonomics.com/se

## a16z
URL: https://a16z.com/podcasts/
Observed: 2026-10-04T16:47:07.227Z
Extraction truncated: false
Verdict: Supported: show/topic identity. Uncertain: specific market data or clip results.

The a16z Podcast discusses the most important ideas within technology with the people building it. Each episode aims to put listeners ahead of the curve, covering topics like AI, energy, genomics, space, and more.

 [Learn more](https://a16z.com/podcasts/a16z-show/)

## Raising Health

 A myriad of AI, science, and technology experts explore the real challenges and opportunities facing entrepreneurs who are building the future of health. Join a16z and hosts Olivia Webb and Kris Tatiossian in conversations with the pioneers behind these advancements.

 [Learn more](https://a16z.com/podcasts/raising-health/)

## web3 with a16z crypto

 A show about the next generation of the internet, and about how builders and users now have the ability to not just “read” (web1) + “write” (web2) but “own” (web3) pieces of the internet, unlocking a new wave of creativity and entrepreneurship.

 [Learn more](https://podcasts.apple.com/us/podcast/id1622312549)

## In the Vault

 “In the Vault” is a new audio podcast series by the a16z Fintech team, where we sit down with the most influential figures in financial services to explore key trends impacting the industry and the pressing innovations that wil

## profg
URL: https://www.profgmedia.com/
Observed: 2026-10-04T16:47:57.916Z
Extraction truncated: false
Verdict: Supported: first-party positioning only. Uncertain: episode specifics, quotability and results.

Uncompromising analysis of the forces transforming business, power, and society. All data, zero filter. Go paid for exclusive content from Scott Galloway and the Prof G crew — and skip the ads for good.
Over 424,000 subscribers

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).
<<<END_EXTERNAL_UNTRUSTED_CONTENT id="d3f7f8d8b793ee90">>>
