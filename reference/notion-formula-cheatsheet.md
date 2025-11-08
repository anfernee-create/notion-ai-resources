# Notion Formula Cheatsheet - Complete Reference

## String Functions

### Basic String Operations

`concat("Hello", " ", "World")` → "Hello World"
`slice("Hello", 0, 3)` → "Hel"
`length("Hello")` → 5
`upper("hello")` → "HELLO"
`lower("HELLO")` → "hello"
`trim(" hello ")` → "hello"
`replaceAll(text, find, replace)` → Replaces all occurrences
`replace(text, find, replace)` → Replaces first occurrence
`startsWith("hello", "he")` → true
`endsWith("hello", "lo")` → true
`contains(text, search)` → true/false
`test(text, regex)` → Test regex pattern
`match(text, regex)` → Extract matches

## Number Functions

### Math Operations

`add(1, 2, 3)` → 6
`subtract(10, 3)` → 7
`multiply(3, 4)` → 12
`divide(10, 2)` → 5
`mod(10, 3)` → 1 (remainder)
`pow(2, 3)` → 8
`sqrt(16)` → 4
`abs(-5)` → 5
`sign(-5)` → -1
`round(3.7)` → 4
`ceil(3.2)` → 4
`floor(3.9)` → 3
`min(1, 5, 3)` → 1
`max(1, 5, 3)` → 5

### Advanced Math

`log(100)` → Natural logarithm
`exp(1)` → e^1 ≈ 2.718
`sin(angle)`, `cos(angle)`, `tan(angle)` → Trigonometry

## Date Functions

### Date Creation & Parsing

`now()` → Current timestamp
`fromTimestamp(1609459200)` → Date from timestamp
`dateAdd(prop("Date"), 7, "days")` → Add 7 days
`dateSubtract(prop("Date"), 1, "weeks")` → Subtract 1 week
`dateBetween(start, end, "days")` → Days between dates
`formatDate(now(), "MMM d, yyyy")` → "Nov 8, 2025"

### Date Formatting Codes

- `yyyy` - 4-digit year (2025)
- `yy` - 2-digit year (25)
- `MMMM` - Full month name (November)
- `MMM` - Short month name (Nov)
- `MM` - 2-digit month (11)
- `M` - Month number (11)
- `dddd` - Full weekday (Saturday)
- `ddd` - Short weekday (Sat)
- `dd` - 2-digit day (08)
- `d` - Day number (8)
- `HH` - 24-hour format (21)
- `hh` - 12-hour format (09)
- `mm` - Minutes (30)
- `ss` - Seconds (45)
- `A` - AM/PM

### Date Comparisons

`dateBetween(now(), prop("Due"), "days") <= 0` → Due today or overdue
`dateAdd(prop("Created"), 30, "days") <= now()` → 30 days passed

## Conditional Functions

### If/Then Logic

`if(prop("Status") == "Done", "✅", "⏳")` → Conditional display
`if(dateBetween(now(), prop("Due"), "days") <= 7, "Urgent", "Normal")` → Time-based
`if(empty(prop("Name")), "Missing", prop("Name"))` → Handle empty

### Switch Statements

```
switch(
  prop("Priority"),
  "High", "🔴",
  "Medium", "🟡",
  "Low", "🟢",
  "❓"
)
```

## Logical Functions

### Boolean Operations

`and(true, true)` → true
`or(false, true)` → true
`not(false)` → true
`xor(true, false)` → true

### Comparison Operators

`prop("Price") > 100` → Greater than
`prop("Price") < 100` → Less than
`prop("Price") >= 100` → Greater or equal
`prop("Price") <= 100` → Less or equal
`prop("Status") == "Done"` → Equals
`prop("Status") != "Done"` → Not equals

## Array Functions

### Working with Relations & Rollups

`length(prop("Related Pages"))` → Count items
`empty(prop("Related Pages"))` → Is empty?
`contains("tag1", prop("Tags"))` → Contains tag?
`filter(list, condition)` → Filter array
`map(list, expression)` → Transform array
`sort(list, "asc")` → Sort array
`reverse(list)` → Reverse order
`unique(list)` → Remove duplicates
`flat(array)` → Flatten nested arrays

## Aggregation Functions

### Rollup Calculations

`count()` → Count items
`sum(prop("Amount"))` → Total sum
`avg(prop("Score"))` → Average
`min(prop("Price"))` → Minimum
`max(prop("Price"))` → Maximum
`count_if(prop("Status") == "Done")` → Conditional count
`percent_complete()` → Checkbox completion %
`concat_if(prop("Name"), prop("Status") == "Done")` → Join matching

## Empty/Null Functions

`empty(prop("Field"))` → Is field empty?
`prop("Field") != empty` → Is not empty?
`if(empty(prop("Email")), "No email", prop("Email"))` → Handle empty
`if(prop("Phone") == null, "Missing", prop("Phone"))` → Check null

