# Citation Architecture

**Stage:** Publish → AI Search Optimization  
**Score:** 4  
**Evidence:** LLM retrieval testing, search engine documentation

## What It Is

Citation architecture is the practice of structuring your owned media content so that AI systems will cite your URL as the source when generating answers. It is the difference between your expertise existing in the AI layer and your expertise being cited, linked, and attributed to you.

## Why It Works

AI systems cite sources that:

1. **Directly answer a question** — not pages that vaguely relate to the topic
2. **Make specific, quotable claims** — not hedged, vague paragraphs
3. **Have clear attribution** — named authors, credentials, dates
4. **Live on authoritative domains** — consistent publishing history, clean technical SEO
5. **Are structured for extraction** — headings, lists, Q&A format, not walls of prose

If your content meets all five criteria, AI systems are more likely to cite you as a source in their generated answers. If it meets none, your content is training data at best — invisible to the end user.

## The Citation Stack

### Level 1: Page-Level Authority

The page itself must signal authority.

| Signal | Implementation |
|---|---|
| Canonical URL | One clean URL per episode: `yoursite.com/episodes/episode-slug` |
| Author markup | Schema.org `author` with name, title, credentials |
| Date published | Visible and in structured data |
| Last updated | Show when content has been revised |
| Domain authority | Consistent publishing cadence, backlinks, HTTPS, fast load |

### Level 2: Content-Level Citability

The content must contain extractable, quotable units.

| Element | What It Does |
|---|---|
| Direct answer paragraphs | 2-3 sentence answers to specific questions |
| Attributed claims | "According to [Name], [Title] at [Company], ..." |
| Specific data points | Numbers, percentages, benchmarks — not vague "many" or "most" |
| Definitions | "X is defined as..." — AI systems love definitional content |
| Comparisons | "Unlike [alternative], [your approach] does X because Y" |

### Level 3: Structural Citability

The page structure must help AI systems find and extract the right answer.

| Element | Why |
|---|---|
| H2/H3 headings as questions | AI systems match user queries to heading text |
| FAQ schema | Explicitly marks Q&A pairs for extraction |
| Bulleted key takeaways | Scannable, extractable lists |
| Blockquotes for key claims | Visually and semantically marked as notable statements |
| Table of contents | Helps AI systems understand page structure |

## Anti-Patterns

Things that make your content **less** citable:

| Anti-Pattern | Why It Hurts |
|---|---|
| Gated content | AI crawlers cannot access gated pages |
| PDF-only publishing | Many AI systems skip PDFs or parse them poorly |
| JavaScript-rendered content | Some crawlers do not execute JS |
| Collapsed/accordion content | May be skipped by crawlers |
| No author attribution | Reduces authority signal |
| Vague hedging | "It depends" and "many experts say" are not citable |
| No dates | AI systems cannot assess recency |

## Quality Bar

- Every episode page has a canonical URL, author, and date
- Minimum 3 extractable Q&A pairs per page
- Key claims use direct attribution with speaker name and credentials
- No critical content behind gates, collapses, or JS-only rendering
- Schema.org markup validates cleanly

## When Not To Use

Always apply citation architecture. There is no downside to making your content more citable. The only cost is the time to structure it — which pays compound returns.

## Prompt Template

```
Review this episode page and improve its citation architecture for AI search systems.

Page URL: [URL]
Page content:
[paste the current page content]

Evaluate and improve:
1. Does the page have a clear canonical URL, author, and date?
2. Are there direct answer paragraphs that an AI system could quote?
3. Are claims attributed with speaker name, title, and company?
4. Are headings structured as questions matching likely search queries?
5. Is there FAQ schema or structured Q&A content?
6. Are there specific data points, numbers, or benchmarks?
7. Is any content gated, collapsed, or JS-rendered?

Output:
- A score (1-5) for current citation readiness
- Specific changes needed
- Rewritten sections where the current version is not citable
```
