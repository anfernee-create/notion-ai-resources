# Content Calendar Template

A comprehensive Notion template for planning and managing content across multiple platforms.

## Database Properties

### Content Items Database

| Property | Type | Description | Options |
|----------|------|-------------|----------|
| Title | Title | Content piece title | - |
| Status | Select | Current status | Ideas, Planning, Writing, Review, Scheduled, Published, Archived |
| Content Type | Select | Type of content | Blog Post, Social Post, Video, Newsletter, Podcast, Infographic |
| Platform | Multi-select | Publishing platforms | Website, Twitter, LinkedIn, Instagram, YouTube, Medium, TikTok |
| Category | Select | Content category | Education, Entertainment, News, Tutorial, Case Study |
| Priority | Select | Content priority | High, Medium, Low |
| Publish Date | Date | Scheduled/actual publish date | - |
| Author | Person | Content creator | - |
| Keywords | Multi-select | SEO keywords | - |
| Target Audience | Select | Primary audience | Beginners, Intermediate, Advanced, All |
| Word Count | Number | Article length | - |
| Engagement | Formula | Calculated engagement score | - |
| Related Content | Relation | Linked content pieces | - |
| Campaign | Relation | Marketing campaign | - |
| Performance | Select | Content performance | Exceeded, Met, Below |

### Campaign Database (Linked)

| Property | Type | Description |
|----------|------|-------------|
| Campaign Name | Title | Campaign title |
| Start Date | Date | Campaign start |
| End Date | Date | Campaign end |
| Goal | Text | Campaign objective |
| Budget | Number | Allocated budget |
| Content | Relation | Related content items |

## Views

### 1. Calendar View
**Purpose**: Visual monthly/weekly content planning
- **Group by**: None
- **Filter**: Status is not "Archived"
- **Sort**: Publish Date (ascending)
- **Properties shown**: Title, Content Type, Platform, Author, Status

### 2. Kanban Board (Status)
**Purpose**: Track content through production pipeline
- **Group by**: Status
- **Filter**: Status is not "Archived" and "Published"
- **Sort**: Priority (descending), then Publish Date (ascending)
- **Properties shown**: Content Type, Platform, Author, Publish Date

### 3. Content Type View
**Purpose**: See content distribution by type
- **Group by**: Content Type
- **Filter**: None
- **Sort**: Publish Date (descending)
- **Properties shown**: Title, Platform, Status, Publish Date

### 4. Platform View
**Purpose**: Manage content per platform
- **Group by**: Platform
- **Filter**: Status is "Scheduled" or "Published"
- **Sort**: Publish Date (descending)
- **Properties shown**: Title, Content Type, Status, Engagement

### 5. Ideas Backlog
**Purpose**: Store and review content ideas
- **Filter**: Status is "Ideas"
- **Sort**: Priority (descending)
- **Properties shown**: Title, Content Type, Category, Keywords

### 6. This Week
**Purpose**: Focus on immediate content tasks
- **Filter**: Publish Date is within next 7 days AND Status is not "Published"
- **Sort**: Publish Date (ascending)
- **Properties shown**: All

### 7. Performance Review
**Purpose**: Analyze published content
- **Filter**: Status is "Published"
- **Sort**: Publish Date (descending)
- **Properties shown**: Title, Content Type, Platform, Publish Date, Engagement, Performance

## AI Prompts for Content Planning

### Monthly Planning

**Generate Content Calendar Prompt:**
```
Create a content calendar for [Month] with:
- 12-16 content pieces
- Mix of content types: 60% blog posts, 20% social media, 10% video, 10% newsletters
- Topics focused on: [your niche/themes]
- 2-3 posts per week
- Include: title ideas, brief description, target keywords, best publish day
- Balance educational and promotional content (80/20 rule)
```

### Content Ideation

**Brainstorm Topics Prompt:**
```
Brainstorm 20 content ideas for [niche] that:
- Address common pain points
- Answer frequently asked questions
- Leverage current trends
- Include seasonal/timely topics
- Mix formats (how-to, listicle, case study, opinion)

For each idea provide:
- Title
- Brief description
- Target audience
- Content type recommendation
```

### Content Brief Generation

**Create Brief Prompt:**
```
Create a content brief for: "[Title]"

Include:
1. Target audience & their needs
2. Main message/value proposition
3. Key points to cover (5-7 points)
4. SEO keywords (primary + 3-5 secondary)
5. Suggested word count
6. Call-to-action
7. Tone and style guidelines
8. Competing content to reference
```

## Automation Ideas

### Status Automations

1. **Content Published**
   - When Status changes to "Published"
   - Send Slack notification
   - Add to analytics tracking

2. **Overdue Content**
   - When Publish Date is past and Status is not "Published"
   - Send reminder email
   - Flag in Kanban board

