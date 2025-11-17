# Query Notion database with filters
# Perfect for solopreneurs managing content workflows

from notion_client import Client
import os
from dotenv import load_dotenv

load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])
database_id = os.environ["NOTION_DATABASE_ID"]

def query_database(database_id, filter_params=None, sorts=None):
    """Query database with optional filters and sorting"""
    try:
        response = notion.databases.query(
            database_id=database_id,
            filter=filter_params,
            sorts=sorts
        )
        return response["results"]
    except Exception as e:
        print(f"✗ Error querying database: {e}")
        return []

# Example 1: Get all published posts
def get_published_posts():
    filter_params = {
        "property": "Status",
        "select": {"equals": "Published"}
    }
    return query_database(database_id, filter_params)

# Example 2: Get recent content (sorted by date)
def get_recent_content(limit=10):
    sorts = [{"property": "Created", "direction": "descending"}]
    results = query_database(database_id, sorts=sorts)
    return results[:limit]

# Example 3: Filter by multiple tags
def get_posts_by_tags(tags):
    filter_params = {
        "and": [
            {"property": "Tags", "multi_select": {"contains": tag}}
            for tag in tags
        ]
    }
    return query_database(database_id, filter_params)

# Example 4: Get drafts older than a date
def get_old_drafts(date_str="2024-01-01"):
    filter_params = {
        "and": [
            {"property": "Status", "select": {"equals": "Draft"}},
            {"property": "Created", "date": {"before": date_str}}
        ]
    }
    return query_database(database_id, filter_params)

if __name__ == "__main__":
    # Test queries
    print("Fetching published posts...")
    posts = get_published_posts()
    print(f"✓ Found {len(posts)} published posts")
    
    print("\nFetching recent content...")
    recent = get_recent_content(5)
    print(f"✓ Found {len(recent)} recent items")
