# Notion AI API Overview

A comprehensive guide to the Notion AI API integration for solopreneurs and developers.

## Introduction

The Notion AI API allows you to programmatically interact with Notion's powerful AI capabilities to automate workflows, enhance productivity, and build custom integrations.

## Key Features

### 1. Database Operations
- Query and filter databases
- Create, read, update, and delete pages
- Manage database properties and relations
- Bulk operations for efficiency

### 2. AI-Powered Content Generation
- Automated content creation
- Text summarization and rewriting
- Smart property suggestions
- Context-aware completions

### 3. Page Management
- Create and structure pages programmatically
- Update page properties and content
- Manage page hierarchies and relationships
- Archive and restore pages

### 4. Block Operations
- Append, update, and delete blocks
- Support for all block types (text, headers, lists, etc.)
- Nested block structures
- Rich text formatting

## API Architecture

### RESTful Design
The Notion AI API follows REST principles:
- Standard HTTP methods (GET, POST, PATCH, DELETE)
- JSON request/response format
- Consistent endpoint structure
- Proper status codes

### Base URL
```
https://api.notion.com/v1/
```

### Versioning
The API uses date-based versioning. Current stable version:
```
Notion-Version: 2022-06-28
```

## Authentication

All API requests require authentication using an integration token or OAuth 2.0. See the [Authentication Guide](./authentication.md) for detailed setup instructions.

## Rate Limits

- **Rate limit**: 3 requests per second per integration
- **Burst capacity**: Up to 50 requests within 10 seconds
- Rate limit headers included in all responses
- Exponential backoff recommended for retries

## Common Use Cases

### For Solopreneurs
1. **Content Management**
   - Auto-populate content calendars
   - Sync blog posts across platforms
   - Generate content ideas

2. **Task Automation**
   - Auto-assign tasks based on criteria
   - Update project statuses
   - Create recurring tasks

3. **Data Integration**
   - Sync CRM data
   - Import analytics
   - Connect with email tools

### For Developers
1. **Custom Integrations**
   - Build Notion bots
   - Create custom dashboards
   - Develop workflow automation

2. **Data Processing**
   - Batch operations
   - Data transformation
   - Real-time syncing

## Getting Started

