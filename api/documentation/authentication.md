
# Notion API Authentication

## Overview

The Notion API uses **Bearer token authentication** to secure all API requests. This guide covers everything you need to know about authenticating with the Notion API.

## Table of Contents

- [Authentication Methods](#authentication-methods)
- [Creating an Integration](#creating-an-integration)
- [Authorization Types](#authorization-types)
- [Using API Keys](#using-api-keys)
- [Security Best Practices](#security-best-practices)
- [Common Errors](#common-errors)

---

## Authentication Methods

Notion API supports two main authentication methods:

### 1. Internal Integrations
- **Use Case**: For personal use or internal tools
- **Access**: Limited to workspaces you have access to
- **Setup**: Simple, no OAuth flow required

### 2. Public Integrations (OAuth)
- **Use Case**: For public applications used by multiple workspaces
- **Access**: Users authorize your app via OAuth 2.0
- **Setup**: Requires OAuth 2.0 implementation

---

## Creating an Integration

### Step 1: Create a New Integration

1. Go to [Notion Integrations](https://www.notion.so/my-integrations)
2. Click **"+ New integration"**
3. Fill in the required information:
   - **Name**: Your integration name
   - **Logo**: Optional integration logo
   - **Associated workspace**: Select your workspace

### Step 2: Configure Capabilities

Choose what your integration can do:

- ✅ **Read content**: Query and retrieve data
- ✅ **Update content**: Modify existing pages/databases
- ✅ **Insert content**: Create new pages/databases
- ✅ **Read comments**: Access page comments
- ✅ **Insert comments**: Add new comments

### Step 3: Get Your Integration Token

After creation, you'll receive:
- **Internal Integration Token**: `secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
- This token is used in all API requests

---

## Authorization Types

### Internal Integration Token

```bash
Authorization: Bearer secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Example cURL Request:**

```bash
curl -X GET https://api.notion.com/v1/users/me \
  -H "Authorization: Bearer secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
  -H "Notion-Version: 2022-06-28"
```

### OAuth 2.0 (Public Integrations)

For public integrations, implement the OAuth 2.0 flow:

1. **Authorization Request**
```
https://api.notion.com/v1/oauth/authorize?
  client_id=YOUR_CLIENT_ID&
  response_type=code&
  owner=user&
  redirect_uri=YOUR_REDIRECT_URI
```

2. **Token Exchange**
```bash
curl -X POST https://api.notion.com/v1/oauth/token \
  -H "Content-Type: application/json" \
  -d '{
    "grant_type": "authorization_code",
    "code": "AUTHORIZATION_CODE",
    "redirect_uri": "YOUR_REDIRECT_URI"
  }'
```

---

## Using API Keys

### Environment Variables (Recommended)

**Node.js / JavaScript:**
```javascript
// .env file
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

// In your code
const { Client } = require('@notionhq/client');

const notion = new Client({
  auth: process.env.NOTION_TOKEN,
});
```

**Python:**
```python
# .env file
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# In your code
import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])
```

**PHP:**
```php
// .env file
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

// In your code
$token = getenv('NOTION_TOKEN');
$headers = [
    'Authorization: Bearer ' . $token,
    'Notion-Version: 2022-06-28',
    'Content-Type: application/json'
];
```

### Sharing Pages with Your Integration

⚠️ **Important**: After creating an integration, you must explicitly share pages/databases with it.

1. Open the page or database
2. Click **"Share"** or **"•••"** menu
3. Select **"Add connections"**
4. Choose your integration
5. Click **"Invite"**

---

## Security Best Practices

### ✅ Do's

1. **Store tokens securely**
   - Use environment variables
   - Never commit tokens to version control
   - Use `.env` files (add to `.gitignore`)

2. **Rotate tokens regularly**
   - Regenerate tokens periodically
   - Update all services using the old token

3. **Use HTTPS only**
   - All API requests must use HTTPS
   - Never send tokens over HTTP

4. **Implement rate limiting**
   - Respect Notion's rate limits (3 requests/second)
   - Implement exponential backoff

5. **Minimal permissions**
   - Only grant necessary capabilities
   - Use read-only access when possible

### ❌ Don'ts

1. **Never hardcode tokens**
   ```javascript
   // ❌ BAD
   const token = 'secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx';
   ```

2. **Don't expose tokens in client-side code**
   - Never include tokens in frontend JavaScript
   - Always use backend/server-side authentication

3. **Don't share tokens publicly**
   - Keep tokens out of screenshots
   - Don't post tokens in forums/support tickets

4. **Don't use tokens in URLs**
   ```bash
   # ❌ BAD
   https://api.notion.com/v1/pages?token=secret_xxx
   ```

---

## Common Errors

### 401 Unauthorized

**Error:**
```json
{
  "object": "error",
  "status": 401,
  "code": "unauthorized",
  "message": "API token is invalid."
}
```

**Solutions:**
- Verify your token is correct
- Check token hasn't been revoked
- Ensure proper `Authorization` header format

### 403 Forbidden

**Error:**
```json
{
  "object": "error",
  "status": 403,
  "code": "restricted_resource",
  "message": "The integration does not have permission to perform this action."
}
```

**Solutions:**
- Share the page/database with your integration
- Grant necessary capabilities in integration settings
- Check workspace permissions

### Missing Notion-Version Header

**Error:**
```json
{
  "object": "error",
  "status": 400,
  "code": "validation_error",
  "message": "Notion-Version header is required."
}
```

**Solution:**
Always include the Notion-Version header:
```bash
Notion-Version: 2022-06-28
```

---

## Testing Your Authentication

### Quick Test: Get Current User

**cURL:**
```bash
curl -X GET https://api.notion.com/v1/users/me \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Notion-Version: 2022-06-28"
```

**Expected Response:**
```json
{
  "object": "user",
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
  "type": "bot",
  "name": "Your Integration Name",
  "avatar_url": null
}
```

---

## Additional Resources

- [Official Notion API Documentation](https://developers.notion.com/reference/authentication)
- [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js)
- [Notion SDK for Python](https://github.com/ramnes/notion-sdk-py)
- [API Reference](./endpoints-reference.md)
- [API Overview](./api-overview.md)

---

## Support

If you encounter authentication issues:

1. Check [Notion API Status](https://status.notion.so/)
2. Review [Notion Developer Community](https://developers.notion.com/)
3. Post in [GitHub Issues](https://github.com/anfernee-create/notion-ai-resources/issues)

---

**Last Updated:** December 2025


---

## Supplemental material merged from legacy `api/authentication.md/authentication.md`

> Preserved during repository restructuring on branch `fix/repo-improvements`. Headings were demoted to avoid duplicating the canonical document structure.

## Notion AI API Authentication (supplemental)

### Overview

Authentication is required to access the Notion AI API securely. This guide covers all authentication methods, security best practices, and common scenarios.

### Authentication Methods

#### 1. API Key (Bearer Token)

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

#### 2. OAuth 2.0

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

### Token Security

#### Storage Best Practices

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

#### Environment Variables

```bash
## .env file (add to .gitignore) (supplemental)
NOTION_API_KEY=secret_abc123def456

## Usage in Python (supplemental)
import os
api_key = os.getenv('NOTION_API_KEY')

## Usage in Node.js (supplemental)
const apiKey = process.env.NOTION_API_KEY;
```

### Token Management

#### Rotating Tokens

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

#### Revoking Access

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

### Error Responses

#### 401 Unauthorized

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

#### 403 Forbidden

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

### Rate Limiting

#### Limits by Plan

| Tier | Requests/sec | Daily Limit |
|------|-------------|-------------|
| Free | 0.2 | 1,000 |
| Pro | 1.0 | 10,000 |
| Team | 2.0 | 50,000 |
| Enterprise | 5.0 | Unlimited |

#### Handling Rate Limits

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

### API Key Formats

**Bearer Token Format:**
```
Authorization: Bearer secret_abc123def456ghi789
```

**Prefix Meanings:**
- `secret_`: Long-lived API key
- `nap_`: Short-lived access token
- `bot_`: Bot user token (OAuth)

### Testing Authentication

#### Simple Test

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

### Multi-Environment Setup

#### Development
```python
if os.getenv('ENV') == 'development':
    api_key = os.getenv('NOTION_DEV_KEY')
    base_url = 'https://sandbox.notion.com/v1'
else:
    api_key = os.getenv('NOTION_PROD_KEY')
    base_url = 'https://api.notion.com/v1'
```

#### Testing
```python
class MockNotionAPI:
    def __init__(self):
        self.calls = []
    
    def get(self, url, headers=None):
        self.calls.append({'method': 'GET', 'url': url})
        return {'status': 200, 'data': {}}
```

### Security Audit Checklist

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

### Common Issues

#### Issue: "Invalid API token"
**Cause:** Token is incorrect or revoked
**Fix:** Generate new token and verify format

#### Issue: "Integration not found"
**Cause:** Integration doesn't exist or was deleted
**Fix:** Create new integration in Settings

#### Issue: "Resource not shared"
**Cause:** Database not shared with integration
**Fix:** Share database in Notion settings

#### Issue: Rate limited
**Cause:** Too many requests
**Fix:** Implement exponential backoff and caching

### Related Documentation

- [API Overview](./api-overview.md)
- [Endpoints Reference](./endpoints-reference.md)
- [Security Best Practices](https://developers.notion.com/docs/getting-started/page-limits)
- [OAuth Documentation](https://developers.notion.com/docs/getting-started/page-limits)

---

**Last Updated:** November 2025
**Status:** Current
**Support:** Email support@notion.com
