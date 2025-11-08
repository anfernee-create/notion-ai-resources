# Contributing to Notion AI Resources

🎉 First off, thank you for considering contributing to this project! 🎉

This repository thrives on community contributions. Whether you're adding prompts, creating templates, writing documentation, or fixing bugs, your help is appreciated!

## 📚 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

---

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

---

## 🚀 How Can I Contribute?

### 1. **Add New Prompts**

Share your best AI prompts!

**What we're looking for:**
- Tested and working prompts
- Clear descriptions and use cases
- Organized by category
- Well-formatted with examples

**How to contribute:**
1. Navigate to the appropriate category in `/prompts`
2. Add your prompt following the format
3. Include examples of expected output
4. Test your prompt before submitting

### 2. **Create Templates**

Build and share Notion templates!

**Template guidelines:**
- Should be production-ready
- Include setup instructions
- Provide screenshots or demos
- Explain the AI integration
- Share as duplicable link or instructions

**How to contribute:**
1. Create your template in Notion
2. Write comprehensive documentation
3. Add to relevant category in `/templates`
4. Include use cases and examples

### 3. **Write Documentation**

Help others learn!

**Documentation needs:**
- Beginner-friendly tutorials
- Advanced technique guides
- Best practices
- Troubleshooting tips
- API integration examples

### 4. **Add Code Examples**

Contribute API integration code!

**Code contribution guidelines:**
- Well-commented code
- Include dependencies/requirements
- Add usage examples
- Test before submitting
- Support multiple languages when possible

### 5. **Report Bugs**

Found an issue?

**Before reporting:**
- Check if it's already reported
- Verify it's reproducible
- Gather relevant information

**Bug report should include:**
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Environment details

### 6. **Suggest Enhancements**

Ideas for improvement?

**Enhancement suggestions:**
- Explain the problem it solves
- Describe the proposed solution
- Provide use cases
- Consider alternatives

---

## 🛠️ Getting Started

### Fork and Clone

```bash
# Fork this repository (click Fork button)

# Clone your fork
git clone https://github.com/YOUR-USERNAME/notion-ai-resources.git

# Navigate to directory
cd notion-ai-resources

# Add upstream remote
git remote add upstream https://github.com/anfernee-create/notion-ai-resources.git
```

### Create a Branch

```bash
# Create and checkout a new branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

### Make Your Changes

1. Add your content
2. Follow style guidelines
3. Test thoroughly
4. Update documentation if needed

---

## ✍️ Contribution Guidelines

### File Structure

**Prompts:**
```
prompts/
  ├── category/
  │   ├── specific-topic.md
  │   └── README.md
```

**Templates:**
```
templates/
  ├── category/
  │   ├── template-name.md
  │   ├── screenshots/
  │   └── README.md
```

**Documentation:**
```
docs/
  ├── category/
  │   ├── guide-name.md
  │   └── README.md
```

### Content Format

#### Prompts Format

```markdown
# [Prompt Title]

## Description
Brief description of what this prompt does.

## Use Cases
- When to use this prompt
- What problems it solves

## Prompt
\`\`\`
[Your prompt here with placeholders]
\`\`\`

## Variables
- `[VARIABLE]`: Description of what to replace

## Example
\`\`\`
Input: [example input]
Output: [example output]
\`\`\`

## Tips
- Best practices
- Common mistakes to avoid
```

#### Template Format

```markdown
# [Template Name]

## Overview
What this template does and who it's for.

## Features
- Key feature 1
- Key feature 2

## Setup Instructions
1. Step-by-step setup
2. Configuration details

## AI Integration
How AI is used in this template.

## Screenshots
![Description](path/to/screenshot.png)

## Get the Template
[Duplicate Link](notion-template-link)
```

---

## 🎨 Style Guidelines

### Markdown

- Use ATX-style headers (`#`)
- Include blank lines between sections
- Use fenced code blocks with language identifiers
- Add alt text to images
- Use relative links for internal references

### Writing Style

- **Clear and concise**: Get to the point
- **Beginner-friendly**: Explain technical terms
- **Action-oriented**: Use active voice
- **Consistent formatting**: Follow existing patterns
- **Proper grammar**: Proofread before submitting

### Code Style

**JavaScript:**
```javascript
// Use meaningful variable names
// Add comments for complex logic
// Follow ES6+ standards
```

**Python:**
```python
# Follow PEP 8 style guide
# Use type hints when appropriate
# Add docstrings for functions
```

---

## 📝 Commit Messages

### Format

```
<type>: <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Formatting changes
- **refactor**: Code refactoring
- **test**: Adding tests
- **chore**: Maintenance tasks

### Examples

**Good:**
```
feat: Add content generation prompts for social media

Added 15 new prompts for generating social media content
across different platforms (Twitter, LinkedIn, Instagram).

Closes #42
```

**Bad:**
```
Updated stuff
```

### Rules

- Use present tense ("Add feature" not "Added feature")
- Start with capital letter
- No period at the end of subject line
- Limit subject line to 50 characters
- Wrap body at 72 characters
- Reference issues and pull requests

---

## 📤 Pull Request Process

### Before Submitting

- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Follow style guidelines
- [ ] Check for typos and errors
- [ ] Add yourself to contributors list
- [ ] Ensure all files are properly formatted

### Submitting

1. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request:**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template

3. **PR Title Format:**
   ```
   [Type] Brief description
   ```
   Examples:
   - `[Feature] Add AI meeting notes template`
   - `[Fix] Correct typo in setup guide`
   - `[Docs] Update API integration examples`

4. **PR Description Should Include:**
   - What changes were made
   - Why these changes are needed
   - How to test the changes
   - Screenshots (if applicable)
   - Related issues

### Review Process

1. **Automated Checks**: Must pass all checks
2. **Maintainer Review**: At least one approval required
3. **Community Feedback**: Address comments and suggestions
4. **Final Review**: Maintainer will merge or request changes

### After Submission

- Respond to feedback promptly
- Make requested changes
- Update your PR branch if needed
- Be patient and respectful

---

## ❓ Questions?

### Need Help?

- **GitHub Discussions**: Ask questions
- **Issues**: Report problems
- **Discord**: Join our community (if available)

### Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## 🎖️ Recognition

Contributors will be:
- Added to CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation
- Featured in community showcases (optional)

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🚀 Quick Start Checklist

- [ ] Read this guide
- [ ] Fork the repository
- [ ] Create a branch
- [ ] Make your changes
- [ ] Follow style guidelines
- [ ] Test thoroughly
- [ ] Commit with clear messages
- [ ] Push to your fork
- [ ] Create Pull Request
- [ ] Respond to feedback

---

**Thank you for contributing to Notion AI Resources! 🎉**

Your contributions help thousands of people enhance their productivity with Notion AI.
