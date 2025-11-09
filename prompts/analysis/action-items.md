# Action Items Extraction Prompts

## Overview

These AI prompts help you automatically identify, extract, and organize action items from meetings, emails, documents, and conversations. Use them to ensure follow-up tasks are never missed and responsibilities are clearly defined.

## Meeting Action Items

### Basic Action Item Extraction

**Prompt**: "Analyze the following meeting notes and extract all action items. For each action item, provide:
- Clear description of the task
- Person responsible (if mentioned)
- Deadline or timeframe (if mentioned)
- Priority level (if indicated)

[MEETING NOTES]

Present the action items in a clear, structured format."

### Detailed Action Item Analysis

**Prompt**: "Review this meeting transcript and create a comprehensive action items list. Include:

1. **Action Items**: What needs to be done
2. **Owner**: Who is responsible
3. **Deadline**: When it's due
4. **Context**: Why it's important
5. **Dependencies**: What needs to happen first
6. **Status**: Not started / In progress / Blocked

[TRANSCRIPT]

Organize by priority and flag any items with unclear ownership."

### Project Action Items

**Prompt**: "Extract actionable next steps from this project discussion. Identify:
- Immediate action items (this week)
- Short-term action items (this month)
- Long-term action items (this quarter)
- Decisions that need to be made
- Information that needs to be gathered

[PROJECT DISCUSSION]

Highlight any blockers or dependencies."

## Email Action Items

### Email Thread Analysis

**Prompt**: "Read through this email thread and identify all action items, commitments, and follow-ups needed. For each:
- What is the action?
- Who committed to it?
- When is it due?
- What's the context?

[EMAIL THREAD]

Present as a task list with clear ownership."

### Multi-stakeholder Emails

**Prompt**: "This email involves multiple people and projects. Extract action items and organize them by person:

[EMAIL CONTENT]

For each person, list:
- Their action items
- Priority level
- Dependencies on others
- Suggested deadlines"

## Document Action Items

### Document Review

**Prompt**: "Analyze this document and identify all implied and explicit action items. Include:
- Tasks mentioned directly
- Implied next steps
- Open questions that require action
- Decisions that need to be made
- Research or information gathering needed

[DOCUMENT]

Organize by urgency and complexity."

### Report Follow-ups

**Prompt**: "Based on this report/analysis, what are the recommended action items? Identify:
- Critical actions based on findings
- Recommended next steps
- Suggested responsible parties
- Proposed timelines
- Success metrics

[REPORT]

Prioritize based on impact and feasibility."

## Task Organization

### Priority Classification

**Prompt**: "Take these action items and classify them using the Eisenhower Matrix:

[ACTION ITEMS LIST]

**Urgent & Important** (Do First)
**Important but Not Urgent** (Schedule)
**Urgent but Not Important** (Delegate)
**Neither Urgent nor Important** (Eliminate)

Provide reasoning for each classification."

### Sprint Planning

**Prompt**: "Convert these action items into a sprint plan:

[ACTION ITEMS]

Organize them into:
- Sprint goals
- User stories or tasks
- Story points or time estimates
- Dependencies
- Success criteria

Suggest how to distribute across team members."

## Follow-up Prompts

### Status Tracking

**Prompt**: "Create a follow-up email template for tracking these action items:

[ACTION ITEMS]

Include:
- Friendly reminder of commitments
- Request for status updates
- Offer of support
- Clear deadlines
- Professional but approachable tone"

### Accountability Check

**Prompt**: "Compare these action items from [DATE] with this update:

**Original Action Items:**
[ORIGINAL LIST]

**Current Update:**
[UPDATE]

Identify:
- Completed items
- In-progress items
- Overdue items
- Blocked items
- Items not mentioned (potentially forgotten)

Provide a clear status summary."

## Best Practices

1. **Be specific** - Extract clear, actionable tasks, not vague intentions
2. **Identify owners** - Always try to determine who is responsible
3. **Set deadlines** - Infer reasonable timelines if not explicitly stated
4. **Flag ambiguity** - Note when ownership or requirements are unclear
5. **Prioritize** - Not all action items are equally important
6. **Context matters** - Include enough background for understanding
7. **Track dependencies** - Note what needs to happen before each task
8. **Regular review** - Use these prompts consistently to build accountability

## Output Formats

### Task List Format
```
☐ [Action Item]
  👤 Owner: [Name]
  📅 Due: [Date]
  🎯 Priority: [High/Medium/Low]
  📝 Context: [Brief description]
```

### Table Format
| Task | Owner | Due Date | Priority | Status | Notes |
|------|-------|----------|----------|--------|-------|
| ... | ... | ... | ... | ... | ... |

### Notion Database Format
- Task (Title)
- Owner (Person)
- Due Date (Date)
- Priority (Select)
- Status (Select)
- Project (Relation)
- Context (Text)

## Related Prompts

- **summarization.md** - For creating meeting summaries
- **key-insights.md** - For extracting important insights
- **editing-prompts.md** - For refining task descriptions

## Version Information

**Last Updated**: 2024
**Version**: 1.0
**Status**: Active
