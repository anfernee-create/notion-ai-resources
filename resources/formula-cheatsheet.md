# Notion Formula Cheatsheet

A collection of 5 essential Notion formulas to boost your productivity and automate common tasks. Perfect for solopreneurs looking to work smarter, not harder.

---

## Table of Contents
1. [Auto-Calculate Project Progress](#1-auto-calculate-project-progress)
2. [Days Until Deadline Tracker](#2-days-until-deadline-tracker)
3. [Smart Task Priority Score](#3-smart-task-priority-score)
4. [Automatic Time Tracking](#4-automatic-time-tracking)
5. [Revenue Per Day Calculator](#5-revenue-per-day-calculator)

---

## 1. Auto-Calculate Project Progress

**Use Case**: Automatically calculate what percentage of your project tasks are complete.

**Setup Required**:
- A project database with a "Status" property (Select: Not Started, In Progress, Done)
- A "Progress" property (Formula)

**Formula**:
```
if(prop("Status") == "Done", "✅ 100%", 
  if(prop("Status") == "In Progress", "🔄 50%", 
    "⚪ 0%"
  )
)
```

**What it does**:
- Shows ✅ 100% when status is "Done"
- Shows 🔄 50% when status is "In Progress"
- Shows ⚪ 0% when status is "Not Started"

**Pro Tip**: For a more advanced version with subtasks, use a rollup to count completed subtasks divided by total subtasks!

### Advanced Version (Numeric Output):

If you need actual numbers instead of text (for calculations or progress bars):

```
if(prop("Status") == "Done", 100, 
  if(prop("Status") == "In Progress", 50, 0)
)
```

Then format the number property to show as a percentage.

---

## 2. Days Until Deadline Tracker

**Use Case**: Show how many days remain until a task deadline, with visual indicators for urgency.

**Setup Required**:
- A "Due Date" property (Date)
- A "Days Remaining" property (Formula)

**Formula**:
```
if(empty(prop("Due Date")), "No deadline",
  if(dateBetween(prop("Due Date"), now(), "days") < 0, 
    "⚠️ Overdue by " + format(abs(dateBetween(prop("Due Date"), now(), "days"))) + " days",
    if(dateBetween(prop("Due Date"), now(), "days") == 0,
      "🔥 Due TODAY",
      if(dateBetween(prop("Due Date"), now(), "days") <= 3,
        "⚡ " + format(dateBetween(prop("Due Date"), now(), "days")) + " days left",
        "📅 " + format(dateBetween(prop("Due Date"), now(), "days")) + " days left"
      )
    )
  )
)
```

**What it does**:
- Shows "⚠️ Overdue by X days" if past due date
- Shows "🔥 Due TODAY" if due today
- Shows "⚡ X days left" if due within 3 days (urgent)
- Shows "📅 X days left" for other future dates
- Shows "No deadline" if no date is set

**Use Cases**:
- Task management
- Project deadlines
- Client deliverables
- Content publication schedules

---

## 3. Smart Task Priority Score

**Use Case**: Automatically calculate task priority based on multiple factors (urgency, importance, effort).

**Setup Required**:
- "Due Date" property (Date)
- "Importance" property (Select: High, Medium, Low)
- "Effort" property (Select: High, Medium, Low)
- "Priority Score" property (Formula)

**Formula**:
```
round(
  (if(prop("Importance") == "High", 10, 
      if(prop("Importance") == "Medium", 5, 2)) +
   if(dateBetween(prop("Due Date"), now(), "days") <= 7, 10,
      if(dateBetween(prop("Due Date"), now(), "days") <= 14, 5, 2)) +
   if(prop("Effort") == "Low", 5,
      if(prop("Effort") == "Medium", 3, 1))
  ) / 3
)
```

**Scoring System**:
- **Importance**: High (10), Medium (5), Low (2)
- **Urgency**: Due within 7 days (10), 14 days (5), or more (2)
- **Effort**: Low effort (5), Medium (3), High (1) - quick wins get higher scores!
- **Final Score**: Average of all three factors (1-10)

**How to Use**:
1. Sort your task database by Priority Score (descending)
2. Focus on tasks with scores of 8-10 first
3. Quick wins (high importance + low effort) will rise to the top

**Result Interpretation**:
- **9-10**: Critical - Do immediately
- **7-8**: High priority - Schedule this week
- **5-6**: Medium priority - Schedule this month
- **1-4**: Low priority - Backlog or delegate

---

## 4. Automatic Time Tracking

**Use Case**: Track how long a task has been "In Progress" or calculate total time spent on a project.

**Setup Required**:
- "Status" property (Select: Not Started, In Progress, Done)
- "Start Date" property (Date)
- "End Date" property (Date)
- "Time Spent" property (Formula)

**Formula**:
```
if(prop("Status") == "Done" and not empty(prop("End Date")), 
  format(dateBetween(prop("End Date"), prop("Start Date"), "days")) + " days",
  if(prop("Status") == "In Progress" and not empty(prop("Start Date")),
    format(dateBetween(now(), prop("Start Date"), "days")) + " days (ongoing)",
    "Not started"
  )
)
```

**What it does**:
- For completed tasks: Shows total days from start to end
- For in-progress tasks: Shows days since start (updated in real-time)
- For not-started tasks: Shows "Not started"

**Pro Tips**:
1. Use Date properties that include time for more precise tracking
2. Change "days" to "hours" for shorter tasks
3. Create a rollup to calculate total time across all project tasks

### Advanced Version with Hours:

If you use date properties with time enabled:

```
if(prop("Status") == "Done" and not empty(prop("End Date")), 
  format(round(dateBetween(prop("End Date"), prop("Start Date"), "hours") * 10) / 10) + " hours",
  if(prop("Status") == "In Progress" and not empty(prop("Start Date")),
    format(round(dateBetween(now(), prop("Start Date"), "hours") * 10) / 10) + " hours (ongoing)",
    "Not started"
  )
)
```

---

## 5. Revenue Per Day Calculator

**Use Case**: Calculate daily revenue rate for projects or track income velocity for solopreneurs.

**Setup Required**:
- "Revenue" property (Number, formatted as currency)
- "Start Date" property (Date)
- "End Date" property (Date)
- "Daily Rate" property (Formula)

**Formula**:
```
if(empty(prop("Revenue")) or empty(prop("Start Date")) or empty(prop("End Date")),
  "N/A",
  if(dateBetween(prop("End Date"), prop("Start Date"), "days") == 0,
    "$" + format(prop("Revenue")),
    "$" + format(round(prop("Revenue") / dateBetween(prop("End Date"), prop("Start Date"), "days") * 100) / 100) + " /day"
  )
)
```

**What it does**:
- Divides total revenue by project duration in days
- Shows rate as dollars per day
- Handles edge cases (same day projects, missing data)
- Rounds to 2 decimal places

**Use Cases**:
- Compare profitability across different projects
- Track if longer projects are actually more profitable
- Calculate effective hourly/daily rates
- Identify your most lucrative work types

**Real-World Example**:
- Project A: $5,000 over 30 days = $166.67/day
- Project B: $2,000 over 7 days = $285.71/day
- **Result**: Project B is more profitable per day!

### Variation - Revenue Per Hour:

For hourly tracking (requires date+time properties):

```
if(empty(prop("Revenue")) or empty(prop("Start Date")) or empty(prop("End Date")),
  "N/A",
  "$" + format(round(prop("Revenue") / dateBetween(prop("End Date"), prop("Start Date"), "hours") * 100) / 100) + " /hour"
)
```

---

## Bonus: Formula Tips & Tricks

### Common Functions Reference

**Date Functions:**
- `now()` - Current date and time
- `dateBetween(date1, date2, "units")` - Calculate difference
- `dateAdd(date, number, "units")` - Add time to a date
- `dateSubtract(date, number, "units")` - Subtract time from a date
- `formatDate(date, "format")` - Format date as string

**Units:** "years", "months", "weeks", "days", "hours", "minutes"

**Text Functions:**
- `format(value)` - Convert to text
- `concat(text1, text2)` - Combine text
- `length(text)` - Count characters
- `contains(text, "search")` - Check if text contains string
- `replace(text, "old", "new")` - Replace text

**Logic Functions:**
- `if(condition, result1, result2)` - Conditional logic
- `empty(property)` - Check if property is empty
- `not(condition)` - Reverse a condition
- `and(condition1, condition2)` - Both must be true
- `or(condition1, condition2)` - Either can be true

**Math Functions:**
- `round(number)` - Round to nearest integer
- `abs(number)` - Absolute value (remove negative sign)
- `max(num1, num2)` - Return larger number
- `min(num1, num2)` - Return smaller number
- `ceil(number)` - Round up
- `floor(number)` - Round down

### Pro Tips for Writing Formulas

1. **Test incrementally**: Build complex formulas step by step
2. **Use prop() correctly**: `prop("Property Name")` must match exactly (case-sensitive)
3. **Handle empty values**: Always check for empty/missing data
4. **Format consistently**: Use format() to ensure proper display
5. **Comment your logic**: Use meaningful property names to document your formulas
6. **Save templates**: Create a formula library page for reuse

### Common Errors & Solutions

**Error**: "Type mismatch"
- **Solution**: Make sure you're comparing the right data types (text vs. numbers vs. dates)

**Error**: Formula returns blank
- **Solution**: Check if any referenced properties are empty; add empty() checks

**Error**: "Property not found"
- **Solution**: Property name in formula must exactly match (including spaces, capitalization)

**Error**: Date calculations seem wrong
- **Solution**: Check if you're using the right units (days vs hours) and date property includes time if needed

---

## How to Add These Formulas

1. **Create or open a database** in Notion
2. **Click the "+" icon** to add a new property
3. **Select "Formula"** as the property type
4. **Give it a name** (e.g., "Days Remaining")
5. **Paste the formula** into the formula editor
6. **Customize property names** in the formula to match your database
7. **Click "Done"** to apply

---

## Next Steps

### Beginner:
- Start with formulas #1 and #2 (simplest)
- Practice modifying the text and emojis
- Experiment with different status options

### Intermediate:
- Combine multiple formulas
- Create rollups that use formula properties
- Build dashboard views with formula filters

### Advanced:
- Use relations and rollups with formulas
- Create complex scoring systems
- Build automated workflows with formula-based triggers
- Integrate with external tools using formula outputs

---

## More Resources

- [Official Notion Formula Documentation](https://notion.so/help/formulas)
- [Notion Formula Examples Gallery](https://notion.so/help/category/formulas)
- Check out the **Templates** folder in this repo for databases with these formulas pre-built!
- Join r/Notion for formula help and community examples

---

## Contributing

Have a useful formula to share? 
- Open a PR with your formula addition
- Include: use case, setup requirements, and explanation
- Follow the same format as above for consistency

Let's build the most comprehensive Notion formula library for solopreneurs! 🚀

---

*Happy formula building! Remember: Formulas are meant to save you time, not become a time sink. Start simple and add complexity only when needed.*