3. **Review Needed**
   - When Status changes to "Review"
   - Assign to editor
   - Set 48-hour review deadline

### Recurring Content

- Weekly newsletter template
- Monthly roundup post
- Quarterly performance review
- Annual planning session

## Usage Workflow

### Step 1: Idea Capture
1. Add content ideas to database immediately
2. Set Status to "Ideas"
3. Add relevant Category and Keywords
4. Use AI to expand rough ideas

### Step 2: Monthly Planning
1. Review Ideas Backlog
2. Use AI to generate content calendar
3. Select 12-16 ideas for the month
4. Set Publish Dates
5. Update Status to "Planning"
6. Assign Authors

### Step 3: Weekly Execution
1. Check "This Week" view every Monday
2. Move items to "Writing" as work begins
3. Update progress daily
4. Move to "Review" when draft complete

### Step 4: Review & Publish
1. Editor reviews content in "Review" status
2. Make revisions if needed
3. Update to "Scheduled" when approved
4. Schedule in publishing platform
5. Update to "Published" after going live

### Step 5: Performance Tracking
1. Add engagement metrics weekly
2. Review Performance once monthly
3. Identify top-performing content
4. Plan related/follow-up content

## Best Practices

### Planning

1. **Batch Planning**: Plan entire month at once
2. **Theme Weeks**: Group similar topics together
3. **Balance**: Mix content types and formats
4. **Buffer**: Always have 2-3 backup pieces ready
5. **Seasonality**: Plan 2-3 months ahead for seasonal content

### Production

1. **Templates**: Use content brief templates
2. **Checklists**: Create publishing checklists
3. **AI Assistance**: Use AI for first drafts and outlines
4. **Batch Creation**: Write multiple pieces in one session
5. **Review Process**: Always have someone review before publishing

### Tracking

1. **Consistent Metrics**: Track same KPIs for all content
2. **Regular Review**: Monthly performance analysis
3. **Learn & Iterate**: Apply insights to future content
4. **Document Success**: Save notes on what works
5. **Archive Smartly**: Keep old content for reference

## KPIs to Track

### Content Production
- Content pieces published per month
- Average time from idea to publish
- Content backlog size
- On-time publish rate

### Content Performance
- Page views/impressions
- Engagement rate (likes, comments, shares)
- Click-through rate
- Time on page/video watch time
- Conversion rate
- SEO rankings for target keywords

### Efficiency Metrics
- Content creation time per piece
- AI assistance usage
- Revision rounds needed
- Content reuse rate

## Formula Examples

### Engagement Score
```
if(prop("Status") == "Published", 
  prop("Views") * 0.01 + prop("Likes") * 1 + prop("Comments") * 3 + prop("Shares") * 5,
  0
)
```

### Days Until Publish
```
if(prop("Status") != "Published",
  dateBetween(prop("Publish Date"), now(), "days"),
  0
)
```

### Content Health
```
if(prop("Days Until Publish") < 0 and prop("Status") != "Published", 
  "🔴 Overdue",
  if(prop("Days Until Publish") <= 3 and prop("Status") != "Scheduled",
    "🟡 Urgent",
    "🟢 On Track"
  )
)
```

## Tips for AI-Enhanced Content Calendar

### 1. AI-Generated Ideas
- Use AI weekly to generate 10-20 new ideas
- Review and select best ones
- Add to Ideas Backlog

### 2. Smart Scheduling
- Ask AI for best posting times per platform
- Use AI to identify content gaps
- Generate complementary content suggestions

### 3. Content Repurposing
- Use AI to suggest repurposing opportunities
- Transform blog posts into social threads
- Convert videos into blog posts
- Extract quotes for social media

### 4. SEO Optimization
- AI keyword research for each piece
- Generate meta descriptions
- Suggest internal linking opportunities

### 5. Performance Analysis
- Ask AI to analyze trends in your data
- Get suggestions for improving low-performers
- Identify patterns in successful content

## Template Checklist

Before publishing any content:
- [ ] Title is compelling and includes target keyword
- [ ] Content provides clear value to target audience
- [ ] All facts and data are verified
- [ ] Grammar and spelling checked
- [ ] Images/media optimized and credited
- [ ] Meta description written (150-160 chars)
- [ ] Internal links added (3-5)
- [ ] External sources cited
- [ ] Call-to-action included
- [ ] Social media snippets prepared
- [ ] Publish date and time scheduled
- [ ] Analytics tracking set up

## Conclusion

This content calendar template, enhanced with Notion AI capabilities, provides:
- Centralized content planning
- Visual scheduling and tracking
- Production workflow management
- Performance monitoring
- AI-powered ideation and optimization

Consistency in content creation leads to audience growth, and this template helps maintain that consistency while maximizing quality and efficiency.
