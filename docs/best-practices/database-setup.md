# Database Setup Best Practices for Notion AI

## Overview

Proper database structure is the foundation for effective Notion AI implementation. This guide covers best practices for setting up databases that maximize AI capabilities and ensure optimal performance.

## Core Database Structure

### 1. Properties Organization

**Essential Properties:**
- **Title** (Text) - Primary identifier
- **Status** (Select) - Workflow stage
- **Created** (Date) - Record creation date
- **Modified** (Date) - Last modification date
- **Tags** (Multi-select) - Categorization

**AI-Specific Properties:**
- **AI Summary** (AI) - Auto-generated overview
- **Key Points** (AI) - Important highlights
- **Sentiment** (AI) - Emotional tone analysis
- **Priority** (AI) - Computed priority level

### 2. Property Types for AI Integration

| Type | Use Case | AI Capability |
|------|----------|---------------|
| Text | General content | Input for analysis |
| Rich Text | Formatted content | Full context understanding |
| Select | Single option | Categorization base |
| Multi-select | Multiple options | Tagging for context |
| Date | Time tracking | Timeline analysis |
| Number | Metrics | Quantitative analysis |
| Checkbox | Binary state | Conditional logic |
| Relation | Link to other DBs | Cross-database context |
| Rollup | Aggregated data | Summary generation |
| Formula | Computed values | Dynamic classification |
| AI Property | AI-generated | Automated intelligence |

## Naming Conventions

### Property Names

**Good:**
- `Customer Name` - Clear, descriptive
- `Order Total (USD)` - Includes unit
- `Next Review Date` - Specific purpose
- `AI Generated Summary` - Indicates AI-driven

**Avoid:**
- `Data` - Too vague
- `Stuff` - Unprofessional
- `Temp` - Suggests impermanence
- `XXX` - Unclear purpose

### Database Names

- Use singular form: "Customer" not "Customers"
- Use descriptive names: "Customer Feedback" not "DB1"
- Include type: "Tasks - Project X" to indicate category
- Keep consistent across related databases

## Database Templates for Common Use Cases

### Template 1: Content Management

```
Database: Articles

Properties:
- Title (Text) - Article title
- Content (Rich Text) - Full article body
- Topic (Select) - Main topic
- Status (Select) - Draft/Published/Archived
- AI Summary (AI) - Auto-generated summary
- AI Keywords (AI) - Extracted keywords
- Read Time (Formula) - Calculated from content length
- Published Date (Date)
- Tags (Multi-select)
- SEO Score (AI) - Quality assessment
```

### Template 2: Project Management

```
Database: Tasks

Properties:
- Task Name (Text)
- Description (Rich Text)
- Project (Relation) - Links to Projects DB
- Status (Select) - Not Started/In Progress/Completed
- Priority (AI) - AI-assessed importance
- Assigned To (Person)
- Due Date (Date)
- Start Date (Date)
- Effort Estimate (Select) - Small/Medium/Large
- Dependencies (Relation) - Links to other tasks
- AI Action Items (AI) - Auto-extracted next steps
- Completion Notes (Rich Text)
```

### Template 3: Customer CRM

```
Database: Customers

Properties:
- Company Name (Text) - Primary identifier
- Contact Name (Text)
- Email (Email)
- Phone (Phone)
- Industry (Select)
- Company Size (Select) - Startup/SMB/Enterprise
- Last Contact (Date)
- AI Relationship Score (AI) - Engagement level
- AI Next Steps (AI) - Suggested actions
- Notes (Rich Text)
- Related Opportunities (Relation)
- Sentiment from Recent Interactions (AI)
```

## AI Property Setup Guide

### Step 1: Choose Property Type

1. Click the `+` to add new property
2. Name the property descriptively
3. Select "AI" from property type dropdown

### Step 2: Configure AI Behavior

**Configuration Options:**

```
Property: AI Sentiment
Prompt: "Analyze the sentiment of this content.
         Respond with: POSITIVE, NEGATIVE, or NEUTRAL"
Output Type: Text
```

### Step 3: Test the AI Property

1. Add test data to source field
2. Let AI property generate output
3. Verify accuracy and adjust prompt if needed
4. Deploy to all records

## Optimization Strategies

### 1. Database Relations

**Good Structure:**
```
Tasks DB (child) ---> Projects DB (parent)
Tasks DB (child) ---> Team Members DB (parent)
Projects DB ---> Clients DB
```

**Benefits:**
- Single source of truth
- Automatic updates cascade
- AI can reference related data

### 2. Rollup Properties

Use rollups to aggregate related data:

