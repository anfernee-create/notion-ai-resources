# Zapier Integration Guide for Notion AI

## Overview
Zapier connects Notion with 7000+ apps enabling powerful automations. This guide covers common Notion + AI workflows.

## Authentication Setup

### 1. Connect Notion to Zapier
- Create Zapier account
- Search for Notion app
- Click Connect
- Copy Integration Token from Notion Settings
- Paste token in Zapier
- Select your workspace and databases

### 2. Connect AI Tools
- ChatGPT: Use OpenAI API key
- Claude: Use Anthropic API key
- Other tools: Follow Zapier app documentation

## Common Workflows

### Email to Notion
**Trigger**: New email received
**Action**: Create Notion database entry
Use case: Capture emails as tasks or notes

### Slack to Notion
**Trigger**: Message posted in channel
**Action**: Create task/note in database
Use case: Team updates logged automatically

### Google Forms to Notion
**Trigger**: New form submission
**Action**: Add row to database
Use case: Survey responses captured

### Scheduled AI Summarization
**Trigger**: Daily at 9 AM
**Action**: Generate summary with ChatGPT
**Action**: Create note in Notion
Use case: Daily digest of tasks

## Advanced Automation Ideas

### Content Creation Pipeline
1. New blog post idea in Notion
2. ChatGPT generates outline
3. Claude expands to draft
4. Update status in Notion
5. Send to Slack for review

### Customer Feedback Loop
1. Stripe receives customer feedback
2. Zapier captures and creates ticket
3. ChatGPT categorizes sentiment
4. Creates Notion database entry
5. Sends alert to team

### Meeting Automation
1. Google Calendar event created
2. Zapier extracts details
3. Creates Notion prep page
4. Sends reminders via Slack
5. Logs notes after meeting

## Code Templates

### JavaScript Webhook
```javascript
const zapierWebhook = async (data) => {
  const response = await fetch(process.env.ZAPIER_WEBHOOK_URL, {
    method: 'POST',
    body: JSON.stringify(data)
  });
  return response.json();
};
```

### Python Integration
```python
import requests

def send_to_zapier(webhook_url, data):
    response = requests.post(webhook_url, json=data)
    return response.status_code
```

## Troubleshooting

**Q: Zapier disconnects from Notion**
A: Regenerate Integration Token in Notion Settings

**Q: Data not syncing**
A: Check database permissions, verify field names match

**Q: Rate limiting errors**
A: Add delays between actions, use batching
