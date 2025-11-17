# GitHub Integration for Notion

Connect GitHub with Notion to manage development projects, track issues, and synchronize documentation across platforms.

## Overview

The GitHub-Notion integration creates a powerful hub for developer workflows:
- Sync GitHub issues and pull requests to Notion databases
- Track repository activity and commits
- Embed code snippets and gists in documentation
- Manage product roadmaps and feature planning
- Auto-update project status from GitHub events

## Setup Instructions

### Prerequisites
- GitHub account (Free or Pro)
- Notion workspace
- Personal access token or GitHub App

### Step 1: Create GitHub Personal Access Token

1. Go to [GitHub Settings](https://github.com/settings/tokens)
2. Click **Generate new token** > **Generate new token (classic)**
3. Name your token (e.g., "Notion Integration")
4. Select scopes:
   - `repo` (full repository access)
   - `read:org` (organization access)
   - `read:user` (user profile)
5. Click **Generate token**
6. **Copy and save immediately** (won't be shown again)

### Step 2: Set Up Notion Integration

1. Go to **Settings & Members** in Notion
2. Navigate to **Integrations**
3. Click **Develop or manage integrations**
4. Create **New integration**
5. Name it "GitHub Connector"
6. Copy **Internal Integration Token**
7. Share target databases with integration

### Step 3: Build the Connection

Use automation platform (Zapier/Make) or build custom integration:
- Store both tokens securely
- Set up webhook listeners
- Configure sync frequency
- Test with sample repository

## Use Cases for Solopreneurs & Developers

### 1. Product Roadmap Management
**Scenario:** Track GitHub repo features in Notion roadmap database

**Setup:**
- Create Notion database: Feature | Status | Priority | GitHub Issue Link
- Sync GitHub issues to database
- Use Notion views for sprint planning
- Update status when PRs merge

**Benefits:**
- Visual roadmap for stakeholders
- Link technical work to business goals
- Track progress without leaving Notion

### 2. Documentation Hub
**Scenario:** Keep README and docs in sync between GitHub and Notion

**Setup:**
- Write documentation in Notion
- Auto-export to markdown
- Push to GitHub repository
- Embed code examples from gists

**Benefits:**
- Beautiful docs in Notion
- Developer-friendly markdown in GitHub
- Single source of truth

### 3. Issue Tracker Database
**Scenario:** Manage bug reports and feature requests in Notion

**Setup:**
- Sync GitHub issues to Notion database
- Add columns: Reporter, Labels, Assignee, Due Date
- Create filtered views by priority
- Auto-comment on GitHub when status changes

**Benefits:**
- Better visualization than GitHub Issues
- Custom workflows and automation
- Integrate with other Notion databases

### 4. Commit Activity Log
**Scenario:** Track development activity for productivity insights

**Setup:**
- Log all commits to Notion database
- Add metrics: Lines changed, Files modified, Time
- Create weekly/monthly activity reports
- Visualize contribution patterns

**Benefits:**
- Understand your productivity cycles
- Show progress to clients/stakeholders
- Identify optimization opportunities

### 5. Release Notes Generator
**Scenario:** Auto-generate release notes from merged PRs

**Setup:**
- Track merged PRs in Notion
- Filter by release milestone
- Format as changelog
- Publish to blog or update page

**Benefits:**
- Automated release documentation
- Professional changelog
- Save hours on manual note writing

## Automation Examples

### Sync GitHub Issues to Notion
```javascript
const { Octokit } = require('@octokit/rest');
const { Client } = require('@notionhq/client');

const github = new Octokit({ auth: process.env.GITHUB_TOKEN });
const notion = new Client({ auth: process.env.NOTION_TOKEN });

// Get issues from repository
const { data: issues } = await github.issues.listForRepo({
  owner: 'your-username',
  repo: 'your-repo',
  state: 'all'
});

// Sync to Notion database
for (const issue of issues) {
  await notion.pages.create({
    parent: { database_id: process.env.NOTION_DB_ID },
    properties: {
      'Title': { title: [{ text: { content: issue.title } }] },
      'Number': { number: issue.number },
      'Status': { select: { name: issue.state } },
      'Labels': { multi_select: issue.labels.map(l => ({ name: l.name })) },
      'URL': { url: issue.html_url },
      'Created': { date: { start: issue.created_at } }
    }
  });
}
```

### Create GitHub Issue from Notion
```javascript
// Watch for new pages in Notion database
const newIssues = await notion.databases.query({
  database_id: process.env.NOTION_DB_ID,
  filter: {
    property: 'GitHub Issue',
    checkbox: { equals: false }
  }
});

// Create issues on GitHub
for (const page of newIssues.results) {
  const title = page.properties.Title.title[0].text.content;
  const body = await getPageContent(page.id);
  
  const { data: issue } = await github.issues.create({
    owner: 'your-username',
    repo: 'your-repo',
    title: title,
    body: body
  });
  
  // Update Notion with GitHub link
  await notion.pages.update({
    page_id: page.id,
    properties: {
      'GitHub Issue': { checkbox: true },
      'Issue URL': { url: issue.html_url },
      'Issue Number': { number: issue.number }
    }
  });
}
```

### Track Repository Activity
```javascript
// Get recent commits
const { data: commits } = await github.repos.listCommits({
  owner: 'your-username',
  repo: 'your-repo',
  per_page: 10
});

// Log to Notion activity database
for (const commit of commits) {
  await notion.pages.create({
    parent: { database_id: process.env.ACTIVITY_DB_ID },
    properties: {
      'Message': { title: [{ text: { content: commit.commit.message } }] },
      'Author': { rich_text: [{ text: { content: commit.commit.author.name } }] },
      'SHA': { rich_text: [{ text: { content: commit.sha.substring(0, 7) } }] },
      'Date': { date: { start: commit.commit.author.date } },
      'URL': { url: commit.html_url }
    }
  });
}
```

## Best Practices

### For Solo Developers
1. **One-way sync first**: Start with GitHub → Notion to avoid conflicts
2. **Use webhooks**: Real-time updates instead of polling
3. **Filter strategically**: Only sync repos/issues you actively work on
4. **Automate repetitive tasks**: Release notes, changelogs, status updates

### Repository Management
1. **Clear naming**: Match Notion page titles with repo names
2. **Consistent labels**: Use same labels in GitHub and Notion
3. **Archive old data**: Move completed projects to archive databases
4. **Backup regularly**: Export Notion pages, GitHub has native backup

### Workflow Optimization
1. **Bi-directional updates**: Keep both platforms in sync
2. **Use GitHub Actions**: Trigger Notion updates from CI/CD
3. **Custom views**: Different perspectives for planning vs execution
4. **Integrate with other tools**: Connect Slack, Jira, Linear

## Native Notion Features

### Embed GitHub Content

Notion supports native embeds for:

**Gists:**
1. Create gist on GitHub
2. Copy gist URL
3. In Notion, type `/embed`
4. Paste URL

**Repository Links:**
- Paste GitHub repo URL
- Notion shows repo preview with stats
- Displays stars, forks, description

**Commit Links:**
- Paste commit URL
- Shows commit message and metadata
- Links directly to GitHub diff

## Advanced Workflows

### Product Launch Pipeline
1. Plan features in Notion roadmap
2. Create GitHub issues from Notion
3. Develop and commit code
4. Auto-update Notion status on PR merge
5. Generate release notes in Notion
6. Publish changelog to website

### Open Source Project Management
1. Track contributor issues in Notion
2. Prioritize community feedback
3. Link PRs to roadmap items
4. Auto-thank contributors
5. Generate monthly progress reports

### Documentation System
1. Write docs in Notion (rich editor)
2. Export to markdown
3. Commit to GitHub repo
4. Deploy with GitHub Pages
5. Maintain single source in Notion

## Troubleshooting

### Common Issues

**Problem:** "Bad credentials" error
- Verify token hasn't expired
- Check token has correct scopes
- Regenerate if necessary

**Problem:** Rate limit exceeded
- GitHub free: 60 requests/hour (unauthenticated)
- With token: 5,000 requests/hour
- Implement caching and request throttling

**Problem:** Webhook not triggering
- Verify webhook URL is publicly accessible
- Check webhook secret matches
- Review delivery logs in GitHub settings

**Problem:** Duplicate entries
- Implement idempotency checks
- Use GitHub issue ID as unique identifier
- Query Notion before creating new pages

## Security Best Practices

### Token Management
- Store tokens in environment variables
- Never commit to version control
- Use GitHub Apps instead of personal tokens (for teams)
- Rotate tokens every 90 days
- Revoke unused integrations

### Access Control
- Minimum required permissions only
- Separate tokens for different projects
- Use read-only tokens when possible
- Enable 2FA on GitHub account

### Data Protection
- Don't expose sensitive code in Notion
- Review Notion page sharing settings
- Keep private repos separate
- Audit integration access regularly

## Cost Analysis

### GitHub
- **Free:** Unlimited public repos, 2,000 Actions minutes/month
- **Pro ($4/month):** Advanced code review, 3,000 Actions minutes
- **API Rate Limits:** 5,000 requests/hour (authenticated)

### Automation Platforms
- **GitHub Actions:** Free for public repos, included with Pro
- **Zapier:** $19.99/month for GitHub integration
- **Make:** $9/month (better value for developers)
- **Self-hosted:** Free (time investment required)

### Solopreneur Recommendation
Build custom integration with GitHub Actions + Notion API. Free, unlimited, and you control the logic.

## Resources
- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [GitHub GraphQL API](https://docs.github.com/en/graphql)
- [Notion API Reference](https://developers.notion.com/)
- [Octokit SDK (Node.js)](https://github.com/octokit/octokit.js)
- [Example Integration Repository](https://github.com/makenotion/notion-sdk-js)

## Starter Template

### Notion Database Properties
Create a database with these columns:
- **Title** (Title): Issue/PR title
- **Number** (Number): GitHub issue number
- **Status** (Select): Open, In Progress, Closed
- **Priority** (Select): High, Medium, Low
- **Labels** (Multi-select): Synced from GitHub
- **Assignee** (Person): Team member
- **GitHub URL** (URL): Direct link to issue
- **Repository** (Select): Repo name
- **Created Date** (Date): Issue creation date
- **Last Updated** (Date): Last activity timestamp

### Quick Start Script
```bash
# Clone starter template
git clone https://github.com/notion-github-sync/starter
cd starter

# Install dependencies
npm install

# Set environment variables
echo "GITHUB_TOKEN=your_token" > .env
echo "NOTION_TOKEN=your_token" >> .env
echo "NOTION_DATABASE_ID=your_db_id" >> .env

# Run initial sync
node sync.js

# Set up webhook (optional)
node setup-webhook.js
```

## Real-World Example: Digital Product Launch

As a solopreneur building digital products:

1. **Planning Phase**
   - Create product roadmap in Notion
   - Break down features into GitHub issues
   - Set milestones and deadlines

2. **Development Phase**
   - Code in your IDE
   - Commit to GitHub
   - Auto-update Notion status
   - Track progress visually

3. **Pre-Launch**
   - Review merged PRs
   - Generate release notes
   - Create launch checklist
   - Prepare marketing materials

4. **Post-Launch**
   - Monitor GitHub issues
   - Track bug reports in Notion
   - Prioritize improvements
   - Plan next version

**Result:** Seamless workflow from idea to shipped product, all tracked in Notion with technical details in GitHub.
