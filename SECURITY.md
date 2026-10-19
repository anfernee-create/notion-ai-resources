# Security Policy

## Reporting a vulnerability

Please do not report security vulnerabilities through public issues.

Use GitHub private vulnerability reporting for this repository if it is enabled (Security tab -> Report a vulnerability). If that option is not available, open a public issue asking a maintainer to contact you, without including exploit details, secrets, or tokens.

Please include:

- A description of the issue and its impact
- Steps to reproduce, if safe to share privately
- Affected files, examples, or dependencies

## Secrets

Never commit Notion tokens, API keys, or other credentials. Examples must use environment variables such as `NOTION_TOKEN`, `NOTION_API_KEY`, and `NOTION_DATABASE_ID`. If a secret is accidentally committed or pasted into an issue or pull request, treat it as compromised and rotate it immediately.
