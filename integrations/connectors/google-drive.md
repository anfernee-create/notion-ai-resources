# Google Drive Integration for Notion

Sync files and documents between Google Drive and Notion to centralize your content workflow and automate file management.

## Overview

The Google Drive-Notion integration enables seamless file sharing and content synchronization:
- Embed Google Docs, Sheets, and Slides in Notion pages
- Auto-sync Drive file updates to Notion databases
- Create backup workflows for important documents
- Organize Drive files with Notion's database structure
- Track file versions and sharing permissions

## Setup Instructions

### Prerequisites
- Google account with Drive access
- Notion workspace (Free or Paid plan)
- Google Cloud Project (for API access)

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **Create Project**
3. Name your project (e.g., "Notion-Drive-Sync")
4. Enable **Google Drive API**:
   - Navigate to **APIs & Services** > **Library**
   - Search for "Google Drive API"
   - Click **Enable**

### Step 2: Set Up OAuth 2.0 Credentials

1. Go to **APIs & Services** > **Credentials**
2. Click **Create Credentials** > **OAuth client ID**
3. Configure consent screen:
   - Select **External** user type
   - Add app name and developer contact
4. Add scopes:
   - `https://www.googleapis.com/auth/drive.readonly`
   - `https://www.googleapis.com/auth/drive.file`
5. Create OAuth client:
   - Application type: **Web application**
   - Add authorized redirect URIs
6. Download credentials JSON file

### Step 3: Connect to Notion

1. Create Notion integration (Settings > Integrations)
2. Get Internal Integration Token
3. Share relevant Notion pages/databases with integration
4. Build connector script or use automation platform

## Use Cases for Solopreneurs

### 1. Content Asset Library
**Scenario:** Maintain a searchable database of all your Google Drive files in Notion

**Setup:**
- Create Notion database with columns: File Name, Type, URL, Last Modified
- Sync Drive folder metadata to database
- Add tags and custom properties in Notion

**Benefits:** 
- Quick search across all assets
- Better organization with Notion's flexible views
- Track content usage and versions

### 2. Newsletter Draft Workflow
**Scenario:** Write drafts in Google Docs, then automatically import to Notion for publishing

**Setup:**
- Write in Google Docs with formatting
- Tag doc with "Ready for Notion"
- Auto-sync content to Notion page
- Review and publish to Substack

**Benefits:** 
- Use Google Docs' superior writing tools
- Keep all content in Notion's central hub
- Maintain version history in Drive

### 3. Client Deliverable Tracking
**Scenario:** Track all client files and share status in Notion

**Setup:**
- Store deliverables in Drive folder
- Sync file list to Notion client database
- Add columns: Status, Client Name, Deadline
- Auto-update when files change

**Benefits:**
- Single source of truth for client work
- Easy status reporting
- Never lose track of deliverables

### 4. Course Material Repository
**Scenario:** Organize course resources from Drive in Notion curriculum database

**Setup:**
- Store PDFs, videos, worksheets in Drive
- Link to Notion lessons database
- Display file previews in Notion
- Track student access and downloads

**Benefits:**
- Beautiful course presentation in Notion
- Reliable file hosting in Drive
- Easy content updates

## Automation Examples

### Sync New Drive Files
```javascript
const { google } = require('googleapis');
const { Client } = require('@notionhq/client');

const drive = google.drive({ version: 'v3', auth });
const notion = new Client({ auth: process.env.NOTION_TOKEN });

// Get files from Drive folder
const response = await drive.files.list({
  q: "'FOLDER_ID' in parents",
  fields: 'files(id, name, mimeType, modifiedTime, webViewLink)'
});

// Add to Notion database
for (const file of response.data.files) {
  await notion.pages.create({
    parent: { database_id: process.env.NOTION_DB_ID },
    properties: {
      'Name': { title: [{ text: { content: file.name } }] },
      'Type': { select: { name: file.mimeType.split('/')[1] } },
      'URL': { url: file.webViewLink },
      'Last Modified': { date: { start: file.modifiedTime } }
    }
  });
}
```

### Import Google Doc Content
```javascript
// Export Google Doc as markdown
const docContent = await drive.files.export({
  fileId: 'DOCUMENT_ID',
  mimeType: 'text/plain'
});

// Create Notion page with content
await notion.pages.create({
  parent: { database_id: process.env.NOTION_DB_ID },
  properties: {
    'Title': { title: [{ text: { content: docTitle } }] }
  },
  children: [
    {
      object: 'block',
      type: 'paragraph',
      paragraph: { rich_text: [{ text: { content: docContent.data } }] }
    }
  ]
});
```

