# Notion API Integration Tutorial

> **Intermediate Tutorial** | Estimated time: 45-60 minutes | Prerequisites: Database Setup, basic JavaScript or Python knowledge

## Overview

The Notion API allows you to read from and write to your Notion workspace programmatically. This tutorial covers authentication, making your first API calls, and practical patterns for integrating external systems with your Notion AI workflows.

---

## Why Use the API?

The Notion API unlocks capabilities that are not possible through the UI alone:

- **Bulk operations** — Create or update hundreds of database records at once
- **External triggers** — Start Notion workflows from webhooks, cron jobs, or other apps
- **Custom integrations** — Connect services that don't have native Notion connectors
- **Data pipelines** — Pull data from external APIs and push it into Notion databases
- **Advanced automation** — Logic that's too complex for Notion's built-in automation conditions

---

## Part 1: Getting Your API Token

### Step 1: Create an Integration

1. Go to https://www.notion.so/my-integrations
2. Click "+ New integration"
3. Give it a name (e.g., "My Workflow Bot")
4. Select the workspace it should access
5. Set capabilities: Read content, Update content, Insert content
6. Click Submit

You will receive an **Internal Integration Secret** — this is your API token. Store it securely (never commit it to a public repository).

### Step 2: Share a Database with Your Integration

The API can only access databases you explicitly share with your integration:

1. Open the Notion database you want to access
2. Click the "..." menu at the top right of the page
3. Select "Connections" (or "Add connections")
4. Find your integration by name and click to add it

---

## Part 2: Your First API Call

### Setup (JavaScript / Node.js)

Install the official Notion SDK:

```bash
npm install @notionhq/client
```

Create a file called `notion-test.js`:

```javascript
const { Client } = require('@notionhq/client');

const notion = new Client({
  auth: process.env.NOTION_TOKEN, // set via environment variable
});

async function testConnection() {
  const response = await notion.users.me();
  console.log('Connected as:', response.name);
}

testConnection();
```

Run it:
```bash
NOTION_TOKEN=your_token_here node notion-test.js
```

### Setup (Python)

Install the SDK:
```bash
pip install notion-client
```

```python
import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

# Test connection
user = notion.users.me()
print(f"Connected as: {user['name']}")
```

---

## Part 3: Querying a Database

### Get All Records from a Database

You will need your database ID — find it in the database URL:
`https://notion.so/your-workspace/DATABASE_ID?v=...`

**JavaScript:**
```javascript
async function queryDatabase(databaseId) {
  const response = await notion.databases.query({
    database_id: databaseId,
    filter: {
      property: 'Status',
      select: {
        equals: 'In Progress'
      }
    },
    sorts: [
      {
        property: 'Priority',
        direction: 'descending'
      }
    ]
  });
  return response.results;
}
```

**Python:**
```python
def query_database(database_id):
    response = notion.databases.query(
        database_id=database_id,
        filter={
            "property": "Status",
            "select": {"equals": "In Progress"}
        }
    )
    return response["results"]
```

---

## Part 4: Creating and Updating Records

### Create a New Database Record

```javascript
async function createRecord(databaseId, title, status, priority) {
  const response = await notion.pages.create({
    parent: { database_id: databaseId },
    properties: {
      'Name': {
        title: [{ text: { content: title } }]
      },
      'Status': {
        select: { name: status }
      },
      'Priority': {
        select: { name: priority }
      }
    }
  });
  return response;
}
```

### Update an Existing Record

```javascript
async function updateRecord(pageId, newStatus) {
  const response = await notion.pages.update({
    page_id: pageId,
    properties: {
      'Status': {
        select: { name: newStatus }
      }
    }
  });
  return response;
}
```

---

## Part 5: Practical Integration Pattern

### Webhook-to-Notion Pipeline

This pattern receives data from any external webhook and creates Notion records:

```javascript
const express = require('express');
const { Client } = require('@notionhq/client');

const app = express();
const notion = new Client({ auth: process.env.NOTION_TOKEN });
const DATABASE_ID = process.env.NOTION_DATABASE_ID;

app.use(express.json());

app.post('/webhook', async (req, res) => {
  const { title, description, source } = req.body;
  
  try {
    await notion.pages.create({
      parent: { database_id: DATABASE_ID },
      properties: {
        'Name': { title: [{ text: { content: title } }] },
        'Description': { rich_text: [{ text: { content: description } }] },
        'Source': { select: { name: source } },
        'Status': { select: { name: 'New' } },
        'Created At': { date: { start: new Date().toISOString() } }
      }
    });
    res.status(200).json({ success: true });
  } catch (error) {
    console.error('Error creating Notion record:', error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(3000, () => console.log('Webhook listener running on port 3000'));
```

Deploy this to any hosting platform (Railway, Render, Fly.io) and point external webhooks to your URL.

---

## Part 6: Rate Limits and Best Practices

### Rate Limits

The Notion API has a rate limit of 3 requests per second. For bulk operations:

- Add a delay between requests: `await new Promise(r => setTimeout(r, 334))`
- Use exponential backoff when you receive a 429 (rate limit) error
- For very large operations (1000+ records), batch overnight or use a queue

### Error Handling

Always wrap API calls in try-catch blocks and handle these common errors:

- **400 Bad Request** — Check your property names match exactly (case-sensitive)
- **401 Unauthorized** — Your token is invalid or expired
- **403 Forbidden** — The database hasn't been shared with your integration
- **404 Not Found** — Double-check the database ID
- **429 Too Many Requests** — Slow down your request rate

### Security Best Practices

- Store API tokens in environment variables, never in source code
- Use separate integrations for dev and production environments
- Audit your integration's database access quarterly
- Rotate API tokens if you suspect they have been compromised

---

## Next Steps

- [Custom Workflows](custom-workflows.md) - Build UI-based workflows that complement your API integrations
- [AI Agent Development](../advanced/ai-agent-development.md) - Use the API to power advanced AI agents
- [API Examples](../../api/examples/) - Browse ready-to-use code samples in JavaScript, Python, and PHP

---

*Last Updated: April 2026 | [Report an issue](https://github.com/anfernee-create/notion-ai-resources/issues)*
