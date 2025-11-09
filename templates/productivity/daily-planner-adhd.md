# ADHD-Friendly Daily Planner

A comprehensive Notion template designed specifically for individuals with ADHD, featuring time-blocking, task prioritization, and built-in breaks and rewards to maintain focus and motivation throughout the day.

## Overview

This template addresses the unique challenges faced by people with ADHD, including:
- Executive function challenges
- Time blindness and poor time estimation
- Task initiation difficulties
- Hyperfocus management
- Working memory limitations

Features include time-blocking, priority matrices, energy level tracking, break reminders, and reward tracking to support sustainable productivity.

## Database Properties

### Main Tasks Database

| Property | Type | Description | AI Autofill |
|----------|------|-------------|-------------|
| Task | Title | Task description | – |
| Date | Date | When the task is scheduled | – |
| Time Block | Text | Scheduled time (e.g., 9:00-9:30) | – |
| Duration (min) | Number | Estimated time needed | – |
| Energy Level Required | Select | Low, Medium, High | ✓ |
| Priority | Select | High, Medium, Low | ✓ |
| Category | Multi-select | Work, Personal, Health, etc. | ✓ |
| Status | Select | Not Started, In Progress, Done, Blocked | – |
| Actual Time Taken | Number | Actual duration completed | – |
| Break Before | Checkbox | Needs break beforehand | – |
| Break After | Checkbox | Needs break afterward | – |
| Distraction Risk | Select | Low, Medium, High | ✓ |
| Environment Setup | Text | Setup needed (quiet space, etc.) | – |
| Reward Type | Select | Small, Medium, Large | – |
| Notes | Text | Additional context | – |

## Setup Instructions

### Step 1: Create the Database
1. Create a new database in Notion
2. Add all properties listed above
3. Configure select options for priorities and status

### Step 2: Set Up Views
1. Create Today view filtered for today's date
2. Create By Energy Level sorted view
3. Create By Time Block sorted view
4. Create Blocked Tasks filtered view
5. Create Weekly Overview calendar view

### Step 3: Configure Automations
1. At 8:00 AM daily: Send notification reminding to fill energy level
2. Every 2 hours: Send break reminder notification
3. When task status changes to Done: Log completion time
4. At end of day: Send summary of completed tasks

## Usage Guide

### Morning Setup
1. Open today's view
2. Set your current energy level (1-5)
3. Review scheduled tasks
4. Identify potential blockers
5. Set one realistic daily goal

### During the Day
1. Follow the time blocks as guides (not strict rules)
2. Update energy level if it changes
3. Mark tasks as In Progress when starting
4. Take breaks at suggested times
5. If hyperfocusing: Set a timer to ensure you don't miss next task

### End of Day Review
1. Mark all completed tasks as Done
2. Log actual time taken vs. estimated
3. Note any patterns
4. Move unfinished tasks to tomorrow
5. Celebrate completed tasks with reward

## Best Practices

1. **Realistic Time Blocking**: Add 25-50% buffer to estimates
2. **Frequent Breaks**: Schedule breaks every 25-50 minutes
3. **Energy-First Planning**: Prioritize high-energy tasks during peak windows
4. **Visual Progress**: Use a daily completion tracker
5. **Flexibility**: Include buffer tasks and overflow time
6. **Movement Breaks**: Include movement to help with restlessness
7. **Reward Logging**: Track small wins
8. **Weekly Review**: Adjust next week based on patterns
9. **Batch Similar Tasks**: Reduce context switching
10. **Emergency Protocol**: Have a fallback for low-energy days

## AI Automation Examples

### Energy-Based Task Suggestion
Prompt: Based on my current energy level and remaining tasks, what should I work on next?

### Break Recommendation
Prompt: What type of break would help my ADHD brain reset?

### Time Estimation Feedback
Prompt: Analyze my pattern of estimated vs. actual time and suggest better estimates.

### Task Prioritization
Prompt: What order should I do these tasks to maintain momentum?

## Integration Ideas

### Calendar Integration
Sync time blocks with your calendar to prevent double-booking

### Slack Integration
Get break reminders and task summaries for accountability

## Examples

### High Energy Day Schedule
- Morning (6:00-9:00): Complex tasks during peak energy
- Midday (12:00-1:00): Lunch and reset
- Afternoon (1:00-5:00): Mixed tasks with energy matching

### Low Energy Day Protocol
- Postpone complex projects
- Focus on simple tasks
- Keep 1-2 easy wins for motivation
- Add extra breaks and movement

## Troubleshooting

**Problem**: Constantly missing estimated times
**Solution**: Multiply estimates by 1.5x and track for calibration

**Problem**: Can't decide what to work on
**Solution**: Use By Energy Level view to match tasks to capacity

**Problem**: Hyperfocus causing schedule disruption
**Solution**: Set phone alarms for transition times

## Advanced Features

### Hyperfocus Harness
Create special Flow State task slots when hyperfocus emerges

### Energy Prediction
Track daily energy to identify patterns

### Distraction Environment
Note environment needs (quiet, social, outdoor) for planning

## Related Templates

- [AI Task Manager](ai-task-manager.md)
- [Meeting Notes](meeting-notes-template.md)
- [Project Roadmap](project-roadmap.md)

---

**Last Updated**: November 2025
**Version**: 1.0
**Compatibility**: Notion with AI features
