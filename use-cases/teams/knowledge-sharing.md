# Team Wiki & Knowledge Sharing

Build a living, AI-enhanced team wiki that keeps organizational knowledge current, searchable, and accessible to every team member.

## The Challenge

Team knowledge lives in people's heads and scattered documents. When someone leaves or a new person joins, crucial context is lost. A Notion team wiki solves this by making knowledge explicit, searchable, and maintainable.

## Wiki Architecture

```
Team Wiki
├── Company
│   ├── Mission & Values
│   ├── Org Chart
│   └── Policies
├── Products
│   ├── Product Specs
│   ├── Roadmaps
│   └── User Research
├── Processes
│   ├── SOPs
│   ├── Runbooks
│   └── How-To Guides
├── Projects
│   └── [linked from Projects database]
└── Onboarding
    ├── 30-60-90 Day Plan
    └── Tool Access Guide
```

## AI-Powered Features

### Content Freshness Monitor
Add an AI property to wiki pages:
> "Based on the last edited date ({{Last Edited}}) and the content, rate the freshness: Current / Needs Review / Likely Outdated. Explain why."

Automation: Flag pages as "Needs Review" after 90 days without edits.

### Onboarding Assistant
Create an AI block on the onboarding page:
> "A new team member is joining as [Role]. Based on our wiki content, create a personalized 30-day learning plan covering: company overview, key processes, tools, and important contacts."

### Knowledge Gap Finder
AI property on the wiki index:
> "Review the list of team processes and identify areas where documentation appears to be missing or incomplete based on what a typical team of this type would need."

## Wiki Maintenance System

### Documentation Owners
Assign an "Owner" to each wiki section. Owners are responsible for keeping their section current. Monthly reminder automation to review.

### Update Workflow
1. Anyone can edit (democratic wiki)
2. Owner reviews and approves significant changes
3. AI property detects if content has become outdated

### Version History
Use Notion's page history for important documents. Add a "Version" date at the top of critical SOPs.

## Onboarding Integration

Create a "New Hire" template that auto-links to all relevant wiki pages for that role. First week task: read and leave comments/questions on key wiki pages.

## Best Practices

- Write for your future self (you'll forget the context)
- Link aggressively — the wiki's value multiplies with connections
- Keep pages focused — one topic per page
- Use consistent formatting so AI can process it better
- Celebrate wiki contributors (gamify updates)

## Related

- [Meeting Management](meeting-management.md)
- [Project Tracking](project-tracking.md)

---

*Last Updated: April 2026*
