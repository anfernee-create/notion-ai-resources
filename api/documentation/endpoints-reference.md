# Notion AI API Endpoints Reference

Complete reference for all Notion AI API endpoints with examples for solopreneurs and developers.

## Base URL

```
https://api.notion.com/v1/
```

## Required Headers

All requests require:
```http
Authorization: Bearer YOUR_TOKEN
Notion-Version: 2022-06-28
Content-Type: application/json
```

---

## Pages

### Retrieve a Page
Get page property values.

**Endpoint:** `GET /pages/{page_id}`

**Example:**
```javascript
const response = await notion.pages.retrieve({
  page_id: 'PAGE_ID',
});
```

### Create a Page
Create a new page in a database or as a child page.

**Endpoint:** `POST /pages`

**Body:**
```json
{
  "parent": { "database_id": "DATABASE_ID" },
  "properties": {
    "Name": {
      "title": [{ "text": { "content": "My Page" } }]
    }
  }
}
```

### Update Page Properties
Update page property values.

**Endpoint:** `PATCH /pages/{page_id}`

---

## Databases

### Query a Database
Retrieve database entries with filters and sorts.

**Endpoint:** `POST /databases/{database_id}/query`

**Body:**
```json
{
  "filter": {
    "property": "Status",
    "select": { "equals": "Done" }
  },
  "sorts": [{
    "property": "Created",
    "direction": "descending"
  }]
}
```

### Create a Database
Create a new database.

**Endpoint:** `POST /databases`

---

## Blocks

### Retrieve Block Children
Get child blocks.

**Endpoint:** `GET /blocks/{block_id}/children`

### Append Block Children
Add content to a page.

**Endpoint:** `PATCH /blocks/{block_id}/children`

**Body:**
```json
{
  "children": [
    {
      "object": "block",
      "type": "paragraph",
      "paragraph": {
        "rich_text": [{ "text": { "content": "Hello World" } }]
      }
    }
  ]
}
```

---

## Users

### Retrieve a User
Get user details.

**Endpoint:** `GET /users/{user_id}`

### List All Users
Get workspace users.

**Endpoint:** `GET /users`

---

## Search

### Search
Search pages and databases.

**Endpoint:** `POST /search`

**Body:**
```json
{
  "query": "marketing",
  "filter": { "property": "object", "value": "page" }
}
```

---

## Filter Operations

### Text Filters
- `equals`, `does_not_equal`
- `contains`, `does_not_contain`
- `starts_with`, `ends_with`
- `is_empty`, `is_not_empty`

### Number Filters
- `equals`, `does_not_equal`
- `greater_than`, `less_than`
- `greater_than_or_equal_to`, `less_than_or_equal_to`

### Date Filters
- `equals`, `before`, `after`
- `on_or_before`, `on_or_after`
- `past_week`, `past_month`, `past_year`
- `next_week`, `next_month`, `next_year`

---

## Rate Limits

- **3 requests per second** per integration
- Rate limit headers in response
- Implement exponential backoff

---

## Error Codes

| Code | Meaning |
|------|---------|  
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 429 | Rate Limited |
| 500 | Internal Error |

---

## Resources

- [API Overview](./api-overview.md)
- [Authentication](./authentication.md)
- [Code Examples](../examples/)
- [Official Docs](https://developers.notion.com/reference)

---

**Note:** This is a quick reference. See official docs for complete details.
