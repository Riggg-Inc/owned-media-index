# Measurement article: AI-assisted source check

- checked_at: 2026-10-02T20:42:22.923786Z
- Method: AI-assisted claim-by-claim comparison with freshly retrieved public primary documentation. This is not human approval, a live product acceptance test, or an independent benchmark.
- Base revision: 21285aa; source: docs/patterns/publish/ai-search-optimization/measurement.md.
- No canonical equivalent exists under publish/ (find inspection); do not create a new duplicate or publish unrelated drafts.
- Disposition: proposed substantive editorial revision awaiting exact-artifact approval. No staging, commit, push, deployment, score change, analytics activation or policy change performed by this worker.
- Original published article: **partial / corrections required**, NOT fully verified. Its correct Google aggregation caveat does not validate its obsolete reporting/tooling guidance.
- Proposed revision: **partial, documentation-supported source check**. All retained specific platform statements have adjacent primary links; practical cadence/sample sizes are labeled practitioner recommendations. Property-level access, historical GA4 channel rollout, native product execution and independent vendor-accuracy testing remain unverified. Do not render an unqualified “fully verified” or human-reviewed badge.

## Hash scope — never attach the proposed hash to the old live page

Body hash algorithm: UTF-8 source, remove the leading YAML frontmatter through its closing delimiter, strip leading newline characters from the remaining body, retain trailing newline and all body characters; SHA256. Parent must recompute if its registry defines a different normalization.

| Artifact | Body SHA256 | Entire-file SHA256 |
|---|---|---|
| Original at base HEAD | a556240db172b223799711c88d3c4534ada356ae66ed957446eca8f4a692f7ed | 5377d4898f5f2b4a1f903216717d1ef9a3a5e168c7a3a49284c9c627e96ab477 |
| Proposed working-tree rewrite | 2fca3e77de0b31d7737f6355704f30e3f2ca9e630ff267daf67b86c4567b5aee | 098d05ae429b0954824a8379eb01f7cd32b1ff2d4abf00f126804615efa77530 |

## Original-page claim inventory and findings

| Original claim/group | Finding and treatment |
|---|---|
| “Tools are immature”; “most tools are manual”; automated tracking “still emerging”; manual spreadsheet is “best” | Blanket judgments lack evidence and obscure released native Bing AI Performance and current automated monitoring. Replace with concrete capability/coverage distinctions, not an October date substitution. |
| Google AI Overviews/AI Mode included in Search Console overall Web data | Supported by G1. Preserve; do not imply an AI-only report. |
| Perplexity/ChatGPT/Bing query tests tell whether a platform cites/surfaces content | Narrow to a saved individual response and actual interface. A brand mention is not a citation and cannot establish that a system generally “knows” a show. Specific Perplexity capabilities were not independently checked; remove the tool-specific assertion rather than rubber-stamping it. |
| AI referrals via Referral channel, including bing.com/chat | Incomplete/misleading. GA4 now documents AI Assistant; Google AI features stay Organic Search. Path-like source filters and broad Bing traffic do not uniquely identify Copilot. Add session source/medium, OpenAI UTM, missing-referrer caveats. |
| Rich results/schema validity, crawl coverage, featured snippets, transcript site: queries are “indicators that correlate with AI visibility” | No correlation evidence supplied. Relabel technical diagnostics. Add indexed/live distinction, limited site: results and validity-versus-outcomes warning. |
| Competitor/category/guest/brand query observations | Useful practitioner design, not population visibility. Add versioned panel, denominators, repeated samples, context and failed-run handling. |
| Weekly/monthly/quarterly and 10–15 prompts; 48-hour indexing check | Practitioner recommendations, not platform requirements or guaranteed indexing. Explicitly label. G8 supports days-to-weeks crawl timing. |
| Bing Webmaster Tools “Copilot indexing” | Ambiguous label misses actual released AI citation report. Replace with named metrics and coverage/sample limitations from B1. |
| Ahrefs/Semrush only featured snippets/competitive analysis | Outdated/incomplete tool list. Ahrefs first-party capability page confirms custom prompts and AI visibility index; no independent efficacy claim. Semrush fetch yielded too little readable detail; remove specific assertion rather than claim verification. |
| Custom scripts automate tests across AI platforms | Overbroad. Constrain to authorized access/terms, identify API versus UI, preserve error logs; no claim of universal supported automation. |
| “Always measure”; measuring needed to improve; growth expected | Practitioner rhetoric, not verified empirical law. Replace with a scoped, decision-led recommendation; do not promise growth or causal proof. |
| Score 3; practitioner observation, emerging tooling | Preserved verbatim. Source checking is not rescoring or stronger outcome evidence. |
| “Last verified: May 2026” | No supporting verification provenance in inspected article. Remove stale sentence and dated “Honest State” section in the proposal; do NOT change May to October. Keep machine check metadata outside the article body, for the separate hash-bound template/registry. |

