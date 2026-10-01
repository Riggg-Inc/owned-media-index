# OMI analytics activation — October 1, 2026

Owner supplied GA4 measurement ID G-T1FBFDLCRE and https://riggg.com/privacy-policy/. Production build values live explicitly in .github/workflows/pages.yml (public identifiers, not secrets). Local builds remain off unless the two environment variables are supplied. To roll back activation, clear OMI_GA_MEASUREMENT_ID in the workflow and redeploy; no tag loads. Earlier instructions to set Actions variables are superseded by these explicit release values.

Purpose: build Riggg SEO/AEO credibility and drive qualified traffic to riggg.com; actual leads happen on the main website. Events: page_view and riggg_visit (outbound Riggg clicks, NOT leads). No OMI-only form/newsletter added.

Search Console: owner reports existing riggg.com property, no separate OMI property. If it is a Domain property, index.riggg.com is already included; submit the OMI sitemap and filter performance by the subdomain. If it is only https://riggg.com/ URL-prefix, add https://index.riggg.com/ or verify a Domain property through Cloudflare TXT. Only an authenticated Search Console view can establish the property type and actual indexing. Do not claim verification or submission from DNS/HTTP accessibility alone.

Required owner account checks after browser QA: confirm GA4 Realtime/DebugView receipt; disable unnecessary enhanced site-search/form events; inspect retention, advertising settings and developer traffic filters; review both domains in the desired measurement journey; instrument real successful inquiry completion on riggg.com. Main-site access/account UI is not provided by a public measurement ID.

Privacy link was checked reachable. Policy mentions cookies/technical information generically; recommend the owner/legal reviewer explicitly cover Google Analytics, OMI/subdomains, optional consent/withdrawal and actual retention/transfers. This implementation is not a legal compliance certification.

## Browser acceptance test

`scripts/check_analytics_browser.cjs` uses Playwright Chromium against the built site by default, or `OMI_TEST_URL` for the live site. Set `PLAYWRIGHT_MODULE` and `CHROMIUM_EXECUTABLE` to installed test-runtime paths where needed; `OMI_TEST_REPORT` writes a JSON artifact. This is an integration test that intentionally sends a small number of test events to the configured property—do not count those as customer demand.

Checks include: no Google analytics request before consent, persisted rejection, explicit opt-in, exactly one explicit page view, sanitized original referrer retained across the consent reload, Riggg-click event, persisted acceptance, working footer preferences, and no new analytics after withdrawal/reload. Google endpoint acceptance is not a substitute for checking the property reporting UI and real lead completion.

A site-wide footer now links visitors to Riggg services. No UTMs are appended to OMI-to-Riggg links. Query/fragment text is excluded from page/referrer/link fields; advertising signals are disabled in code. Campaign-tag reporting and main-site attribution settings need an account-level review before claiming end-to-end acquisition reporting.
