# Contributing

The Owned Media Index is a practical library of patterns, standards, tools, and benchmarks for owned media.

## Good Contributions

Good contributions are:

- Specific.
- Evidence-informed.
- Useful in real production.
- Clear about tradeoffs.
- Free of vendor fluff.

## Entry Types

You can contribute:

- Patterns.
- Tool entries.
- Hardware entries.
- Benchmarks.
- Distribution standards.
- Corrections.
- Stale-entry reports.

## Pattern Standard

Every pattern should answer:

- What is it?
- Best for what?
- Why does it work?
- Example patterns.
- Quality bar.
- When not to use it.
- Score.
- Evidence.
- Related patterns.

## Scoring

- **5:** Recommended default. Strong evidence and broad usefulness.
- **4:** Strong fit. Works well in common scenarios.
- **3:** Viable. Useful with tradeoffs.
- **2:** Niche. Good for a narrow case.
- **1:** Not recommended as a default.

## Discoverability and answer quality

Every public page needs a unique, accurate description and a direct opening explanation. Pattern entries should explain when to use the pattern, limitations, and concrete examples; comparison hubs should help readers choose between linked published entries. Cite sources that support specific claims, distinguish illustrations from verified examples, and do not invent review dates or reviewer attribution.

Breadcrumbs, canonical URLs, metadata, structured data and internal links are validated during publishing. Run the strict site build, `scripts/validate_site.py`, `scripts/validate_aeo.py`, and regression tests before release. See [the publication checklist](docs-internal/aeo-publishing-standard.md). Existing evidence and approval requirements remain in force.

## Review

Riggg reviews contributions before merge. Accepted entries may be tagged `riggg-reviewed`.

