---
description: "Build an owned-media library with source files, approved transcripts, stable IDs, reuse permissions, simple search and tested recovery—not just a public archive."
---

# Owned Media Library: A Practical Content Memory Standard

An owned-media library is the controlled collection of source media, finished assets and context that lets a team find, verify and reuse its work. Start with shared storage, a spreadsheet and clear permissions. A public website, a backup or a search index alone is not the library.

**Stage:** Preserve

**Score:** 3 — Viable (proposed revision)

**Evidence:** practitioner-observation

## What It Is

The library connects each recording to its edits, approved transcript, published versions and reuse conditions. It answers four operational questions: **What do we have? Which version is approved? What may we do with it? Can we retrieve it without the original producer or publishing platform?**

This expands the Content Memory Standard from transcript retrieval into the practical system that makes retrieval trustworthy. It covers recorded media and its derivatives, not live-session facilitation.

| Layer | Job | What it does not replace |
|---|---|---|
| Library | Maintain authoritative files, context, relationships and permissions | Public delivery or disaster recovery |
| Public website | Present selected approved assets at a canonical address | Private masters, edit projects or restricted context |
| Distribution | Deliver versions through feeds, video hosts, email and social platforms | The authoritative asset inventory |
| Backup | Recover files and records after loss or corruption | A usable catalog or editorial approval |
| Search/vector index | Find relevant records and passages | Source files, current permissions or proof that a quote is accurate |

The library may span more than one system. Declare which system is authoritative for each job; do not call every copy the source of truth.

## Best For

Small teams running recurring interviews, podcasts, recorded webinars, customer education or other programs where somebody will need the material again. It is especially useful when editing, publishing and reuse happen with different people.

## Why It Works

A file becomes reusable only when someone can identify it, understand its context, verify permission and reach the underlying source. Stable IDs connect those steps even when titles, folders and distribution URLs change. Keeping a recoverable copy outside the publishing platform makes access less dependent on that platform.

These are operating judgments, not measured promises of higher revenue, search rankings or faster production. The effort is worthwhile only if the team maintains the records and uses the library.

## Required Elements

### Keep the assets needed to make the next version

| Keep | Include | Practical boundary |
|---|---|---|
| Source recordings and production masters | Original camera/audio tracks where available; high-quality edited master | Preserve the actual source format. A compressed platform download is not automatically a master. |
| Editable work | Project files, linked media, graphics, fonts/licenses and export notes | Note application/version and missing dependencies. Keep a rendered master when the edit cannot be reopened elsewhere. |
| Finals and derivatives | Approved full-length exports, audio, clips, reels, articles and their versions | Tie every derivative to its source; do not mistake a social upload for the only copy. |
| Approved transcripts | Speaker labels, timestamps, session title/date, subject, relevant caveats and revision | Link timestamps to the exact media version. Keep machine drafts separate; mark uncertainty instead of inventing words. |
| Captions and artwork | Timed caption files such as VTT/SRT, thumbnails, stills and editable artwork where useful | A prose transcript is not a timing-checked caption file. Check names and synchronization. |
| Metadata and provenance | IDs, relationships, creator/source, dates, topics, status, approval and publication references | Record material edits and AI-assisted transformations when relevant. |
| Rights and permissions | Release/license references, allowed uses/channels, restrictions, expiry and approval authority | Keep signed agreements in restricted storage; expose only the clearance summary needed for the task. |

“Owned” is not a blanket rights claim. A recording can contain licensed music, guest contributions or confidential information that restrict reuse. Unknown permission means **hold**, not assumed clearance.

Audience records are permissioned personal data, not media inventory to collect indiscriminately. Do not routinely copy registration lists, attendee email addresses, private chat or individual engagement histories into the library. Keep necessary audience data in its authorized system under its purpose, access and retention rules. Use an aggregate report or a restricted reference when that is sufficient. An export capability is not permission to export everything.

### Give every asset an identity and a home

Assign a stable program ID, session ID and asset ID. A title is a label, not an identifier. Record the asset's parent ID and source version: a clip comes from a particular approved master, which comes from a particular recording. Record clip in/out points against that version, not against whichever upload is easiest to find.

Use one catalog as the authority for status, rights summaries and the current approved version; use designated storage as the authority for file bytes. Publishing platforms hold delivery copies. Do not overwrite approved files: save a new version and update the current-version pointer after approval. Keep a short change note and who approved it. A correction to the master should flag affected transcripts, captions, clips and posts for review.

