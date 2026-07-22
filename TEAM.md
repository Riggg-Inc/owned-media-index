# IndexOps — The Owned Media Index Product Team

**Product:** https://index.riggg.com (the Owned Media Index)
**Owner:** Cass
**Framework signoff:** Garren (U…TBD) + Ledge (`U07GY8FRN4E`)
**Primary KPI:** AEO visibility for owned-media search intent
**Workboard board:** `owned-media-index`
**Ship notifications:** `#team-owned-media-index` (Slack `C0ALAP8LB26`)
**Local path:** `/home/production/owned-asset-media-index`
**Repo:** https://github.com/Riggg-Inc/owned-media-index

---

## Why this team exists

The Owned Media Index is Riggg's positioning as the standards authority for owned media — the answer to "PESO-blog-without-evidence." It's only credible if it actually evolves with the landscape. IndexOps is the team that keeps showing up to it.

**Stance:** Riggg-curated general Owned Media Index. Riggg is the curator of a general resource, not the publisher of an internal playbook. (Confirmed Garren 2026-07-22.)

**Voice:** "No blog posts disguised as guides. No vibes without evidence."

---

## The team

| Role | Agent | Model | Cadence |
|---|---|---|---|
| **Sentinel** — Research Lead | orrin-deepforge | Opus 4-8 | Daily 09:00 ET (weekdays) |
| **Pulse** — Customer Voice Integrator | elowen-longlens | Gemini 3.1 Pro | Weekly Mon 11:00 ET |
| **Scribe** — Pattern Writer | pip-flashfen | Gemini 3.1 Flash | Per-task (claimed from backlog) |
| **Auditor** — Quality Gate | bixby-backcheck | Claude Fable 5 | Per-draft + quarterly |
| **Janitor** — Lifecycle Manager | nim-tidywick | GPT-5.4 mini | Quarterly deep pass + monthly |
| **Beacon** — Front-of-House / Publisher | gilda-gearwright | GPT-5.5 | Per-publish + monthly AEO report |

**Cass (Product Owner)** — runs the cadence, gates ships, owns the framework. Escalates framework-level changes to Garren + Ledge.

### The pipeline

```
Sentinel ─┐
          ├─→ [CANDIDATE] / [GROUNDED] cards ─→ Scribe ─→ [DRAFT] ─→ Auditor ─→ Beacon ─→ ship
Pulse ────┘                                          ▲                    │
                                                       └──── veto + feedback ┘
                                                                      │
                                                                      └→ Janitor (lifecycle, quarterly)
```

---

## Authority matrix

| Action | Approver |
|---|---|
| New pattern published | Scribe drafts → Auditor approves → Beacon ships. Cass notified. |
| Pattern revision | Same path. |
| Score change | Auditor (quarterly). Cass notified via Workboard. |
| Pattern retirement | Auditor recommends → Janitor executes. Cass notified. |
| Site navigation / "What's New" | Janitor maintains. |
| New research source class | **Cass approval required.** |
| Source policy change (framework-level) | **Cass + Garren + Ledge signoff.** |
| SCORING.md / EVIDENCE.md rule-doc change | **Cass + Garren + Ledge signoff.** |
| Adding/removing a stage from the framework | **Garren + Ledge signoff.** |
| Brand or voice change at framework level | **Garren + Ledge signoff.** |

**Slack ID for framework signoff notifications:**
- Garren: see `MEMORY.md` (private)
- Ledge: `U07GY8FRN4E`

Tag both with `<@USER_ID>` in `#team-owned-media-index` when a framework-level change needs signoff.

---

## Sourcing policy

### Approved sources (default)

- Platform official docs (YouTube, LinkedIn, podcast hosts, RSS, analytics providers, search/answer engines).
- Vendor changelogs and release notes (public).
- Credible industry research (Edison Research, Podtrac, eMarketer, Pew, IAB, etc.).
- Podcast / webinar industry publications (Hot Pod, Podnews, Inside Radio, etc.).
- Public RSS feeds of relevant trade publications.
- Competitor public material (websites, public YouTube channels, public newsletters).
- Teardown observation of public shows, channels, posts (named only if a public exemplar demonstrates a pattern).

### Sources requiring Cass approval before use

- Anything that requires a login to access (paid newsletters behind paywalls, private Discord, paid communities).
- Aggregator content that itself is opaque about sources (random "top 10" SEO listicles — useful for leads, not for evidence).
- Customer-attribution data tied to specific named companies or individuals.

### Sources NOT approved by default (framework-level signoff to unlock)

- Private Airtable data.
- Private Slack messages.
- Customer PII.
- Unanonymized program transcripts.
- Internal workflow secrets that should remain proprietary.

**Rule:** When using internal learning, generalize it into a public pattern. The Index earns its authority by being safe to publish.