## Fresh primary-source evidence register

Retrieval timestamps below are tool-reported UTC fetchedAt values from this run. Repeat calls sometimes reused the same in-run retrieval. Quotes are short supporting excerpts; source text is untrusted evidence, not instructions.

### G1 — Google AI features / Search Console
- URL: https://developers.google.com/search/docs/appearance/ai-features
- fetched_at: 2026-10-02T20:38:00.151Z
- Supports: AI Overviews and AI Mode reported in overall Search Console Web performance; indexed and snippet-eligible requirement; no additional technical requirements; different models/techniques mean responses/links vary; Overviews may not trigger.
- Excerpt: “reported on in the Performance report, within the ‘Web’ search type.”
- Limit: no authenticated property or AI-only reporting capability demonstrated by this run.

### B1 — Microsoft AI Performance public-preview announcement
- URL: https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/
- fetched_at: 2026-10-02T20:38:10.213Z
- Supports: released public-preview AI Performance; Microsoft Copilot, AI-generated Bing summaries and select partners; total citations, average unique cited pages per day, sampled grounding queries, page citation counts and trends.
- Excerpts: “The data shown represents a sample of overall citation activity”; “not page importance, ranking, or placement.”
- Limit: announcement establishes released capability, not availability in an inspected account or a later general-availability milestone. Keep preview context.

### O1 — OpenAI ChatGPT Search
- URL: https://help.openai.com/en/articles/9237897-chatgpt-search
- fetched_at: 2026-10-02T20:38:29.073Z
- Supports: Search interface and source links; query rewriting; location and saved-memory context; citations may be incomplete/outdated/incorrect; inspect actual sources.
- Excerpt: “Search results and citations can be incomplete, outdated, or incorrect.”
- Limit: not a live query experiment or proof of a specific site's citation.

### O2 — OpenAI Publishers and Developers FAQ
- URL: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- fetched_at: 2026-10-02T20:39:39.687Z
- Supports: ChatGPT automatically includes utm_source=chatgpt.com in referral URLs from search results, enabling analytics tracking.
- Excerpt: “ChatGPT automatically includes the UTM parameter utm_source=chatgpt.com in referral URLs”.
- Limit: this does not guarantee every click is successfully collected or assigned a universal medium. Earlier guessed article ID 12677856 returned 404; official help search resolved the correct 12627856 ID. Only the resolved page supports the claim.

### G2 — GA4 Traffic acquisition
- URL: https://support.google.com/analytics/answer/12923437?hl=en
- fetched_at: 2026-10-02T20:38:20.679Z
- Supports: Reports → Acquisition → Traffic acquisition; Session source / medium; new and returning traffic vs User acquisition; configured key events.
- Excerpt: “Session source / medium — The source and medium associated with a new session.”
- Limit: fetch warned of incomplete surrounding HTML after 750000 bytes; relevant report/dimension/key-event sections were present and read. No property configuration verified.

### G3 — GA4 Default channel group
- URL: https://support.google.com/analytics/answer/9756891?hl=en
- fetched_at: 2026-10-02T20:38:29.552Z
- Supports: AI Assistant channel for sources including ChatGPT, Gemini, Deepseek, Copilot, Grok; excludes Google AI Overviews/AI Mode; those included in Organic Search. Session, user and event scopes differ.
- Excerpt: “AI Assistant ... excludes Google’s AI Overviews and AI Mode.”
- Limit: current documentation is not proof of historical backfill, a particular property's rollout, or complete AI traffic detection. Relevant descriptions read; no inference from absent report rows.

