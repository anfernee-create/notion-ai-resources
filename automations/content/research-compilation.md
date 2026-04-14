# Research Compilation Automation

Automatically gather, summarize, and organize research from multiple sources into structured Notion databases using AI.

## Overview

Research compilation is one of the highest-leverage use cases for Notion AI. Instead of manually reading dozens of sources and transferring notes, this workflow uses AI to extract key information, identify patterns, and synthesize findings — all organized in your Notion workspace.

## Setup

### 1. Research Inbox Database

Create a database to capture raw research:
- **Source URL** (URL) — link to original content
- **Source Type** (Select) — Article, Paper, Video, Podcast, Book
- **Raw Content** (Text) — paste or summarize the source
- **AI Key Points** (AI) — extracted main insights
- **AI Relevance Score** (AI) — rate relevance to your research question
- **AI Connections** (AI) — how this connects to other research
- **Research Topic** (Select/Relation) — categorization

### 2. AI Extraction Prompts

**Key Points Extraction:**
> "Extract the 5 most important insights from this content. Focus on novel findings, statistics, and actionable information. Content: {{Raw Content}}"

**Relevance Scoring:**
> "On a scale of 1-10, rate how relevant this content is to the topic: [YOUR TOPIC]. Explain your rating in one sentence. Content: {{Raw Content}}"

**Connection Finding:**
> "What existing knowledge, theories, or concepts does this content support, contradict, or extend? Content: {{Raw Content}}"

### 3. Synthesis Database

Create a second database for compiled findings:
- **Research Question** (Title)
- **Compiled Insights** (Text) — roll up from Research Inbox
- **AI Synthesis** (AI) — generate a synthesis from all linked sources
- **AI Gaps** (AI) — identify what's missing in the research
- **Sources** (Relation) — linked research items

### 4. Automated Tagging

Use an automation to auto-tag research items:
1. Trigger: "When new item is created"
2. Action: Run AI property to classify topic
3. Action: Set Research Topic based on classification

## Advanced: Multi-Source Synthesis

For deep research projects, use the Synthesis database:
1. Link 10-20 research items to a research question
2. Use AI property: "Synthesize the key findings from all linked sources. Identify consensus views, contradictions, and knowledge gaps."
3. Export synthesis as a structured report

## Best Practices

- Add sources as you find them — don't batch later
- Use consistent tagging for cross-project research retrieval
- Run synthesis after adding every 5-10 new sources
- Include your own annotations alongside AI summaries

## Related

- [Content Repurposing](content-repurposing.md)
- [Meeting to Tasks](meeting-to-tasks.md)

---

*Last Updated: April 2026*
