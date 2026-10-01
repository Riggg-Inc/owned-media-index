# OMI search, analytics and answer-engine growth plan

Owner: Cass. Decision owners: Garren and Ledge where framework/editorial approval is required.
Site: https://index.riggg.com/
Date: 2026-09-30

## Goal
Owner-confirmed October 1: OMI is an SEO/AEO credibility resource for Riggg. Build credible discovery and citations, send qualified visitors to riggg.com, and drive information requests through the main Riggg website—not a separate OMI lead funnel. Track OMI-to-Riggg visits as a micro-conversion; real inquiries must be verified on riggg.com. Subdomain content does not automatically confer rankings on the main site: earn relevance through useful content, attributable publisher identity, contextual links and external citations. Indexability is a prerequisite, not proof of indexing; traffic is not itself a business outcome.

## Verified baseline
- Public homepage, robots.txt and sitemap return HTTP 200 without authentication.
- Release baseline has 124 published content pages. Keep repository drafts out of the build.
- Canonical links already point to index.riggg.com; robots advertised the old github.io sitemap.
- 63 pages had explicit descriptions; 61 used the generic site description. Some emitted two description tags.
- Structured data called all pages Articles, hardcoded publication dates and treated build dates as edits. Sitemap lastmod also represented rebuild time.
- No active GA tag found in sampled live HTML or repository configuration. Google property ownership, actual indexing, traffic and conversions are not verified without account access.
- Existing bibliography/evidence/scoring and deep-link breadcrumbs are assets to retain.

## Phase 1: technical foundation — current release
- Fix robots sitemap reference; retain existing crawler permissions (no change to training-bot policy).
- Emit exactly one description per page. Preserve authored descriptions; derive absent descriptions from existing visible paragraphs, not new editorial claims. Editorial review can later replace these fallbacks.
- Serialize JSON-LD safely; identify WebSite, Organization, WebPage/CollectionPage and pattern TechArticle appropriately; preserve breadcrumb parity.
- Omit unknown publication/revision dates and sitemap lastmod rather than manufacture freshness. Later introduce verified, visible editorial revision dates through the publication workflow.
- CI verifies all published page metadata, sitemap URL count/host, JSON validity, breadcrumb/internal links and analytics configuration constraints.
- Wire optional GA4 with explicit opt-in, reject/manage controls and a preferences link. Disabled until a measurement ID and approved privacy-policy URL are supplied. No ads signals, raw search queries, form values or URL queries/fragments intentionally sent by the custom code. Page views plus riggg_visit clicks only; a click is NOT a lead.

## Phase 2: activate discovery and measurement — week 1 after owner handoff
### Google Search Console
1. Reuse an existing verified riggg.com domain property if available; otherwise create a property for index.riggg.com. DNS verification is strongest for a domain property; URL-prefix verification can use a Google HTML file/meta token.
2. Owner performs Google login. Supply the verification TXT value or HTML/meta token if implementation help is needed; never share passwords/session cookies.
3. Submit https://index.riggg.com/sitemap.xml in Search Console. Inspect homepage, owned-media definition, framework, one hub and several priority pattern URLs; request indexing for priority pages where appropriate, not mass repetitive submissions.
4. Record Google-selected canonical, crawl status, robots accessibility, rendered content, indexing exclusions and sitemap acceptance. Do not treat a site: search as an indexing inventory.
5. Add Bing Webmaster Tools (import verified Search Console where available) and submit the same sitemap. GitHub Pages cannot implement automatic server-side IndexNow without additional integration; optional, not a blocker.

### GA4
1. Prefer the existing Riggg GA4 property if it supports the intended OMI-to-Riggg journey; create an OMI web stream or choose the existing shared stream deliberately. Avoid two competing tags and duplicate page views. Use direct GA4 for this simple static site; GTM only if the team already standardizes on it.
2. Supply the G- measurement ID and an approved public privacy-policy URL covering the actual use. Review applicable consent/privacy requirements; this template is not legal certification. Existing embedded media and third-party assets also need a separate privacy review.
3. In GitHub repository Actions variables, set OMI_GA_MEASUREMENT_ID and OMI_PRIVACY_URL; build/deploy via the existing workflow. Supplying only an ID fails the build intentionally.
4. Before activation, browser-test no analytics requests before consent, rejection, acceptance, persistence and withdrawal/reload. Inspect actual outbound payloads for PII, full query strings and accidental duplicate hits. Disable unneeded Enhanced Measurement (especially site-search/form collection); review retention, Google Signals and ad personalization in the property.
5. Verify consented page_view and riggg_visit in DebugView/Realtime. The latter is a micro-conversion. Confirm real generate_lead/booking events on the destination only after successful form/booking completion; do not relabel an outbound click as a lead.
6. Align tag/property and cookie configuration across index.riggg.com and riggg.com where needed. Do not add UTMs to ordinary links between them; that distorts attribution. If the journey moves to another domain, configure cross-domain measurement deliberately.
7. Exclude internal/developer traffic after testing; link Search Console to GA4; document consent-denied and ad-blocked measurement gaps.

