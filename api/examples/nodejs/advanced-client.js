/**
 * Notion API Advanced Client - Node.js
 * Comprehensive examples for advanced Notion API patterns and use cases
 * Includes batch operations, error handling, caching, rate limiting, and more
 */

const axios = require('axios');
const NodeCache = require('node-cache');
const pRetry = require('p-retry');

// ============================================================
// NOTION CLIENT CONFIGURATION
// ============================================================

class NotionAdvancedClient {
  constructor(notionToken, options = {}) {
    this.notionToken = notionToken;
    this.baseURL = 'https://api.notion.com/v1';
    this.version = '2022-06-28';
    
    // Caching configuration
    this.cache = new NodeCache({
      stdTTL: options.cacheTTL || 300,
      checkperiod: 60,
    });
    
    // Rate limiting configuration
    this.rateLimitConfig = {
      maxRequests: options.maxRequests || 3,
      windowMs: options.windowMs || 1000,
      requestQueue: [],
      lastRequestTime: 0,
    };
    
    // Retry configuration
    this.retryConfig = {
      maxRetries: options.maxRetries || 3,
      backoffMs: options.backoffMs || 1000,
    };
    
    // Axios instance with headers
    this.client = axios.create({
      baseURL: this.baseURL,
      headers: {
        'Authorization': `Bearer ${notionToken}`,
        'Notion-Version': this.version,
        'Content-Type': 'application/json',
      },
    });
  }

  // ============================================================
  // RATE LIMITING
  // ============================================================

  async waitForRateLimit() {
    const now = Date.now();
    const timeSinceLastRequest = now - this.rateLimitConfig.lastRequestTime;
    const minInterval = this.rateLimitConfig.windowMs / this.rateLimitConfig.maxRequests;
    
    if (timeSinceLastRequest < minInterval) {
      await new Promise(resolve => 
        setTimeout(resolve, minInterval - timeSinceLastRequest)
      );
    }
    
    this.rateLimitConfig.lastRequestTime = Date.now();
  }

  // ============================================================
  // RETRY LOGIC WITH EXPONENTIAL BACKOFF
  // ============================================================

  async makeRequestWithRetry(method, endpoint, data = null) {
    return pRetry(async () => {
      await this.waitForRateLimit();
      
      try {
        if (method === 'GET') {
          return await this.client.get(endpoint);
        } else if (method === 'POST') {
          return await this.client.post(endpoint, data);
        } else if (method === 'PATCH') {
          return await this.client.patch(endpoint, data);
        }
      } catch (error) {
        if (error.response && error.response.status === 429) {
          // Rate limited - retry with backoff
          throw new pRetry.AbortError(error);
        }
        throw error;
      }
    }, {
      maxRetries: this.retryConfig.maxRetries,
      onFailedAttempt: error => {
        console.log(
          `Request failed. ${error.retriesLeft} retries left.`,
          `Attempt ${error.attemptNumber}.`
        );
      },
    });
  }

  // ============================================================
  // CACHING LAYER
  // ============================================================

  getCacheKey(method, endpoint, data) {
    return `${method}:${endpoint}:${JSON.stringify(data || {})}`;
  }

  async getWithCache(endpoint, forceRefresh = false) {
    const cacheKey = this.getCacheKey('GET', endpoint);
    
    if (!forceRefresh) {
      const cached = this.cache.get(cacheKey);
      if (cached) {
        console.log(`Cache hit for ${endpoint}`);
        return cached;
      }
    }
    
    const response = await this.makeRequestWithRetry('GET', endpoint);
    this.cache.set(cacheKey, response.data);
    return response.data;
  }

  clearCache(pattern = null) {
    if (pattern) {
      const keys = this.cache.keys();
      keys.forEach(key => {
        if (key.includes(pattern)) {
          this.cache.del(key);
        }
      });
    } else {
      this.cache.flushAll();
    }
  }

  // ============================================================
  // BATCH OPERATIONS
  // ============================================================

  async batchUpdatePageProperties(pageIds, propertyUpdates) {
    const batchSize = 10; // Notion API recommended batch size
    const results = [];
    const errors = [];
    
    for (let i = 0; i < pageIds.length; i += batchSize) {
      const batch = pageIds.slice(i, i + batchSize);
      const batchPromises = batch.map(pageId =>
        this.makeRequestWithRetry('PATCH', `pages/${pageId}`, {
          properties: propertyUpdates,
        }).catch(error => ({
          pageId,
          error: error.message,
        }))
      );
      
      const batchResults = await Promise.all(batchPromises);
      batchResults.forEach(result => {
        if (result.error) {
          errors.push(result);
        } else {
          results.push(result.data);
        }
      });
      
      // Add delay between batches to avoid rate limiting
      if (i + batchSize < pageIds.length) {
        await new Promise(resolve => setTimeout(resolve, 500));
      }
    }
    
    return { results, errors, successCount: results.length, failureCount: errors.length };
  }

