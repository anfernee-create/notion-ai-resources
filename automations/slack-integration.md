# Slack-Notion Integration & Automation Guide

## Overview
Complete guide for connecting Slack to Notion and automating workflows across both platforms.

## Part 1: Basic Setup

### Prerequisites
- Slack workspace with admin access
- Notion workspace
- Zapier or Make account

### Step 1: Connect Slack to Zapier
1. Open Zapier.com
2. Create new Zap
3. Choose Slack as trigger
4. Authorize Slack workspace
5. Select trigger event (message, reaction, etc.)

### Step 2: Connect Notion to Zapier
1. Add Notion as action
2. Authorize Notion workspace
3. Select database to update
4. Map Slack fields to Notion properties

## Part 2: Common Automations

### Automation 1: Save Slack Messages to Notion

**Trigger**: User reacts to message with ✅ emoji

**Actions**:
1. Capture message text
2. Extract sender name
3. Add message timestamp
4. Create Notion page with:
   - Title: Message snippet
   - Author: Sender name
   - Content: Full message
   - Source: Slack
   - Date: Timestamp
   - Status: New

**Use Case**: Save important discussions for later reference

### Automation 2: Create Tasks from Slack

**Trigger**: Message starts with "/task"

**Actions**:
1. Extract task description from message
2. Identify assignee from message mentions
3. Set default priority (Medium)
4. Create Notion task with:
   - Name: Task description
   - Assigned to: Mentioned user
   - Status: To Do
   - Priority: Medium
   - Created in Slack: True
5. Reply to Slack message with task link

**Example**: User types "/task @john Fix login bug"

### Automation 3: Daily Notion Summary in Slack

**Trigger**: Every day at 9 AM

**Actions**:
1. Query Notion for today's tasks
2. Filter by status (not completed)
3. Summarize into bullet points
4. Count by priority
5. Send Slack message with:
   - Good morning greeting
   - "Today's Tasks" header
   - Tasks grouped by priority
   - Total count
   - Motivational message

**Example Message**:
```
Good morning! 🌅

📋 Today's Tasks (5 total)

🔴 URGENT (2)
• Fix production bug
• Client call prep

🟡 HIGH (2)
• Review PR #234
• Update documentation

🟢 MEDIUM (1)
• Organize desk
```

### Automation 4: Project Status Updates

**Trigger**: When project status changes in Notion

**Actions**:
1. Check new status
2. Find project lead in Notion
3. Format update message
4. Send to appropriate Slack channel
5. Include:
   - Project name
   - Status change
   - Completion percentage
   - Next milestone
   - Owner

### Automation 5: Standup Reports

**Trigger**: Every Monday-Friday at 5 PM

**Actions**:
1. Query completed tasks this week
2. Query in-progress tasks
3. Query blocked tasks
4. Format standup message
5. Send to #standup channel
6. Include individual breakdown by team member

### Automation 6: Deadline Reminders

**Trigger**: Task due date is tomorrow (scheduled)

**Actions**:
1. Find assignee's Slack ID
2. Calculate hours until deadline
3. Send direct message with:
   - Task name
   - Due time
   - Priority level
   - Quick link to task
4. Mark reminder sent in Notion

### Automation 7: Idea Capture

**Trigger**: Threaded message in #ideas channel

**Actions**:
1. Extract all thread messages
2. Create Notion page with:
   - Title: First message as title
   - Description: Full thread
   - Reactions: Count emoji reactions
   - Contributors: List thread participants
   - Status: Backlog
3. Reply to thread with Notion link

## Part 3: Advanced Workflows

### Multi-Step Workflow: Bug Reporting

**Step 1: Bug Report Triggered**
- User in #bugs channel uses /bug command
- Slack modal appears with fields:
  - Bug Title
  - Description
  - Severity (Critical/High/Medium/Low)
  - Browser/OS
  - Steps to reproduce

**Step 2: Create Notion Bug Entry**
- Zapier creates new Notion bug record
- Properties:
  - Title: Bug title
  - Description: Full description
  - Severity: Selected level
  - Status: Backlog
  - Reporter: Slack user
  - Created Date: Now
  - Environment: Browser/OS

