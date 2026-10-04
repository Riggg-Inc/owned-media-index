# Published-page fact check — 2026-10-04 v1

Reviewer: Cass Reelman, AI — openai/gpt-6-astra. No human signoff.
Start: 2026-10-04T16:45:23Z. Source reading completed: 2026-10-04T16:48:17Z.
Base: origin/main 76020a518f02ea1e49c955972a5147a8cb88dc8f. Isolated branch: review/fact-check-2026-10-04. Primary dirty checkout untouched.

## Queue and identity
126 published pages, including 86 Articles; 126 due (125 unreviewed, one expired partial), zero registry errors. This differs from yesterday's 125 because Measurement's retry expired. No publication occurred yesterday; its three proposals are still open.

Skip exact-body proposals: evidence.md fda7c2464edc7cbdcaf5aefd4e401bc0adcc3d55a0b4f2d50b49b66ffb48c513 (card 3f310466-8571-4a31-8ea8-7f3be3ba9275), framework.md 5d2081da100f8525c5c0a8ca6e552210ff6f758e9f5885165a6d06dedbf1669c (4823a06e-d037-43e7-bbce-dbbbf6743bec), index.md 1f48724164ca94e101fb6e15e791995cda333adb5cea48e9fbbc5dd88341e47d (42dce931-c8d7-47b5-82a0-ce1c6a3c603e). Matched current queue against yesterday's report/tasks and open board cards. No matching fact-check proposal exists for the selected three paths.

Selected in CLI risk/age order: Measurement (AI-search priority), Owned Media, Data Drop (high risk, unknown review age; lexical tie-break). Full bodies read, not just snippets. Debate Moment was read during candidate inspection but NOT selected, checked or registered.

## Evidence interpretation
Source files preserve URL, actual fetchedAt UTC and extracted content; source-map.md records exact excerpts and verdicts. A fetch is not evidence of performance. Truncated extractions support only the visible quoted sections, never unseen sections. Public vendor documentation supports what is documented, not independent efficacy. No paid tool, login-only source, customer data or private metrics accessed. No platform interfaces were executed. Practitioner recommendations, sample sizes and prompt durations are not empirical findings.

## Measurement — partial, no confirmed body correction
Path: patterns/publish/ai-search-optimization/measurement.md
Body SHA256: a743c2475f1b934884fd4db693303d4af1fcf95acd27d43593338a00466f228a

- Opening, What It Is, Why It Matters: the three-layer distinction (sampled answers, platform counts, attributable visits/outcomes) is measurement guidance. A citation does not itself demonstrate a visit, inquiry or causal effect. No claimed measured lift.
- Direct Signals Google row, different-model/trigger paragraph, Proxy index requirement: supported by google-ai.json, sections How AI features work, Technical requirements and Measuring performance: overall Search Console Web, varying links/models, Overviews often do not trigger, indexed/snippet eligible, no additional technical requirement.
- Bing row and tool row: bing.json supports named metrics, Microsoft Copilot/Bing summaries/select partners, sample grounding phrases, no rank/placement inference. It describes an introduced dashboard, not merely a future promise. URL/title calls it public preview; current account availability and whether the preview label is still exhaustive are not independently established. Keep qualified status; do not claim universal availability or a GA release.
- ChatGPT query rewriting, approximate location, saved memories, source links and incomplete/outdated/incorrect citations: supported by chatgpt.json. No inference that an API response reproduces consumer UI.
- Proxy structured data: schema.json explicitly says quality guidelines are not easily testable automatically; valid syntax is not sufficient for rich results. It does not establish AI citations or factual correctness.
- Proxy URL Inspection: inspection.json distinguishes indexed and live status; “URL is on Google” does not guarantee appearance. site.json says site: need not return all indexed URLs. Featured snippets are instructed to be counted separately, not claimed to predict AI exposure.
- Competitive Signals and six-step workflow: practitioner design, denominator explicitly panel responses, not population/market share. 10–15 questions and two repetitions are recommendations, explicitly not statistical confidence. No outcomes are reported.
- GA4 report route/session source-medium/new-versus-returning distinction and key events: acquisition.json supports the report and dimensions; channel scope definitions in channels.json distinguish session/user/event. Availability in a specific property/history remains untested.
- AI Assistant versus Organic Search: channels.json supports named AI sources and exclusion of Google AI Overviews/Mode from AI Assistant. No historical rollout date or retroactive reclassification proven.
- ChatGPT utm_source=chatgpt.com: utm.json explicitly documents it for search-result referrals. This does not establish a universal medium or every arrival retaining tags.
- Direct/none and source loss through missing tags, redirects/shorteners/ad blockers: direct.json supports. Broad Bing traffic cannot identify a particular sending interface without additional evidence; recommendation not to infer it is sound.
- Weekly/monthly/quarterly and 48-hour check: recommendations, not platform deadlines. recrawl.json says days to weeks.
- Ahrefs: ahrefs.json documents Custom Prompts and AI Visibility Index, prompts modeled from its keyword database. Vendor evidence supports marketed functionality only, not accuracy, unbiased coverage, account access or causal business value. No purchase/test performed.
- Quality Bar/When Not To Use: operating recommendations, not outcome claims. Score 3 and evidence wording unchanged.