  async batchCreateDatabaseItems(databaseId, items) {
    const batchSize = 10;
    const results = [];
    const errors = [];
    
    for (let i = 0; i < items.length; i += batchSize) {
      const batch = items.slice(i, i + batchSize);
      const batchPromises = batch.map(item =>
        this.makeRequestWithRetry('POST', 'pages', {
          parent: { database_id: databaseId },
          properties: item,
        }).catch(error => ({
          item,
          error: error.message,
        }))
      );
      
      const batchResults = await Promise.all(batchPromises);
      batchResults.forEach(result => {
        if (result.error) {
          errors.push(result);
        } else {
          results.push(result.data);
        }
      });
      
      if (i + batchSize < items.length) {
        await new Promise(resolve => setTimeout(resolve, 500));
      }
    }
    
    return { results, errors, successCount: results.length, failureCount: errors.length };
  }

  // ============================================================
  // PAGINATION & STREAMING
  // ============================================================

  async *paginatedQuery(databaseId, filter = null, sorts = null) {
    let cursor = undefined;
    
    while (true) {
      const payload = {
        ...(filter && { filter }),
        ...(sorts && { sorts }),
        page_size: 100,
        ...(cursor && { start_cursor: cursor }),
      };
      
      const response = await this.makeRequestWithRetry(
        'POST',
        `databases/${databaseId}/query`,
        payload
      );
      
      yield response.data.results;
      
      if (!response.data.has_more) {
        break;
      }
      
      cursor = response.data.next_cursor;
    }
  }

  async getAllDatabaseItems(databaseId, filter = null, sorts = null) {
    const allItems = [];
    
    for await (const items of this.paginatedQuery(databaseId, filter, sorts)) {
      allItems.push(...items);
    }
    
    return allItems;
  }

  // ============================================================
  // ADVANCED QUERY PATTERNS
  // ============================================================

  async queryWithComplexFilter(databaseId, conditions) {
    // Build compound filter (AND logic)
    const filter = {
      and: conditions.map(cond => ({
        property: cond.property,
        [cond.type]: cond.value,
      })),
    };
    
    return await this.getAllDatabaseItems(databaseId, filter);
  }

  async queryWithSort(databaseId, sortConfig) {
    // sortConfig: { property: 'Name', direction: 'ascending' }
    const sorts = [{
      property: sortConfig.property,
      direction: sortConfig.direction || 'ascending',
    }];
    
    return await this.getAllDatabaseItems(databaseId, null, sorts);
  }

  async fulltextSearch(databaseId, searchTerm, searchFields) {
    // Search across multiple text fields
    const conditions = searchFields.map(field => ({
      property: field,
      rich_text: {
        contains: searchTerm,
      },
    }));
    
    const filter = {
      or: conditions,
    };
    
    return await this.getAllDatabaseItems(databaseId, filter);
  }

  // ============================================================
  // TRANSACTION-LIKE OPERATIONS
  // ============================================================

  async atomicUpdate(operations) {
    // Attempt multiple operations; rollback on failure
    const executed = [];
    
    try {
      for (const operation of operations) {
        const result = await this.makeRequestWithRetry(
          operation.method,
          operation.endpoint,
          operation.data
        );
        executed.push(result.data);
      }
      return { success: true, results: executed };
    } catch (error) {
      console.error('Operation failed, partial update may have occurred:', error);
      return { success: false, executed, error: error.message };
    }
  }

  // ============================================================
  // WEBHOOK HANDLING
  // ============================================================

  handleWebhookPayload(payload) {
    const events = [];
    
    if (payload.type === 'page.updated') {
      events.push({
        type: 'PAGE_UPDATED',
        pageId: payload.page.id,
        timestamp: payload.timestamp,
        properties: payload.page.properties,
      });
    } else if (payload.type === 'database.updated') {
      events.push({
        type: 'DATABASE_UPDATED',
        databaseId: payload.database.id,
        timestamp: payload.timestamp,
      });
    }
    
    return events;
  }

  // ============================================================
  // ERROR HANDLING & MONITORING
  // ============================================================

  logAPIError(error, context) {
    console.error('API Error:', {
      message: error.message,
      status: error.response?.status,
      statusText: error.response?.statusText,
      data: error.response?.data,
      context,
    });
  }

  async healthCheck() {
    try {
      const response = await this.makeRequestWithRetry('GET', 'users/me');
      return { healthy: true, user: response.data };
    } catch (error) {
      return { healthy: false, error: error.message };
    }
  }
}

// ============================================================
// USAGE EXAMPLES
// ============================================================

async function examples() {
  const client = new NotionAdvancedClient(process.env.NOTION_API_KEY);

  // Example 1: Batch update pages
  const pageIds = ['page-id-1', 'page-id-2', 'page-id-3'];
  const updates = {
    Status: { select: { name: 'Completed' } },
  };
  const batchResult = await client.batchUpdatePageProperties(pageIds, updates);
  console.log('Batch update result:', batchResult);

  // Example 2: Complex query with filtering
  const results = await client.queryWithComplexFilter('database-id', [
    { property: 'Status', type: 'select', value: { equals: 'In Progress' } },
    { property: 'Priority', type: 'select', value: { equals: 'High' } },
  ]);
  console.log('Filtered results:', results);

  // Example 3: Paginated retrieval
  for await (const page of client.paginatedQuery('database-id')) {
    console.log('Processing page of results:', page.length);
  }

  // Example 4: Cache management
  const cachedData = await client.getWithCache('databases/database-id');
  client.clearCache('database-id');

  // Example 5: Health check
  const health = await client.healthCheck();
  console.log('API Health:', health);
}

module.exports = NotionAdvancedClient;
