# Notion 3.0 AI Agents

An introduction to Notion's AI Agent capabilities introduced with Notion 3.0 — autonomous workflows that take action across your workspace.

## What Are Notion AI Agents?

Notion AI Agents are autonomous AI-powered workflows that can:
- **Read** content from your Notion databases and pages
- **Reason** about what actions to take based on instructions
- **Write** new content, update properties, and create pages
- **Connect** to external sources via Notion's AI Connectors

Unlike static AI properties that run once per trigger, agents can take multi-step actions — similar to having a digital assistant that works in your workspace.

## Core Agent Capabilities

### Read Operations
- Query databases with filters
- Read page content and properties
- Access connected sources (Slack, Drive, GitHub)

### Write Operations
- Create new database entries
- Update existing properties
- Generate page content
- Add comments and annotations

### Decision Making
- Evaluate conditions before acting
- Choose between multiple action paths
- Ask for clarification when instructions are ambiguous

## Getting Started

### 1. Access Notion AI Agents

Available on Business and Enterprise plans:
1. Open a database or page
2. Click **Automations** → **AI Agent**
3. Describe what you want the agent to do in natural language

### 2. Your First Agent

A simple example — a "New Task Briefing" agent:
> "When a new task is created in this database: 
> 1. Read the task title and description
> 2. Look up the assigned person's current workload (other tasks assigned to them)
> 3. Write a brief summary including: task complexity estimate, recommended timeline, and 3 key steps to complete it"

### 3. Agent Triggers

Agents can be triggered by:
- **Database changes** — when a record is created, updated, or deleted
- **Scheduled runs** — daily, weekly, or custom schedule
- **Manual trigger** — button click or slash command
- **External events** — via connected integrations

## Example Agents

### Content Brief Generator
When a new content item is added to your content calendar, automatically generate a detailed brief including target audience, key messages, SEO keywords, and competitor examples.

### Project Risk Monitor
Daily agent that reviews all active projects, identifies any with overdue tasks or missed milestones, and creates a risk report with recommended actions.

### Customer Feedback Categorizer
When new feedback is added, categorize it by type (bug, feature request, complaint, praise), assign to the right team, and update the feedback tracking dashboard.

## Limitations (as of 2026)

- Agents cannot access external URLs or browse the internet
- Complex multi-agent workflows require careful orchestration
- Agent runs consume AI credits (varies by plan)
- Real-time triggers have latency (typically 1-5 minutes)

## Related

- [Multi-Step Workflows](multi-step-workflows.md)
- [Scheduled Agents](scheduled-agents.md)

---

*Last Updated: April 2026*