```
Project Database has:
- Project Name
- Related Tasks (Relation)
- Tasks Count (Rollup: count)
- Total Hours (Rollup: sum of effort)
- AI Project Summary (AI: uses above data)
```

### 3. Formula Properties

Create computed properties for AI context:

```
Formula: Concatenate priority, status, and due date
Result: Used by AI for smart sorting and summarization
```

## Performance Optimization

### Database Size Limits

| Item | Free Plan | Paid Plan |
|------|-----------|----------|
| Database Size | 5 MB | Unlimited |
| Records | ~100 | Millions |
| Properties | 1,000+ | 1,000+ |
| Views | Unlimited | Unlimited |

### Speed Optimization

1. **Reduce AI Property Triggers**
   - Only enable AI for essential properties
   - Use batch updates instead of individual changes

2. **Limit Database Relations**
   - Too many relations slow down queries
   - Consolidate where possible

3. **Archive Old Data**
   - Move completed items to archive DB
   - Reduces main DB size
   - Improves performance

4. **Use Filters Strategically**
   - Filter data at database level
   - Reduces processing load

## AI-Optimized Database Design

### Principle 1: Rich Context

**Goal:** Provide AI with complete context

```
Poor: "Task: Write article"
Good: "Task: Write technical article on Notion AI
      For: Marketing team
      Purpose: Lead generation
      Format: 2,000 words, with examples
      Audience: Developers
      Status: In progress"
```

### Principle 2: Standardized Data

**Goal:** Ensure AI receives consistent input

```
Bad: Dates formatted as "1/2/3", "Jan 2", "Today"
Good: All dates in ISO format (2024-01-15)
```

### Principle 3: Semantic Tags

**Goal:** Enable AI to understand relationships

```
Tags: Bug, Critical, Backend, Auth
Not: x, bug-234, TODO, urgent!!!!
```

## Common Database Mistakes

### Mistake 1: Overusing AI Properties

**Problem:** Too many AI properties slow down the database

**Solution:** Use only 3-5 key AI properties per database

### Mistake 2: Inconsistent Data Entry

**Problem:** AI produces inconsistent results from messy data

**Solution:** Use templates and validation rules

### Mistake 3: Missing Context Properties

**Problem:** AI lacks information for good analysis

**Solution:** Add all relevant context properties even if not immediately visible

### Mistake 4: Wrong Property Types

**Problem:** Using Text when Select would be better

**Solution:** Choose property types that constrain data appropriately

## Database Maintenance Checklist

- [ ] Review property structure monthly
- [ ] Archive completed/old records quarterly
- [ ] Test AI property accuracy regularly
- [ ] Update AI prompts based on feedback
- [ ] Clean up unused properties
- [ ] Verify relations still make sense
- [ ] Backup critical databases
- [ ] Monitor database performance
- [ ] Update team on new best practices
- [ ] Gather feedback from users

## Advanced Setup: Multi-Database Systems

### Scenario: Sales Management System

**Databases:**
1. **Accounts** - Company information
2. **Contacts** - Individual relationships
3. **Opportunities** - Sales deals
4. **Activities** - Interactions and follow-ups
5. **Products** - What you sell

**Relations:**
- Contacts → Accounts (Many-to-One)
- Opportunities → Accounts (Many-to-One)
- Opportunities → Products (Many-to-Many)
- Activities → Contacts (Many-to-One)
- Activities → Opportunities (Many-to-One)

**AI Properties:**
- Account: AI Engagement Score
- Contact: AI Interest Level
- Opportunity: AI Probability to Close
- Activity: AI Next Steps

## Migration Guide

### Migrating from Simple to AI-Optimized

1. **Audit Current Setup**
   - Document all properties
   - Identify data gaps
   - Note pain points

2. **Design New Structure**
   - Add AI properties
   - Create proper relations
   - Plan formula properties

3. **Test with Sample Data**
   - Create test database
   - Populate with examples
   - Verify AI output quality

4. **Migration Process**
   - Export existing data
   - Import to new structure
   - Validate data integrity
   - Train team on new setup

5. **Iterative Improvement**
   - Gather feedback
   - Adjust AI prompts
   - Optimize structure
   - Document learnings

## Related Documentation

- [Workflow Optimization](./workflow-optimization.md)
- [Writing Effective Prompts](./writing-prompts.md)
- [AI Features Guide](../features/)
- [Database Tutorial](../../tutorials/beginner/database-setup.md)

---

**Last Updated:** November 2025
**Difficulty Level:** Intermediate
**Estimated Reading Time:** 12 minutes
**Estimated Setup Time:** 1-3 hours per database
