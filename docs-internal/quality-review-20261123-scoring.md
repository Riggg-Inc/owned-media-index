# Quality review: scoring.md
Outcome: needs_revision. AI editorial review: openai/gpt-6-astra; not human testing or approval.
Completed UTC: 2026-11-23T16:50:24Z
Exact body SHA-256: ed8ff9f99b580ef2c01ae1e18f94837dcec74f9c2f95fae9134367874d87aaea

usefulness: pass
The page tells readers what a one-to-five score means and explicitly distinguishes editorial judgment from popularity.

substance: pass
All five score meanings and five evidence levels are defined succinctly; enough for interpreting scores without forcing a production worksheet onto a rules reference.

coherence: pass
Score usefulness and evidence support remain separate concepts; the opening says usefulness, evidence, repeatability and fit jointly inform editorial judgment.

cross_page_consistency: pass
Score names match Pattern Library and canonical SCORING.md; public Evidence Rules distinguishes source types while this page lists support levels, not an incompatible replacement taxonomy.

reasonable_claims: pass
Definitions are first-party editorial rules, not empirical performance claims; the published text matches canonical SCORING.md wording and does not promise universal outcomes.

usability: needs_revision
Viewed desktop/mobile dark captures obscure the Strong fit and Niche rows with near-white text on pale striping; these are essential score definitions, not decorative content.

Practitioner reader checks
Purpose PASS: understand editorial scores. First action PASS: look up the displayed score in the table. Example PASS: score 2 means narrow-case fit, an appropriate reference decision example. Quality Bar PASS: repeatability, evidence and production fit orient judgment. Meaning/voice PASS: retain definitions without rewriting rules. Essential limits PASS: scores are editorial judgments rather than popularity or performance guarantees.

Evidence and corrections
Full body, public neighbors, SCORING.md, EVIDENCE.md and TEAM.md read. TEAM evidence-cap table differs in taxonomy/detail from canonical rules; this does not authorize inventing caps in the public page. Framework owner reconciliation can happen in existing governance, not this correction batch. Actual four scoring screenshots inspected; no document overflow. Existing shared contrast issue owns alternating table rows and dark links. PREPARATION only; no scoring changes, dates or framework edits.

{
  "source_checks": {
    "applicable": false,
    "rationale": "First-party score definitions are checked against repository rule documents; external research cannot establish the intended editorial policy and no platform claim is made.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read actual public evidence and pattern-index bodies alongside full canonical SCORING.md and EVIDENCE.md.",
    "items": [
      {
        "path": "patterns/index.md",
        "claim": "The one-to-five labels help readers interpret recommendations.",
        "finding": "Pattern Library uses the same default, strong fit, viable, niche and not recommended sequence; its explicit default wording is compatible with the scoring context.",
        "checked_at": "2026-11-23T16:50:23Z"
      },
      {
        "path": "evidence.md",
        "claim": "Evidence identifies support behind an entry.",
        "finding": "Evidence Rules names source types including platform documentation and privacy requirements; scoring calls platform documentation a possible support within external research exactly as canonical SCORING.md does.",
        "checked_at": "2026-11-23T16:50:23Z"
      }
    ]
  }
}