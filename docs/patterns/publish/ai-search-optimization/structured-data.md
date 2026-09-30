---
description: "Structured data describes episode identity, media, and visible page content in machine-readable JSON-LD."
---

# Structured Data

Structured data describes episode identity, media, and visible page content in machine-readable JSON-LD. Use applicable Schema.org types and validate markup; schema does not replace readable content or guarantee search features.

**Stage:** Publish → AI Search Optimization  
**Score:** 5  
**Evidence:** Google documentation, platform observation

## What It Is

Structured data is machine-readable markup (JSON-LD) embedded in your episode web pages that tells search engines and AI systems exactly what your content is, who created it, what it covers, and how to cite it.

## Why It Works

Schema.org markup gives an episode explicit, machine-readable identity alongside the visible page. It is not a universal requirement for AI discovery: [Google states](https://developers.google.com/search/docs/appearance/ai-features) that its AI features require no special schema or additional markup. Keep structured data consistent with the visible content, and do not treat valid markup as proof of citation eligibility across every platform.

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

FAQPage describes visible questions and answers. Use it only for content actually present on the page; do not infer Google rich-result eligibility or AI-citation benefit from this template.

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
  "contentUrl": "https://yourcdn.com/episode-42.mp4",
  "embedUrl": "https://youtube.com/embed/xxxxx"
}
```

The example URLs and dates are placeholders. A VideoObject contentUrl should identify the media file; use embedUrl for the player. Validate Schema.org vocabulary separately from eligibility for a specific search feature.

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
