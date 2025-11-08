# Email Notification Automations for Notion

## Overview
Complete guide to setting up automated email notifications triggered by Notion database changes using Zapier, Make, and IFTTT.

## Email Automation Types

### 1. Daily Digest Emails

**Use Case**: Summary of today's tasks and updates

**Setup with Zapier**:
1. Trigger: Schedule (every day at 8 AM)
2. Action 1: Query Notion database
   - Filter: Due Date = Today
   - Sort: Priority (descending)
3. Action 2: Formatter - Format tasks into readable list
4. Action 3: Send email
   - To: User email
   - Subject: "Your Daily Digest - [Date]"
   - Body: Formatted task list

**Email Template**:
```
Subject: Your Daily Digest - November 8, 2025

Good Morning! 🌅

Here's what's on your plate today:

🔴 URGENT (3 tasks)
• Task 1 - Due 5:00 PM
• Task 2 - Due 3:00 PM
• Task 3 - Due 6:00 PM

🟡 HIGH (2 tasks)
• Task 4 - Due 11:00 AM
• Task 5 - Due 2:00 PM

🟢 MEDIUM (1 task)
• Task 6 - No specific time

Total: 6 tasks
Completed today: 2/8

Have a productive day! 🚀
```

### 2. Deadline Reminders

**Use Case**: Alert when task due date is approaching

**Setup with Zapier**:
1. Trigger: Schedule (every morning)
2. Action 1: Query Notion
   - Filter: Due Date = Tomorrow
3. Action 2: For each result, send email
   - Subject: "Reminder: [Task Name] due tomorrow"
   - Include deadline time
   - Add link to task

**Advanced Setup**:
```
Condition: If days until due date < 2
  Then: Send urgent email
  Include: Escalation instructions
  Cc: Manager/supervisor
Else: Send normal reminder
```

### 3. Status Change Notifications

**Use Case**: Alert when project/task status changes

**Setup with Zapier**:
1. Trigger: Notion database item updated
   - Filter: Status property changed
2. Action 1: Get full record details
3. Action 2: Send email to stakeholders
   - Subject: "[Project] Status changed to [Status]"
   - Body: Include previous status, new status, timestamp
   - Include who made the change

**Example**:
```
Subject: Project Alpha Status Updated

Project: Project Alpha
Previous Status: In Progress
New Status: Review
Updated By: John Smith
Updated At: 2:30 PM today

Next Steps:
1. Internal review (2 days)
2. Client approval (3 days)
3. Final deployment

Review the project: [Link]
```

### 4. New Record Notifications

**Use Case**: Alert when new item added to database

**Setup with Zapier**:
1. Trigger: Notion database item created
2. Action 1: Send email to assigned person
   - Subject: "New [Type]: [Name]"
   - Body: Include all important details
   - Add due date if applicable

**Email Content**:
```
A new task has been assigned to you:

Task: Complete quarterly review
Assigned By: HR Department
Due Date: November 15, 2025
Priority: HIGH
Description: [Full description]

Action Required By: November 15

View task: [Link]
```

### 5. Approval Request Emails

**Use Case**: Request approval for pending items

**Setup**:
1. Trigger: Database item status = "Pending Approval"
2. Action 1: Find approver from database
3. Action 2: Send approval request email
   - Include approve/reject buttons (if supported)
   - Include item details
   - Include deadline

**Email Format**:
```
Subject: Approval Needed: [Item Name]

Action Required:

Please review and approve:
[Item Details]

[Approve Button] [Request Changes]

Deadline: November 10, 2025

View details: [Link]
```

### 6. Weekly Reports

**Use Case**: Weekly summary of progress

**Setup with Zapier**:
1. Trigger: Schedule (every Monday at 9 AM)
2. Actions: Query multiple databases
   - Completed tasks this week
   - In-progress items
   - Blocked items
   - Upcoming deadlines
3. Send formatted weekly email

**Email Template**:
```
Subject: Weekly Report - Week of November 3-9

📊 This Week's Overview

✅ Completed (8 items)
• Item 1
• Item 2
• Item 3
[...]

🔄 In Progress (5 items)
• Item A - 75% complete
• Item B - 50% complete
[...]

🚧 Blocked (2 items)
• Item X - Waiting for client feedback
• Item Y - Resource unavailable

⏰ Next Week's Priorities
1. Complete Item Z
2. Start new project
3. Team meeting

Metrics:
Productivity: 85%
On-time completion: 92%
Team morale: 8/10
```

### 7. Custom Alert Emails

**Use Case**: Alert on specific conditions

**Conditions to trigger**:
- Budget exceeded
- Deadline missed
- Priority changed to Critical
- Assignment changed
- Database item archived
- Field value reaches threshold

