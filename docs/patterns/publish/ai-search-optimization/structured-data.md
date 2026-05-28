---
description: "Schema.org structured data for podcast episodes. JSON-LD templates for PodcastEpisode, FAQPage, and VideoObject markup."
---

# Structured Data

**Stage:** Publish → AI Search Optimization  
**Score:** 5  
**Evidence:** Google documentation, platform observation

## What It Is

Structured data is machine-readable markup (JSON-LD) embedded in your episode web pages that tells search engines and AI systems exactly what your content is, who created it, what it covers, and how to cite it.

## Why It Works

AI systems do not "read" your page like a human. They parse structured signals. Schema.org markup is the universal language that Google, Bing, Perplexity, and other AI systems use to understand content at scale. Without it, your episode is just another blob of text. With it, your episode has typed, structured identity.

## Required Schema Types

### PodcastEpisode

The primary schema for every episode page.

```json
{
  "@context": "https://schema.org",
  "@type": "PodcastEpisode",
  "name": "Episode Title",
  "description": "Episode description",
  "url": "https://yoursite.com/episodes/episode-slug",
  "datePublished": "2026-05-28",
  "duration": "PT45M",
  "episodeNumber": 42,
  "partOfSeries": {
    "@type": "PodcastSeries",
    "name": "Your Show Name",
    "url": "https://yoursite.com"
  },
  "associatedMedia": {
    "@type": "AudioObject",
    "contentUrl": "https://yourcdn.com/episode-42.mp3",
    "encodingFormat": "audio/mpeg"
  },
  "author": {
    "@type": "Person",
    "name": "Host Name"
  },
  "guest": {
    "@type": "Person",
    "name": "Guest Name",
    "jobTitle": "Guest Title",
    "worksFor": {
      "@type": "Organization",
      "name": "Guest Company"
    }
  }
}
```

### FAQPage

Add FAQ schema when your show notes include questions and answers extracted from the episode.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the best way to repurpose podcast episodes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The most effective approach is to create horizontal and vertical assets during production, not after. This includes..."
      }
    }
  ]
}
```

### VideoObject

Add when the episode has a video version.

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Episode Title",
  "description": "Episode description",
  "thumbnailUrl": "https://yoursite.com/thumbnails/ep42.jpg",
  "uploadDate": "2026-05-28",
  "duration": "PT45M",
  "contentUrl": "https://youtube.com/watch?v=xxxxx",
  "embedUrl": "https://youtube.com/embed/xxxxx"
}
```

## Quality Bar

- Every episode page must have `PodcastEpisode` schema at minimum
- Add `FAQPage` when show notes contain Q&A content
- Add `VideoObject` when a video version exists
- Validate with [Google Rich Results Test](https://search.google.com/test/rich-results)
- Keep `datePublished` accurate — AI systems use recency as a quality signal
- Include `guest` data with full name, title, and company

## When Not To Use

Always use structured data. There is no scenario where omitting it is beneficial. The only risk is incorrect markup, which is worse than no markup — validate before publishing.

## Prompt Template

Copy and customize this prompt to generate structured data for an episode:

```
Generate JSON-LD structured data for a podcast episode page.

Episode details:
- Title: [episode title]
- Description: [episode description]
- Show name: [series name]
- Episode number: [number]
- Date published: [YYYY-MM-DD]
- Duration: [minutes]
- Host: [name]
- Guest: [name, title, company]
- Audio URL: [MP3 URL]
- Video URL: [YouTube URL, if applicable]
- Episode page URL: [canonical URL]
- Key Q&A from the episode (for FAQ schema):
  - Q: [question from the episode]
  - A: [answer discussed]

Generate:
1. PodcastEpisode schema
2. FAQPage schema (if Q&A provided)
3. VideoObject schema (if video URL provided)

Output as valid JSON-LD ready to paste into <script type="application/ld+json"> tags.
```
