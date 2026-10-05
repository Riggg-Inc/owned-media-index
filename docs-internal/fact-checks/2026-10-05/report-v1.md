# Published factual review — 2026-10-05, v1

AI reviewer: Cass Reelman (openai/gpt-6-astra). No human signoff.
Scope: entire unchanged Markdown bodies of three published clip-pattern articles; public primary-source documentation and show descriptions, not private customer evidence or measured clip outcomes.
Started 2026-10-05T16:46:10Z; completed 2026-10-05T16:49:39.912Z.
Base: origin/main 3296782, isolated worktree. Primary dirty checkout untouched.

## Queue and identity
126/126 published pages due (86 Articles); production records unchanged. Six exact-body open proposals skipped: measurement, evidence, framework, homepage, owned-media, data-drop. Branch identities from October 3/4 matched today's queue and live Workboard review statuses. High-risk unknown deadlines tie lexically; next three are below. No fourth article reviewed.

- patterns/package/clips/debate-moment.md: 9d0814315e9e63ffe4366dfb5465c9dc903c9da800b7dd093135d4625cd56641
- patterns/package/clips/golden-nugget.md: aaf010734e9fd8332bd57584fe14b7bfc2679dd9ff894707019dae3eca8744be
- patterns/package/clips/hot-take.md: 8732b030dfe6c933d0707844c7824a155b020c004774503fc4deae969858e48b

All three PARTIAL. Retry 2026-10-12T16:45:00Z (under seven days); skip unchanged open proposals between runs. Changed bodies invalidate this evidence immediately. Do not attach these records to future rewritten articles.