**Setup Example** (Budget Alert):
```
Trigger: Database item updated
Condition: "Budget Used" > "Budget"
Actions:
1. Send alert email to:
   - Project manager
   - Finance lead
   - Project owner
2. Include:
   - Budget amount
   - Amount spent
   - Overage amount
   - Percentage over budget
3. Add: Approval link to increase budget
```

## Advanced Email Features

### Conditional Logic

```
IF Status = "Overdue"
  THEN: Send urgent email with red styling
  BCC: Supervisor
ELSE IF Priority = "High"
  THEN: Send normal email
ELSE
  THEN: Add to weekly digest
```

### Dynamic Recipients

```
Email recipient based on:
1. Assigned person from database
2. Project lead (lookup from Clients DB)
3. Team lead (lookup from Teams DB)
4. Department manager (lookup from Org chart)
5. Stakeholders (multi-select field)
```

### Email Formatting

HTML-formatted emails with:
- Color coding by priority
- Embedded buttons/links
- Tables for data display
- Logos and branding
- Conditional sections
- Dynamic content

### Attachment Support

```
Zapier Formatter:
1. Generate CSV from Notion data
2. Create PDF report
3. Attach to email
4. Send with formatted body
```

## Email Templates Library

### Template 1: Task Assignment
```
Subject: New Task: [Name]
To: [Assigned Person]
From: system@notion-automation.com

You've been assigned a new task:

Task: [Task Name]
Assigned By: [Person]
Due: [Date] at [Time]
Priority: [Priority]
Project: [Project]

[Description]

Start task: [Button Link]
```

### Template 2: Status Update
```
Subject: Status Update: [Project]
To: [Stakeholders]

[Project Name] Status: [Status]

Progress:
[Status Bar]
[Percentage]% Complete

Next Milestone: [Milestone]
Expected: [Date]

Latest Updates:
• [Update 1]
• [Update 2]
• [Update 3]
```

### Template 3: Approval Request
```
Subject: Approval Required: [Item]
To: [Approver]
Urgency: [High/Normal/Low]

Request:
[Item Details]

[Approve] [Reject] [Request Changes]

Deadline: [Date]
```

## Best Practices

### Email Frequency
- Daily digest: Once per day (8-9 AM)
- Urgent alerts: Immediate (no delay)
- Status updates: Real-time on change
- Weekly reports: Once per week (Monday 9 AM)
- Reminders: 1-2 days before deadline

### Preventing Email Overload
1. Use digest/summary emails
2. Set minimum priority threshold
3. Batch similar notifications
4. Allow user preferences
5. Unsubscribe options
6. Daily limits per person

### Email Subject Lines
✅ Good:
- "Task Due Tomorrow: Complete Report"
- "Project Status Changed to Review"
- "Your Daily Digest - 5 tasks today"

❌ Avoid:
- "Notification"
- "Update"
- "Action Required"

### Personalization
- Use recipient's name
- Reference their role
- Include relevant context
- Use their timezone
- Match communication style

## Automation Recipes

### Recipe 1: Daily Standup
```
Schedule: 8 AM daily
Content: Tasks + In progress + Blockers
Recipient: Team members
Frequency: Every work day
```

### Recipe 2: Weekly Digest
```
Schedule: Monday 9 AM
Content: Weekly summary + Metrics
Recipient: Stakeholders
Frequency: Weekly
```

### Recipe 3: Urgent Alerts
```
Trigger: Deadline missed OR Priority=Critical
Content: Alert + Action items
Recipient: Owner + Manager
Frequency: Immediate
Escalation: SMS after 1 hour if not acknowledged
```

### Recipe 4: Monthly Report
```
Schedule: 1st of month, 10 AM
Content: Monthly summary + KPIs
Recipient: Leadership + Team
Format: HTML with charts
Frequency: Monthly
```

## Integration Options

**Email Providers**:
- Gmail (via Zapier)
- Outlook (via Make)
- SendGrid (via API)
- Mailgun (via API)
- AWS SES (via integration)

**Automation Platforms**:
- Zapier (easiest, 15-min check-in free)
- Make (more flexible, 1-min check-in)
- IFTTT (simple, limited)
- n8n (self-hosted, advanced)
- Integromat (Make's name in some regions)

## Cost Optimization

**Zapier Pricing**:
- Free: 100 tasks/month, 15-min intervals
- Pro: $20-99/month, faster intervals
- Enterprise: Custom pricing

**Strategy**:
1. Use free tier for non-critical emails
2. Batch emails to reduce task count
3. Use schedules instead of continuous monitoring
4. Consolidate multiple notifications

## Troubleshooting

**Emails not sending**:
1. Check Zapier task history
2. Verify email address format
3. Check spam filters
4. Verify filter conditions
5. Test with sample record

**Wrong recipient**:
1. Verify email mapping
2. Check lookup formulas
3. Test field references
4. Ensure data exists in lookup tables

**Formatting issues**:
1. Test with HTML formatter
2. Check special characters
3. Verify line breaks
4. Test in different email clients