## Example Patterns

### A minimum spreadsheet and folder implementation

The following is an illustrative structure, not a real program or a required naming convention:

~~~text
library/
  catalog/                         # controlled workbook; dated CSV exports
  PRG-001/
    SES-0042/
      manifest.csv                # asset rows exported from the catalog
      source/                     # original capture and provenance notes
      edits/                      # projects, dependencies, edit notes
      masters/AST-0100_v02.mp4
      text/AST-0101_v02.md         # approved transcript of AST-0100 v02
      captions/AST-0102_v02.vtt
      derivatives/AST-0103_v01.mp4
      artwork/
      context.md                  # session summary and clearance reference
~~~

Folder names organize work; they do not enforce access. Configure storage permissions separately. Sensitive releases belong in the restricted rights system, not in a public delivery folder.

A shared workbook can start with two tabs:

- **Sessions:** session ID, program ID, title, recording date, short summary, topic tags and responsible editor. Add speaker names/roles only as needed and permitted.
- **Assets:** asset ID, session ID, type, version, source asset/version and time range, file path, status, access group, rights reference/allowed uses, approver/date, current-version flag, publication URL, retention review date and checksum.

An asset manifest is a portable export of those records, not a second independently edited catalog. For example, this shortened CSV row connects a clip to its master; the actual export also includes the other Assets fields:

~~~csv
asset_id,session_id,type,version,source_asset,source_version,in,out,path,status,access,rights_ref
AST-0103,SES-0042,clip,1,AST-0100,2,00:12:10,00:13:05,derivatives/AST-0103_v01.mp4,approved,editorial,CLR-0042
~~~

Define column meanings and allowed status values in a short README. Use paths relative to the session folder in exports, not expiring share links alone. Record file size and a checksum such as SHA-256 at intake/export so a later restore can detect changed bytes. A matching checksum does not prove editorial accuracy or rights clearance.

### Find a moment, then reuse it safely

Illustrative request: “Find a useful explanation of implementation delays for a new article.”

1. Filter the catalog by topic and clearance; search approved transcript text for the phrase and related terms. Spreadsheet filters and ordinary full-text search are enough to start.
2. Open the matching passage with the speaker, session date, surrounding question and timestamp. Listen to the corresponding approved master; a search excerpt or AI answer is not verification.
3. Check whether the statement is still current and whether the intended article or clip use is allowed. A public interview release may not cover every new use. If unclear, ask the rights owner before proceeding.
4. Create a derivative with its own ID, source version, time range and edit note. Send it through approval, then log where it was published.
5. Record whether the request succeeded and what was missing. Repeated failures should guide better tags, transcripts or tooling.

Add semantic/vector search only when actual retrieval problems justify it. Keep source IDs and timestamps on results, restrict retrieval to permitted content, and propagate corrections, permission changes and deletion into indexes and caches. The index should be rebuildable from approved source material; it is not the archive.

## Routine Operation

One person may wear several hats. Name the responsibility anyway:

- **Producer/editor:** intake, completeness, playable files, transcript/caption QA and relationships.
- **Program or rights owner:** publication/reuse clearance, restrictions and retention decisions.
- **Publisher:** release only approved versions and log delivery URLs.
- **Library steward:** catalog integrity, access, backup/export checks and recovery drills. This can be a recurring duty, not a new job.

Use a short lifecycle: **intake → QA → approved → published → archived or withdrawn**. Published records remain governed; publication is not permission for every future derivative.

**At intake:** assign IDs, copy authorized source files, inventory missing items and record provenance. Quarantine unreviewed or sensitive material from public access.

**Before approval:** check playback, file completeness, transcript speaker/timestamp accuracy, captions, source relationships and intended-use permissions. Record gaps honestly. Limit edits to responsible people, use read-only access for others and share only the assets each recipient needs.

**At publication:** export an approved delivery version, build or update the public canonical page, and record its URL plus platform copies. Preview the release; never publish a raw transcript or restricted folder automatically because it appears in storage.

**After correction or withdrawal:** identify affected derivatives and delivery copies, update or remove them where authorized, and record what remains outside your control. Rebuild affected search entries; do not let an old index quietly restore a withdrawn quote.