Unresolved: property-level report availability, historical channel coverage, present preview lifecycle, cross-interface execution, independent vendor accuracy. These unresolved items are retained from the previous partial scope, not falsely closed by re-fetching docs. All cited primary URLs were freshly retrieved. No substantive textual error confirmed within the supported documentation scope. Proposed partial record only; next targeted retry 2026-10-11T16:48:17Z. Do not re-fetch the same unchanged documentation daily while this exact-hash proposal is open. Next owner: Cass for scoped account/rollout evidence; Beacon only after authorized release checks.

## Owned Media — partial; two confirmed overclaims
Path: owned-media.md
Body SHA256: ab915437082f29dcfa77d443ca4a597c4b395ec99d6a1e1d5d0476b83ab6c6e5

- “The asset ... is always owned”, “you created it, you own it”, “What you create is always yours”, and Asset test: contradicted as universal ownership assertions. copyright-html.json, Who is a copyright owner?, explains employment works made for hire, some commissioned works, assignments/transfers. Originality section also excludes titles/short phrases from copyright. This is US primary guidance, not a global legal opinion or adjudication of any customer's rights. Operational asset categories are not themselves copyright determinations.
- “no third party can revoke your access” and “losing the platform means losing nothing”, including a podcast hosting account: contradicted as unconditional availability/control statements. transistor.json, Account suspension and deletion, reserves suspension/deletion of accounts. Owning masters or controlling a domain/feed is distinct from host account access, delivery, discovery and monetization. No equivalence between these layers.
- YouTube asset/distribution distinction: youtube-terms.json says “You retain ownership rights in your Content” but requires rights/licenses and reserves changes to the service. Supported for retained existing rights, not proof a person owns every component they upload. “eliminate the audience relationship entirely” is too absolute: no source proves loss of independently retained contacts. Proposed qualification below.
- 5Ps and asset/channel category lists: Riggg's editorial taxonomy, not an external empirical finding. No stage/score/rule change made. Because this is a definition page, changes require owner/framework review rather than automatic correction.
- PESO authorship/year (Dietrich, 2014), four quadrants and social placement: not freshly confirmed; primary Spin Sucks page returned HTTP403. Retry with accessible author material, do not substitute a search snippet. Preserve uncertain status.
- Platform table: examples are not a claim that platforms have identical ingestion, hosting, monetization or export. Only YouTube terms checked in this run; Apple/Spotify/LinkedIn/Instagram/X/Facebook feature availability and hosting/feed portability were NOT independently validated. This is a material scope limit, not a blanket pass.
- “These compound over time and power AI search discoverability”: unsupported as an assured outcome. google-ai.json supports useful textual content and ordinary SEO, not a causal guarantee that vector libraries/schema create citations. Recommendations should be phrased as intended benefits.
- Prove “Owned by definition”, all-package “Fully owned”: same rights qualification applies; no private customer records accessed to establish ownership.

### Exact proposed wording (internal only, not applied)
1. Replace definition paragraph with: “At Riggg, owned media means content you hold the necessary rights to use and channels where you retain practical control over the audience relationship. That control can still depend on providers, contracts, permissions and portable backups.”
2. Replace the asset bullet with: “The asset is distinct from its distribution platform. Retain masters and confirm ownership or sufficient licenses, including contributor agreements and third-party components; creating or uploading a file alone does not establish every right.”
3. Replace “These are the only channels where losing the platform means losing nothing — because you own the relationship.” with: “These channels can improve continuity when you retain the necessary rights, audience permissions, independent exports and a migration path. A hosting account is still subject to its provider's terms.”
4. Replace “A channel termination or policy change would eliminate the audience relationship entirely.” with: “A channel termination or policy change can remove access to that platform audience; independently retained, permissioned relationships may remain.”
5. Replace Asset test with: “Do you own or hold sufficient rights to retain, reuse and distribute it, including all incorporated components?”
6. Qualify all repeated “always owned”, “always yours”, “fully owned”, “Owned by definition” statements consistently using the rights test; revise Preserve sentence to “These assets can support retrieval and reuse; AI-search visibility must be measured rather than assumed.”
These are review proposals, not adopted framework rules. A final full-page revised artifact, mirror reconciliation, re-audit and exact-revision dashboard decision are mandatory before publication. No rewrite hash is attached to the current public body.
Retry: 2026-10-11T16:48:17Z; human review remains required regardless of retry date. Garren/Ledge own definition decision; Cass owns source gaps.

