# OMI discoverability and answer-quality publication standard

Applies to existing-page revisions and every newly approved public page. This is an implementation checklist, not a change to the framework, score rubric, evidence rules, or human approval contract.

## Author and review

1. Read the actual approved page and its sources. Give it a distinct, faithful description and a direct opening answer to its main question; preserve a good existing introduction rather than adding filler. Explain applicability, limits and examples where relevant. Policy and contribution pages should describe their actual purpose, not mimic a pattern.
2. Make category and comparison hubs useful for choosing: summarize existing documented differences in readable text/tables and link to real published destinations. Preserve anchors. Do not turn practitioner judgment into an empirical ranking.
3. Link primary sources beside factual claims where available, verify that the source supports the precise claim, and record unresolved evidence gaps in the audit. Label hypothetical examples. Existing evidence labels or a link to a show homepage do not independently prove a claim. Preserve human review/score-change gates. Never invent reviewer names, dates, outcomes or citations.
4. The homepage omits its redundant single-item Home trail and BreadcrumbList (owner-requested design exception). Interior pages retain the full breadcrumb requirement. Keep breadcrumbs visible, keyboard-accessible and consistent with actual published hierarchy and BreadcrumbList. Never link a repository draft as though it were a public page.

## Build and release

5. Keep one description meta tag, canonical URL and safely serialized structured data matching visible page content. Use appropriate page types. Include editorial dates only with verifiable provenance; a build date is not an editorial update. Point robots.txt at the canonical sitemap.
6. In an isolated clean checkout of current origin/main, run the strict MkDocs build and both scripts/validate_site.py and scripts/validate_aeo.py against the resulting output; run regression tests. CI and the publisher must reject failed validation. Preserve customer-data scans, exact-revision approval, unrelated working files and no-smuggled-commit safeguards.
7. Inspect the scoped diff, commit/push only authorized changes, verify deployment success and live canonical pages. Check mobile/desktop/keyboard behavior when a browser is available; disclose when verification is HTML-only. Record measured page/test counts and proof, not a generic success claim.

## Measure without fabricating results

8. Use the fixed question panel in aeo-measurement-panel.json to compare observations over time. Record engine/interface/model where available, UTC time, exact prompt, geography/login context when relevant, response artifact and exact cited URLs. General web-search results are not evidence of ChatGPT, Perplexity or Google AI citations. Repeat samples and report variance.
9. Report Search Console indexing and Web performance separately from answer-engine citations. Track attributable AI referral visits and defined conversions only when analytics access and events exist. Do not equate a citation with a conversion or promise inclusion. If an integration is unavailable, mark that metric unavailable rather than zero.
10. Include these checks in each publication and the existing monthly AEO review. Keep unresolved evidence and access gaps visible with an owner. Do not start paid services, change tracking/privacy policy or schedule new jobs without the appropriate authorization.

## Homepage freshness exception
Never display the Last updated / Last fact-checked section on `/` (`docs/index.md`). This is the only published content page exempt from the shared display; retain it on all interior pages. Keep homepage provenance/review records intact. Run `scripts/validate_freshness.py` each cycle; any homepage display or missing interior display blocks publication.
