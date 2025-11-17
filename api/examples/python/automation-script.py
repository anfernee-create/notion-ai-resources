# Notion workflow automation for solopreneurs
# Auto-archive, tag, and manage content

from notion_client import Client
import os
from datetime import datetime, timedelta

notion = Client(auth=os.environ["NOTION_TOKEN"])

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
    print(f"Archived {len(results['results'])} tasks")

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

if __name__ == "__main__":
    db_id = os.environ.get("NOTION_DATABASE_ID")
    archive_completed_tasks(db_id)
    auto_tag_content(db_id)
    print("Automation complete!")