**Step 3: Assign & Notify**
- If severity Critical: assign to tech lead
- If severity High: assign to available dev
- Send Slack notification to assignee
- Include bug link and priority

**Step 4: Update Status**
- When bug status changes to "Fixed"
- Send notification to #bugs channel
- Include fix details
- Archive bug in Notion

### Multi-Step Workflow: Project Kickoff

**Trigger**: New project created in Notion

**Step 1: Create Slack Channel**
- Use Slack API to create channel
- Format: project-[name]
- Add team members
- Set description to project details

**Step 2: Create Task Breakdown**
- Query project in Notion
- Extract milestones
- Create task for each milestone
- Link to Slack channel

**Step 3: Announcement Message**
- Post to #announcements
- Include:
  - Project name
  - Team members
  - Timeline
  - Key objectives
  - Slack channel link

**Step 4: Schedule Kickoff**
- Create calendar event
- Add team via Slack
- Send calendar invite
- Post reminder in Slack channel

## Part 4: Using Slack Buttons & Forms

### Interactive Button Example

**Use Case**: Approve/Reject Notion items from Slack

**Setup**:
1. When Notion item needs approval
2. Send Slack message with buttons:
   - "✅ Approve" button
   - "❌ Reject" button
3. When clicked:
   - Update Notion item status
   - Reply to user with confirmation
   - Log action with timestamp

### Modal Form Example

**Use Case**: Quick note taking from Slack

**Setup**:
1. User triggers "/note" command
2. Modal form appears with:
   - Note title
   - Note content
   - Category dropdown
   - Tags field
3. On submit:
   - Create Notion note
   - Reply with confirmation
   - Show Notion link

## Part 5: Best Practices

### Do's
1. ✅ Test automations with sample data first
2. ✅ Use conditional logic to avoid errors
3. ✅ Archive old Slack messages periodically
4. ✅ Keep Notion links short and accessible
5. ✅ Use rich formatting in Slack messages
6. ✅ Set up error notifications
7. ✅ Document automation purposes

### Don'ts
1. ❌ Don't send too many Slack notifications (causes alert fatigue)
2. ❌ Don't sync every Notion change to Slack
3. ❌ Don't hardcode values - use variables
4. ❌ Don't forget to test error scenarios
5. ❌ Don't over-complicate workflows

### Rate Limiting
- Limit automations: Max 5-10 per day
- Batch operations: Combine multiple changes
- Delay notifications: 5-15 minute intervals
- Archive messages: Weekly cleanup

## Part 6: Troubleshooting

### Common Issues

**Issue**: Automations not triggering
- Check Slack and Notion permissions
- Verify trigger conditions match exactly
- Test trigger manually
- Check Zapier task history

**Issue**: Missing data in Notion
- Verify Slack field mapping
- Check data type compatibility
- Test with simple message first
- Check for special characters

**Issue**: Slack messages not sending
- Verify channel permissions
- Check message formatting
- Test with direct message first
- Verify bot has channel access

## Part 7: Templates

### Daily Standup Template
```
@channel Good morning! 🌅

Here's today's overview:

📊 Status: [TOTAL TASKS] tasks
✅ Completed yesterday: [COUNT]
⏳ In progress: [COUNT]  
🚧 Blocked: [COUNT]

Top priorities today:
1. [TASK]
2. [TASK]
3. [TASK]

Any blockers? Reply in thread 👇
```

### Project Update Template
```
📈 Project Update: [PROJECT NAME]

Status: [CURRENT STATUS]
Completion: [PERCENTAGE]%
On track? [YES/NO]

Milestones:
✅ [COMPLETED]
🔄 [IN PROGRESS]
⏳ [UPCOMING]

Next steps: [DESCRIPTION]
Any risks? [DESCRIPTION]
```

## Integration Cost Considerations

- **Zapier Free**: Limited automations, 15 min check-in
- **Zapier Paid**: From $20-99/month for unlimited
- **Make**: From €9.99/month with more flexibility
- **Slack Bot**: Can be free if self-hosted

## Security Best Practices

1. Use OAuth for authentication
2. Never hardcode API keys
3. Restrict bot permissions
4. Audit access logs regularly
5. Use encrypted channels for sensitive info
6. Rotate API keys quarterly
7. Monitor failed automation attempts
