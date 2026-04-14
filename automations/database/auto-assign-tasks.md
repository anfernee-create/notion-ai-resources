# Auto-Assign Tasks

Automatically assign tasks to team members based on rules, workload, and expertise using Notion AI.

## Overview

This automation workflow uses Notion AI database properties and formulas to intelligently assign tasks without manual intervention. By combining AI-powered categorization with database relations, you can build a system that routes work to the right person automatically.

## Prerequisites

- Notion Business or Enterprise plan
- Team database with member profiles
- Project/task database with relevant properties

## Setup

### 1. Configure Your Task Database

Add these properties to your task database:
- **Assignee** (Person) — who the task belongs to
- **Skill Tags** (Multi-select) — required skills
- **Priority** (Select) — High / Medium / Low
- **AI Category** (AI property) — auto-categorized task type
- **Complexity** (AI property) — estimated complexity score

### 2. Build the Assignment Formula

Use a formula property to suggest assignees:

```
if(
  prop("AI Category") == "Engineering",
  "Engineering Team",
  if(
    prop("AI Category") == "Design",
    "Design Team",
    "General Team"
  )
)
```

### 3. Create Assignment Triggers

Use Notion automations (Button or recurring trigger):
1. Go to **Automations** in your database
2. Set trigger: "When task status changes to In Progress"
3. Action: "Edit property" → Set Assignee based on formula result

### 4. AI-Assisted Routing

Use the Notion AI property to auto-fill:
- **AI Category**: Prompt — "Categorize this task into: Engineering, Design, Marketing, Operations, or Other"
- **Complexity**: Prompt — "Rate task complexity 1-5 based on title and description"

## Workflow Example

1. New task created in database
2. AI Category auto-fills (Engineering)
3. Formula calculates suggested assignee
4. Automation triggers assignment
5. Assignee notified via Slack/email integration

## Best Practices

- Regularly review AI categorization accuracy
- Update skill tags as team expertise evolves
- Build in escalation rules for high-priority items
- Monitor assignment distribution for workload balance

## Related Automations

- [Status Updates](status-updates.md)
- [Property Cascading](property-cascading.md)

---

*Last Updated: April 2026*
