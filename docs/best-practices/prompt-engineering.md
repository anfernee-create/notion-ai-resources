# Prompt Engineering Best Practices for Notion AI

Master the art of crafting effective prompts to get the best results from Notion AI.

## Table of Contents

1. [Core Principles](#core-principles)
2. [Prompt Structure](#prompt-structure)
3. [Common Patterns](#common-patterns)
4. [Advanced Techniques](#advanced-techniques)
5. [Common Mistakes](#common-mistakes)
6. [Examples](#examples)

## Core Principles

### 1. Be Specific

**Vague prompts lead to generic outputs.**

❌ Bad:
```
Write something about productivity
```

✅ Good:
```
Write a 300-word blog post introduction about time-blocking techniques for remote workers, emphasizing the benefits of focused work sessions.
```

### 2. Provide Context

**AI performs better with background information.**

❌ Bad:
```
Summarize this
```

✅ Good:
```
Summarize this quarterly business review meeting transcript, focusing on:
- Key decisions made
- Action items with owners
- Metrics discussed
- Concerns raised
```

### 3. Set Clear Expectations

**Define format, length, tone, and style.**

❌ Bad:
```
Explain machine learning
```

✅ Good:
```
Explain machine learning in 3 paragraphs for a business audience with no technical background. Use analogies and avoid jargon. Include 1-2 real-world business applications.
```

### 4. Use Examples

**Show, don't just tell.**

❌ Bad:
```
Format this data nicely
```

✅ Good:
```
Format this sales data as a markdown table with columns:
- Month
- Revenue (formatted as currency)
- Growth % (vs previous month)

Example row: | January | $125,000 | +15% |
```

### 5. Iterate and Refine

**First output is rarely perfect.**

Workflow:
1. Start with a basic prompt
2. Review AI output
3. Identify gaps or issues
4. Refine prompt with more specifics
5. Repeat until satisfied

##Prompt Structure

### Basic Template

```
[Action Verb] + [What] + [How] + [Constraints/Format]
```

**Examples:**

```
Write [what: a project proposal] 
for [how: implementing a new CRM system] 
with [constraints: 500 words, executive summary, budget estimate]
```

```
Analyze [what: customer feedback data]
to identify [how: top 3 pain points]
and provide [constraints: specific quotes, frequency of mention]
```

### Advanced Template

```
Role: [Specify perspective]
Task: [Clear action]
Context: [Background info]
Format: [Structure]
Tone: [Style]
Constraints: [Limitations]
Example: [Sample if needed]
```

**Example:**

```
Role: You are a senior product manager
Task: Write a feature specification
Context: We're adding dark mode to our mobile app based on user requests
Format: Use headings for: Overview, User Story, Requirements, Success Metrics
Tone: Technical but clear
Constraints: Under 400 words
Example: Similar to how we specified the notification feature
```

## Common Patterns

### Pattern 1: Transformation

**Convert content from one format to another**

```
Convert this [source format] to [target format]:
[content]

Maintain [what to preserve]
Format as [structure]
```

**Example:**
```
Convert these bullet points to a narrative paragraph:
- Launched new feature
- Saw 30% adoption
- Positive feedback

Maintain all numerical data
Format as professional project update
```

### Pattern 2: Analysis

**Extract insights from data or text**

```
Analyze [what] and identify:
1. [Aspect 1]
2. [Aspect 2]
3. [Aspect 3]

Provide [evidence/examples]
Rank by [criteria]
```

**Example:**
```
Analyze this user feedback and identify:
1. Most common complaints
2. Feature requests
3. Praise patterns

Provide quote examples for each
Rank by frequency of mention
```

### Pattern 3: Generation

**Create new content from scratch or brief**

```
Generate [count] [type] about [topic] that:
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]

Each should [constraints]
```

**Example:**
```
Generate 5 social media post ideas about our product launch that:
- Highlight different features
- Include a call-to-action
- Are under 280 characters

Each should target a different audience segment
```

### Pattern 4: Comparison

**Evaluate options or alternatives**

```
Compare [Option A] vs [Option B] based on:
- [Factor 1]
- [Factor 2]
- [Factor 3]

Provide:
- Pros/cons for each
- Recommendation
- Rationale
```

### Pattern 5: Simplification

**Make complex content accessible**

```
Simplify [complex content] for [audience]:

- Explain key concepts
- Remove jargon
- Use analogies
- Maintain accuracy

Length: [constraint]
```

## Advanced Techniques

### Chain Prompting

**Use output of one prompt as input for next**

Step 1:
```
Brainstorm 10 blog post topics about remote work productivity
```

Step 2 (using output):
```
From these topics, select the top 3 that would:
- Appeal to managers
- Be evergreen content
- Have strong SEO potential

Explain your selection
```

Step 3:
```
For the #1 topic, create a detailed outline with:
- Introduction hook
- 5 main sections
- Key points per section
- Conclusion with CTA
```

### Constrained Creativity

**Set boundaries to focus AI output**

```
Brainstorm solutions to [problem] with these constraints:
- Must work with existing tools
- Budget under $5000
- Can implement in 2 weeks
- No additional headcount

For each solution provide:
- Implementation steps
- Expected impact
- Potential risks
```

### Role-Based Prompting

**Have AI adopt a specific perspective**

```
As a [role], review this [content] and provide:
- What works well
- What needs improvement
- Specific recommendations
- Priority order

Consider [role-specific factors]
```

**Example:**
```
As a UX designer, review this product feature description and provide:
- Clarity of user benefit
- Potential usability concerns  
- Missing information users would need
- Suggested improvements

Consider accessibility and mobile experience
```

### Perspective Shifting

**Get multiple viewpoints**

```
Analyze [situation/decision] from these perspectives:

1. Customer viewpoint:
2. Business viewpoint:
3. Technical viewpoint:
4. Competitive viewpoint:

For each, explain:
- Key concerns
- Opportunities
- Risks
```

### Socratic Prompting

**Ask AI to question assumptions**

```
I'm planning to [decision/action].

Challenge this by asking:
- Critical questions I should answer first
- Assumptions I might be making
- Alternative approaches to consider
- Potential unintended consequences

For each, explain why it matters
```

##Common Mistakes

### Mistake 1: Too Vague

❌ **Problem:**
```
Make this better
```

✅ **Solution:**
```
Improve this paragraph by:
- Removing redundancy
- Strengthening word choice
- Adding transition sentences
- Maintaining professional tone
```

### Mistake 2: No Context

❌ **Problem:**
```
Write a proposal
```

✅ **Solution:**
```
Write a proposal for implementing flexible work policies at a 50-person tech startup. Include: rationale, proposed policy details, implementation plan, expected benefits. Audience: CEO and leadership team. Tone: professional but conversational.
```

### Mistake 3: Unrealistic Expectations

❌ **Problem:**
```
Write a complete business plan for my startup
```

✅ **Solution:**
```
Create an executive summary section for a SaaS business plan, covering: problem, solution, target market, revenue model, competitive advantage. 300-400 words.

[Then iterate for each section separately]
```

### Mistake 4: No Format Specification

❌ **Problem:**
```
Organize these ideas
```

✅ **Solution:**
```
Organize these ideas as a numbered list, grouped by theme. Use markdown headers for themes. Within each theme, rank ideas by implementation difficulty (easy to hard).
```

### Mistake 5: Accepting First Output

❌ **Problem:**
Using first AI response without review

✅ **Solution:**
1. Review AI output critically
2. Identify what's missing or wrong
3. Follow up with: "Improve this by adding [specific request]"
4. Or: "Revise the section about [X] to be more [specific improvement]"

## Examples

### Example 1: Email Writing

**Basic Prompt:**
```
Write an email declining a meeting
```

**Better Prompt:**
```
Write a professional but warm email declining a meeting request. 

Context: 
- Meeting is about a potential partnership
- I'm interested but currently overcommitted
- Want to reschedule for next quarter
- Maintain good relationship

Tone: Appreciative and honest
Length: 3-4 sentences
Include: Appreciation, brief reason, alternative timing, next steps
```

### Example 2: Data Analysis

**Basic Prompt:**
```
Analyze this data
```

**Better Prompt:**
```
Analyze this monthly revenue data for patterns:

[data]

Identify:
1. Overall trend (growing/declining/stable)
2. Seasonal patterns
3. Anomalies or outliers
4. Month-over-month growth rates
5. Potential concerns

For each finding:
- Provide specific numbers
- Explain significance
- Suggest follow-up questions
```

### Example 3: Brainstorming

**Basic Prompt:**
```
Give me ideas for content
```

**Better Prompt:**
```
Brainstorm 10 content ideas for our B2B SaaS blog.

Target audience: Mid-level managers at 100-500 person companies
Topics: Productivity, team management, remote work
Goal: Drive newsletter signups

For each idea provide:
- Working title
- One-sentence description  
- Target keyword
- Content type (how-to, listicle, case study, etc.)

Prioritize ideas that:
- Solve specific pain points
- Have search potential
- Can include data/examples
```

## Tips for Success

### 1. Start Broad, Then Narrow

First prompt: Get general ideas
Second prompt: Refine specific aspect
Third prompt: Polish details

### 2. Save Your Best Prompts

Create a prompt library in Notion:
- Category (writing, analysis, brainstorming)
- Template
- Example usage
- Tips for customization

### 3. Experiment with Variables

Try different:
- Tones (formal, casual, enthusiastic)
- Formats (bullets, paragraphs, tables)
- Lengths (brief, moderate, detailed)
- Perspectives (customer, technical, business)

### 4. Combine Human + AI

Optimal workflow:
1. You: Provide rough ideas/outline
2. AI: Expand and draft
3. You: Review and edit
4. AI: Polish specific sections
5. You: Final review and personalize

### 5. Know When NOT to Use AI

Don't rely on AI for:
- Highly specialized technical details
- Confidential or sensitive information
- Final decisions without human review
- Content requiring personal experience
- Fact-checking (always verify)

## Quick Reference

### Prompt Checklist

Before submitting a prompt, ensure you've included:

- [ ] Clear action verb (write, analyze, summarize, etc.)
- [ ] Specific subject matter
- [ ] Context or background
- [ ] Desired format/structure
- [ ] Length constraints
- [ ] Tone/style guidance
- [ ] Success criteria or key points to cover
- [ ] Example or reference (if helpful)

### Common Action Verbs

**Creation:**
- Write, generate, create, draft, compose, design

**Transformation:**
- Rewrite, rephrase, simplify, expand, condense, convert

**Analysis:**
- Analyze, evaluate, compare, assess, review, examine

**Organization:**
- Organize, structure, categorize, prioritize, sort, group

**Extraction:**
- Summarize, extract, identify, list, highlight, find

## Conclusion

Effective prompt engineering is a skill that improves with practice. The key is being specific, providing context, and iterating based on results. Start with these patterns and adapt them to your needs. Remember: AI is a tool that amplifies your expertise, not a replacement for your judgment.
