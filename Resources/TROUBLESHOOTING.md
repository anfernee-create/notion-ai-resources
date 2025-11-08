# Troubleshooting Guide - Notion AI

## Common Issues & Solutions

### Database & Structure Issues

#### Problem: Relations not showing
**Symptoms**: Relation property shows empty even though related records exist

**Solutions**:
1. Check relation direction - make sure you're looking at the correct side
2. Verify both databases haven't been deleted
3. Recreate the relation:
   - Delete the relation property
   - Create new relation between same databases
   - Manually link records again
4. Check filters - hidden records won't show
5. Ensure you have access to both databases

#### Problem: Database won't load
**Symptoms**: Database page shows loading spinner indefinitely or displays error

**Solutions**:
1. Refresh the page (Cmd+R)
2. Close and reopen the database
3. Try accessing from different browser
4. Clear browser cache
5. Check internet connection
6. Try Notion web vs mobile app
7. Check database size - very large databases take longer
8. Remove complex formulas temporarily to test

#### Problem: Too many properties showing "error"
**Symptoms**: Multiple formula/rollup properties show #ERROR

**Solutions**:
1. Check if related databases were deleted
2. Verify property names haven't changed
3. Delete and recreate affected properties
4. Check data type compatibility
5. Ensure formula syntax is correct
6. Test formulas one at a time

### Formula Issues

#### Problem: Formula returns #ERROR
**Symptoms**: Formula property displays "#ERROR" instead of result

**Common Causes & Fixes**:

**Cause 1: Property name typo**
```
// Wrong
if(prop("Due Date") > now(), "Late", "On Time")

// Right (if property is named "Due date")
if(prop("Due date") > now(), "Late", "On Time")
```

**Cause 2: Wrong data type**
```
// Wrong - trying to add text to number
prop("Task Name") + 5

// Right - convert or use correct type
toNumber(prop("Count")) + 5
```

**Cause 3: Missing relation**
```
// Wrong - relation deleted
rollup(relation("Tasks"), "prop(\"Hours\")", "sum")

// Right - verify relation exists
if(empty(relation("Tasks")), 0, rollup(relation("Tasks"), "prop(\"Hours\")", "sum"))
```

**Cause 4: Comparison with wrong type**
```
// Wrong
if(prop("Status") == 5, "Yes", "No")  // Status is text, comparing to number

// Right
if(prop("Status") == "Complete", "Yes", "No")
```

**Cause 5: Empty relation**
```
// This will error if relation is empty
rollup(relation("Tasks"), "prop(\"Hours\")", "sum")

// Better - handle empty case
if(empty(relation("Tasks")), 0, rollup(relation("Tasks"), "prop(\"Hours\")", "sum"))
```

#### Problem: Formula too complex/slow
**Symptoms**: Formula takes long time to calculate or times out

**Solutions**:
1. Break formula into multiple properties:
   ```
   // Slow
   if(and(prop("A") > 10, prop("B") < 5, prop("C") != "Done"), calculation1, calculation2)
   
   // Faster
   // Property 1: if(prop("A") > 10, true, false)
   // Property 2: if(prop("B") < 5, true, false)
   // Property 3: if(and(prop("Prop1"), prop("Prop2"), prop("C") != "Done"), calculation1, calculation2)
   ```

2. Avoid nested rollups:
   ```
   // Slow
   rollup(relation("Projects"), "rollup(relation(\"Tasks\"), \"1\", \"count\")", "sum")
   
   // Better - query directly or simplify
   rollup(relation("Projects"), "1", "count")
   ```

3. Limit filter complexity
4. Archive old data if database is very large

### Rollup Issues

#### Problem: Rollup shows wrong results
**Symptoms**: Rollup calculation seems incorrect

**Solutions**:
1. Check filter is correct:
   ```
   // Make sure filter is specific
   rollup(relation("Tasks"), "if(prop(\"Status\") == \"Done\", 1, 0)", "sum")
   ```

2. Verify aggregation function:
   - sum: Adds all values
   - count: Counts items (ignores actual values)
   - count_values: Counts non-empty items
   - count_all: Counts all items including empty
   - average: Mean value
   - median: Middle value
   - min/max: Smallest/largest
   - concat: Joins text
   - unique: Counts unique values

3. Check for empty values affecting calculation

### Integration & Automation Issues

#### Problem: Zapier automation not triggering
**Symptoms**: Zap shows as enabled but never runs

**Solutions**:
1. Check Notion connection:
   - Open Zapier settings
   - Re-authorize Notion account
   - Verify workspace access

2. Verify trigger condition:
   - Test trigger manually in Zapier
   - Make sure trigger event matches what you're doing
   - Check if database/fields still exist

3. Check task history:
   - Log into Zapier
   - View task history
   - Look for error messages

4. Rate limits:
   - Free Zapier checks every 15 minutes
   - Consider upgrading for faster checks
   - Check if action is failing silently

#### Problem: Zapier automation running but not creating records
**Symptoms**: Zap runs but nothing appears in Notion

**Solutions**:
1. Verify Notion database access:
   - Database still exists
   - You have edit access
   - Database hasn't been archived

