# AEO technical implementation — 2026-09-30

## Scope and identity

- Hook: `hooks/metadata.py`; templates serialize the **entire** graph with Jinja `tojson`, escaping quotes, backslashes, ampersands and script terminators.
- 124 content pages: 28 directory/home CollectionPages, 12 general WebPages, 84 editorial pattern/tool Articles with a separate canonical WebPage identity. No blanket FAQ, Review, Person or rating schema.
- Stable IDs: publisher `https://riggg.com/#organization`, site `https://index.riggg.com/#website`, canonical page URL + `#webpage`, `#article` and `#breadcrumb` as applicable.
- Titles reflect visible H1 rather than abbreviated nav labels. Existing visible breadcrumb names remain unchanged and their JSON-LD matches them.
- Material alone emits the description meta tag; explicit source descriptions must match OG, Twitter and JSON-LD. Duplicate normalized descriptions fail validation.
- Twelve homepage topic/highlight headings now link to actual published pages. What's New explicitly labels these as undated highlights, not a release log.

## Truthful dates

All generated publication, modification and review dates are omitted. The old blanket May 28 publication date was not verified. MkDocs' default update_date is build time, not substantive revision history. The sitemap override therefore omits lastmod entirely, including in the generated gzip companion. This is an intentional conservative policy, not missing telemetry.

CI checks out full history, but **does not claim commit dates are publication dates**: migrations, formatting-only changes, metadata-only edits and imported content make that inference unreliable. Future dates require a defensible substantive-edit/publication source, human review and matching validator changes. No review or author identity was fabricated. Publisher identity is not an author claim.

## Mechanical gates

Run from repository root, using the installed MkDocs environment:

Command sequence:

    mkdocs build --strict
    python scripts/validate_site.py [optional-built-site-directory]
    python scripts/validate_aeo.py [optional-built-site-directory]
    python -m unittest discover -s scripts -p "test_*.py" -v

Both validators accept a custom build directory. validate_aeo.py resolves source docs relative to its own repository, not the built-site location. Dependencies are stdlib plus PyYAML/Jinja already provided by MkDocs.

CI runs strict builds and both validators plus regression tests on pushes, manual runs and pull requests. PRs never deploy or upload deployment artifacts. The existing link/breadcrumb gate covers every built HTML page including off-nav leaves and the not-found page, with draft/template nonpublication regression coverage. The AEO gate covers canonical content pages (not 404), description uniqueness/parity, types and entity IDs, H1 parity, canonical/OG URLs, undated sitemap URL-set parity and robots sitemap discovery.

Summary coverage requires each Article to have a real introductory paragraph/What It Is definition before detail sections (minimum ten words is a structural floor, not an editorial target). Existing Sources/References/Evidence sections require an external citation somewhere on-page or explicit observational/internal basis. This **does not prove a source supports a claim**, that a summary is accurate, or that a source is still available; those remain human evidence-review gates. No automated gate upgrades evidence labels or scores.

## Verification / handoff

Initial strict build passed. Link gate: 125 HTML pages (124 content + 404), 7,961 internal link/resource references (latest shared-worktree build), zero errors. Latest regression run: 14/15 passed; AEO reports 105 errors at this intermediate shared-worktree snapshot; the all-pages AEO test deliberately blocks on unfinished parallel content edits (missing descriptions and source gaps), not schema/breadcrumb failures.

At initial validation, existing uncited Evidence sections on `patterns/prove/amp-accords-play-standard.md` and `patterns/produce/recording/hls-video-podcast-distribution.md` need content-worker attention. Preserve claims/scores; add only verified supporting links or explicitly record the gap. Rerun all gates after workers finish; do not waive the blocker silently.

No commit, stage, push or deployment performed by this worker. No Markdown content pages changed by this worker. No framework/evidence/scoring rules altered.