## Type Conversion

`toNumber("123")` → Convert to number
`toString(123)` → Convert to string
`parseFloat(prop("Price"))` → Parse float
`parseInt(prop("Count"))` → Parse integer

## Complex Formula Patterns

### Pattern 1: Status Badge with Emoji

```
switch(
  prop("Status"),
  "Done", "✅ Complete",
  "In Progress", "⏳ Working",
  "Blocked", "🚫 Blocked",
  "Not Started", "⭕ To Do",
  "Unknown"
)
```

### Pattern 2: Days Until/Overdue

```
let("days", dateBetween(now(), prop("Due"), "days"),
if(prop("Due") == null,
  "No due date",
  if([days] <= 0,
    abs([days]) + " days overdue",
    [days] + " days left"
  )
)
```

### Pattern 3: Progress Percentage

```
if(prop("Total Tasks") == 0,
  0,
  round(prop("Completed") / prop("Total Tasks") * 100
)
```

### Pattern 4: Quarter from Date

```
let("month", toNumber(formatDate(prop("Date"), "M")),
  "Q" + if([month] <= 3, "1", if([month] <= 6, "2", if([month] <= 9, "3", "4")))
)
```

### Pattern 5: Age Calculator

```
let("years", dateBetween(now(), prop("Birth Date"), "years"),
  [years] + " years old"
)
```

### Pattern 6: Business Days Until Due

```
let("days", dateBetween(now(), prop("Due"), "days"),
  round([days] * 0.714)  // Approximate: 5 business days per 7 calendar days
)
```

### Pattern 7: Score Category

```
let("score", prop("Score"),
  if([score] >= 90, "A",
    if([score] >= 80, "B",
      if([score] >= 70, "C",
        if([score] >= 60, "D", "F")
      )
    )
  )
)
```

### Pattern 8: Multi-Status Filter Logic

```
if(
  and(
    prop("Status") != "Archived",
    prop("Priority") == "High",
    dateBetween(now(), prop("Due"), "days") <= 7
  ),
  "🔴 Action Required",
  "•"
)
```

## Regular Expression Patterns

### Email Validation

`test(prop("Email"), "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}")`

### Phone Number Format

`test(prop("Phone"), "^\\+?[1-9]\\d{1,14}$")`

### Extract Domain from URL

`match(prop("URL"), "https?://([^/]+)")[1]`

### Extract Numbers from Text

`match(prop("Description"), "\\d+")[0]`

## Performance Tips

1. **Avoid nested formulas** when possible
2. **Cache calculations** in separate formula fields
3. **Use switch** instead of many nested ifs
4. **Minimize date operations** - heavy on performance
5. **Test with large datasets** before using complex formulas
6. **Use let()** to store intermediate results
7. **Avoid regex** in heavily-used formulas

## Common Mistakes & Solutions

| Problem | Solution |
|---------|----------|
| "Invalid formula" | Check parentheses and quotes |
| Empty result | Check for null/empty values first |
| Incorrect dates | Verify timezone and format |
| Slow formula | Simplify or break into multiple fields |
| Unexpected type | Use toNumber() or toString() conversion |
| Comparing null | Use empty() or != empty instead |

## Formula Debugging

1. Break complex formulas into steps
2. Test each part individually
3. Use if(true, "test", ...) to verify execution
4. Check property names for typos
5. Verify property types match expectations
6. Use empty() and ! empty checks
7. Test with sample data first

## Advanced: Using let() for Complex Calculations

```
let("priority_value",
  switch(prop("Priority"),
    "Critical", 3,
    "High", 2,
    "Normal", 1,
    0
  ),
  let("urgency",
    if(dateBetween(now(), prop("Due"), "days") <= 3, 2, 1),
    [priority_value] * [urgency]
  )
)
```

## Quick Reference by Use Case

### For Status Tracking
- `switch(prop("Status"), ...)` - Multi-option display
- `if(empty(prop("Completed")), "Pending", "Done")` - Simple toggle

### For Dates
- `formatDate(now(), "MMM d")` - Today's date
- `dateBetween(now(), prop("Due"), "days")` - Days until
- `dateAdd(prop("Date"), 30, "days")` - Add duration

### For Numbers
- `round(divide(a, b), 2)` - Round to 2 decimals
- `if(prop("Count") > 0, "Available", "Out of stock")` - Threshold check

### For Text
- `concat(prop("First"), " ", prop("Last"))` - Combine names
- `replace(prop("Text"), "old", "new")` - Text replacement
- `slice(prop("Code"), 0, 3)` - Extract first 3 chars

## Conclusion

Notion formulas are powerful but require practice. Start simple, build complexity gradually, and always test before using in production. Use this cheatsheet as your quick reference while learning and building.
