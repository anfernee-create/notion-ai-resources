# Property Cascading

Automatically propagate property changes across related database entries in Notion — keeping your project hierarchy in sync without manual updates.

## Overview

Property cascading uses Notion's relations and rollups combined with automations to push changes from parent records down to child records (or bubble them up). This is essential for large project hierarchies where status, priority, or date changes need to ripple through the system.

## Common Cascading Patterns

### Top-Down Cascades
- **Project → Tasks**: When a project is marked "Cancelled", all tasks should be updated
- **Epic → Stories**: Priority changes flow from epic to all user stories
- **Client → Projects**: Client status (active/paused) cascades to all client projects

### Bottom-Up Rollups
- **Tasks → Project**: When all tasks are "Done", project auto-completes
- **Subtasks → Task**: Completion percentage bubbles up to parent task

## Setup

### 1. Configure Relations

In your task database:
1. Add a **Project** relation property
2. Enable the reverse relation in the Project database
3. Set up a **Rollup** in Project: "Count tasks where Status = Done"

### 2. Create Cascade Automations

**When project is cancelled → cancel all tasks:**
1. Automation trigger: "When Project.Status changes to Cancelled"
2. Action: "Edit related tasks" → Set Status = Cancelled

**When all tasks complete → complete project:**
1. Trigger: "When Rollup(Done Tasks) = Rollup(Total Tasks)"
2. Action: Edit Project Status → "Completed"

### 3. AI-Assisted Cascade Decisions

Add an AI property to flag cascade candidates:
- **AI Impact Analysis**: "List the tasks that should be updated if this project priority changes"

## Advanced: Multi-Level Cascading

For deep hierarchies (Portfolio → Program → Project → Task):

```
Portfolio.Status = "On Hold"
  ↓ cascade
Program.Status = "On Hold"
  ↓ cascade
Project.Status = "On Hold"
  ↓ cascade
Task.Status = "Blocked"
```

Use sequential automations at each level to achieve this.

## Best Practices

- Test cascades on non-production data first
- Build in manual override options — not every cascade should be automatic
- Log cascade events for audit trails
- Avoid circular cascade references

## Related

- [Auto-Assign Tasks](auto-assign-tasks.md)
- [Status Updates](status-updates.md)

---

*Last Updated: April 2026*
