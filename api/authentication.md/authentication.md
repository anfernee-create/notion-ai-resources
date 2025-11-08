# Notion AI API Authentication

## Overview

Authentication is required to access the Notion AI API securely. This guide covers all authentication methods, security best practices, and common scenarios.

## Authentication Methods

### 1. API Key (Bearer Token)

**Best For:** Server-to-server communication, automated scripts

**Setup:**
1. Go to Notion Settings & Members
2. Click Integrations
3. Create new integration
4. Name your integration (e.g., "AI Script")
5. Copy the API key
6. Share databases with integration

**Usage:**
```bash
Curl example:
curl -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Notion-Version: 2024-11-15" \
  https://api.notion.com/v1/databases
```

**Headers Required:**
- `Authorization: Bearer YOUR_API_KEY`
- `Notion-Version: 2024-11-15`

### 2. OAuth 2.0

**Best For:** User-facing applications, multi-user scenarios

**Flow:**
```
1. User clicks "Connect Notion"
2. Redirect to: https://api.notion.com/v1/oauth/authorize
3. User authenticates with Notion
4. Redirect back with auth code
5. Exchange code for access token
6. Use token for API calls
```

**Parameters:**
- `client_id`: Your integration ID
- `redirect_uri`: Your callback URL
- `response_type`: "code"
- `owner`: "user" or "workspace"

**Token Exchange:**
```bash
POST https://api.notion.com/v1/oauth/token

{
  "grant_type": "authorization_code",
  "code": "AUTH_CODE",
  "redirect_uri": "YOUR_REDIRECT_URI",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET"
}
```

**Response:**
```json
{
  "access_token": "secret_...",
  "token_type": "bearer",
  "bot_id": "abc123",
  "workspace_id": "def456"
}
```

## Token Security

### Storage Best Practices

**❌ NEVER:**
- Commit tokens to version control
- Store in frontend code
- Log tokens
- Share via email
- Embed in URLs

**✅ DO:**
- Use environment variables
- Store in secure vaults (AWS Secrets Manager, etc.)
- Rotate regularly (monthly)
- Use short-lived tokens
- Monitor token usage

### Environment Variables

```bash
# .env file (add to .gitignore)
NOTION_API_KEY=secret_abc123def456

# Usage in Python
import os
api_key = os.getenv('NOTION_API_KEY')

# Usage in Node.js
const apiKey = process.env.NOTION_API_KEY;
```

## Token Management

### Rotating Tokens

**When to rotate:**
- Monthly maintenance
- After security incident
- Employee departure
- End of project

**Process:**
1. Create new integration
2. Update applications with new token
3. Test thoroughly
4. Revoke old token
5. Document change

### Revoking Access

```
1. Go to Notion Settings & Members
2. Click Integrations
3. Find integration
4. Click delete/revoke
5. Confirm action
```

**Effects of revocation:**
- All API calls fail immediately
- Token is completely invalid
- Cannot be recovered
- Must create new integration to restore

## Error Responses

### 401 Unauthorized

```json
{
  "object": "error",
  "status": 401,
  "code": "unauthorized",
  "message": "API token is invalid."
}
```

**Solutions:**
- Check token is correct
- Verify token hasn't been revoked
- Ensure token has required permissions
- Check Authorization header format

### 403 Forbidden

```json
{
  "object": "error",
  "status": 403,
  "code": "restricted_resource",
  "message": "Integration does not have access to this resource."
}
```

**Solutions:**
- Share database with integration
- Check integration permissions
- Verify integration is active
- Ensure correct database ID

## Rate Limiting

### Limits by Plan

| Tier | Requests/sec | Daily Limit |
|------|-------------|-------------|
| Free | 0.2 | 1,000 |
| Pro | 1.0 | 10,000 |
| Team | 2.0 | 50,000 |
| Enterprise | 5.0 | Unlimited |

### Handling Rate Limits

```python
import time
import requests

def make_request_with_retry(url, headers, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 429:
            retry_after = int(response.headers.get('Retry-After', 60))
            print(f"Rate limited. Waiting {retry_after} seconds...")
            time.sleep(retry_after)
            continue
        
        return response
    
    raise Exception("Max retries exceeded")
```

## API Key Formats

**Bearer Token Format:**
```
Authorization: Bearer secret_abc123def456ghi789
```

**Prefix Meanings:**
- `secret_`: Long-lived API key
- `nap_`: Short-lived access token
- `bot_`: Bot user token (OAuth)

## Testing Authentication

### Simple Test

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Notion-Version: 2024-11-15" \
  https://api.notion.com/v1/users/me
```

**Expected Response:**
```json
{
  "object": "user",
  "id": "abc123",
  "type": "bot",
  "bot": {
    "owner": {
      "type": "workspace",
      "workspace": true
    }
  }
}
```

## Multi-Environment Setup

### Development
```python
if os.getenv('ENV') == 'development':
    api_key = os.getenv('NOTION_DEV_KEY')
    base_url = 'https://sandbox.notion.com/v1'
else:
    api_key = os.getenv('NOTION_PROD_KEY')
    base_url = 'https://api.notion.com/v1'
```

### Testing
```python
class MockNotionAPI:
    def __init__(self):
        self.calls = []
    
    def get(self, url, headers=None):
        self.calls.append({'method': 'GET', 'url': url})
        return {'status': 200, 'data': {}}
```

## Security Audit Checklist

- [ ] Token stored in environment variables
- [ ] No tokens in code/logs
- [ ] Token rotation schedule established
- [ ] Integration permissions minimal (least privilege)
- [ ] Only necessary databases shared
- [ ] Audit logging enabled
- [ ] Access monitoring in place
- [ ] Incident response plan ready
- [ ] Team trained on security
- [ ] Secrets vault configured

## Common Issues

### Issue: "Invalid API token"
**Cause:** Token is incorrect or revoked
**Fix:** Generate new token and verify format

### Issue: "Integration not found"
**Cause:** Integration doesn't exist or was deleted
**Fix:** Create new integration in Settings

### Issue: "Resource not shared"
**Cause:** Database not shared with integration
**Fix:** Share database in Notion settings

### Issue: Rate limited
**Cause:** Too many requests
**Fix:** Implement exponential backoff and caching

## Related Documentation

- [API Overview](./api-overview.md)
- [Endpoints Reference](./endpoints-reference.md)
- [Security Best Practices](https://developers.notion.com/docs/getting-started/page-limits)
- [OAuth Documentation](https://developers.notion.com/docs/getting-started/page-limits)

---

**Last Updated:** November 2025
**Status:** Current
**Support:** Email support@notion.com
