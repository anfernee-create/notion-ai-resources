# Meeting to Tasks Automation

Automatically convert meeting notes and transcripts into structured, assigned action items using Notion AI.

## Overview

Stop losing action items in meeting notes. This automation uses Notion AI to extract commitments, assign owners, and create tasks directly from your meeting records — eliminating manual follow-up work.

## Workflow

```
Meeting Notes/Transcript
         ↓
   Notion AI Extraction
         ↓
┌─────────────────────┐
│ Action Items        │
│ Owners Identified   │
│ Due Dates Suggested │
│ Priority Assigned   │
└─────────────────────┘
         ↓
   Tasks Database
```

## Setup

### 1. Meeting Notes Database

Create a database with these properties:
- **Title** (Title) — meeting name
- **Date** (Date) — when the meeting occurred
- **Attendees** (Person) — who was present
- **Raw Notes** (Text) — meeting notes/transcript
- **AI Action Items** (AI property) — extracted actions
- **AI Summary** (AI property) — condensed meeting summary

### 2. Configure AI Action Item Extraction

Set up the AI property:
- Name: **Action Items**
- Prompt: "From the following meeting notes, extract all action items. For each action item, list: (1) the task description, (2) the owner (person responsible), (3) suggested due date if mentioned, (4) priority (High/Medium/Low). Format as a numbered list. Notes: {{Raw Notes}}"

### 3. Create the Task Creation Automation

Option A — Manual trigger (Button property):
1. Add a Button property: "Create Tasks from Meeting"
2. When clicked, use AI output to create entries in your Tasks database

Option B — Automatic (Notion AI Agents):
1. Set up an AI Agent to watch for new meeting notes
2. Agent reads AI Action Items property
3. Agent creates individual task entries for each action item

### 4. Task Database Integration

Configure your Tasks database to accept meeting-generated tasks:
- **Source** (Select) — "Meeting Auto-Generated" vs "Manual"
- **Meeting Link** (Relation) — link back to originating meeting
- **AI Confidence** (Select) — High/Medium/Low extraction confidence

## Best Practices

- Clean up notes before running AI extraction for better results
- Review AI-generated tasks before they're assigned
- Use a naming convention for meeting-generated tasks
- Send a follow-up summary to attendees with extracted action items

## Related

- [Content Repurposing](content-repurposing.md)
- [Research Compilation](research-compilation.md)

---

*Last Updated: April 2026*
