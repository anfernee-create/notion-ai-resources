
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
3. Post in [GitHub Discussions](../../discussions)

---

**Last Updated:** December 2025