2. Check field mapping:
   - Verify field names match
   - Check data type compatibility
   - Some fields may be required

3. Test manually:
   - Create test record manually
   - Try different field combinations
   - Check for validation rules

4. Check Zapier action settings:
   - Database selected correctly
   - All required fields mapped
   - No conditional logic preventing creation

#### Problem: Make scenario showing errors
**Symptoms**: Make shows "Error executing module" messages

**Solutions**:
1. Check module configuration:
   - Verify all required fields filled
   - Check data format matches expectation
   - Ensure IDs are correct format

2. Test with simpler data:
   - Start with minimal fields
   - Add complexity gradually
   - Use test data to verify

3. Check error message:
   - Click on error for details
   - Look for field validation issues
   - Check for authentication problems

### Performance Issues

#### Problem: Notion workspace running slowly
**Symptoms**: Slow loading, laggy interactions, frequent loading spinners

**Causes & Solutions**:

**Cause 1: Too many properties**
- Remove unused properties
- Archive old databases
- Consolidate similar data

**Cause 2: Complex formulas**
- Simplify formulas
- Break into multiple steps
- Pre-calculate results when possible

**Cause 3: Too many relations**
- Evaluate which relations are needed
- Use properties instead when possible
- Consider denormalizing data

**Cause 4: Large database**
- Archive completed items
- Create separate databases by year/category
- Use filters to reduce visible data

**Cause 5: Too many views**
- Delete unused views
- Hide views not regularly used
- Consolidate similar views

**Cause 6: Resource-heavy integrations**
- Reduce automation frequency
- Batch operations
- Use scheduled runs instead of continuous

### Import/Export Issues

#### Problem: CSV import failing
**Symptoms**: Error when trying to import CSV file

**Solutions**:
1. Check file format:
   - Ensure it's valid CSV format
   - Check encoding is UTF-8
   - Verify no special characters in column names

2. Check column structure:
   - Database column headers must match property names exactly
   - Remove special characters from headers
   - Try with simpler data first

3. Verify data types:
   - Dates must be in recognizable format
   - Numbers shouldn't have currency symbols
   - Text can be plain or rich text

4. Try alternative import:
   - Create new empty database
   - Try importing to that
   - Or manually create structure first

#### Problem: Export file corrupted or incomplete
**Symptoms**: Exported file missing data or won't open

**Solutions**:
1. Try different export format:
   - PDF for viewing
   - CSV for data preservation
   - Markdown for content

2. Check file size:
   - Very large exports may fail
   - Try exporting smaller sections
   - Export by date ranges

3. Check application:
   - Use correct app to open file
   - Update spreadsheet app for CSV
   - Try opening in different program

### Access & Permissions Issues

#### Problem: Can't see shared database
**Symptoms**: Shared database not appearing in workspace

**Solutions**:
1. Check invitation:
   - Confirm you received invitation
   - Check email spam folder
   - Resend invitation if needed

2. Verify account:
   - Using correct email address
   - Logged into correct Notion account
   - Refresh page after accepting

3. Check permissions:
   - Verify permission level assigned
   - Editor access needed for modifications
   - Viewer access might show as read-only

#### Problem: Invited person can't access
**Symptoms**: User says they don't see shared database/page

**Solutions**:
1. Verify invitation sent:
   - Check if invitation was actually sent
   - Try sending again
   - Try different email address

2. Check user's account:
   - Ensure they accepted invitation
   - Verify they logged in with correct email
   - May need to create Notion account first

3. Check permission level:
   - Must be at least "Editor" to edit
   - "Viewer" only allows viewing
   - Check guest access settings

## Quick Diagnostic Steps

### General Troubleshooting Process

1. **Identify exact problem**: Describe what you see vs. what you expect
2. **Isolate the issue**: Is it a specific database, property, automation?
3. **Check basics**:
   - Is your internet working?
   - Have you refreshed the page?
   - Are you logged into the right account?
   - Do you have appropriate permissions?
4. **Search for error messages**: Note any specific error text
5. **Try workarounds**: Test alternate approaches
6. **Clear cache**: Hard refresh browser
7. **Try different browser/device**: Isolate browser-specific issues
8. **Check system**: Sufficient storage? Updated Notion app?

## Getting Help

When asking for help, include:
1. **What were you trying to do?**
2. **What happened instead?**
3. **What error message (if any)?**
4. **Screenshots** showing the issue
5. **What have you already tried?**
6. **When did this start happening?**

## Resources

- **Notion Status Page**: notion.status.page - Check if services are down
- **Notion Help**: notion.so/help
- **Community**: notion.so/community
- **Twitter**: @notionhq for announcements
- **Reddit**: r/Notion for community help

## Prevention Tips

1. **Regular backups**: Export important data monthly
2. **Version control**: Keep change log in CHANGELOG.md
3. **Document setup**: Note formula logic and why
4. **Test changes**: Try on duplicate before applying to live
5. **Monitor performance**: Watch for slowdowns
6. **Regular maintenance**: Archive old data, review automations
7. **Keep it simple**: Complex systems harder to troubleshoot
8. **Stay updated**: Keep Notion app current
