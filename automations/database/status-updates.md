status-updates.md# Status Updates Automation

Automatically update task and project statuses in Notion based on triggers, time conditions, and AI analysis.

## Overview

This automation keeps your databases current without manual updates, using Notion's built-in automations combined with AI properties to intelligently advance status through your workflow.

## Common Status Workflows

### Task Status Progression
`Not Started → In Progress → In Review → Done`

### Project Health Status
`On Track → At Risk → Blocked → Completed`

## Setup

### 1. Define Your Status Flow

Configure your database's Status property with clear stages:
- **Not Started** — work hasn't begun
- **In Progress** — actively being worked on
- **In Review** — awaiting feedback or approval
- **Blocked** — waiting on dependency
- **Done** — completed

### 2. Create Automation Triggers

**Time-based:** Move overdue tasks to "At Risk"
1. Open database Automations
2. Trigger: "When Due Date is passed"
3. Action: Edit Status → "At Risk"

**Completion-based:** Auto-close subtasks
1. Trigger: "When all sub-items are checked"
2. Action: Edit Status → "Done"

### 3. AI-Powered Status Suggestions

Add an AI property for smart status recommendations:
- Property name: **AI Status Check**
- Prompt: "Based on the task description, due date, and last edited date, suggest: On Track, At Risk, or Blocked. Explain briefly."

### 4. Cascading Status Updates

Use relations to cascade status:
- When a parent project moves to "Done", prompt review of all child tasks
- When a task is "Blocked", flag the parent project

## Notification Setup

Connect to Slack or email:
1. Trigger: "When Status changes to Blocked"
2. Action: Send Slack message to project channel

## Best Practices

- Review AI status suggestions weekly
- Set clear criteria for each status value
- Don't over-automate — some status changes need human judgment
- Archive "Done" items monthly to keep databases clean

## Related

- [Auto-Assign Tasks](auto-assign-tasks.md)
- [Property Cascading](property-cascading.md)

---

*Last Updated: April 2026*
