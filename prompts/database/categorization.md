# Database Categorization Prompts

## Overview

These AI prompts help categorize and classify Notion database entries automatically. Use them to maintain consistent taxonomies, apply appropriate labels, and organize information effectively.

## Single-Level Categorization

### Basic Category Assignment

**Prompt**: "Categorize this content into one of these categories: [CATEGORY LIST]. Base your decision on content analysis, keywords, and primary focus: [TEXT]"

### Topic Classification

**Prompt**: "Classify this article/content by primary topic. Choose the most relevant from: Technology, Business, Health, Education, Finance, Marketing, Personal Development, Other. Content: [TEXT]"

### Content Type Classification

**Prompt**: "Identify the content type: Article, Tutorial, Case Study, Research, Opinion, News, Review, Guide, Reference. Analyze structure and purpose: [TEXT]"

### Difficulty Level

**Prompt**: "Assign difficulty level (Beginner/Intermediate/Advanced/Expert) based on technical depth, prerequisite knowledge, and complexity: [TEXT]"

## Multi-Level Categorization

### Hierarchical Classification

**Prompt**: "Categorize this content in a 3-tier hierarchy:
- **Level 1** (Broad): Main category
- **Level 2** (Medium): Subcategory
- **Level 3** (Specific): Detailed classification

Content: [TEXT]

Example: Technology > Software Development > Web Frameworks"

### Multi-Tag System

**Prompt**: "Apply multiple relevant tags from this taxonomy:

**Primary Tags**: [LIST]
**Secondary Tags**: [LIST]
**Attribute Tags**: [LIST]

Select 3-7 total tags that best describe: [TEXT]"

## Domain-Specific Categorization

### Content Calendar

**Prompt**: "Categorize this content piece:
- **Platform**: Blog/Social/Email/Video
- **Stage**: Awareness/Consideration/Decision
- **Format**: How-to/Listicle/Story/Data-driven
- **Pillar**: Which content pillar
- **Audience**: Target segment

Content: [TEXT]"

### Task Management

**Prompt**: "Categorize this task:
- **Type**: Feature/Bug/Improvement/Research
- **Area**: Frontend/Backend/Design/DevOps
- **Impact**: User-facing/Internal/Infrastructure
- **Effort**: Small/Medium/Large
- **Theme**: Which project theme

Task: [TEXT]"

### Customer Feedback

**Prompt**: "Classify this feedback:
- **Type**: Feature Request/Bug Report/Complaint/Praise/Question
- **Category**: Product/Service/Support/Pricing/UX
- **Sentiment**: Positive/Neutral/Negative
- **Priority**: Critical/High/Medium/Low
- **Theme**: Common theme identifier

Feedback: [TEXT]"

## Intelligent Categorization

### Context-Aware Classification

**Prompt**: "Given this database context: [DESCRIPTION], categorize new entry: [TEXT].

Consider existing patterns, naming conventions, and category distributions to maintain consistency."

### Auto-Suggest Categories

**Prompt**: "Analyze these existing categories: [EXISTING]. Suggest the best fitting category for: [NEW ENTRY]. If none fit well, suggest a new category name that maintains taxonomy consistency."

### Batch Categorization

**Prompt**: "Categorize these [N] items consistently using the same taxonomy:

[ITEM 1]
[ITEM 2]
[ITEM 3]...

Provide category for each with reasoning."

## Category Validation

### Category Refinement

**Prompt**: "This item is currently categorized as [CURRENT]. Review and either confirm or suggest better category with reasoning: [TEXT]"

### Taxonomy Improvement

**Prompt**: "Analyze these categorized items: [LIST WITH CATEGORIES]. Identify:
- Overcrowded categories to split
- Underused categories to merge
- Missing categories needed
- Inconsistent classifications
- Suggested taxonomy improvements"

## Best Practices

1. **Define clear categories** - Mutually exclusive when possible
2. **Provide examples** - Show AI what belongs in each category
3. **Maintain consistency** - Use same taxonomy across similar items
4. **Limit category count** - 5-15 primary categories ideal
5. **Use hierarchies** - Organize broad to specific
6. **Review regularly** - Audit AI categorizations
7. **Allow multi-tagging** - Some items fit multiple categories
8. **Document rules** - Explain boundary cases

## Example Workflows

**New Content Entry:**
"Categorize this blog post by topic, difficulty, and content type: [POST]"

**Task Organization:**
"Classify this task by area, type, and priority: [TASK]"

**Research Library:**
"Tag this paper with subject areas, methodology, and relevance: [ABSTRACT]"

**CRM Categorization:**
"Classify this contact by industry, company size, and engagement level: [INFO]"

## Advanced Techniques

### Probabilistic Classification

**Prompt**: "Provide confidence scores for top 3 most likely categories:
Content: [TEXT]
Categories: [LIST]

Format: Category (Confidence %)"

### Multi-Criteria Decision

**Prompt**: "Categorize using weighted criteria:
- Content focus (40%)
- Target audience (30%)
- Format (20%)
- Business goal (10%)

Content: [TEXT]"

## Related Prompts

- **autofill-examples.md** - For populating other fields
- **summary-generation.md** - For creating descriptions
- **query-optimization.md** - For finding similar items

## Version Information

**Last Updated**: 2024
**Version**: 1.0
**Status**: Active