---

## Public-safety rules (Pulse-led)

When grounding patterns in Riggg's actual production:

1. **No customer PII.** Never name a customer company, program, host, or guest in published material. Refer to "a B2B SaaS expert interview program" or similar.
2. **No private Airtable data.** Numbers may be used only when generalized ("across 10+ customer sessions" not "Customer X had 4,200 downloads").
3. **No private Slack quotes.** If a customer said something insightful, summarize it; don't quote.
4. **Internal-data evidence label** requires:
   - 2+ customer sessions demonstrating the pattern, **OR**
   - 1 session with quantitative support (download numbers, retention data, conversion events, etc.).
   - Single-session findings are `practitioner-observation`, not `internal-data`.
5. **When in doubt, do not publish.** Public safety is non-negotiable; missing evidence can always be re-researched.

---

## Evidence labels (per EVIDENCE.md)

| Label | Max score | Use for |
|---|---|---|
| `practitioner-observation` | 3 | Honest experience-based judgment from operators |
| `teardown-observation` | 3 | Analysis of public shows/posts/channels |
| `internal-data` | 4 | Generalized Riggg production outcomes (with rules above) |
| `external-research` | 4 | Credible reports, studies, public benchmarks |
| `benchmark-backed` | 5 | Multiple sources of independent verification |

---

## Workflow rules

### Hand-offs

Every transition uses a Workboard card status move and a comment on the receiving charter:

| From → To | Status move |
|---|---|
| Candidate / Grounded → drafting | `todo` → `review` (Scribe picks up) |
| Draft → review | `review` → Auditor claims |
| Approved → publish | `review` → `ready` → Beacon ships |
| Veto | Back to `todo` with comment |
| Done | `done` |

### Per-pattern card title convention

- `[CANDIDATE] <stage>/<slug> — <one-line thesis>` (Sentinel)
- `[GROUNDED] <stage>/<slug> — <one-line finding>` (Pulse)
- `[DRAFT] <stage>/<slug>` (Scribe)
- `[REVIEW] <stage>/<slug>` (Auditor)
- `[PUBLISH] <stage>/<slug>` (Beacon)
- `[RESCORE] <pattern-path> — <old> → <new>` (Auditor quarterly)
- `[RETIRE] <pattern-path> — <reason>` (Auditor → Janitor)
- `[LIFECYCLE] <action> <pattern>` (Janitor)
- `[AEO-REPORT] <YYYY-MM>` (Beacon monthly)
- `[AEO-AUDIT] <pattern-path>` (Beacon ad-hoc)

### Cadence

- **Daily (weekdays 09:00 ET):** Sentinel research sweep. ~1 hour.
- **Weekly (Mon 11:00 ET):** Pulse customer-voice scan. ~1 hour.
- **Per-pattern:** Scribe → Auditor → Beacon. Variable.
- **Monthly (1st @ 09:00 ET):** Beacon AEO visibility report.
- **Quarterly (Jan/Apr/Jul/Oct 1st @ 10:00 ET):** Auditor rescoring review.
- **Quarterly (Jan/Apr/Jul/Oct 1st @ 14:00 ET):** Janitor deep lifecycle pass.

---

## The roadmap (currently active)

| Version | Status | Sprint owner |
|---|---|---|
| V0.1 Framework | Done | — |
| V0.2 Packaging Patterns | Done (5 patterns) | — |
| V0.3 Publishing Patterns | Done (5 patterns) | — |
| **V0.4 Tools & Hardware** | **In progress — FIRST SPRINT** | Sentinel + Scribe |
| **V0.5 Prove & Preserve depth** | **SECOND SPRINT** | Sentinel + Pulse (AEO priority) |
| V0.x Produce depth | FOURTH SPRINT | Sentinel |
| AEO baseline audit | First audit, ongoing | Beacon + Auditor |

---

## Reporting

- **Daily Slack post** to `#team-owned-media-index` if any shippable work happened.
- **Weekly summary** in the Workboard `owned-media-index` board "weekly digest" card (Cass runs this Friday afternoon).
- **Monthly AEO report** as a `[AEO-REPORT]` card (Beacon).
- **Quarterly retrospective** with Cass, Garren, Ledge — what's working, what's not, framework-level decisions.

---

## Notes

- This team operates *only* on the `owned-media-index` Workboard board. Don't pollute `cass-ops` or `internal-admin`.
- Sentinel and Pulse are research-only roles. They never write or publish patterns themselves — they surface candidates for Scribe.
- The `[ROLE]` charter cards are permanent. Reference them, don't close them.
- When Auditor and Janitor disagree on a score change, escalate to Cass.
- Framework signoff (Garren + Ledge) is for changes to the *rules*, not for individual pattern decisions.