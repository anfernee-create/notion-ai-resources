# Project Tracking for Teams

Build a centralized, AI-enhanced project tracking system in Notion that gives your team real-time visibility into progress, risks, and blockers.

## System Overview

A team project tracking system needs to answer three questions instantly: What's the current status? What's at risk? What needs attention today? Notion AI helps surface these answers automatically.

## Database Structure

### Projects Database
- **Name** (Title)
- **Status** (Select) — Planning / Active / On Hold / Complete
- **Owner** (Person)
- **Start Date** / **Due Date** (Date)
- **Priority** (Select) — P0 / P1 / P2 / P3
- **Health** (Select) — Green / Yellow / Red
- **AI Status Summary** (AI) — auto-generated project summary
- **AI Risk Analysis** (AI) — identifies potential issues
- **Progress %** (Number)

### Tasks Database
- **Task** (Title)
- **Project** (Relation) → Projects
- **Assignee** (Person)
- **Status** (Select)
- **Due Date** (Date)
- **Blockers** (Text)
- **AI Blocker Analysis** (AI) — suggests how to resolve blockers

## AI-Powered Views

### Daily Standup View
Filter: Tasks due today or overdue, grouped by assignee
AI property: "Based on open tasks and blockers, what should this person focus on today?"

### Weekly Status Report
AI property on Projects: "Generate a 3-sentence status update for stakeholders covering: current progress, key accomplishments this week, and any risks or blockers."

### Risk Radar
Filter: Projects where Health = Yellow or Red
AI property: "What are the top 3 risks for this project and what are the recommended mitigation actions?"

## Automation Workflows

1. **Auto-update project health**: When task overdue count > 3, set Health = Yellow; > 6 = Red
2. **Milestone notifications**: When Progress % reaches 25/50/75/100, send Slack update
3. **Weekly report generation**: Every Monday, AI generates project status summary

## Dashboard Setup

Create a Team Dashboard page with:
- Linked database view: Active projects (board view by health)
- Linked database view: Tasks due this week (table view)
- Linked database view: Overdue tasks (table view)
- Weekly AI summary (AI block)

## Best Practices

- Update task status daily — 30 seconds per person
- Use health indicators consistently (define criteria as a team)
- Review AI risk analysis in weekly team sync
- Archive completed projects monthly

## Related

- [Meeting Management](meeting-management.md)
- [Team Wiki](knowledge-sharing.md)

---

*Last Updated: April 2026*
