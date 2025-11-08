# Database Query Optimization Prompts

A comprehensive collection of AI prompts for optimizing Notion database queries, improving performance, and streamlining data retrieval.

## Core Query Optimization Prompts

### 1. Analyze Query Performance
"I have a Notion database with [describe structure]. Currently my query is [share query/view setup]. The performance is [describe issue]. Can you suggest optimizations?"

### 2. Filter Strategy
"I need to filter my Notion database for [describe criteria]. I have [X number of] records. What's the most efficient way to set this up?"

### 3. Sort Optimization
"I'm sorting a database by [property]. I have [describe data structure]. Is this the optimal approach? What alternatives exist?"

### 4. Database Relations Efficiency
"I have related databases with [describe relations]. How can I optimize queries across these relations?"

### 5. Rollup and Aggregation
"I need to aggregate data from [describe structure]. Currently using [method]. How can I improve performance?"

## Advanced Optimization Scenarios

### Filtering Across Relations
"I need to filter Database A by properties in Database B. Current approach: [describe]. What's more efficient?"

### Large Database Performance
"My database has [X,000] records. Queries are slow. Current structure: [describe]. How should I reorganize?"

### Complex Search Queries
"Users need to search [describe search criteria]. Current implementation: [describe]. Suggest optimized approach."

### Multi-Level Relations
"I have a 3-level relational structure: [describe]. How should I optimize queries across levels?"

### Dynamic Filtering
"I need to allow users to filter by multiple optional criteria. Structure: [describe]. Best practice?"

## Index and Structure Optimization

### 1. Database Restructuring
"Analyze this database structure: [describe]. Suggest optimization for [specific use case]."

### 2. Property Type Selection
"For [describe data], should I use [option A] or [option B] property type? Performance implications?"

### 3. Relation vs Rollup
"Should this data be a relation with rollup or calculated? Trade-offs?"

### 4. Denormalization Strategy
"Currently normalized structure: [describe]. Would denormalization help? Trade-offs?"

### 5. Archiving Strategy
"Database has [X] inactive records. Archive strategy implications for query performance?"

## Real-World Query Optimization

### E-commerce Example
"Product database: [X] products, [Y] variants each, filtering by [criteria]. Optimize approach."

### Project Management
"Tasks database: [X] tasks, multiple status filters, date ranges. Performance issue: [describe]."

### Content Management
"Articles database: [X] articles, tagged with [Y] tags, searched frequently. Optimize."

### Customer Relations
"Customers [X] records, related to [related databases], complex filters. Performance tuning?"

### Inventory Tracking
"Inventory: [X] SKUs, distributed across [Y] locations, real-time updates. Query optimization?"

## Performance Benchmarking

### 1. Baseline Measurement
"Current query time: [X]ms for [Y] records. Is this acceptable? Optimization targets?"

### 2. Load Testing
"How should I test database performance at [X scale]? Best practices?"

### 3. Bottleneck Identification
"Slow queries: [describe]. Is it filtering/sorting/relations? Diagnosis approach?"

### 4. Scaling Strategy
"Database growing to [X] records. Current optimization: [describe]. Will it scale?"

## Query Alternatives

### 1. View-Based vs Formula-Based
"Currently using [method] for [purpose]. Should I use [alternative]? Pros/cons?"

### 2. Rollup Functions
"Which rollup function best for [use case]? Options: sum, avg, count, max, min. Recommendation?"

### 3. Formula Optimization
"Current formula: [share formula]. Simplify for performance?"

### 4. Relation Cardinality
"Relation is one-to-many/many-to-many. Performance implications for [use case]?"

## Batch Operations

### 1. Bulk Updates
"Need to update [X] records with [criteria]. Efficient approach in Notion?"

### 2. Data Migration
"Migrating [X] records from [source] to Notion. Optimize import structure?"

### 3. Syncing Performance
"Syncing external data: [X] records, [Y] frequency. Structure for efficiency?"

## API Query Optimization

### 1. API Filter Strategy
"Using Notion API to query [database]. Current: [share filter]. Optimize for [goal]?"

### 2. Pagination
"Fetching [X] records via API. Optimize pagination for [use case]?"

### 3. Batch API Queries
"Multiple related queries needed: [describe]. Batch efficiently?"

### 4. Field Selection
"Retrieving [Y] properties per record. Should I limit to needed fields only?"

## Caching Strategies

### 1. Query Result Caching
"Cache frequently-run queries? Frequency: [X] times/day. Stale data tolerance?"

### 2. Computed Caching
"Cache rollup/formula results? Update frequency needed: [X]."

### 3. Client-Side Caching
"Caching strategy for external app querying Notion? Requirements: [describe]."

## Troubleshooting

### 1. Unexpected Slow Query
"Query was fast, now slow: [timeline]. Changes made: [describe]. Root cause?"

### 2. Filter Not Working
"Filter criteria: [describe]. Expected results: [X], actual: [Y]. Debug?"

### 3. Sort Inconsistencies
"Sorting by [property]. Results seem wrong. Debug approach?"

### 4. Relation Query Issues
"Querying relation: [describe]. Expected: [X] results, getting [Y]. Issue?"

## Best Practices Prompts

### 1. Database Design Review
"Review database structure for: [describe use case]. Suggest optimizations."

### 2. Query Strategy
"Design optimal query strategy for: [use case]. Consider: [factors]."

### 3. Scaling Plan
"Plan database scaling from [current scale] to [target scale]. Optimize now?"

### 4. Performance SLA
"Target query time: [X]ms for [Y] records. Current: [Z]. Achievable? How?"
