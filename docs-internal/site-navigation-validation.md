# Site navigation validation

The MkDocs build publishes only `docs/` content. Repository pattern drafts outside that directory are not site destinations. The `docs/overrides/` directory supplies templates and is explicitly excluded from output.

## Breadcrumbs

`hooks/breadcrumbs.py` builds one shared trail for HTML navigation and JSON-LD from the actual documentation file registry. It walks existing ancestor `index.md` pages, including those omitted from `nav`, skips directories without an index, and uses published page titles/URLs. Home is a single current crumb. The 404 page has an accessible recovery trail but deliberately no canonical BreadcrumbList.

The template uses an ordered list, a named navigation landmark, a non-linked `aria-current="page"` endpoint, hidden decorative separators, keyboard focus indication, and wrapping rather than truncation on narrow screens. Homepage navigation precedes the animated hero.

## Run before deployment

	.venv/bin/mkdocs build --strict
	.venv/bin/python scripts/validate_site.py
	.venv/bin/python -m unittest discover -s scripts -p 'test_*.py' -v

Use the installed `mkdocs`/`python` commands in CI. The existing Pages workflow runs the audit and tests before artifact upload. The audit checks generated HTML, because MkDocs does not resolve/check raw HTML hrefs the same way as Markdown links. It checks all same-origin links/resources, HTML fragments, breadcrumb presence and HTML/JSON-LD parity. External URLs are not network-tested.

## 2026-09-30 repair findings

- 123 content pages plus the 404 page: 124 navigation trails; 123 matching BreadcrumbLists.
- 39 quadrant raw-HTML URLs had one too few parent-directory segments; all now resolve to existing published patterns.
- The OBS template download had the same issue; fixed against the existing JSON asset.
- Four code-formatted Related Patterns repository references in the HLS distribution page now link to their existing published equivalents.
- All 16 Related Patterns sections audited: 24 clickable links now resolve.
- Homepage template headings now preserve the five anchor destinations exposed by its Markdown-generated navigation (nine broken fragment references previously).
- Raw template copies were incorrectly being shipped as HTML; excluded rather than treated as public pages.
- Final generated audit: 7,760 internal link/resource references, zero errors. Nine regression tests pass; strict build passes. Source-level responsive/semantic checks completed; no browser executable is installed in this environment, so visual viewport verification remains a release smoke check.

### References intentionally left unlinked

No existing published equivalent was found for these code-formatted references; do not copy their drafts into `docs/` or invent a nearby destination:

- HLS distribution: `package/reels/vertical-reel-package-standard.md`.
- AMP Accords: `preserve/ad-metadata-brand-safety/ad-metadata-brand-safety.md`.
- AMP Accords: `publish/syndication/spotify-native-upload-bypasses-rss.md`.
- AMP Accords: `preserve/podcasting2-transcript-namespace.md` (already marked not yet written).

These are unresolved publication/editorial references, not broken clickable links.

## Deployment

This change does not publish or push. After approval, push the scoped commit to `main`; `.github/workflows/pages.yml` builds, validates and deploys the Pages artifact. Confirm workflow success and smoke-test Home, a nested off-nav title page, a deep social-post leaf, a quadrant link and the OBS download on `https://index.riggg.com/`. Check 320px mobile and desktop, light/dark themes and keyboard navigation. Keep the unrelated dirty `prove/benchmarks/video-threshold-economics.md` draft out of the deployment commit.
