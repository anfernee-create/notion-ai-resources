# AI-Powered Habit Tracker Template

## Overview
A comprehensive personal habit tracking system with AI-powered insights, progress analysis, and motivation optimization. Track daily habits, visualize streaks, identify patterns, and get smart recommendations for sustainable behavior change.

## Database Structure

### Habits Database
- **Properties:**
  - Habit Name (Title)
  - Description (Rich text)
  - Category (Select: Health, Fitness, Learning, Productivity, Finance, Mindfulness, Relationships, Other)
  - Frequency (Select: Daily, Weekly, 3x/week, 2x/week, Monthly)
  - Target Count (Number) - e.g., 8 for 8 glasses of water
  - Unit (Text) - e.g., glasses, minutes, miles
  - Started Date (Date)
  - Goal End Date (Date)
  - Status (Select: Active, Paused, Completed, Abandoned)
  - Priority (Select: Essential, Important, Nice-to-have)
  - Why I'm doing this (Rich text)
  - Log Entries (Relation to Log)
  - Current Streak (Rollup - count consecutive days)
  - Longest Streak (Rollup - max streak)
  - Completion Rate (Formula)
  - AI Score (Formula)
  - Notes (Rich text)

### Daily Log Database
- **Properties:**
  - Date (Date)
  - Habit (Relation to Habits)
  - Completed (Checkbox)
  - Count (Number) - actual count achieved
  - Feeling Before (Select: Great, Good, Neutral, Bad, Terrible)
  - Feeling After (Select: Great, Good, Neutral, Bad, Terrible)
  - Notes (Rich text)
  - Mood (Select: 1-5 scale)
  - Energy Level (Select: 1-5 scale)
  - Obstacles (Multi-select: Time, Motivation, Environment, Health, Other)
  - Tags (Multi-select)

### Streaks Database
- **Properties:**
  - Habit (Relation to Habits)
  - Start Date (Date)
  - End Date (Date)
  - Days (Formula - count)
  - Status (Select: Active, Broken, Completed)
  - Best Streak (Checkbox)

### Insights Database (AI-generated)
- **Properties:**
  - Date (Date)
  - Insight Type (Select: Pattern, Warning, Celebration, Recommendation)
  - Content (Rich text)
  - Habit (Relation)
  - Data Points (Number)
  - AI Generated (Checkbox)

## Views

### 1. Daily Dashboard
- Table view of today's habits
- Columns: Habit, Frequency, Completed, Count, Feeling Before, Feeling After, Notes
- Filter: Today's Date
- Sorted by Category then Priority

### 2. Habit Calendar
- Calendar view of Daily Log
- Shows completed habits with color coding
- Color by Category
- Current month view

### 3. Streaks Leaderboard
- Sorted by Current Streak (descending)
- Shows: Habit, Current Streak, Longest Streak, Status, Completion %
- Filter: Status = Active
- Highlight best performing habits

### 4. Category View
- Grouped by Category
- Shows: Habit, Status, Current Streak, Completion %
- Summary stats per category

### 5. Weekly Review
- Table of habits with weekly completion rate
- Filter: Last 7 days
- Columns: Habit, Goal, Achieved, %, Mood Trend, Notes

### 6. Monthly Insights
- Monthly completion rates
- Trend analysis
- Best and worst performing habits
- Correlation analysis (habits affecting mood/energy)

### 7. AI Recommendations
- Table of Insights database
- Filter: Insight Type = Recommendation
- Shows suggestions for improvement

### 8. Obstacle Analysis
- Table of Daily Log filtered by obstacles
- Shows which obstacles appear most frequently
- Correlate with completion rates

## Formulas

### Completion Rate
```
let total_logs = length(prop("Log Entries"));
let completed = length(filter(prop("Log Entries"), current.prop("Completed") == true));
if(total_logs == 0, 0, divide(completed, total_logs) * 100)
```

### Current Streak
```
// Count consecutive days completed from today backwards
// Complex: Requires checking last log entry, then previous day, etc.
// Simplified: dateBetween(now(), prop("Log Entries").max(prop("Date")), "days") == 0 ? increment : 0
```

### AI Score (Overall Habit Health)
```
let completion = prop("Completion Rate");
let streak_bonus = if(prop("Current Streak") > 30, 20, if(prop("Current Streak") > 14, 10, 0));
let consistency = if(completion >= 80, 25, if(completion >= 60, 15, if(completion >= 40, 5, 0)));
let recency = if(dateBetween(now(), prop("Last Log Date"), "days") <= 1, 10, -10);
completion * 0.5 + consistency + streak_bonus + recency
```

## Automations

### 1. Daily Reset
- Every day at 6 AM: Create new log entries for all Active habits
- Pre-populate with habit targets and category

### 2. Streak Tracking
- When log is marked Completed: Check for streak continuation
- If streak broken (date gap > 1 day): Move current streak to history
- Reset current streak counter

### 3. Mood Correlation Analysis
- Every Monday: Analyze correlation between habit completion and mood
- Identify which habits most impact wellbeing
- Send summary to user

### 4. Motivation Notifications
- When streak reaches 7, 14, 30, 60, 100 days: Send celebration
- When current streak = 0: Send motivation/reset message
- When completion rate drops below 50%: Send gentle reminder