### Backup Notion to Drive
```javascript
// Export Notion page as markdown
const blocks = await notion.blocks.children.list({ block_id: pageId });
const content = blocks.results.map(block => convertToMarkdown(block)).join('\n');

// Upload to Google Drive
await drive.files.create({
  requestBody: {
    name: `${notionPageTitle}.md`,
    parents: ['BACKUP_FOLDER_ID']
  },
  media: {
    mimeType: 'text/markdown',
    body: content
  }
});
```

## Best Practices

### For Content Creators
1. **Folder structure**: Mirror your Notion structure in Drive for consistency
2. **Naming conventions**: Use clear, searchable file names
3. **Regular syncs**: Schedule hourly/daily syncs for active projects
4. **Archive old files**: Move completed projects to archive folders

### File Management
1. **Use Drive for large files**: Keep videos, images, PDFs in Drive
2. **Embed vs Link**: Embed docs for viewing, link for editing
3. **Permission sync**: Match Drive sharing settings with Notion page access
4. **Version control**: Enable Drive version history for important docs

### Performance Optimization
1. **Incremental syncs**: Only sync changed files
2. **Batch operations**: Group API calls to reduce quota usage
3. **Cache metadata**: Store file info locally to reduce API calls
4. **Filter by folder**: Only sync specific Drive folders

## Native Notion Embeds

Notion supports embedding Google Drive files natively:

### Embed Google Docs
1. Open Google Doc
2. Click **Share** > **Copy link**
3. In Notion, type `/embed`
4. Paste Drive link
5. Click **Embed Link**

### Supported File Types
- ✅ Google Docs (full document view)
- ✅ Google Sheets (interactive spreadsheet)
- ✅ Google Slides (presentation viewer)
- ✅ PDFs (inline preview)
- ✅ Images (full display)
- ❌ Google Forms (link only)

## Advanced Workflows

### Content Pipeline Automation
1. Write article in Google Docs
2. Move to "Ready" folder
3. Auto-import to Notion
4. Trigger social media posts
5. Archive to "Published" folder

### Client Approval System
1. Create deliverable in Drive
2. Share link in Notion client database
3. Client updates status in Notion
4. Auto-notify you via Slack/email
5. Move to appropriate Drive folder

### Course Material Distribution
1. Upload resources to Drive
2. Sync to Notion course database
3. Students access via Notion portal
4. Track downloads and engagement
5. Update materials in Drive (auto-syncs)

## Troubleshooting

### Common Issues

**Problem:** "Access Denied" errors
- Verify OAuth scopes include required permissions
- Re-authenticate with Google account
- Check Drive file sharing settings

**Problem:** Files not syncing
- Confirm folder ID is correct
- Check API quota limits (10,000 requests/day free)
- Verify webhook is active

**Problem:** Embedded files not displaying
- Ensure Drive file is set to "Anyone with link can view"
- Use `/embed` command instead of paste
- Try refreshing Notion page

**Problem:** Slow sync performance
- Reduce sync frequency
- Limit to specific folders
- Use incremental updates only

## Security Considerations

### Protecting Your Data
- Never commit OAuth credentials to code repositories
- Use service accounts for automated scripts
- Enable 2FA on Google account
- Regularly audit integration permissions
- Revoke unused OAuth tokens

### Compliance
- GDPR: Ensure proper data handling if syncing client files
- Data residency: Consider where Drive stores files (regional)
- Backup strategy: Maintain separate backups beyond sync

## Cost Analysis

### Google Drive
- **Free:** 15 GB storage
- **Google One:** 100 GB for $1.99/month
- **API Quota:** 10,000 queries/day (free)
- **Beyond quota:** $4 per 10,000 queries

### Automation Options
- **Self-hosted:** Free (your time investment)
- **Zapier:** From $19.99/month (limited tasks)
- **Make (Integromat):** From $9/month (better value)
- **n8n:** Free (self-hosted)

### Solopreneur Recommendation
Start with native Notion embeds (free), then add automation only when manual workflows become bottlenecks.

## Resources
- [Google Drive API Documentation](https://developers.google.com/drive/api/guides/about-sdk)
- [Notion API Reference](https://developers.notion.com/)
- [OAuth 2.0 Setup Guide](https://developers.google.com/identity/protocols/oauth2)
- [Example Integration Code](https://github.com/googleapis/google-api-nodejs-client)

## Quick Win: No-Code Embed Method

**For immediate results without coding:**
1. Create your content in Google Docs/Sheets
2. Set sharing to "Anyone with link"
3. Copy the share link
4. In Notion, type `/embed` and paste link
5. Done! File displays inline with live updates

**Perfect for:** Newsletter drafts, budget spreadsheets, presentation decks, client deliverables
