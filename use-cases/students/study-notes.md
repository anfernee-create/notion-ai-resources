# Note-Taking System for Students

Build a comprehensive, AI-powered study notes system in Notion that helps you capture, organize, recall, and synthesize knowledge from any subject.

## Overview

A well-designed Notion note-taking system transforms passive reading into active learning. By combining structured databases with Notion AI, you can automatically generate summaries, create flashcard-style review questions, and connect ideas across subjects.

## System Architecture

```
Courses Database
    └── Lectures/Readings
            └── Notes Database
                    ├── AI Summary
                    ├── AI Key Concepts
                    ├── AI Review Questions
                    └── AI Connections
```

## Setup

### 1. Courses Database

Track all your courses:
- **Course Name** (Title)
- **Semester** (Select)
- **Professor** (Text)
- **Grade** (Number)
- **Status** (Select) — Active / Completed

### 2. Notes Database

Capture lecture and reading notes:
- **Title** (Title) — lecture/chapter name
- **Course** (Relation) → Courses Database
- **Date** (Date)
- **Type** (Select) — Lecture / Reading / Lab / Discussion
- **Raw Notes** (Text) — your actual notes
- **AI Summary** (AI) — condensed version of your notes
- **AI Key Concepts** (AI) — bullet list of must-know concepts
- **AI Review Questions** (AI) — 5 questions to test understanding
- **AI Connections** (AI) — how this connects to previous notes

### 3. AI Prompts

**Summary:**
> "Summarize these study notes in 3-5 bullet points. Focus on the most important concepts and any formulas, definitions, or frameworks. Notes: {{Raw Notes}}"

**Key Concepts:**
> "Extract the 5-10 most important concepts from these notes. For each concept, provide: the term, a one-sentence definition, and why it matters. Notes: {{Raw Notes}}"

**Review Questions:**
> "Create 5 study questions based on these notes. Mix question types: definition, application, analysis, and comparison. Include answers. Notes: {{Raw Notes}}"

**Connections:**
> "What concepts from previous study sessions or general knowledge does this content connect to? Identify patterns, contradictions, or extensions. Notes: {{Raw Notes}}"

## Study Workflow

1. **Capture**: Take raw notes during class/reading
2. **Process**: Run AI to generate summaries and questions (same day)
3. **Review**: Use AI-generated questions for active recall
4. **Connect**: Review AI connections to build knowledge networks
5. **Synthesize**: Before exams, use AI to synthesize across lectures

## Exam Preparation

Use a filtered view: "Notes from [Course] in last 30 days"
1. Read all AI summaries in one session
2. Work through all AI review questions
3. Use Notion AI chat to ask questions about the material
4. Create a "Concept Map" page linking related ideas

## Related

- [Study Planner](study-planner.md)

---

*Last Updated: April 2026*