## Data Drop — partial; performance evidence missing
Path: patterns/package/clips/data-drop.md
Body SHA256: e67e1ac9a3b6003a01bf25e6f3a0eeca6609918ea901582ecb5346c9f7875f54

- Definition/opening, selection criteria and When Not To Use: editorial selection recommendations, not measured findings. “surprises/reframes” describes intended selection, not an assured effect on every viewer.
- “Data creates authority”, “Data clips perform well because they give the audience something concrete to reference”: uncertain causal/performance assertions. No disclosed dataset, comparison, metric, sample size or measured clip outcome supplied. Public source pages do not substantiate them.
- Score 4 / “internal production data”: present in current body, but substantiation was not available in public sources. Never infer private customer support or change this score/evidence label automatically. Auditor must determine what safe generalized evidence can support it through the existing rules.
- Prof G: profg.json states “analysis ... business, power, and society. All data, zero filter” and names Scott Galloway. Supports first-party positioning only, not a verified episode, quotability or clip results.
- Freakonomics: freakonomics.json names the podcast and discusses economics topics and surprising questions. Supports show identity/topic context; not “Built around surprising data points” for every episode or measured reframing.
- a16z: a16z.json states podcast discusses technology with people building it, topics AI/energy/genomics/space. Supports the show identity and topical context, not specific market statistics or Data Drop effectiveness.
- All three show rows remain teardown starting points, as the page already warns. No episode timestamp/transcript was obtained; the show-level claims of specific recurring mechanics remain uncertain. No source passage was treated as episode-level verification.
- Prompt 30–60 seconds is a requested output constraint, not tested runtime. “The more context ... the better the output” is an unmeasured universal quality claim, not demonstrated by these sources.

### Exact proposed wording (internal only, not applied)
Replace Why It Works with: “A well-sourced statistic can give viewers a concrete point to examine or discuss. This is a practitioner selection rationale, not evidence of better clip performance; measure retention and other relevant outcomes for your audience.”
Replace final prompt sentence with: “Provide relevant audience, guest and episode context, then check the generated selection against the source and intended use.”
Retain the existing show-level warning; do not strengthen attributed examples until an exact public episode/quote supports each. No score or evidence-label change proposed under this task; missing substantiation is an Auditor blocker.
Retry: 2026-10-11T16:48:17Z. Cass/Auditor must obtain safe performance evidence or present an honestly limited revised artifact for exact human decision.

## Release disposition and failures
All three statuses PARTIAL. No substantive corrections, public fact-check records, timestamps, scores, tracking, rules or drafts published. Public due count remains 126. Proposed records bind OLD PUBLIC BYTES only and must not be carried onto rewritten bodies. No Last updated bump.
The internal partial records defer retries by seven days; open exact-revision task/proposal identity is the durable skip mechanism until adoption. Do not merge the proposed store wholesale over newer production reviews.

Failures: initial workspace skill and primary-checkout procedure paths were absent; recovered by installed skill and isolated origin/main worktree. Initial shell file probes for scripts/*review* and deploy.yml did not exist (queue itself succeeded). Two Code Mode quoting errors dispatched no commands; recovered with direct reads. Spin Sucks primary PESO retrieval HTTP403; Copyright FAQ guessed URL HTTP404; circular PDF response not suitable readable evidence, recovered using official copyright HTML. Several web extractions were truncated: only visible sections were evaluated, not assumed complete. Workboard list transport was truncated once; repeated with bounded relevant fields. No hidden source failures counted as support. Source claims and limitations remain explicit.

Validation and canonical task links are recorded alongside this report. Build/tests are mechanical checks, not source verification or approval. Human approval is absent; publication/deployment was not attempted.

## Validation outcome
Strict MkDocs build passed; validate_site audited 127 HTML pages / 8182 references with zero errors; validate_aeo covered 126 pages with zero errors; validate_freshness and production fact-check validation passed; all 57 regression tests passed. See validation.txt. Proposed evidence store validates independently with zero errors and would defer these three entries (123 due); production remains 126 due. Tests used unchanged public content/registry, not a deployed proposal. No live freshness claim.

Additional tool limit: validate_freshness.py has no --help handler; invoking it before building actually ran validation and correctly reported 126 missing built pages. The subsequent strict build and real validator passed. Earlier failed lookup attempts and retrieval limits above remain documented. Proposed records completed at 2026-10-04T16:51:17.124Z after source analysis. Stable hashes recomputed with content_hash() all matched. No public bytes changed.
