# Code Snippet Library

Build a searchable, AI-enhanced personal and team code snippet library in Notion — eliminating the "I wrote this before, where is it?" problem.

## Overview

Developers reuse code constantly but often waste time searching through old projects, Stack Overflow bookmarks, or their memory. A Notion code snippet library makes your accumulated code knowledge instantly searchable and AI-queryable.

## Database Structure

- **Title** (Title) — descriptive snippet name
- **Language** (Select) — JavaScript, Python, SQL, Bash, etc.
- **Category** (Multi-select) — API, Auth, Data Transform, UI, Algorithm, etc.
- **Code** (Code block) — the actual snippet
- **Description** (Text) — what it does and when to use it
- **AI Explanation** (AI) — plain English explanation
- **AI Use Cases** (AI) — when to use this snippet
- **AI Variations** (AI) — alternative approaches
- **Tags** (Multi-select) — searchable keywords
- **Source** (URL) — original reference
- **Last Used** (Date)

## AI Property Prompts

**Plain English Explanation:**
> "Explain what this code does in plain English. Assume the reader is a junior developer. Include: what problem it solves, how it works step by step, and any important edge cases. Code: {{Code}}"

**Use Cases:**
> "List 5 specific scenarios where you would use this code snippet. Be concrete and practical. Code: {{Code}}"

**Variations:**
> "Show 2-3 alternative ways to achieve the same result as this code. Include tradeoffs (performance, readability, browser support, etc.). Code: {{Code}}"

## Using the Library

### Search Strategy
Notion's search works well for snippet libraries. Search by:
- Language (filter)
- Category (filter)
- Keywords in title or description
- AI Explanation (contains natural language)

### AI-Powered Discovery
Use Notion AI chat on your snippet database:
> "I need to parse a JWT token in JavaScript without a library. Do we have any snippets that could help?"

## Snippet Capture Workflow

When you write useful code:
1. Create a new snippet entry immediately (takes 2 minutes)
2. Paste the code
3. Write a brief description
4. Let AI generate explanation and use cases
5. Add tags

When you find useful code online:
1. Capture URL + code
2. Adapt it to your patterns before saving
3. Note any dependencies or limitations

## Team Library

For shared team snippets:
- Add a "Contributor" (Person) property
- Add a "Verified" (Checkbox) property — vetted by senior devs
- Create a "Proposed" section for unverified submissions
- Weekly review to promote good snippets to verified

## Best Practices

- Name snippets descriptively: "Parse ISO date string to local timezone" not "date helper"
- Include the failing test case that led to the snippet
- Update snippets when you find better approaches — don't delete, add to "Variations"
- Tag with framework versions to avoid outdated code confusion

## Related

- [Documentation Generator](documentation-generation.md)
- [Bug Tracking](bug-tracking.md)

---

*Last Updated: April 2026*
