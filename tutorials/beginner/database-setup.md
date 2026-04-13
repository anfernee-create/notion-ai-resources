# Database Setup for Notion AI

> **Beginner Tutorial** | Estimated time: 20-30 minutes | Prerequisites: Your First AI Prompt tutorial

## Overview

Notion databases are where AI truly shines. This tutorial covers how to create a database from scratch, add AI-powered properties, and set up your first automation — all without writing a single line of code.

---

## What is a Notion Database?

A Notion database is a structured collection of pages where each row is a page and each column is a property (like a spreadsheet, but much more powerful). Databases can be viewed as tables, boards, calendars, galleries, or timelines.

AI can automatically fill, categorize, and summarize database properties, turning your database into a smart data hub.

---

## Part 1: Create Your First Database

### Step 1: Add a Database to a Page

1. Open a Notion page (or create a new one)
2. Type /database and select "Table - Inline" from the menu
3. A new table appears with a default "Name" column and a "Tags" column

### Step 2: Add Key Properties

Click the + button at the end of the column headers to add properties. For a basic task tracker, add:

- **Status** (Type: Status) — tracks progress: Not Started, In Progress, Done
- **Priority** (Type: Select) — options: High, Medium, Low
- **Due Date** (Type: Date) — when the task is due
- **Notes** (Type: Text) — free-form notes

### Step 3: Add Your First Entries

Add 3-5 sample tasks by clicking "+ New" at the bottom of the table. Fill in the Name and set a Status for each.

---

## Part 2: Add AI Properties

AI properties automatically fill themselves based on the content of your database pages. This is where Notion AI starts to do real work for you.

### Step 1: Add an AI Summary Property

1. Click + to add a new property
2. Select type: "AI custom autofill"
3. Name it "AI Summary"
4. Write the prompt: "Summarize the task notes in 1-2 sentences. If no notes exist, write 'No notes added yet.'"
5. Click Save

Notion AI will now generate a summary for every entry that has notes in the Notes field.

### Step 2: Add an AI Priority Suggestion

Add another AI autofill property:
- Name: "Suggested Priority"
- Prompt: "Based on the task name and due date, suggest a priority level: High, Medium, or Low. Respond with only the priority word."

### Step 3: Trigger the AI

Click on any database entry and open its page. Click the sparkle icon next to your AI property to generate the value, or enable "Auto-fill" so it triggers automatically when the record is created.

---

## Part 3: Set Up Your First Automation

Database automations trigger actions automatically when conditions are met — no manual work needed.

### Step 1: Open Automations

Click the lightning bolt icon at the top right of your database, then click "+ New automation."

### Step 2: Configure the Trigger

Set the trigger to: **"When a property is edited" → Status → changes to → "Done"**

### Step 3: Add an Action

Add an action: **"Edit a property" → Due Date → set to → Today**

This automatically sets the completion date whenever you mark a task as Done.

### Step 4: Add a Second Action

Add another action: **"Send a Slack notification"** (if you have Slack connected) or **"Add a comment"** with the text "Task completed! Great work."

Click Save and test it by changing a task's status to Done.

---

## Part 4: Views — Different Ways to See Your Data

The same database can be viewed in multiple ways. Add views by clicking "+ Add a view" at the top of the database.

**Table view** — Spreadsheet-style, best for seeing all properties at once.

**Board view** — Kanban-style, grouped by Status. Drag cards between columns.

**Calendar view** — Shows tasks on their Due Date. Great for planning.

**Gallery view** — Visual grid, best when tasks have cover images.

Create a Board view grouped by Priority to see your High/Medium/Low tasks at a glance.

---

## Part 5: Filter and Sort

### Filtering

Click "Filter" at the top of the database:
- Filter by Status = "In Progress" to see only active tasks
- Filter by Due Date = "This week" to focus on what's urgent

### Sorting

Click "Sort":
- Sort by Priority (descending) to see High priority tasks first
- Sort by Due Date (ascending) to see what's due soonest

---

## Common Beginner Questions

**Q: How many AI autofill properties can I have?**
A: There is no hard limit, but each AI property counts toward your workspace's AI usage. Start with 2-3 and expand as needed.

**Q: Can AI properties update automatically when I edit a record?**
A: Yes — in the AI property settings, enable "Auto-fill on add" to trigger when new records are created, or "Auto-fill on request" to trigger manually.

**Q: Can I use the same database in multiple pages?**
A: Yes — use /linked database to embed a view of any existing database on a different page. The data stays in sync.

---

## Next Steps

- [Your First AI Prompt](first-ai-prompt.md) - If you haven't already, start here
- [Notion AI Basics](notion-ai-basics.md) - Full overview of all AI features
- [Advanced Prompting](../../tutorials/intermediate/advanced-prompts.md) - Level up your AI property prompts

---

*Last Updated: April 2026 | [Report an issue](https://github.com/anfernee-create/notion-ai-resources/issues)*