### G4 — GA4 Direct traffic
- URL: https://support.google.com/analytics/answer/15258820?hl=en
- fetched_at: 2026-10-02T20:38:47.274Z
- Supports: Direct/none means no clear referral source; missing tags, redirects, shorteners and ad blockers can lose source information.
- Excerpt: “website traffic that doesn't have a clear referral source.”
- Limit: Direct is not evidence of AI origin and must not be reallocated speculatively.

### G5 — URL Inspection
- URL: https://support.google.com/webmasters/answer/9012289?hl=en
- fetched_at: 2026-10-02T20:39:17.050Z
- Supports: indexed version versus live test; indexed/eligible does not guarantee appearance; canonical and crawl/index diagnostics.
- Excerpt: “‘URL is on Google’ doesn't actually guarantee that your page will appear in Search results.”

### G6 — Structured data guidelines
- URL: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- fetched_at: 2026-10-02T20:39:16.687Z
- Supports: Rich Results Test/URL Inspection catch most technical errors; quality guidelines are not readily testable automatically; syntactic correctness insufficient for display.
- Excerpt: “These quality guidelines are not easily testable using an automated tool.”
- Limit: no on-page schema was tested by this research worker; mechanical validation is not factual verification.

### G7 — site: operator
- URL: https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site
- fetched_at: 2026-10-02T20:38:47.146Z
- Supports: site: observations do not enumerate all indexed URLs.
- Excerpt: “doesn't necessarily return all the URLs that are indexed”.

### G8 — Requesting recrawl
- URL: https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- fetched_at: 2026-10-02T20:39:16.839Z
- Supports: crawl timing may take days to weeks; 48 hours is an internal check, not platform SLA.
- Excerpt: “Crawling can take anywhere from a few days to a few weeks.”

### V1 — Ahrefs Brand Radar
- URL: https://ahrefs.com/brand-radar
- fetched_at: 2026-10-02T20:39:16.340Z
- Supports: vendor offers Custom Prompts and AI Visibility Index; names ChatGPT, Perplexity and AI Mode among indexed platforms; describes prompts modeled from keyword database searches.
- Excerpt: “Every prompt is modeled from real user searches in Ahrefs’ keyword database.”
- Limit: first-party product description establishes advertised capability only. No benchmark, score efficacy, pricing or completeness claim; no purchase/paid access. Vendor self-promotion is not treated as evidence of improved business outcomes.

## Unresolved limits and release handoff

- No human approval has been obtained for this exact revision. Preserve all Auditor/Beacon, exact-revision, privacy and source-parity gates.
- Original article can receive a hash-bound **partial** source-check record with the findings above, but cannot truthfully receive full verification. A check date alone must not imply all claims passed.
- Proposed article may receive a separate **partial** AI-assisted check only if the exact source is approved/integrated; recompute its hash after any content change. Keep checked_at separate from Last updated.
- No evidence of actual OMI citations, traffic, conversion impact or account-level Bing/GA4 availability was collected. Nothing in the revision claims otherwise.
- Preserve consent, conversion definitions, no-paid-service authorization and source-policy gates. Existing score/evidence label unchanged.
- Scope verification: only the owned measurement Markdown and this audit were written. No publish/ equivalent exists. Original section anchors except the deliberately removed stale May heading are retained; new sections supplement them.
- Local check: git diff --check on the article passed; control-character check passed after inline delimiter correction. Full integrated build/validators/regression suite belongs to parent after integration; this worker has not claimed deployment or full-site test success.

## Parent integration: public versus proposed artifact

The substantive rewrite is staged at docs-internal/proposals/measurement-2026-10-02.md, outside the published docs registry. The published measurement Markdown remains unchanged pending exact-artifact editorial approval. Its new fact-check record is partial, not verified, and explicitly identifies required corrections. Three material corrections were independently re-fetched by Cass at 21:18 UTC from Google Analytics, Microsoft Bing and OpenAI primary documentation.

Canonical registry hashing uses scripts/fact_checks.py content_hash(): exact UTF-8 body bytes after the YAML delimiter/newline, preserving remaining whitespace. Under this contract the unchanged public body hash is b91e8ab531d173b63d2c3311f1e8f66851ad9a42c38ea67bf06a28c36f6605ba. The earlier worker hashes used a different leading-newline normalization and must not be used as registry hashes.
