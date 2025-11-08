/**
 * Basic Notion API Query Example
 * 
 * This example demonstrates how to query a Notion database
 * using the official Notion JavaScript SDK.
 */

const { Client } = require('@notionhq/client');

// Initialize the Notion client
const notion = new Client({
  auth: process.env.NOTION_API_KEY,
});

/**
 * Query a database with basic filters
 */
async function queryDatabase(databaseId) {
  try {
    const response = await notion.databases.query({
      database_id: databaseId,
      filter: {
        property: 'Status',
        select: {
          equals: 'In Progress',
        },
      },
      sorts: [
        {
          property: 'Created',
          direction: 'descending',
        },
      ],
    });
    
    console.log(`Found ${response.results.length} pages`);
    return response.results;
  } catch (error) {
    console.error('Error querying database:', error);
    throw error;
  }
}

/**
 * Retrieve a page with all its properties
 */
async function getPage(pageId) {
  try {
    const page = await notion.pages.retrieve({ page_id: pageId });
    console.log('Page title:', page.properties.Name.title[0]?.plain_text);
    return page;
  } catch (error) {
    console.error('Error retrieving page:', error);
    throw error;
  }
}

/**
 * Create a new page in a database
 */
async function createPage(databaseId, title, status) {
  try {
    const response = await notion.pages.create({
      parent: { database_id: databaseId },
      properties: {
        Name: {
          title: [
            {
              text: {
                content: title,
              },
            },
          ],
        },
        Status: {
          select: {
            name: status,
          },
        },
      },
    });
    
    console.log('Created page:', response.id);
    return response;
  } catch (error) {
    console.error('Error creating page:', error);
    throw error;
  }
}

/**
 * Update page properties
 */
async function updatePage(pageId, newStatus) {
  try {
    const response = await notion.pages.update({
      page_id: pageId,
      properties: {
        Status: {
          select: {
            name: newStatus,
          },
        },
      },
    });
    
    console.log('Updated page:', response.id);
    return response;
  } catch (error) {
    console.error('Error updating page:', error);
    throw error;
  }
}

/**
 * Search for pages by title
 */
async function searchPages(query) {
  try {
    const response = await notion.search({
      query: query,
      filter: {
        property: 'object',
        value: 'page',
      },
      sort: {
        direction: 'descending',
        timestamp: 'last_edited_time',
      },
    });
    
    console.log(`Found ${response.results.length} matching pages`);
    return response.results;
  } catch (error) {
    console.error('Error searching:', error);
    throw error;
  }
}

// Usage examples
if (require.main === module) {
  const DATABASE_ID = 'your-database-id-here';
  
  // Query database
  queryDatabase(DATABASE_ID)
    .then(results => console.log('Query results:', results.length))
    .catch(console.error);
  
  // Create new page
  createPage(DATABASE_ID, 'New Task', 'To Do')
    .then(page => console.log('Created:', page.id))
    .catch(console.error);
  
  // Search for pages
  searchPages('project')
    .then(results => console.log('Search results:', results.length))
    .catch(console.error);
}

module.exports = {
  queryDatabase,
  getPage,
  createPage,
  updatePage,
  searchPages,
};