## Phase 3: demand and content — days 1–30
Working audience assumption to confirm: B2B marketing leaders and expert-led companies implementing owned media. Working conversion: qualified strategy/implementation inquiry to Riggg.

- Inventory all 124 URLs with intent, stage, evidence quality, author/reviewer accountability, current metadata, internal links and conversion path. Map one preferred URL per intent; check near-duplicate pages before creating more.
- Use Search Console queries once available plus direct buyer questions to choose the first 10 priority URLs. Start with existing owned-media definition/framework, pattern hubs, video investment economics, title/clip choices, distribution, measurement and AI-search resources. These are hypotheses, not keyword-volume claims.
- Refresh 10 high-value pages rather than bulk-generate new pages: direct opening answer, when to use/not use, concrete example, defensible evidence with primary-source links, related alternatives and useful next action. Preserve existing review/score/source gates.
- Name real accountable authors/reviewers only when approved and actually involved. Publish truthful review dates and methodology. No fabricated expertise, statistics, case studies or freshness.
- Add a contextual conversion path approved by Garren: recommended default is 'Get help implementing this' to a real Riggg inquiry/booking page. Add newsletter signup only if an owned list and follow-through actually exist. No new CTA destination is invented in this release.
- Measure field Core Web Vitals when data exists; run mobile Lighthouse and inspect homepage animation, fonts/images and YouTube embed loading. Optimize based on measurements, not assumed scores.

## Phase 4: authority and answer visibility — days 31–60
- Strengthen existing hubs and comparison resources with readable selection criteria, alternatives, limitations and link paths. Avoid new pages that duplicate current intent.
- Produce 2–3 genuinely differentiated resources from approved knowledge: decision worksheet, transparent benchmark/methodology, or comparison matrix. New resource proposals go through normal editorial approval; private customer inputs remain private.
- Link OMI from relevant Riggg website pages, episode/show notes, newsletters and approved team profiles. Repurpose each substantial update into useful distribution with links to its canonical OMI resource. Outreach/posts require their normal send approvals; no paid-link schemes.
- Establish a fixed 20-question panel across buyer stages. Sample Google AI experiences, ChatGPT search, Perplexity and Bing/Copilot manually or with an approved provider. Record exact question, date, region, engine/model, whether an AI answer appeared, cited URLs, OMI citation, competitors and captured evidence. Repeat samples to reflect volatility.
- Distinguish mention, citation, referral visit and conversion. AI referral traffic undercounts citations/no-click answers; Search Console Web aggregates Google AI-feature traffic with ordinary search.

## Phase 5: iterate — days 61–90
- Refresh pages with impressions but poor click-through, prioritize high-intent pages with engagement but weak next steps, and improve pages earning citations but not qualified visits.
- Review crawl/index exclusions, duplicate/canonical issues and actual search demand before expanding publishing volume.
- Decide whether paid AI visibility tooling is worth the cost based on the manual baseline. No paid tool purchase is required for phase 1.
- Publish a monthly scorecard and a prioritized next batch. Set numerical growth targets only after a 28-day reliable baseline; do not promise rankings, citation inclusion or arbitrary lead counts.

## Scorecard
- Technical: sitemap submitted/accepted; priority URLs indexed; canonical/exclusion issues; Core Web Vitals coverage.
- Search: non-brand impressions/clicks/CTR by landing page and intent; branded traffic separate; compare 28-day periods and seasonality when data exists.
- Content: organic engaged sessions, useful resource paths, return visits (consent-dependent).
- AEO: panel citation rate per engine and cited URLs with evidence, not an opaque blended score.
- Business: riggg_visit clicks, verified inquiry/booking completions, qualified leads and influenced pipeline with human CRM confirmation. Never equate a click or citation with revenue.

## What Garren needs to provide
1. Existing Search Console ownership/access status for riggg.com or index.riggg.com; verification value if a new property is needed. A signed-in owner browser session can be used for setup where available.
2. Existing GA4/GTM status and the intended GA4 measurement ID (G-...). This ID is public, not a password. Confirm whether OMI and the main website should share a measurement journey.
3. Approved privacy-policy URL and permission to activate consent-gated analytics after validation.
4. Primary audience, primary conversion and exact inquiry/booking URL. Recommended default above; confirm or replace it.
5. Later, access to approved aggregate search/analytics reports and main-site integration if we are to maintain the scorecard and verify real conversions.

## Boundaries and evidence
No Google account property created, verified or sitemap submitted by this release. No analytics property invented; tracking remains off without configuration. No ranking/indexing/citation guarantee. No new editorial knowledge or private source material published. Existing framework and human review gates stay intact.

Google's own guidance says AI-feature eligibility uses ordinary SEO fundamentals and has no additional technical requirement or special schema: https://developers.google.com/search/docs/appearance/ai-features (checked 2026-09-30). Prioritize helpful, crawlable, cited content over llms.txt, generic FAQ markup or content volume.
