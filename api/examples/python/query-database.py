# Query Notion database with filters
# Perfect for solopreneurs managing content workflows

from notion_client import Client
import atexit
import os
from dotenv import load_dotenv
from posthog import Posthog

load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])
database_id = os.environ["NOTION_DATABASE_ID"]

posthog_client = Posthog(
    os.environ["POSTHOG_PROJECT_TOKEN"],
    host=os.environ.get("POSTHOG_HOST", "https://us.i.posthog.com"),
    enable_exception_autocapture=True,
)
atexit.register(posthog_client.shutdown)

SCRIPT_USER_ID = "query-database-script"

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
        posthog_client.capture_exception(e, SCRIPT_USER_ID)
        return []

# Example 1: Get all published posts
def get_published_posts():
    filter_params = {
        "property": "Status",
        "select": {"equals": "Published"}
    }
    results = query_database(database_id, filter_params)
    posthog_client.capture(
        distinct_id=SCRIPT_USER_ID,
        event="published_posts_fetched",
        properties={"result_count": len(results)},
    )
    return results

# Example 2: Get recent content (sorted by date)
def get_recent_content(limit=10):
    sorts = [{"property": "Created", "direction": "descending"}]
    all_results = query_database(database_id, sorts=sorts)
    results = all_results[:limit]
    posthog_client.capture(
        distinct_id=SCRIPT_USER_ID,
        event="recent_content_fetched",
        properties={"limit": limit, "result_count": len(results)},
    )
    return results

# Example 3: Filter by multiple tags
def get_posts_by_tags(tags):
    filter_params = {
        "and": [
            {"property": "Tags", "multi_select": {"contains": tag}}
            for tag in tags
        ]
    }
    results = query_database(database_id, filter_params)
    posthog_client.capture(
        distinct_id=SCRIPT_USER_ID,
        event="posts_by_tags_fetched",
        properties={"tag_count": len(tags), "result_count": len(results)},
    )
    return results

# Example 4: Get drafts older than a date
def get_old_drafts(date_str="2024-01-01"):
    filter_params = {
        "and": [
            {"property": "Status", "select": {"equals": "Draft"}},
            {"property": "Created", "date": {"before": date_str}}
        ]
    }
    results = query_database(database_id, filter_params)
    posthog_client.capture(
        distinct_id=SCRIPT_USER_ID,
        event="old_drafts_fetched",
        properties={"cutoff_date": date_str, "result_count": len(results)},
    )
    return results

if __name__ == "__main__":
    # Test queries
    print("Fetching published posts...")
    posts = get_published_posts()
    print(f"✓ Found {len(posts)} published posts")
    
    print("\nFetching recent content...")
    recent = get_recent_content(5)
    print(f"✓ Found {len(recent)} recent items")
