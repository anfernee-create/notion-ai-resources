# Project Roadmap Template

A comprehensive Notion template for planning, tracking, and visualizing project timelines, milestones, dependencies, and deliverables with team collaboration and progress monitoring.

## Overview

This template helps teams:
- Define project vision and objectives
- Break projects into phases and milestones
- Track dependencies between tasks
- Monitor progress against timelines
- Identify and manage risks
- Coordinate team efforts
- Communicate status to stakeholders

## Database Properties

### Milestones Database

| Property | Type | Description | AI Autofill |
|----------|------|-------------|-------------|
| Milestone | Title | Key project milestone | – |
| Start Date | Date | When milestone begins | – |
| Target Date | Date | Expected completion | – |
| Phase | Select | Planning, Development, Testing, Launch, Post-Launch | ✓ |
| Completion % | Number | Progress percentage | – |
| Status | Select | Not Started, In Progress, Completed, Delayed, At Risk | – |
| Dependencies | Relation | Related milestones | – |
| Owner | Person | Responsible person | – |
| Description | Text | Details about milestone | ✓ |
| Key Deliverables | Multi-select | Associated deliverables | – |
| Risks | Relation | Associated risks | – |
| Notes | Text | Additional notes | – |

### Tasks Database

| Property | Type | Description | AI Autofill |
|----------|------|-------------|-------------|
| Task | Title | Task description | – |
| Milestone | Relation | Associated milestone | – |
| Assignee | Person | Team member | – |
| Start Date | Date | Start date | – |
| Due Date | Date | Due date | – |
| Estimated Hours | Number | Time estimate | – |
| Actual Hours | Number | Time logged | – |
| Priority | Select | Critical, High, Medium, Low | ✓ |
| Status | Select | To Do, In Progress, Done, Blocked | – |
| Dependencies | Relation | Dependent tasks | – |
| Subtasks | Relation | Child tasks | – |
| Progress % | Number | Completion percentage | – |

## Setup Instructions

### Step 1: Create Databases
1. Create Milestones database
2. Create Tasks database
3. Create Risks database
4. Create Deliverables database

### Step 2: Configure Relations
1. Link Milestones to Tasks
2. Link Tasks to Deliverables
3. Link Milestones to Risks
4. Configure task dependencies

### Step 3: Set Up Views
1. Create Timeline view for Gantt visualization
2. Create By Phase view
3. Create By Assignee view
4. Create Critical Path view
5. Create Burndown chart view

### Step 4: Add Automations
1. Calculate milestone progress from tasks
2. Send due date reminders
3. Update status based on task completion
4. Generate weekly progress reports

## Usage Guide

### Defining Project Scope
1. Write project vision statement
2. Define success criteria
3. Identify key phases
4. List major milestones
5. Determine timeline

### Planning Phase
1. Break milestones into tasks
2. Assign resources and owners
3. Identify task dependencies
4. Estimate effort required
5. Set realistic deadlines

### Execution Phase
1. Update task status daily
2. Log actual hours worked
3. Document progress notes
4. Flag blockers immediately
5. Communicate with team

### Monitoring Phase
1. Review milestone progress weekly
2. Check critical path status
3. Assess risk register
4. Update stakeholder reports
5. Adjust timeline if needed

## Best Practices

1. **Define Clear Milestones**: Each should represent meaningful progress
2. **Realistic Estimates**: Add 20-30% buffer for unknowns
3. **Regular Updates**: Keep status current (minimum daily)
4. **Risk Management**: Identify risks early and plan mitigations
5. **Communication**: Share updates with stakeholders regularly
6. **Flexibility**: Plan for changes and adjustments
7. **Documentation**: Record decisions and reasons
8. **Progress Tracking**: Monitor against baseline regularly
9. **Dependency Management**: Map and monitor task dependencies
10. **Resource Planning**: Ensure adequate capacity allocation

## AI Automation Examples

### Smart Timeline Adjustment
Prompt: Based on current progress and remaining work, will we meet the target date?

### Risk Identification
Prompt: Analyze task dependencies and identify potential critical path risks.

### Resource Allocation
Prompt: Recommend resource allocation based on skillsets and capacity.

### Progress Forecasting
Prompt: Given current velocity, predict actual completion date.

## Integration Ideas

### Calendar Integration
Export milestones to team calendar for visibility

### Slack Integration
Post daily standup summaries and alerts

## Examples

### Typical Project Phases
- Planning: 2-4 weeks (requirements, design)
- Development: 6-12 weeks (implementation)
- Testing: 2-4 weeks (QA, UAT)
- Launch: 1-2 weeks (deployment)
- Post-Launch: 2-4 weeks (monitoring, fixes)

### Critical Path Tracking
Identify longest sequence of dependent tasks to focus team on impactful work.

## Troubleshooting

**Problem**: Consistently missing dates
**Solution**: Review estimation accuracy and add buffers

**Problem**: Unclear task dependencies
**Solution**: Create explicit dependency map early

**Problem**: Scope creep affecting timeline
**Solution**: Implement change control process

## Advanced Features

### Burndown Charts
Track remaining work against ideal pace

### Velocity Tracking
Monitor team speed improvements

### Scenario Planning
Model different timeline scenarios

## Related Templates

- [AI Task Manager](ai-task-manager.md)
- [Meeting Notes](meeting-notes-template.md)
- [Daily Planner ADHD](daily-planner-adhd.md)

---

**Last Updated**: November 2025
**Version**: 1.0
**Compatibility**: Notion with AI features