1. **Create an Integration**
   - Go to [Notion Integrations](https://www.notion.so/my-integrations)
   - Click "New integration"
   - Configure capabilities and permissions
   - Copy your integration token

2. **Share Pages with Your Integration**
   - Open the page you want to access
   - Click "Share" → "Invite"
   - Select your integration

3. **Make Your First API Call**
   ```javascript
   const response = await fetch('https://api.notion.com/v1/databases/{database_id}/query', {
     method: 'POST',
     headers: {
       'Authorization': `Bearer ${NOTION_TOKEN}`,
       'Notion-Version': '2022-06-28',
       'Content-Type': 'application/json'
     }
   });
   ```

## Best Practices

### 1. Error Handling
- Always implement retry logic with exponential backoff
- Handle rate limit errors (429 status)
- Log errors for debugging
- Validate responses before processing

### 2. Performance
- Use batch operations when possible
- Implement caching for frequently accessed data
- Minimize API calls by fetching only needed properties
- Use pagination for large datasets

### 3. Security
- Never expose integration tokens in client-side code
- Use environment variables for sensitive data
- Rotate tokens regularly
- Implement proper access controls

### 4. Data Management
- Validate data before sending to API
- Handle edge cases (empty databases, missing properties)
- Implement data backup strategies
- Clean up unused integrations

## API Resources

### Core Endpoints
- **Databases**: `/v1/databases`
- **Pages**: `/v1/pages`
- **Blocks**: `/v1/blocks`
- **Users**: `/v1/users`
- **Search**: `/v1/search`

### Additional Resources
- [Official Notion API Documentation](https://developers.notion.com)
- [Authentication Guide](./authentication.md)
- [Endpoints Reference](./endpoints-reference.md)
- [Code Examples](../examples/)

## Support and Community

- **Official Support**: [Notion Help Center](https://www.notion.so/help)
- **Developer Forum**: [Notion Developers](https://developers.notion.com/community)
- **GitHub Issues**: Report bugs and request features
- **Stack Overflow**: Tag questions with `notion-api`

## Updates and Changelog

Stay informed about API changes:
- Subscribe to the [Notion Developers Newsletter](https://developers.notion.com/newsletter)
- Check the [Changelog](https://developers.notion.com/changelog)
- Follow [@NotionAPI](https://twitter.com/notionapi) on Twitter

## Next Steps

1. Review the [Authentication Guide](./authentication.md)
2. Explore [Code Examples](../examples/)
3. Check out [Endpoints Reference](./endpoints-reference.md)
4. Start building your integration!

---

**Need help?** Join our community or open an issue in the repository.


---

## Supplemental material merged from legacy `api/api-overview.md/api-overview.md`

> Preserved during repository restructuring on branch `fix/repo-improvements`. Headings were demoted to avoid duplicating the canonical document structure.

## Notion AI API Overview (supplemental)

### Introduction

The Notion API provides programmatic access to Notion databases, pages, and AI capabilities. This guide covers the essentials for integrating Notion AI into your applications.

### API Basics

#### Authentication

Notion uses bearer token authentication:

```bash
Authorization: Bearer YOUR_NOTION_API_KEY
```

#### Getting Your API Key

1. Go to Notion Settings & Members
2. Select Integrations
3. Create new integration
4. Copy the API key
5. Share database with integration

#### Rate Limits

| Tier | Requests/min | Burst |
|------|-------------|-------|
| Free | 3 | 5 |
| Paid | 20 | 30 |
| Enterprise | 100 | 150 |

### Base URL

```
https://api.notion.com/v1
```

### AI-Specific Endpoints

#### 1. Process AI Chat

**Endpoint:** `POST /pages/{page_id}/ai/chat`

**Description:** Send a message to Notion AI and get a response based on page content.

**Request:**
```json
{
  "message": "Summarize this page",
  "context": "page-content"
}
```

**Response:**
```json
{
  "response": "This page discusses...",
  "tokens_used": 150,
  "model": "gpt-4"
}
```

#### 2. Generate Database Summary

**Endpoint:** `POST /databases/{database_id}/ai/summarize`

**Description:** Generate AI summary of database records.

**Request:**
```json
{
  "property": "content",
  "filter": {
    "property": "status",
    "select": { "equals": "completed" }
  }
}
```

**Response:**
```json
{
  "summary": "Summary of completed items...",
  "items_processed": 25,
  "confidence_score": 0.95
}
```

#### 3. Extract Database Properties

**Endpoint:** `POST /databases/{database_id}/ai/extract`

**Description:** Extract structured data from unstructured content using AI.

**Request:**
```json
{
  "source_property": "content",
  "target_properties": [
    "sentiment",
    "key_topics",
    "action_items"
  ]
}
```

**Response:**
```json
{
  "extractions": [
    {
      "page_id": "abc123",
      "sentiment": "positive",
      "key_topics": ["AI", "API"],
      "action_items": ["Review docs", "Test integration"]
    }
  ]
}
```

### Common API Patterns

#### Pagination

```bash
GET /databases/{database_id}/query

{
  "start_cursor": "next_page_token_here",
  "page_size": 100
}
```

#### Filtering

```json
{
  "filter": {
    "and": [
      {
        "property": "status",
        "select": { "equals": "In Progress" }
      },
      {
        "property": "due_date",
        "date": { "before": "2024-12-31" }
      }
    ]
  }
}
```

#### Sorting

```json
{
  "sorts": [
    {
      "property": "created_time",
      "direction": "descending"
    }
  ]
}
```

### Error Handling

#### Status Codes

| Code | Meaning | Example |
|------|---------|----------|
| 200 | Success | Request completed |
| 400 | Bad Request | Invalid parameters |
| 401 | Unauthorized | Invalid API key |
| 403 | Forbidden | No access to resource |
| 404 | Not Found | Database doesn't exist |
| 429 | Rate Limited | Too many requests |
| 500 | Server Error | Notion service issue |

#### Error Response

```json
{
  "object": "error",
  "status": 400,
  "code": "validation_error",
  "message": "Filter properties must be valid database properties."
}
```

### Best Practices

#### 1. Authentication
- Store API keys securely (environment variables)
- Rotate keys regularly
- Use workspace level tokens for production
- Never commit keys to version control

#### 2. Rate Limiting
- Implement exponential backoff
- Cache responses when possible
- Batch requests
- Monitor rate limit headers

#### 3. Error Handling
- Retry on 429 (rate limit)
- Log 5xx errors
- Validate input before sending
- Handle connection timeouts

#### 4. AI API Specific
- Provide clear prompts
- Include context when available
- Validate AI output
- Monitor token usage

### Response Headers

```
X-RateLimit-Remaining: 19
X-RateLimit-Reset: 1637617452
X-Notion-Request-Id: abc-123-def-456
```

### Webhook Events (Premium)

Available events:
- `page.created`
- `page.updated`
- `page.deleted`
- `database_row.created`
- `database_row.updated`
- `database_row.deleted`

### API Versioning

- Current version: v1
- Version date: 2024-11-15
- Legacy versions: Deprecated

**Set version with:**
```
Notoin-Version: 2024-11-15
```

### Sandbox Environment

For testing:
```
https://sandbox.notion.com/v1
```

### Rate Limit Example

When you hit the rate limit:

```json
{
  "object": "error",
  "status": 429,
  "code": "rate_limited",
  "message": "You have exceeded the request rate limit.",
  "retry_after_seconds": 30
}
```

**Handling:**
```javascript
if (response.status === 429) {
  const retryAfter = response.json().retry_after_seconds;
  await sleep(retryAfter * 1000);
  retry();
}
```

### AI Capabilities

#### Content Generation
- Summarization
- Extraction
- Classification
- Sentiment analysis
- Translation

#### Supported Languages
- English
- Spanish
- French
- German
- Japanese
- Chinese

### Related Documentation

- [Authentication](./authentication.md)
- [Endpoints Reference](./endpoints-reference.md)
- [Code Examples](../examples/)
- [API Reference](https://developers.notion.com/reference)

---

**Last Updated:** November 2025
**API Version:** v1 (2024-11-15)
**Status:** Production Ready
