# Content Repurposing Automation

Use Notion AI to automatically transform a single piece of content into multiple formats — saving hours of manual reformatting work.

## Overview

A blog post can become a LinkedIn article, Twitter thread, email newsletter, and YouTube script. This automation workflow uses Notion AI properties to generate each format automatically from your source content.

## Workflow

```
Source Content (Blog Post)
        ↓
   Notion AI Properties
        ↓
┌───────────────────────────┐
│  LinkedIn Post            │
│  Twitter/X Thread         │
│  Email Newsletter Snippet │
│  YouTube Script Outline   │
│  Instagram Caption        │
└───────────────────────────┘
```

## Setup

### 1. Create a Content Database

Properties needed:
- **Title** (Title)
- **Source Content** (Text) — your original long-form content
- **Content Type** (Select) — Blog, Video Script, Podcast Notes, etc.
- **Target Audience** (Text) — who this is for

### 2. Add AI Repurposing Properties

Add one AI property per output format:

**LinkedIn Post:**
> "Rewrite the following content as a LinkedIn post (150-300 words). Use a professional tone, include 2-3 insights, and end with a question to drive engagement. Content: {{Source Content}}"

**Twitter Thread:**
> "Convert the following content into a Twitter thread of 5-8 tweets. Each tweet must be under 280 characters. Start with a hook, number each tweet. Content: {{Source Content}}"

**Email Newsletter:**
> "Summarize the following content into a 100-word email newsletter teaser. Include a compelling subject line suggestion. Content: {{Source Content}}"

**YouTube Script Outline:**
> "Create a YouTube video script outline from this content: intro hook, 3-5 main sections with talking points, and a call-to-action. Content: {{Source Content}}"

### 3. Automate the Workflow

Create a button property "Repurpose Content":
1. Click the button to trigger all AI properties to populate
2. Review and edit each output
3. Use a "Publishing Status" property to track which formats have been published

## Best Practices

- Always review AI-generated content before publishing
- Customize the prompts to match your brand voice
- Keep a "Content Vault" database to track all repurposed versions
- Use consistent hashtag/keyword properties to maintain SEO alignment

## Related

- [Meeting to Tasks](meeting-to-tasks.md)
- [Research Compilation](research-compilation.md)

---

*Last Updated: April 2026*
