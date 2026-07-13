# Notion workflow automation for solopreneurs
# Auto-archive, tag, and manage content

from notion_client import Client
import os
import atexit
from datetime import datetime, timedelta
from dotenv import load_dotenv
from posthog import Posthog

load_dotenv()

notion = Client(auth=os.environ["NOTION_TOKEN"])

posthog_client = Posthog(
    os.environ["POSTHOG_PROJECT_TOKEN"],
    host=os.environ.get("POSTHOG_HOST", "https://us.i.posthog.com"),
    enable_exception_autocapture=True,
)
atexit.register(posthog_client.shutdown)

SCRIPT_USER_ID = "automation-script"

def archive_completed_tasks(db_id, days=30):
    """Archive old completed tasks"""
    cutoff = (datetime.now() - timedelta(days=days)).isoformat()
    results = notion.databases.query(
        database_id=db_id,
        filter={"and": [
            {"property": "Status", "select": {"equals": "Done"}},
            {"property": "Date", "date": {"before": cutoff}}
        ]}
    )
    for page in results["results"]:
        notion.pages.update(page_id=page["id"], archived=True)
    archived_count = len(results["results"])
    print(f"Archived {archived_count} tasks")
    posthog_client.capture(
        distinct_id=SCRIPT_USER_ID,
        event="tasks_archived",
        properties={"archived_count": archived_count, "cutoff_days": days},
    )

def auto_tag_content(db_id):
    """Auto-tag based on keywords"""
    tags_map = {
        "AI": ["ai", "automation", "gpt"],
        "Content": ["blog", "article", "post"]
    }
    results = notion.databases.query(database_id=db_id)
    for page in results["results"]:
        title = page["properties"].get("Name", {}).get("title", [{}])[0].get("plain_text", "").lower()
        tags = []
        for tag, keywords in tags_map.items():
            if any(k in title for k in keywords):
                tags.append({"name": tag})
        if tags:
            notion.pages.update(page_id=page["id"], properties={"Tags": {"multi_select": tags}})
    tagged_count = sum(
        1 for page in results["results"]
        if any(
            any(k in page["properties"].get("Name", {}).get("title", [{}])[0].get("plain_text", "").lower() for k in keywords)
            for keywords in tags_map.values()
        )
    )
    posthog_client.capture(
        distinct_id=SCRIPT_USER_ID,
        event="content_auto_tagged",
        properties={"tagged_count": tagged_count, "total_pages": len(results["results"])},
    )

if __name__ == "__main__":
    db_id = os.environ.get("NOTION_DATABASE_ID")
    archive_completed_tasks(db_id)
    auto_tag_content(db_id)
    print("Automation complete!")
