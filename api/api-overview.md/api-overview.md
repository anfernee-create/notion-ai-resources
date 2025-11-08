# Notion AI API Overview

## Introduction

The Notion API provides programmatic access to Notion databases, pages, and AI capabilities. This guide covers the essentials for integrating Notion AI into your applications.

## API Basics

### Authentication

Notion uses bearer token authentication:

```bash
Authorization: Bearer YOUR_NOTION_API_KEY
```

### Getting Your API Key

1. Go to Notion Settings & Members
2. Select Integrations
3. Create new integration
4. Copy the API key
5. Share database with integration

### Rate Limits

| Tier | Requests/min | Burst |
|------|-------------|-------|
| Free | 3 | 5 |
| Paid | 20 | 30 |
| Enterprise | 100 | 150 |

## Base URL

```
https://api.notion.com/v1
```

## AI-Specific Endpoints

### 1. Process AI Chat

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

### 2. Generate Database Summary

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

### 3. Extract Database Properties

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

## Common API Patterns

### Pagination

```bash
GET /databases/{database_id}/query

{
  "start_cursor": "next_page_token_here",
  "page_size": 100
}
```

### Filtering

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

### Sorting

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

## Error Handling

### Status Codes

| Code | Meaning | Example |
|------|---------|----------|
| 200 | Success | Request completed |
| 400 | Bad Request | Invalid parameters |
| 401 | Unauthorized | Invalid API key |
| 403 | Forbidden | No access to resource |
| 404 | Not Found | Database doesn't exist |
| 429 | Rate Limited | Too many requests |
| 500 | Server Error | Notion service issue |

### Error Response

```json
{
  "object": "error",
  "status": 400,
  "code": "validation_error",
  "message": "Filter properties must be valid database properties."
}
```

## Best Practices

### 1. Authentication
- Store API keys securely (environment variables)
- Rotate keys regularly
- Use workspace level tokens for production
- Never commit keys to version control

### 2. Rate Limiting
- Implement exponential backoff
- Cache responses when possible
- Batch requests
- Monitor rate limit headers

### 3. Error Handling
- Retry on 429 (rate limit)
- Log 5xx errors
- Validate input before sending
- Handle connection timeouts

### 4. AI API Specific
- Provide clear prompts
- Include context when available
- Validate AI output
- Monitor token usage

## Response Headers

```
X-RateLimit-Remaining: 19
X-RateLimit-Reset: 1637617452
X-Notion-Request-Id: abc-123-def-456
```

## Webhook Events (Premium)

Available events:
- `page.created`
- `page.updated`
- `page.deleted`
- `database_row.created`
- `database_row.updated`
- `database_row.deleted`

## API Versioning

- Current version: v1
- Version date: 2024-11-15
- Legacy versions: Deprecated

**Set version with:**
```
Notoin-Version: 2024-11-15
```

## Sandbox Environment

For testing:
```
https://sandbox.notion.com/v1
```

## Rate Limit Example

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

## AI Capabilities

### Content Generation
- Summarization
- Extraction
- Classification
- Sentiment analysis
- Translation

### Supported Languages
- English
- Spanish
- French
- German
- Japanese
- Chinese

## Related Documentation

- [Authentication](./authentication.md)
- [Endpoints Reference](./endpoints-reference.md)
- [Code Examples](../examples/)
- [API Reference](https://developers.notion.com/reference)

---

**Last Updated:** November 2025
**API Version:** v1 (2024-11-15)
**Status:** Production Ready