**At retention review:** keep material with a continuing permitted use or required retention basis. Review duplicates, superseded exports, expired licenses, obsolete content and personal data that is no longer needed. Set actual review dates according to the program's obligations, rather than “keep everything forever.” Preserve material subject to a legal hold; involve the responsible legal/privacy owner when required. Record authorized deletion without retaining the sensitive content in the deletion log. Coordinate deletion across active storage, derivatives, search and backup expiry; document any backup lag and prevent deleted items from returning to active use after restore.

### Independence means a tested recovery, not an export button

Keep files and catalog exports outside the publishing platform, plus a separately recoverable backup. A synchronized folder that propagates deletion is not sufficient on its own. Document who controls the storage account, recovery credentials and access if a producer leaves.

Export media, approved text/captions, artwork, metadata, rights references and relationship records in formats the team can open. Preserve native edit files too, while recording dependencies. CSV and plain text are useful fallbacks, not guarantees that every field or behavior transfers.

Run a practical drill on a representative session at setup, after material workflow changes and on an agreed recurring schedule:

1. Restore into a separate test location from the independent backup/export, without fetching missing files from the original publishing service.
2. Compare the inventory, file sizes and checksums; play the media and open the approved text and artwork.
3. Have a teammate trace a clip to its master and clearance record, recover the intended approved version, and reconstruct a draft episode page or reuse package in a sandbox. Do not republish during the drill.
4. Record elapsed time, missing dependencies, broken links, excluded features and the person responsible for fixing each failure. Re-test the failed steps.

Preserving files is not lossless platform migration. Interactive polls, registration workflows, chat, proprietary analytics, player behavior, recommendation history, engagement counts, URLs and editing plugins may not transfer or reproduce. Classify each relevant dependency as **portable, reconstructible with work, or nonportable**. Keep only authorized exports; document accepted losses and alternatives. Set a recovery target based on what the team needs to resume, and verify it rather than promising zero loss or minimal effort.

### Start small; maintain what you start

For a minimum viable library, choose one recurring program and a few representative sessions. Name the steward; create the storage location, workbook and access groups; ingest the files and rights summaries; run one find-and-reuse exercise and one recovery drill. Fix those gaps before backfilling the entire archive.

A workable starting rhythm for a small team is an intake check for every session, a short weekly missing-files/approval queue review, and a monthly access, link and upcoming-retention check. Schedule a deeper recovery exercise quarterly to start, adjusting to risk, change rate and cost. These are suggested cadences, not research-backed thresholds.

Track simple operational facts: sessions with complete required assets, retrieval requests that reached a verified source, unresolved rights holds and the last successful recovery test. Do not equate more stored files or embeddings with a healthier library. Add a digital asset manager or automated indexing only when the spreadsheet's actual failure modes justify the extra work.

## Quality Bar

A teammate other than the original editor can find an approved moment, inspect its context and permissions, retrieve the correct files and create a traceable derivative. A recovery drill demonstrates what can be restored independently and records what cannot.

The minimum acceptance check is not “everything uploaded.” It is **find → verify → retrieve → reuse → recover**, with missing assets and restrictions visible. Never mark an untested recovery as passed.

## When Not To Use

Do not build a complex catalog for a few one-off files with no foreseeable reuse. Keep the basic IDs, permissions and recovery copy, then scale only as needed. Do not retain content merely because storage is cheap when permission, confidentiality or retention obligations prohibit it. This standard does not require a public archive, a vector database or the indefinite preservation of every take.

## Riggg Score

**3 — Viable**, proposed for this revision. The structure is practical but requires ongoing operator judgment, storage discipline and rights administration. Practitioner evidence caps the score at 3; neither vendor acquisition news nor the completeness of this checklist validates a higher score.

## Evidence

Evidence level: **practitioner-observation**. This is an editorial operating standard, not an outcome study. The folder, CSV and retrieval scenario are hypothetical implementation examples. No measured improvements in reuse, cost, revenue or discoverability are claimed. Program-level retrieval and recovery results would be needed to evaluate its effectiveness in practice.

## Related Patterns

- [Canonical Episode Page](../publish/canonical-episode-page.md): the public home for selected approved assets, not the private library.
- [Feed Metadata Standard](../publish/feed-metadata-standard.md): consistent delivery metadata, not the full preservation record.
- [Build an Audience Question Set for AI Discovery Checks](geo-aeo-citation-volatility.md): public answer quality and bounded discovery checks, not internal asset recovery.
