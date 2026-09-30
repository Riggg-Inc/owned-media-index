# Discoverability measurement baseline — 2026-09-30

## Executed observations

- DuckDuckGo via available web_search: `site:index.riggg.com "owned media"` returned no results.
- Same interface: `site:index.riggg.com "Contrarian Hook"` returned no results.
- Follow-up exact-host query `"index.riggg.com"` failed with a provider connection/configuration error.

These are limited, inconclusive public-search observations. They do **not** establish that the site is absent from Google/Bing indexes or uncited by an answer engine. Provider failure further limits confidence; do not record this as zero AI visibility.

## Access limitations

No Search Console or analytics integration was found in available tools or the inspected workspace scripts/docs; site configuration/templates showed no GA/plausible/umami integration. No authenticated property access, conversion event definitions, or direct answer-engine observation interface has been verified. Browser execution was unavailable in the navigation run. Therefore indexing coverage, AI citation baseline, referral traffic and conversions remain **unmeasured**, not zero. No tracking code, paid service, credential or policy change was introduced.

## Ready for repeatable measurement

The fixed ten-question panel and observation schema are in `aeo-measurement-panel.json`. Use them in the existing monthly AEO review. Capture actual answer-engine responses and cited URLs once an authorized interface is available. Search Console access and analytics property/event access require the property owner if not already connected. Keep technical page-quality checks separate: they can pass without proving a citation or ranking improvement.
