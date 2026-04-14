# Meeting Management for Teams

Use Notion AI to make your team meetings more effective — from preparation to follow-up.

## The Meeting Problem

Most teams waste 30-50% of meeting time on logistics: finding previous decisions, recapping context, and writing action items. Notion AI eliminates this overhead.

## System Setup

### Meeting Database

- **Title** (Title) — meeting name
- **Type** (Select) — Standup / Planning / Retrospective / 1:1 / All-hands
- **Date** (Date)
- **Attendees** (Person)
- **Agenda** (Text) — pre-meeting agenda
- **Notes** (Text) — live notes
- **AI Summary** (AI) — post-meeting summary
- **AI Action Items** (AI) — extracted tasks
- **AI Decisions** (AI) — key decisions made
- **AI Follow-ups** (AI) — items needing follow-up

### AI Property Prompts

**Summary:** "Summarize this meeting in 3-5 bullet points covering the main topics discussed and outcomes. Notes: {{Notes}}"

**Action Items:** "Extract all action items from these meeting notes. For each: task description, owner, due date (if mentioned). Notes: {{Notes}}"

**Decisions:** "List all decisions made in this meeting. Format: Decision → Rationale → Owner. Notes: {{Notes}}"

## Meeting Templates

### Standup Template (15 min)
- Yesterday: What did you complete?
- Today: What are you working on?
- Blockers: What's in your way?

### Sprint Planning Template (1 hour)
- Goal for this sprint
- Capacity per team member
- Stories to commit
- Dependencies and risks

### Retrospective Template (45 min)
- What went well?
- What could improve?
- Action items for next sprint

## Automated Follow-up Workflow

After each meeting:
1. AI generates summary and action items
2. Action items auto-created in team task database
3. Summary shared in team Slack channel (via integration)
4. Next meeting agenda seeded with open action items

## Best Practices

- Assign a note-taker rotation
- Use live AI suggestions during meetings
- Review AI action items before ending the meeting
- Link meeting notes to relevant projects

## Related

- [Project Tracking](project-tracking.md)
- [Team Wiki](knowledge-sharing.md)

---

*Last Updated: April 2026*
