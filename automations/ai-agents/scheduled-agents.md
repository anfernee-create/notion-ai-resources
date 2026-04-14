scheduled-agents.md# Scheduled Agents

Run Notion AI Agents on a schedule to automatically maintain, update, and audit your workspace without manual intervention.

## Overview

Scheduled agents are time-based automations that run at defined intervals — daily, weekly, monthly, or on a custom schedule. They're ideal for recurring tasks like daily standup preparation, weekly report generation, and monthly data cleanup.

## Common Scheduled Agent Use Cases

### Daily Agents (Run every morning)
- **Standup Prep**: Summarize yesterday's completed tasks and today's priorities for each team member
- **Overdue Task Alert**: Scan all databases for tasks past their due date and create a daily alert page
- **Inbox Zero**: Process and categorize items in a "capture" database

### Weekly Agents (Run every Monday)
- **Weekly Review**: Compile completed work from the past week into a summary report
- **Goal Progress Check**: Compare current progress against weekly goals and flag at-risk items
- **Pipeline Refresh**: Update sales pipeline status based on last activity date

### Monthly Agents (Run first of month)
- **Link Audit**: Check for broken links or outdated references across documentation
- **Content Calendar Reset**: Create next month's content calendar from template
- **Team Performance Summary**: Generate monthly productivity metrics from task completion data

## Setup

### 1. Create a Scheduled Automation

1. Open your target database
2. Go to **Automations** → **New Automation**
3. Set trigger to **"On a schedule"**
4. Configure: Daily / Weekly / Monthly / Custom (cron-like)
5. Set the time zone and run time

### 2. Define Agent Instructions

Write clear, specific instructions for what the agent should do:

**Good agent instruction:**
> "Every Monday at 8 AM: 
> 1. Query all tasks in the 'Active Projects' database where Status = 'In Progress' and Due Date < today
> 2. For each overdue task, update the 'Risk Flag' property to 'Overdue'
> 3. Create a new page called 'Overdue Report - [date]' in the 'Weekly Reports' database
> 4. List all overdue tasks grouped by project with owner names"

### 3. Test Your Schedule

Before enabling on schedule:
1. Use the "Run now" button to test manually
2. Check the output carefully
3. Verify no unintended side effects
4. Enable the schedule once verified

## Monitoring Scheduled Agents

### Agent Run Log

Create a monitoring database:
- **Agent Name** (Title)
- **Last Run** (Date)
- **Status** (Select) — Success / Failed / Warning
- **Output Summary** (Text)
- **Error Details** (Text)

Have your agent write to this log at the end of each run.

### Alert on Failure

Set up a secondary automation:
- Trigger: When "Status" in Agent Run Log changes to "Failed"
- Action: Send Slack or email notification

## Scheduling Best Practices

- Stagger heavy agents to avoid running simultaneously
- Run daily agents during off-peak hours (e.g., 6 AM)
- Test with weekly frequency before moving to daily
- Build in a "pause" mechanism — a property that skips the run if set to "Paused"
- Review agent outputs weekly for the first month

## Related

- [Notion 3.0 Agents](notion-3-agents.md)
- [Multi-Step Workflows](multi-step-workflows.md)

---

*Last Updated: April 2026*
