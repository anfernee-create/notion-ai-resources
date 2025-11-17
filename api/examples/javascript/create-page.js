// Create a new page in a Notion database
// Perfect for solopreneurs automating content workflows

const { Client } = require('@notionhq/client');

const notion = new Client({
  auth: process.env.NOTION_TOKEN,
});

async function createPage() {
  try {
    const response = await notion.pages.create({
      parent: {
        database_id: process.env.NOTION_DATABASE_ID,
      },
      properties: {
        Name: {
          title: [
            {
              text: {
                content: 'New Content Idea',
              },
            },
          ],
        },
        Status: {
          select: {
            name: 'In Progress',
          },
        },
        Tags: {
          multi_select: [
            { name: 'Content' },
            { name: 'AI' },
          ],
        },
      },
      children: [
        {
          object: 'block',
          type: 'heading_2',
          heading_2: {
            rich_text: [
              {
                type: 'text',
                text: {
                  content: 'Getting Started',
                },
              },
            ],
          },
        },
        {
          object: 'block',
          type: 'paragraph',
          paragraph: {
            rich_text: [
              {
                type: 'text',
                text: {
                  content: 'This page was created automatically using the Notion API.',
                },
              },
            ],
          },
        },
      ],
    });

    console.log('✓ Page created successfully!');
    console.log('Page ID:', response.id);
    console.log('URL:', response.url);
    return response;
  } catch (error) {
    console.error('✗ Error creating page:', error.message);
    throw error;
  }
}

// Run if called directly
if (require.main === module) {
  createPage();
}

module.exports = { createPage };
