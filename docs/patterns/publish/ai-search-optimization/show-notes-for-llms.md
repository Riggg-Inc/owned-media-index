---
description: "How to structure show notes so AI systems can extract and cite your content. Q&A formatting, key claims, and direct answer architecture."
---

# Show Notes for LLMs

**Stage:** Publish → AI Search Optimization  
**Score:** 4  
**Evidence:** LLM retrieval testing, practitioner observation

## What It Is

Show notes structured specifically so that AI systems can extract direct answers from your episode page. This goes beyond traditional show notes (timestamps + links) into a format that turns your episode into an answer source for AI queries.

## Why It Works

When someone asks ChatGPT, Perplexity, or Google AI a question, the AI looks for content that directly answers the question in a structured, citable format. Traditional show notes — a paragraph summary plus a list of timestamps — do not give AI systems extractable answers.

Show notes structured as Q&A, key claims, and structured takeaways become candidate sources for AI-generated answers.

## Structure

### 1. Episode Summary (2-3 sentences)

The summary should read like a direct answer to "What is this episode about?"

```markdown
## Summary

Sarah Chen, VP of Content at HubSpot, explains why B2B podcast teams should stop 
optimizing for downloads and start building a content repurposing engine. She shares 
the exact system her team uses to turn one recorded conversation into 15 publishable 
assets in under a week.
```

### 2. Key Questions Answered

Frame show notes as questions the episode answers. AI systems are literally answering questions — give them your content in that format.

```markdown
## Questions Answered in This Episode

### How many assets should one podcast episode produce?
Sarah's team produces a minimum of 15 derivative assets from each recording session, 
including 3 video clips, 5 social posts, 2 quote graphics, 1 blog summary, 1 email, 
1 guest-share package, and the full episode in audio and video.

### What is the biggest mistake B2B podcast teams make?
According to Sarah, the biggest mistake is treating the podcast as a campaign instead 
of a media property — optimizing for lead capture instead of audience value.

### How long should the production turnaround be?
Sarah recommends a 3-5 day turnaround from recording to full asset package delivery. 
Teams taking longer than 7 days are losing momentum and relevance.
```

### 3. Key Claims (Specific, Quotable)

List 3-5 specific claims from the episode that AI systems can quote and attribute.

```markdown
## Key Claims

- "One recorded conversation should produce a minimum of 15 publishable assets." — Sarah Chen
- "Teams taking longer than 7 days to deliver are losing 40% of their distribution window." — Sarah Chen
- "The podcast is not a campaign. It is a media property. Treat it like one." — Sarah Chen
```

### 4. Resources and References

Structured with names and URLs so AI systems can verify and link.

```markdown
## Resources Mentioned

- [HubSpot Content Repurposing Framework](https://example.com) — Sarah's internal playbook
- [Owned Media Index](https://riggg-inc.github.io/owned-media-index/) — patterns for packaging and distribution
```

## Quality Bar

- Summary answers "What is this about?" in 2-3 sentences
- Minimum 3 questions answered, each with a direct, extractable answer
- Minimum 3 key claims with speaker attribution
- Resources linked with full URLs
- Published on the canonical episode page (not gated)
- All answers must be factually accurate and verifiable from the episode content

## When Not To Use

Always structure show notes this way. If you do not have time to format Q&A, at minimum publish the summary and key claims. Even partial structure is better than none.

## Prompt Template

```
Write AI-optimized show notes for this podcast episode.

Episode details:
- Title: [title]
- Guest: [name, title, company]
- Host: [name]
- Episode summary: [1-2 sentences about what the episode covers]
- Key topics discussed: [list 3-5 topics]

Transcript excerpt (or full transcript):
[paste transcript or key sections]

Generate:
1. Summary (2-3 sentences, direct answer to "what is this episode about")
2. Questions Answered (3-5 questions with direct, extractable answers from the episode)
3. Key Claims (3-5 specific, quotable statements with speaker attribution)
4. Resources Mentioned (name + URL for anything referenced)

Requirements:
- Every answer must be specific enough for an AI to quote directly
- Claims must include speaker attribution
- Questions should match how a practitioner would ask them in a search engine
- Total length: 400-600 words
```