### 5. Weekly Report
- Every Sunday evening: Generate weekly summary
- Show: Completion %, streaks, mood changes, obstacle analysis
- Highlight improvements and areas needing support

### 6. AI Insights Generation
- Daily: Analyze patterns and generate insights
- Identify positive correlations (habits that support each other)
- Flag negative trends early
- Suggest habit stacking opportunities

## AI Enhancement Ideas

### Pattern Detection
- Identify which days of week you're most consistent
- Detect time-based patterns (morning vs evening habits)
- Correlate habits with external factors (weather, calendar events)

### Predictive Analytics
- Predict likelihood of abandoning habits based on early warning signs
- Suggest best time to start new habits based on existing routine
- Forecast streak length at current completion rate

### Smart Recommendations
- Recommend habits to pair with existing ones (habit stacking)
- Suggest modifications when habits aren't sustainable
- Recommend best time to start new habits
- Predict which habits you'll struggle with this week

### Adaptive Difficulty
- Automatically adjust targets based on performance
- Increase difficulty when exceeding goals consistently
- Suggest breaking down difficult habits into smaller chunks
- Recommend temporary pause for overwhelmed users

### Mood & Energy Optimization
- Identify which habit combinations maximize mood
- Correlate habits with energy levels
- Suggest optimal daily sequence

## Real-World Examples

### Example 1: New Year's Resolution
1. Create 5 new habits: Meditation, Exercise, Reading, Water Intake, Sleep Schedule
2. Set frequency to Daily, target to compete by end of January
3. System creates daily log entries automatically
4. After week 1: AI identifies meditation boosts mood
5. After month 1: Show progress - 3 habits at 80%+, 2 below 60%
6. AI recommends: Drop one struggling habit, focus on winners

### Example 2: Habit Stacking
1. Morning routine established: Meditation → Coffee → Reading
2. Add new habit "Take Vitamins" - pair with morning coffee
3. System recognizes stacking opportunity
4. Correlation analysis shows stacked habits have higher completion
5. Suggest similar opportunities for other habits

### Example 3: Crisis Response
1. Stress period identified (low mood, low energy for 3 days)
2. Many habits broken due to obstacles marked as "Health"
3. AI suggests: Temporarily pause 2 less important habits
4. Recommends shifting focus to stress-relief habits (meditation, exercise)
5. Once stress passes, help re-establish paused habits

## Getting Started

### Step 1: Define Your Habits
1. List 3-5 habits you want to track
2. Set realistic frequency and targets
3. Write motivational "Why" for each
4. Set start date (today or soon)

### Step 2: Set Up Daily Logging
1. Create today's log entries
2. Test logging a completed habit
3. Check streak updates
4. Review dashboard view

### Step 3: Configure Automations
1. Set up daily log entry creation
2. Test streak tracking automation
3. Enable notifications for milestones
4. Set up weekly report schedule

### Step 4: Review Insights
1. Check AI recommendations
2. Review correlation analysis
3. Look for pattern insights
4. Adjust habits based on data

### Step 5: Establish Routine
1. Pick consistent daily check-in time
2. Weekly review (ideally Sunday)
3. Monthly assessment and planning
4. Adjust as needed

## Best Practices

1. **Start Small**: Begin with 3-5 habits max; add more gradually
2. **Be Specific**: Concrete targets (e.g., 30 min, 2 miles) vs vague (e.g., "exercise")
3. **Log Immediately**: Log completed habits same day
4. **Honest Tracking**: Mark incomplete even when disappointing
5. **Weekly Review**: Spend 15 min each week reviewing data
6. **Stack Habits**: Attach new habits to existing routines
7. **Obstacle Tracking**: Note obstacles to identify patterns
8. **Celebrate Wins**: Acknowledge and celebrate streaks
9. **Forgive Breaks**: One missed day isn't failure; refocus
10. **Evolve Slowly**: Adjust targets based on realistic assessment

## Psychological Insights

### Streak Motivation
- Streaks create powerful psychological motivation
- Missing one day feels like breaking a chain
- Celebrate milestone streaks (7, 14, 30, 100 days)

### Habit Stacking
- New habits attach to existing routines (highest success rate)
- Morning routines are often easiest to establish
- Consider habit pairs that support each other

### Obstacle Identification
- Common obstacles: Time, Motivation, Environment
- Different obstacles need different solutions
- Track obstacles to identify patterns

### Identity Shift
- Habit tracking helps identity shift (I'm someone who exercises)
- Visual evidence of consistency reinforces identity
- Regular review strengthens conviction

## Advanced Customizations

### Habit Dependencies
- Create related habits field
- Track habits that support or conflict
- Optimize daily schedule

### Social Features
- Share streaks with accountability partner
- Export weekly summaries
- Challenge mode (compete with others)

### Integration Ideas
- Sync with fitness trackers (Apple Health, Fitbit)
- Connect to calendar (see if busy days affect habits)
- Link with mood tracking apps

## Troubleshooting

**Q: Streaks seem wrong**
A: Verify daily logs have correct dates. Check formula for streak counting.

**Q: Too many habits to maintain**
A: Start with 3, add more after establishing routine. Quality over quantity.

**Q: Not seeing patterns in data**
A: Need minimum 2-4 weeks of data. Review obstacles and mood correlations.

**Q: AI recommendations not helpful**
A: Check you've logged mood and obstacles. More data = better insights.
