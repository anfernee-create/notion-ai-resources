# Database Autofill Examples

## Overview

This guide provides AI prompts for automatically populating Notion database fields using AI capabilities. These prompts help extract structured data from unstructured text, generate consistent values, and maintain data quality.

## Property-Specific Autofill

### Status/Category Generation

**Prompt**: "Analyze this content and assign an appropriate status: [TEXT]. Choose from: Not Started, In Progress, Completed, On Hold, Blocked. Consider keywords, timeline references, and task state indicators."

### Priority Assignment

**Prompt**: "Determine the priority level (High/Medium/Low) for this item based on urgency indicators, deadline proximity, and importance signals: [TEXT]"

### Tag Extraction

**Prompt**: "Extract relevant tags from this content: [TEXT]. Generate 3-5 descriptive tags that capture key topics, themes, or categories. Use lowercase, hyphenated format."

### Date Inference

**Prompt**: "Identify and extract dates from this text: [TEXT]. Return in YYYY-MM-DD format. If multiple dates, identify which is start vs end date."

## Multi-Property Autofill

### Complete Task Entry

**Prompt**: "Extract structured task information from: [TEXT]

Provide:
- **Title**: Concise task name (3-7 words)
- **Description**: 1-2 sentence summary
- **Status**: Current state
- **Priority**: High/Medium/Low
- **Tags**: 3-5 relevant tags
- **Estimated Time**: Hours or days
- **Category**: Primary classification"

### Project Entry Autofill

**Prompt**: "Generate complete project database entry from: [TEXT]

**Fields:**
- Name
- Description (50-100 words)
- Status
- Priority
- Start Date
- End Date
- Budget Range
- Team Size
- Key Milestones (3-5)
- Success Metrics"

### Contact Information Extraction

**Prompt**: "Extract contact details from this text and format for database: [TEXT]

**Extract:**
- Full Name
- Company
- Title/Role
- Email
- Phone
- LinkedIn URL
- Location
- Tags (industry, relationship type)
- Notes (relevant context)"

## Content-Based Autofill

### Article Metadata

**Prompt**: "Generate metadata for this article: [TEXT]

- **Title**: Headline (5-10 words)
- **Summary**: 2-3 sentence overview
- **Key Topics**: 4-6 main themes
- **Target Audience**: Who benefits most
- **Content Type**: Tutorial/Guide/Analysis/etc
- **Reading Time**: Minutes
- **Difficulty**: Beginner/Intermediate/Advanced
- **Keywords**: SEO keywords"

### Meeting Notes Parsing

**Prompt**: "Structure this meeting content: [TEXT]

**Extract:**
- Meeting Title
- Date & Time
- Attendees
- Key Decisions (bulleted)
- Action Items (with owners)
- Next Meeting Date
- Follow-up Required (Yes/No)
- Priority Topics"

## Smart Defaults

### Template-Based Autofill

**Prompt**: "For a [TYPE] entry in my [DATABASE NAME], suggest default values for empty fields based on this context: [TEXT]

Provide intelligent defaults that match typical patterns for this entry type."

### Related Fields

**Prompt**: "Given that [FIELD 1] = [VALUE], suggest appropriate values for [FIELD 2], [FIELD 3], and [FIELD 4] that typically correlate or are logically related."

## Validation & Enhancement

### Data Cleanup

**Prompt**: "Clean and standardize this database entry: [DATA]. Fix inconsistent formatting, expand abbreviations, standardize capitalization, and ensure values match expected formats."

### Missing Field Suggestions

**Prompt**: "This database entry is incomplete: [EXISTING DATA]. Suggest plausible values for empty fields based on the existing information and typical patterns."

## Best Practices

1. **Provide context** - Include examples of desired outputs
2. **Define field constraints** - Specify allowed values, formats
3. **Use consistent formats** - Maintain standardization
4. **Validate AI outputs** - Review generated data
5. **Iterate prompts** - Refine based on results
6. **Include fallbacks** - Handle cases where data can't be extracted
7. **Batch similar items** - Process multiple entries efficiently

## Example Use Cases

**Task Management:**
"Parse this email and create task entries: [EMAIL]"

**Content Calendar:**
"Generate content database entries from these ideas: [IDEAS]"

**CRM Updates:**
"Extract contact information from meeting notes: [NOTES]"

**Research Database:**
"Create structured entries from these article summaries: [SUMMARIES]"

## Related Prompts

- **categorization.md** - For classification systems
- **summary-generation.md** - For creating descriptions
- **query-optimization.md** - For finding related entries

## Version Information

**Last Updated**: 2024
**Version**: 1.0
**Status**: Active
