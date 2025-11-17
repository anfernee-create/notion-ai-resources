// Update database properties in Notion
// Useful for batch updating content status

const { Client } = require('@notionhq/client');

const notion = new Client({
  auth: process.env.NOTION_TOKEN,
});

async function updateDatabase(pageId, properties) {
  try {
    const response = await notion.pages.update({
      page_id: pageId,
      properties: properties,
    });

    console.log('✓ Page updated successfully!');
    return response;
  } catch (error) {
    console.error('✗ Error updating page:', error.message);
    throw error;
  }
}

// Example: Update task status
async function updateTaskStatus(pageId, status) {
  return updateDatabase(pageId, {
    Status: {
      select: {
        name: status,
      },
    },
  });
}

// Example: Batch update multiple pages
async function batchUpdate(pageIds, properties) {
  const results = [];
  
  for (const pageId of pageIds) {
    try {
      const result = await updateDatabase(pageId, properties);
      results.push({ success: true, pageId, result });
    } catch (error) {
      results.push({ success: false, pageId, error: error.message });
    }
  }
  
  return results;
}

module.exports = { updateDatabase, updateTaskStatus, batchUpdate };
