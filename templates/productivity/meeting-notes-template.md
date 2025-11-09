# Meeting Notes Template

A comprehensive Notion template for capturing, organizing, and actioning meeting notes with AI-powered insights.

## Overview

This template helps you systematically document meetings with automatic AI-powered summaries, action item extraction, and follow-up tracking.

## Database Properties

### Meetings Database

| Property | Type | Description | AI Autofill |
|----------|------|-------------|--------------|
| Meeting Title | Title | Name of the meeting | - |
| Date | Date | When the meeting occurred | - |
| Type | Select | Meeting category | Options: Stand-up, Planning, Review, One-on-One, Client, Team |
| Attendees | Multi-select | Who attended | - |
| Status | Select | Meeting status | Options: Scheduled, Completed, Cancelled |
| Duration | Number | Length in minutes | - |
| Summary | AI Property | Auto-generated summary | "Summarize the key points and decisions from this meeting in 2-3 sentences" |
| Action Items | AI Property | Extracted tasks | "Extract all action items and tasks mentioned in these notes as a bullet list" |
| Key Decisions | AI Property | Important decisions | "List the key decisions made during this meeting" |
| Follow-up Required | Checkbox | Needs follow-up | - |
| Next Meeting | Date | Scheduled follow-up | - |

## Template Structure

### Meeting Header
```
📅 Date: [Date]
🕐 Time: [Start] - [End]
👥 Attendees: [Names]
📍 Location/Link: [Physical location or video call link]
```

### Meeting Sections

#### 1. Agenda
- Pre-meeting topics to discuss
- Expected outcomes
- Time allocations

#### 2. Discussion Notes
- Main points discussed
- Questions raised
- Answers provided

#### 3. AI-Generated Summary
- *Notion AI will auto-generate a concise summary*
- Key highlights
- Important context

#### 4. Action Items
- *Notion AI will extract tasks automatically*
- Assigned to
- Due dates
- Priority levels

#### 5. Decisions Made
- *AI-identified key decisions*
- Context for each decision
- Impact analysis

#### 6. Next Steps
- Follow-up required
- Next meeting date
- Preparation needed

## AI Prompts

### Summary Generation
```
Summarize these meeting notes in 3-4 sentences, focusing on:
- Main discussion topics
- Key decisions made
- Important outcomes
```

### Action Items Extraction
```
Extract all action items from these notes and format as:
- [ ] Task description (Assigned to: Name, Due: Date)
```

### Decision Documentation
```
Identify and list all decisions made during this meeting with:
1. Decision made
2. Rationale
3. Impact
```

### Follow-up Email
```
Draft a follow-up email summarizing:
- Meeting attendees
- Key discussion points
- Action items with assignments
- Next meeting details
```

## Setup Instructions

### 1. Create the Database
1. Create a new database in Notion
2. Add all properties listed above
3. Configure AI autofill properties

### 2. Configure AI Properties

**Summary Property:**
- Type: AI-powered
- Prompt: "Summarize the key points and decisions from this meeting in 2-3 sentences"

**Action Items Property:**
- Type: AI-powered  
- Prompt: "Extract all action items and tasks mentioned in these notes as a detailed bullet list with assignments"

**Key Decisions Property:**
- Type: AI-powered
- Prompt: "List the key decisions made during this meeting with context"

### 3. Create Meeting Template
1. Create a new page in your database
2. Add the template structure
3. Save as a template

## Usage Guide

### Before the Meeting
1. Create a new meeting entry
2. Fill in: Date, Type, Attendees
3. Add agenda items
4. Share with attendees

### During the Meeting
1. Take notes in Discussion Notes section
2. Capture decisions as they're made
3. Note any action items
4. Record important questions

### After the Meeting
1. Let AI generate summary
2. Review extracted action items
3. Verify key decisions
4. Assign follow-up tasks
5. Schedule next meeting if needed

## AI Automation Examples

### Auto-Create Tasks
Use Notion AI to automatically create task pages from action items:
```
For each action item:
1. Create a new task in Tasks database
2. Link to this meeting
3. Assign to person mentioned
4. Set due date from context
```

### Meeting Insights
```
Analyze patterns across meetings:
- Common topics discussed
- Action item completion rate
- Average meeting duration
- Attendee participation
```

### Smart Reminders
```
Generate reminder for:
- Incomplete action items
- Upcoming follow-up meetings
- Overdue tasks from this meeting
```

## Best Practices

### 1. Consistent Format
- Use the same structure for all meetings
- Maintain clear section headers
- Keep notes concise and actionable

### 2. Real-time Documentation
- Take notes during the meeting
- Don't rely on memory afterward
- Use bullet points for clarity

### 3. AI Enhancement
- Review AI-generated summaries for accuracy
- Refine action items before assigning
- Use AI to draft follow-up communications

### 4. Follow-through
- Review action items within 24 hours
- Send meeting summary to attendees
- Track completion of tasks
- Schedule follow-ups promptly

### 5. Regular Review
- Weekly review of open action items
- Monthly analysis of meeting effectiveness
- Quarterly optimization of template

## Integration Ideas

### Link to Other Databases
- **Projects**: Connect meetings to relevant projects
- **Tasks**: Auto-create tasks from action items
- **People**: Track who attends which meetings
- **Documents**: Link to related materials

### Connect with Tools
- **Calendar**: Sync with Google Calendar
- **Slack**: Send summaries to channels
- **Email**: Auto-send follow-ups
- **Zoom**: Embed recordings

## Examples

### Stand-up Meeting
```
# Daily Stand-up - Nov 9, 2025

## Updates
- Alice: Completed user authentication
- Bob: Working on database optimization
- Carol: Starting UI redesign

## Blockers
- Need API keys for payment integration

## Action Items
- [ ] Alice: Provide API documentation (Due: Today)
- [ ] Bob: Review database indexes (Due: Tomorrow)
```

### Client Meeting
```
# Q4 Strategy Review - Client XYZ

## Discussion
- Reviewed Q3 results: 25% growth
- Discussed Q4 campaign strategy
- Budget allocation for new initiatives

## Decisions
1. Increase social media budget by 30%
2. Launch email campaign in December
3. Focus on customer retention

## Next Steps
- Proposal draft by Friday
- Follow-up call next Tuesday
```

## Troubleshooting

### AI Summary Issues
- **Problem**: Summary too generic
- **Solution**: Add more detailed notes with specific data

### Missing Action Items  
- **Problem**: AI doesn't catch all tasks
- **Solution**: Use clear action words ("will", "should", "must")

### Incomplete Data
- **Problem**: Properties not filling automatically
- **Solution**: Check AI property configuration and refresh

## Advanced Features

### Meeting Analytics
Create a dashboard view showing:
- Meetings per week/month
- Average duration
- Action item completion rate
- Most frequent topics

### Template Variations
- One-on-One meetings
- Brainstorming sessions
- Sprint planning
- Retrospectives
- Board meetings

### Custom AI Prompts
Tailor AI prompts for specific meeting types:
- Technical discussions
- Sales calls
- Strategic planning
- Team updates

## Related Templates

- [AI Task Manager](ai-task-manager.md)
- [Project Roadmap](project-roadmap.md)
- [Team Collaboration Hub](../../docs/best-practices/team-collaboration.md)

---

**Last Updated**: November 2025  
**Version**: 1.0  
**Compatibility**: Notion with AI features