## Source observations
URL, actual retrieval time, complete returned extraction and failure details are versioned in sources/*.json. These are public source snapshots, not independent verification of promotional claims. First-party show positioning supports only identity/topic/intent. No video was watched; no episode transcript or analytics was obtained. Announced future episodes are not treated as released. No platform availability or measured outcomes inferred from a show landing page.

- allin.json: https://allin.com/ at 2026-10-05T16:47:15.045Z. September 25 synopsis: “The group debates free-market competition, cybersecurity, rapid model releases”. Supports publisher-described debate in that episode; not genuine debate in EVERY episode or four investors always present.
- mfm.json: https://www.mfmpod.com/ at 2026-10-05T16:47:14.856Z. “A podcast where Shaan Puri and Sam Parr brainstorm business ideas every week.” Supports host identity and topic; not frequency of disagreement or standalone clip performance. Extraction truncated; no inference about omitted material.
- tim.json: https://tim.blog/podcast/ at 2026-10-05T16:47:15.470Z. “extract the tactics, tools, and routines you can use.” Supports show's stated editorial intent, not consistent actionable results or saves.
- knowledge.json: https://fs.blog/knowledge-project-podcast/ at 2026-10-05T16:46:55.478Z. “Deep conversations ... uncover the timeless principles”. Tobi Lutke listing explicitly names Shane Parrish. Official Apple link ends id990149481. Does not establish dense quotable mental models from EVERY guest. October 6 public-release listing is future, not a released example.
- knowledge-correct.json: https://podcasts.apple.com/us/podcast/the-knowledge-project/id990149481 at 2026-10-05T16:47:57.278Z. “Hosted by Shane Parrish”; same show identity confirmed by readable description. Published article destination id990149903 returned 404 (knowledge-old.json, 16:47:43.766Z). Confirmed destination correction, not merely HTTP success.
- profg.json: https://www.profgmedia.com/ at 2026-10-05T16:47:15.012Z. “Uncompromising analysis ... business, power, and society” and Scott Galloway named. Supports broad positioning, not clip suitability/performance.
- prompt.json: https://platform.openai.com/docs/guides/prompt-engineering (redirects to developers.openai.com/api/docs/guides/prompt-engineering) at 2026-10-05T16:47:56.898Z. “content generated from a model is non-deterministic”; different model types/snapshots can produce different results; recommends evaluation suites. Supports qualified advice to test prompts; does not support monotonic “more context ... better output.” Extraction truncated, relevant section read.

## Debate Moment — claim verdicts and proposed wording
- Definition/opening/selection criteria/when-not-to-use and 30–90 second prompt constraint: editorial recommendations, not empirical efficacy claims. Preserve them; timing must be checked against source media, not invented from untimed text.
- “The energy of real-time debate is inherently engaging” / “Conflict is engaging”: UNCERTAIN universal behavioral claim; retrieved show descriptions do not measure audience engagement. Proposed replacement: “The intended mechanism is to give viewers competing positions to consider; test engagement with your own audience.” Retain existing measurement caveat.
- “Four investors ... genuine debate every episode”: PARTIAL support only for the specific publisher synopsis above. Proposed replacement: “The publisher's September 25, 2026 episode synopsis describes a group debate; verify the exchange in the episode before selecting a clip.” Use https://allin.com/ as source entry point rather than the unverified @alaboratory link; no claim that its handle is definitively wrong.
- MFM “regularly disagree ... natural debate clips”: UNCERTAIN. Hosts/business topic supported, frequency/mechanism not. Proposed replacement: “Sam Parr and Shaan Puri brainstorm business ideas; a specific disagreement still needs episode-level verification.”
- Diary CEO “interview style surfaces disagreements ... tension-filled moments”: UNCERTAIN. Site returned title only; YouTube extraction failed. Proposed removal of this example pending a public episode/transcript with coherent competing positions.
- Evidence header “internal production data”: UNRESOLVED provenance. No approved anonymized outcome evidence in article; no private customer records accessed. Preserve score 4 and evidence label unchanged; route substantiation to Auditor, do not silently rescore.

## Golden Nugget — claim verdicts and proposed wording
- Definition/selection criteria/audience fit/when-not-to-use/30–90 seconds: normative recommendations. “Works for both beginners and experienced practitioners” is a selection goal, not established efficacy.
- “When someone hears ... they save it, screenshot it, or send it”: UNCERTAIN behavioral generalization. Proposed: “The intended response is a save or share; whether it occurs must be measured.” Preserve existing no-guaranteed-advantage caveat.
- Tim Ferriss “consistently surface ... tactics”: PARTIAL; official description supports intended extraction of tactics, not consistent observed results. Proposed: “The show describes its aim as extracting tactics, tools, and routines; validate any selected advice in its episode context.”
- Knowledge Project “dense, quotable mental models from every guest”: UNCERTAIN universal claim; official positioning is narrower. Proposed: “Shane Parrish hosts conversations about principles and decision-making; identify a specific usable insight before clipping.” Confirmed link replacement: https://podcasts.apple.com/us/podcast/the-knowledge-project/id990149481 .
- Ali Deep Dive “Designed around extracting specific, implementable advice”: UNCERTAIN; both /podcast/ and /deep-dive/ blocked 403. Proposed removal pending accessible primary episode evidence. No availability claim from blocked fetch.
- Internal-data header/score 5: provenance unresolved; no score/rule/label edit proposed. Existing framework inconsistency cannot be resolved by this audit.

## Hot Take — claim verdicts and proposed wording
- Definition/selection criteria/avoid uninformed or retracted claims/30–90 seconds: editorial recommendations, not empirical outcomes.
- “Opinions create engagement. People share, comment on, and argue with strong takes”: UNCERTAIN behavioral generalization; no comparative analytics. Proposed: “The intended mechanism is a reaction to a clear position; measure comments, shares, and impressions rather than assuming uplift.”
- Diary CEO “Guest hot takes drive millions of clip views”: UNSUPPORTED numerical and causal claim. Title-only website and failed YouTube extraction cannot establish which clips, observation date, view counts or causality. Proposed remove entire example until evidence exists; not declared false solely because retrieval failed.
- Prof G “sharp opinions ... built for clip extraction”: broad topic/name supported; suitability is editorial judgment. Proposed: “Scott Galloway's publication describes analysis of business, power, and society; clip suitability requires episode-level review.”
- MFM “hot takes ... perform as standalone clips”: UNCERTAIN performance claim. Proposed: “Sam Parr and Shaan Puri discuss business ideas; validate a specific standalone position before clipping.”
- Internal-data header/score 5: unresolved substantiation, unchanged pending Auditor evidence.

## Shared prompt claim
All three end “The more context ... the better the output.” UNCERTAIN universal claim. Official prompting guide explicitly says output is nondeterministic and model-dependent. Proposed replacement: “Provide relevant audience, guest, and episode context, then evaluate the output against the source. More context alone does not guarantee better results. Verify timestamps against the recording.” No paid model tests performed.

## Failures and limits
Initial conventional skill path missing; recovered installed Workshop skill. Primary checkout lacked current procedure; recovered after fetching origin/main into clean worktree. Some tool display outputs truncated; recovered relevant source substance from saved snapshots. Ali 403 twice; Diary title-only response and YouTube extraction failure; @alaboratory extraction failure; old Knowledge Project Apple link 404, corrected destination substantively identified. Missing outcome/internal-data evidence is an editorial blocker, not an HTTP error. No customer data, score/framework changes, tracking changes, draft publication, date changes, or human signoff.

## Approval and next action
Only internal audit, qualified records and exact proposed wording staged. No public body edited, no evidence store published, no Last updated change. Auditor must obtain allowable episode-level and generalized outcome evidence or review the proposed removals/qualifications. Garren/Ledge decision must bind the final revised artifact under existing authenticated dashboard contract; this prose proposal is not publication approval. Recompute evidence for final body before release. One fact-check task per stable article identity; no duplicates found for these three. Branch/report links in task registry.

No release attempted: strict build, generated-site validators, freshness/deployment/live checks are release gates still outstanding, not implied passes. Fact-check proposal validation and regressions are recorded separately in validation files.
