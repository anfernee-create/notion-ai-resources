# Freelancer Project Management System in Notion

## Overview
A complete Notion workspace for freelancers to manage projects, clients, invoices, and finances using AI-powered automation.

## Core Databases

### 1. Clients Database
Manages client information and history

**Properties**:
- Name (Title)
- Company (Text)
- Email (Email)
- Phone (Phone)
- Rate (Currency)
- Status (Select: Active, Inactive, Blocked)
- Total Revenue (Rollup - Sum)
- Projects Count (Rollup - Count)
- Last Contact (Date)
- Notes (Text)

### 2. Projects Database
Track all projects and their status

**Properties**:
- Name (Title)
- Client (Relation to Clients)
- Status (Select: Proposal, Accepted, In Progress, Completed, Cancelled)
- Budget (Number)
- Start Date (Date)
- End Date (Date)
- Completion % (Formula)
- Rate (Rollup from Client)
- Total Tasks (Rollup - Count from Tasks)
- Tasks Completed (Rollup with Filter)
- Revenue (Formula: Rate × Hours)
- Priority (Select: Low, Medium, High, Urgent)

### 3. Tasks Database
Detailed task management for projects

**Properties**:
- Name (Title)
- Project (Relation to Projects)
- Status (Select: Backlog, To Do, In Progress, Review, Done)
- Hours Estimated (Number)
- Hours Actual (Number)
- Priority (Select)
- Due Date (Date)
- Assigned To (Person)
- Notes (Text)
- Completed (Checkbox)

### 4. Invoices Database
Invoice tracking and payment status

**Properties**:
- Invoice Number (Text - auto-generated)
- Project (Relation to Projects)
- Client (Relation to Clients)
- Amount (Currency)
- Date Issued (Date)
- Due Date (Date)
- Date Paid (Date)
- Status (Select: Draft, Sent, Overdue, Paid, Cancelled)
- Payment Method (Select)
- Notes (Text)

### 5. Time Tracking Database
Hourly time entries

**Properties**:
- Date (Date)
- Task (Relation to Tasks)
- Project (Relation to Projects)
- Hours (Number)
- Notes (Text)
- Billable (Checkbox)
- Rate (Currency)
- Amount (Formula: Hours × Rate)

## Advanced Formulas

### Project Completion Formula
```
let completed = rollup(
  relation("Tasks"),
  "if(prop(\"Status\") == \"Done\", 1, 0)",
  "sum"
);
let total = rollup(relation("Tasks"), "1", "count");
if(total == 0, 0, round(completed / total * 100))
```

### Revenue Calculation
```
let hours = rollup(
  relation("Tasks"),
  "prop(\"Hours Actual\")",
  "sum"
);
hours * prop("Rate")
```

### Invoice Status Color
```
switch(prop("Status"))
  case "Paid": "✅ Paid"
  case "Overdue": "⚠️ Overdue"
  case "Sent": "📧 Sent"
  case "Draft": "📝 Draft"
  default: prop("Status")
```

## Dashboard Views

### Active Projects
- Filter: Status != "Completed" && Status != "Cancelled"
- Sort: End Date ascending
- Timeline view to see Gantt

### Income Dashboard
- Monthly revenue rollup
- Invoice status breakdown
- Outstanding balance calculation

### Time Tracking
- Weekly hours logged
- Billable vs non-billable
- Time per project

## Automation Setup

### Invoice Generation
1. When project status → "Completed"
2. Create invoice with project details
3. Set due date to 30 days out
4. Send email notification

### Payment Reminders
1. When invoice status → "Sent"
2. Set reminder for due date
3. If unpaid after due date → mark "Overdue"
4. Send reminder email

### Project Milestone Alerts
1. When task completion ≥ 50%
2. Send update notification
3. When task completion = 100%
4. Mark project complete if all tasks done

## Financial Tracking

### Monthly Revenue Report
- Total billable hours
- Average hourly rate
- Revenue by client
- Outstanding invoices
- Cash flow forecast

### Tax Deduction Tracker
- Expense categories
- Equipment purchases
- Software subscriptions
- Professional development
- Home office deduction

## Integrations

### Stripe Payment Integration
- Auto-update invoice status when paid
- Track payment processing fees
- Reconcile transactions

### Calendar Sync
- Sync project deadlines to calendar
- Show task due dates
- Block time for projects

### Email Integration
- Send project updates
- Invoice reminders
- Payment notifications

## Best Practices

### Rate Management
1. Track rates by client
2. Implement rate increases
3. Offer bulk discounts for long projects
4. Create tiered pricing structure

### Project Scoping
1. Always estimate hours
2. Build in buffer time (20%)
3. Track scope creep
4. Create change order process

### Financial Health
1. Invoice within 24 hours of completion
2. Set payment terms clearly
3. Follow up on overdue invoices
4. Maintain 3-month expense buffer

## Custom AI Prompts

### Project Health Assessment
Analyze: completion %, hours tracking, budget vs actual, timeline status

### Revenue Optimization
Identify: high-margin clients, underpriced services, capacity utilization

### Proposal Generator
Create: scope, timeline, pricing, terms for new projects

## Templates

### Project Proposal Template
- Overview
- Scope of work
- Timeline
- Pricing
- Terms and conditions
- Payment schedule

### Invoice Template
- Invoice number
- Date issued/due
- Client details
- Project description
- Itemized breakdown
- Total amount due
- Payment instructions

## Metrics to Track

1. **Utilization Rate**: Billable hours / Total hours
2. **Average Project Value**: Total revenue / Project count
3. **Invoice Aging**: Days outstanding on invoices
4. **Profit Margin**: (Revenue - Expenses) / Revenue
5. **Client Retention**: Repeat clients / Total clients
6. **Project Profitability**: Revenue / Hours spent

## Growth Optimization

### Identify High-Value Work
- Projects with highest profit margins
- Fastest-completing projects
- Most satisfied clients
- Repeatable scope patterns

### Scale Pricing
- Increase rates for popular services
- Create package deals
- Offer retainer agreements
- Premium rush fees

### Manage Capacity
- Track available hours per month
- Buffer for admin tasks (20%)
- Set project limits
- Create waitlist for overflow
