# Independent narrow homepage review — 2026-10-13

**Recommendation: ready for owner review as a narrow factual-only draft.** No blocking defect in the proposed changes. Internal draft readiness only, not a published quality assessment; no cards, publication, or assessment quota consumption. Rejected broad proposal 9bc305c is superseded and was not the acceptance standard.

## Scope and findings

Read both homepage files in full, including CSS; both current scoring policies; and linked sources listed below. Compared working tree against HEAD/base 42ddb64b5dfe341004f70111178c5e159893f5e6. Tracked diff: exactly two homepage files, 16 lines added / 16 removed. No CSS, markup structure, classes, URLs, layout configuration, or unrelated tracked files changed. git diff --check passes. Text wrapping may naturally change; this was source review, not rendered-browser visual assessment.

- **Score 5:** all three revised explanations match current public policy: recommended default, strong evidence, broad usefulness. Editorial criteria match both policies. Root SCORING.md allows strong evidence **or internal production validation**, not mandatory industry-standard status or benchmark proof. No policy redesign.
- **Rankings/outcomes:** “Editorially ranked” / “Riggg-Ranked” correctly distinguish recommendations from measured top performance. “Designed to help” makes description benefits an intent rather than demonstrated lift. “Easier to find and reuse” removes the forever guarantee without weakening the pitch.
- **Measurement:** Prove has an empty benchmarks section; its scorecard is a hypothesis and explicitly not validated benchmarks. Performance Measurement and audience references to scorecards are justified factual corrections. “Show how ... is working” and “Measure ROI” no longer promise positive results.
- **Other corrections:** five-stage and shared-structure statements are properly scoped to patterns. Roadmap explicitly calls its quarterly issue proposed. Simulcast replacement accurately summarizes its decision checklist rather than promising a complete platform implementation guide.
- **Owner-preserved marketing:** Everything You Need; Open Source. Opinionated.; broadcast-quality aspirations; podcasts, webinars, livestreams and virtual events produced like real shows; and complete-media-package service copy remain intact. “Every contribution is reviewed by the Riggg team” is preserved under the owner's Oct 13 20:10 confirmation supplied with this assignment (also consistent with contribute metadata). No new blanket criticism of marketing or repetitive disclaimers.

## Nonblocking ambiguities / optional surgical advice

Pre-existing issues, not reasons to reopen the rejected broad rewrite:

- Unchanged anatomy paragraph still says “every entry” uses a structured template after the subtitle now correctly says patterns. If touching it, change only “every entry” to “every pattern.”
- Unchanged Content Memory highlight describes building a library “using vector databases and transcript indexing.” Its current destination starts with storage, a spreadsheet and permissions; vector search is optional. Precise replacement: “Build a searchable, reusable library with source files, approved transcripts, clear permissions, and tested recovery.” No warning paragraph needed.
- “Measure ROI with scorecards and attribution models” is broader than the linked scorecard's lightweight qualitative categories: the scorecard is not a worked ROI model. Optional tighter copy: “Track business outcomes with performance scorecards.” This is not a guaranteed ROI claim and need not block this narrow draft.
- Generic “benchmarks” in introduction/framework remains category-level positioning, not a numerical benchmark or measured-performance assertion. Do not globally purge the word or retained broadcast-quality aspiration.

## Exact reviewed hashes (SHA-256)

Hashes identify reviewed bytes, not future revisions. Paths relative to worktree.

~~~text
ec19dabfb35900a0cde4da5cc07f09375ee36884885a3ed1424780c73ebefded  docs/index.md
1a4d80e1b11234fbd0e89d331dc633681fda1417019cd51ca604d6070e7fe801  docs/overrides/home.html
2be856c32a3d8d947b3b7211ed068e0092acf5ae2954059ad13f9dba272b793d  docs/scoring.md
ba84b2eb61c9529ad5481674f5188e9d48bf6a6c01faa662330fe0d6de1d9d81  SCORING.md
99c4cbe508a0f4fbb6c95aab0159dc6d4d13be86a4890a14ffe6e32064e887a3  docs/framework.md
08086f014cdbb1dd9a3f9806b2a11adae52effe9c92434e19ea539b735e688dc  docs/patterns/index.md
0087c51a7ca1f20f89f80488780f8ec536f6e7e8bee9058ff0669af7d3f2659b  docs/roadmap.md
66f153ab951072605eff61cb75366834daa616b2d938cdb007ce62f94f0b9b9b  docs/contribute.md
01951191e91ee33370242eba8c308bd3f56ffca1c39a5007330a0d692745ca79  docs/patterns/package/titles/index.md
6c1389a0f927ae9900e414ffbb2cb613f1e18ebd74b66c7f9699e6c0cb76aada  docs/patterns/package/descriptions/index.md
c1d21ffbcf3ee67f620936bba6d9873a218a1c837730a622720010becb974c01  docs/patterns/prove/index.md
f58eb49ae7716bc685af7f60bb5935057817a84b6d8e1cb53c47aaa8652a690a  docs/patterns/prove/session-performance-scorecard.md
ccf2fb114d651faf7948c00626d541a1d9e4b60165b13750aedc8475bbb254a6  docs/patterns/publish/simulcast-standard.md
f4bf19f6a8f86932b09808fdc39cf2d1732037c9a64bcfa4444096d19c55b4c0  docs/patterns/preserve/content-memory-standard.md
71b24299e1ae22cd51652aeb62b72742ff7bad9c6fd10fb5e8b3ba8b3b51950e  docs/patterns/produce/index.md
01f554e7ee91b4ae1c4dc1f92adeb91928ae048c3b0e02d40da068ddf3b86f60  docs/patterns/package/index.md
2fd1ede1c740513d20c66a043368488b372a2c56e50d41f40a1a76be8940bc4c  docs/patterns/publish/index.md
1fc3c0dfe12e3083eea64fa8d637f8530593c013347fcf37bfb1cba389e0fb7e  docs/patterns/preserve/index.md
ee89bcd30a6732dec30de04bbabfaa8cc53a20b7156081a6da2253ba6a84daff  docs/patterns/produce/obs-production-standard.md
~~~
