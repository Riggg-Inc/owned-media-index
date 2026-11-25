# Quality review: evidence.md
Outcome: needs_revision. AI editorial review: openai/gpt-6-astra; not human testing or approval.
Completed UTC: 2026-11-25T16:51:05Z
Exact body SHA-256: fda7c2464edc7cbdcaf5aefd4e401bc0adcc3d55a0b4f2d50b49b66ffb48c513

usefulness: pass
The short reference explains what supports OMI entries and what private information must stay out, a clear reader and contributor task.

substance: pass
Five defined evidence types and a concrete list of prohibited information are enough for an overview; expanding it into an audit manual would not improve this task.

coherence: pass
Evidence categories are kept distinct from public-safety restrictions; generalization is not presented as permission to publish confidential data.

cross_page_consistency: pass
Public Scoring calls scores editorial judgments and defines practitioner observation as experience; Contribute asks for evidence and tradeoffs. This overview does not promise every entry is benchmark-proven.

reasonable_claims: pass
The page states the Index editorial policy rather than empirical platform or performance claims; root EVIDENCE.md supports the same five types and privacy restrictions.

usability: needs_revision
Core prose is readable, but current dark breadcrumb Home and footer links, including Analytics preferences, have visibly poor contrast. Shared navigation and privacy-control access remain materially impaired on both viewport sizes.

Practitioner reader checks
Purpose PASS: identify what supports an entry. First action PASS: identify the kind of evidence and keep private information out. Example PASS for reference task: official requirements versus expert operating judgment are concrete distinguishing categories; a pattern-style worked example is unnecessary. Quality Bar PASS: prohibited customer information and unapproved metrics form an observable exclusion check. Meaning and voice PASS: concise policy remains useful without an audit narrative. Essential limits PASS: confidentiality and generalization are explicit and appropriately prominent. Rendered navigation usability REVISE, not the policy content.

Evidence and corrections
All four current canonical evidence-default/slate-1440/390.png screenshots visually inspected, with fresh article DOM and no outer overflow. No tables or code blocks on this page: do not falsely attribute the shared table failure to it. Dark breadcrumb and footer controls are the actual observed defect. Existing shared CSS proposal, no duplicate proposal. No external sources fetched for this page and no root policy changes made; shared card link is issue history only.

{
  "source_checks": {
    "applicable": false,
    "rationale": "This is a first-party editorial policy summary, with no external performance, platform limit or attribution claim requiring a fresh outside source.",
    "items": []
  },
  "cross_page_comparisons": {
    "applicable": true,
    "rationale": "Read full public Scoring, Contribute and the actual Audience Pain pattern, alongside root EVIDENCE.md and TEAM.md.",
    "items": [
      {
        "path": "scoring.md",
        "claim": "Evidence provenance does not make scores popularity votes.",
        "finding": "Scoring explicitly calls ratings editorial judgments and distinguishes observation, internal data and research; no conflict requiring a policy rewrite.",
        "checked_at": "2026-11-25T16:51:03Z"
      },
      {
        "path": "contribute.md",
        "claim": "Contributions should state evidence and tradeoffs.",
        "finding": "The full contribution checklist requests both evidence and when-not-to-use guidance, consistent with transparent support rather than proof of every recommendation.",
        "checked_at": "2026-11-25T16:51:03Z"
      },
      {
        "path": "patterns/package/descriptions/audience-pain-breakdown.md",
        "claim": "Practitioner observation can support actionable guidance without fabricated outcomes.",
        "finding": "Actual pattern labels its example illustrative and its references starting points, a concrete compatible instance; no claim that all library entries are compliant.",
        "checked_at": "2026-11-25T16:51:03Z"
      }
    ]
  }
}