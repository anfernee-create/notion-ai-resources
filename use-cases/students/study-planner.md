# Student Study Planner Use Case

## Overview
A comprehensive Notion system designed for students to organize coursework, manage deadlines, track grades, and optimize study habits. Perfect for managing multiple courses, assignments, exams, and long-term learning goals.

## Core Databases

### Courses Database
- **Properties:**
  - Course Name (Title)
  - Course Code (Text)
  - Instructor Name (Text)
  - Meeting Times (Rich text)
  - Location/Link (Text)
  - Credit Hours (Number)
  - Grade Weight (Number)
  - Current Grade (Number)
  - Grade History (Relation)
  - Assignments (Relation)
  - Exams (Relation)
  - Resources (Relation)
  - Status (Select: Active, Completed, Dropped)

### Assignments Database
- **Properties:**
  - Assignment Name (Title)
  - Course (Relation)
  - Type (Select: Essay, Problem Set, Project, Reading, Discussion, Other)
  - Description (Rich text)
  - Due Date (Date)
  - Due Time (Text)
  - Points Possible (Number)
  - Points Earned (Number)
  - Grade % (Formula)
  - Status (Select: Not Started, In Progress, Submitted, Graded)
  - Submission Link (URL)
  - Rubric (Attachment)
  - Feedback (Rich text)
  - Study Materials (Relation)
  - Priority (Select: High, Medium, Low)
  - Estimated Hours (Number)
  - Actual Hours (Number)

### Exams Database
- **Properties:**
  - Exam Name (Title)
  - Course (Relation)
  - Exam Type (Select: Midterm, Final, Quiz, Practical)
  - Date (Date)
  - Time (Text)
  - Duration (Number - minutes)
  - Location/Link (Text)
  - Topics (Multi-select)
  - Score (Number)
  - Possible Points (Number)
  - Grade % (Formula)
  - Notes (Rich text)
  - Study Guide (Attachment)
  - Practice Problems (Relation to Resources)
  - Study Sessions (Relation)

### Study Materials Database
- **Properties:**
  - Title (Title)
  - Course (Relation)
  - Material Type (Select: Textbook, Lecture Notes, Video, Article, Problem Set, Practice Exam)
  - Content/Link (Rich text or URL)
  - Topic (Text)
  - Difficulty (Select: Beginner, Intermediate, Advanced)
  - Last Reviewed (Date)
  - Usefulness Rating (Select: 1-5 stars)
  - Tags (Multi-select)
  - Attachments (Files)

### Study Sessions Database
- **Properties:**
  - Date (Date)
  - Course (Relation)
  - Topic (Text)
  - Duration (Number - minutes)
  - Material Covered (Relation to Study Materials)
  - Notes (Rich text)
  - Questions (Rich text)
  - Effectiveness (Select: Very Effective, Effective, Neutral, Ineffective)
  - Next Review Date (Date)

### Grades Database
- **Properties:**
  - Grade Entry (Title) - Auto-generated from Course + Assignment/Exam
  - Course (Relation)
  - Item (Text)
  - Score (Number)
  - Possible Points (Number)
  - Percentage (Formula)
  - Weight (Number)
  - Contribution to Course Grade (Formula)
  - Date Received (Date)

## Key Views

### 1. Semester Overview
- Timeline view of all courses
- Shows start/end dates
- Color-coded by department

### 2. Weekly Schedule
- Calendar view of all assignments and exams
- Color by course
- Shows due dates prominently

### 3. Assignment Tracker
- Table sorted by due date
- Filter: Status = Not Started or In Progress
- Shows: Assignment, Course, Due Date, Priority, Grade

### 4. Grade Tracker
- Current grades by course
- Shows: Course, Current %, Target %, Difference
- Color-coded by grade range

### 5. Study Plan
- Shows upcoming exams with prep timeline
- Recommended study sessions
- Topics to cover

### 6. GPA Dashboard
- Overall GPA
- GPA by semester
- Projected final GPA
- Grade distribution

## Formulas & Calculations

### Grade Percentage
```
if(prop("Possible Points") > 0, divide(prop("Score"), prop("Possible Points")) * 100, 0)
```

### Course Grade
```
sum of all assignment/exam percentages weighted by their point values
```

### GPA Calculation
```
Letter grade → Point value (A=4.0, B=3.0, C=2.0, D=1.0, F=0.0) × Credit Hours / Total Credit Hours
```

## Automations

### 1. Assignment Due Date Reminders
- 1 week before: Send reminder
- 3 days before: Highlight in yellow
- 1 day before: Highlight in red + send urgent reminder

### 2. Grade Updates
- When grade received: Auto-calculate course grade
- Update GPA dashboard
- Alert if grade falls below target

### 3. Study Session Suggestions
- Recommend study before exams
- Track based on topic difficulty
- Adjust based on previous exam performance

### 4. Mid-Semester Alerts
- Flag if course grade below 75%
- Suggest meeting instructor
- Recommend tutoring

## Real-World Workflow

### Semester Start
1. Add all courses with meeting times
2. Input syllabus info (grading breakdown, exam dates)
3. Set grade targets for each course
4. Create study material library

### Weekly
1. Review upcoming assignments (next 2 weeks)
2. Plan study sessions
3. Log completed assignments
4. Update study notes

### After Exams/Assignment Submission
1. Input grades received
2. Review performance
3. Analyze areas needing improvement
4. Adjust study strategy if needed

### End of Semester
1. Calculate final grades
2. Update GPA
3. Archive course
4. Reflect on what worked

## Getting Started

### Phase 1: Foundation
1. Create all 6 databases
2. Add current semester courses
3. Input syllabus information
4. Set grade targets

### Phase 2: Population
1. Add all assignments from syllabi
2. Add exam dates
3. Create study material links
4. Set up grade weighting

### Phase 3: Tracking
1. Log study sessions
2. Track assignment submissions
3. Record grades as received
4. Monitor GPA progress

## Tips for Success

1. **Update Regularly**: Enter assignments immediately after each class
2. **Set Realistic Targets**: Base on personal goals and course difficulty
3. **Review Weekly**: Check upcoming deadlines every Sunday
4. **Track Study Time**: Log hours spent to find optimal study patterns
5. **Analyze Grades**: Review mistakes to improve performance
6. **Adjust Strategy**: If not meeting targets, change study methods
7. **Use Notifications**: Enable alerts for critical deadlines
8. **Plan Ahead**: Start major projects early

## Integration Ideas

- Google Calendar sync for deadline visibility
- Email alerts for upcoming assignments
- Discord bot for study reminders
- Zapier integration with course portals
- Canvas/Blackboard auto-import of deadlines

## Advanced Features

### AI-Powered Study Recommendations
- Analyze past exam performance
- Suggest topics needing review
- Recommend study materials by effectiveness
- Predict exam scores based on prep time

### Study Streak Tracking
- Consecutive days studied
- Hours per week
- Consistency rating
- Comparison to targets

### Exam Preparation Timeline
- Weeks to exam countdown
- Optimal start date
- Daily prep schedule
- Topic coverage checklist

## Troubleshooting

**Q: Grades not calculating correctly**
A: Verify all weights sum to 100%. Check formula includes all assignment types.

**Q: Missing assignment deadlines**
A: Enable notifications. Check course syllabi again. Set phone calendar reminders.

**Q: GPA calculation seems wrong**
A: Verify credit hours per course. Confirm grading scale. Check term context.

**Q: Overwhelmed by workload**
A: Use Priority field. Focus on high-weight assignments first. Break projects into milestones.
