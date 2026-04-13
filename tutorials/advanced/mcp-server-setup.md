# MCP Server Setup for Notion AI

> **Advanced Tutorial** | Estimated time: 45-60 minutes | Prerequisites: Node.js installed, Notion API access, AI Agent Development tutorial

## Overview

The Model Context Protocol (MCP) allows you to connect Notion AI to external tools, databases, and services beyond the built-in AI Connectors. This tutorial walks you through setting up an MCP server that extends your Notion AI agents with custom capabilities.

---

## What is MCP?

The Model Context Protocol is an open standard that enables AI assistants to securely connect with external data sources and tools. For Notion AI, MCP servers allow your agents to:

- Access data from any external API or database
- Execute custom business logic
- Interact with internal tools not covered by native connectors
- Build proprietary integrations without exposing credentials

---

## Prerequisites

Before starting, ensure you have:

1. Node.js 18 or later installed
2. A Notion API integration token (from https://www.notion.so/my-integrations)
3. Access to Notion AI (Business or Enterprise plan)
4. Basic familiarity with the command line and JSON

---

## Part 1: Understanding the MCP Architecture

An MCP setup for Notion consists of three components:

**MCP Server** - A lightweight Node.js (or Python) process that you run locally or on a server. It exposes tools and resources that AI agents can call.

**MCP Client** - The Notion AI agent that connects to your server and calls its tools during a workflow.

**Transport Layer** - The communication channel between client and server (stdio for local, HTTP/SSE for remote).

---

## Part 2: Setting Up Your First MCP Server

### Step 1: Initialize the Project

Create a new directory and initialize a Node.js project:

```bash
mkdir notion-mcp-server
cd notion-mcp-server
npm init -y
npm install @modelcontextprotocol/sdk
```

### Step 2: Create the Server File

Create a file called `server.js` with the following structure:

```javascript
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';

const server = new Server(
  { name: 'notion-mcp-server', version: '1.0.0' },
  { capabilities: { tools: {} } }
);

// Define a tool your Notion AI agent can call
server.setRequestHandler('tools/list', async () => ({
  tools: [
    {
      name: 'get_crm_data',
      description: 'Retrieve customer data from the internal CRM',
      inputSchema: {
        type: 'object',
        properties: {
          customer_id: { type: 'string', description: 'The customer ID to look up' }
        },
        required: ['customer_id']
      }
    }
  ]
}));

// Handle tool calls
server.setRequestHandler('tools/call', async (request) => {
  if (request.params.name === 'get_crm_data') {
    const { customer_id } = request.params.arguments;
    // Replace with your actual CRM API call
    const data = await fetchFromCRM(customer_id);
    return { content: [{ type: 'text', text: JSON.stringify(data) }] };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

### Step 3: Test the Server Locally

Run the server and verify it starts without errors:

```bash
node server.js
```

You should see the server waiting for connections on stdio.

---

## Part 3: Connecting to Notion AI

### Step 1: Register the MCP Server

In your Notion workspace, navigate to **Settings > AI > MCP Servers** and add your server:

- **Name**: Give it a descriptive name (e.g., "Internal CRM Connector")
- **Command**: `node /path/to/your/notion-mcp-server/server.js`
- **Environment Variables**: Add any API keys your server needs (stored securely)

### Step 2: Grant Permissions

After registering, specify which AI agents or automation workflows are allowed to use this server. Apply the principle of least privilege — only grant access to agents that need it.

### Step 3: Test the Connection

Create a test Notion page with an AI block and ask it to use your custom tool. For example: "Use the CRM connector to look up customer C-12345 and summarize their recent activity."

---

## Part 4: Common MCP Server Patterns

### Pattern 1: Database Bridge

Connect Notion AI to any SQL or NoSQL database. The MCP server handles authentication and query translation, while the AI agent focuses on what data to retrieve and how to use it.

### Pattern 2: Internal API Gateway

Expose internal microservices or REST APIs to your AI agents through the MCP server, without needing to create individual Notion integrations for each service.

### Pattern 3: Computation Engine

Offload complex calculations (financial modeling, data analysis, ML inference) to the MCP server, returning clean results for the AI agent to interpret and summarize.

### Pattern 4: File System Access

Allow agents to read from shared network drives or cloud storage beyond what native connectors support (e.g., reading Excel files, processing CSVs, scanning directories).

---

## Part 5: Security Best Practices

**Authentication** - Always validate that requests come from authorized Notion AI agents. Use environment variables for secrets, never hardcode credentials.

**Input Validation** - Sanitize all inputs from the AI agent before using them in queries or API calls. The AI may generate unexpected parameter values.

**Rate Limiting** - Implement rate limiting on your MCP server to prevent runaway agents from overwhelming downstream services.

**Audit Logging** - Log all tool calls with timestamps, inputs, and outputs. This is essential for debugging agent behavior and compliance.

**Network Security** - If running the server remotely, use HTTPS and restrict access by IP range or VPN.

---

## Part 6: Deploying to Production

For production use, run your MCP server as a managed process:

### Using PM2 (Node.js)

```bash
npm install -g pm2
pm2 start server.js --name notion-mcp
pm2 save
pm2 startup
```

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
CMD ["node", "server.js"]
```

Deploy to your preferred container platform (Railway, Fly.io, AWS ECS, etc.).

---

## Troubleshooting

| Problem | Likely Cause | Solution |
|---|---|---|
| Server not connecting | Path or command incorrect | Double-check the command path in Notion Settings |
| Tools not appearing in agent | Server not returning tools/list correctly | Test the server with MCP Inspector CLI tool |
| Tool calls returning errors | Input validation failing | Add console.error logging and check server logs |
| Agent ignores the tool | Tool description too vague | Rewrite the description to be more specific about when to use it |

---

## Next Steps

- [AI Agent Development](ai-agent-development.md) - Build the agents that will use your MCP server
- [Complex Automations](complex-automations.md) - Combine MCP tools with multi-step workflows
- [API Integration Tutorial](../intermediate/api-integration.md) - Learn the Notion API fundamentals

---

*Last Updated: April 2026 | Contribute improvements via [GitHub Issues](https://github.com/anfernee-create/notion-ai-resources/issues)*
