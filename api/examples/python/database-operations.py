"""
Notion API Database Operations - Python Examples

Demonstrates CRUD operations on Notion databases using the official Python SDK.

Installation:
pip install notion-client posthog python-dotenv
"""

import atexit
import os
from notion_client import Client
from datetime import datetime, timedelta
from dotenv import load_dotenv
from posthog import Posthog

load_dotenv()

# Initialize the Notion client
notion = Client(auth=os.environ.get("NOTION_API_KEY"))

# Example database ID (replace with your own)
DATABASE_ID = "your-database-id-here"

posthog_client = Posthog(
    os.environ["POSTHOG_PROJECT_TOKEN"],
    host=os.environ.get("POSTHOG_HOST", "https://us.i.posthog.com"),
    enable_exception_autocapture=True,
)
atexit.register(posthog_client.shutdown)

SCRIPT_USER_ID = "database-operations-script"


def query_database(database_id, filter_params=None, sorts=None):
    """
    Query a database with optional filters and sorting.
    
    Args:
        database_id (str): The ID of the database
        filter_params (dict): Filter conditions
        sorts (list): Sort parameters
    
    Returns:
        list: Query results
    """
    try:
        query_payload = {"database_id": database_id}
        
        if filter_params:
            query_payload["filter"] = filter_params
        
        if sorts:
            query_payload["sorts"] = sorts
        
        response = notion.databases.query(**query_payload)
        results = response["results"]
        posthog_client.capture(
            distinct_id=SCRIPT_USER_ID,
            event="database_queried",
            properties={
                "has_filter": filter_params is not None,
                "has_sort": sorts is not None,
                "result_count": len(results),
            },
        )
        return results

    except Exception as e:
        print(f"Error querying database: {e}")
        posthog_client.capture_exception(e, SCRIPT_USER_ID)
        return []


def query_with_filters():
    """
    Example: Query with multiple filter conditions.
    """
    # Filter for tasks that are "In Progress" and high priority
    filters = {
        "and": [
            {
                "property": "Status",
                "select": {
                    "equals": "In Progress"
                }
            },
            {
                "property": "Priority",
                "select": {
                    "equals": "High"
                }
            }
        ]
    }
    
    results = query_database(DATABASE_ID, filter_params=filters)
    print(f"Found {len(results)} high-priority tasks in progress")
    return results


def query_with_date_filter():
    """
    Example: Query items due within next 7 days.
    """
    today = datetime.now().isoformat()
    next_week = (datetime.now() + timedelta(days=7)).isoformat()
    
    filters = {
        "and": [
            {
                "property": "Due Date",
                "date": {
                    "on_or_after": today
                }
            },
            {
                "property": "Due Date",
                "date": {
                    "on_or_before": next_week
                }
            }
        ]
    }
    
    results = query_database(DATABASE_ID, filter_params=filters)
    print(f"Tasks due in next 7 days: {len(results)}")
    return results


def create_page(database_id, properties):
    """
    Create a new page in a database.
    
    Args:
        database_id (str): The ID of the database
        properties (dict): Page properties
    
    Returns:
        dict: Created page object
    """
    try:
        new_page = notion.pages.create(
            parent={"database_id": database_id},
            properties=properties
        )
        print(f"Created page: {new_page['id']}")
        posthog_client.capture(
            distinct_id=SCRIPT_USER_ID,
            event="page_created",
            properties={"property_count": len(properties)},
        )
        return new_page

    except Exception as e:
        print(f"Error creating page: {e}")
        posthog_client.capture_exception(e, SCRIPT_USER_ID)
        return None


def create_task_example():
    """
    Example: Create a new task in the database.
    """
    properties = {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "Complete project documentation"
                    }
                }
            ]
        },
        "Status": {
            "select": {
                "name": "To Do"
            }
        },
        "Priority": {
            "select": {
                "name": "High"
            }
        },
        "Due Date": {
            "date": {
                "start": (datetime.now() + timedelta(days=3)).isoformat()
            }
        },
        "Tags": {
            "multi_select": [
                {"name": "Documentation"},
                {"name": "Important"}
            ]
        }
    }
    
    return create_page(DATABASE_ID, properties)


def update_page(page_id, properties):
    """
    Update properties of an existing page.
    
    Args:
        page_id (str): The ID of the page
        properties (dict): Properties to update
    
    Returns:
        dict: Updated page object
    """
    try:
        updated_page = notion.pages.update(
            page_id=page_id,
            properties=properties
        )
        print(f"Updated page: {page_id}")
        posthog_client.capture(
            distinct_id=SCRIPT_USER_ID,
            event="page_updated",
            properties={"updated_property_count": len(properties)},
        )
        return updated_page

    except Exception as e:
        print(f"Error updating page: {e}")
        posthog_client.capture_exception(e, SCRIPT_USER_ID)
        return None


def mark_task_complete(page_id):
    """
    Example: Mark a task as complete.
    """
    properties = {
        "Status": {
            "select": {
                "name": "Done"
            }
        },
        "Completed Date": {
            "date": {
                "start": datetime.now().isoformat()
            }
        }
    }

    result = update_page(page_id, properties)
    if result:
        posthog_client.capture(
            distinct_id=SCRIPT_USER_ID,
            event="task_marked_complete",
            properties={},
        )
    return result


def get_page(page_id):
    """
    Retrieve a specific page with all its properties.
    
    Args:
        page_id (str): The ID of the page
    
    Returns:
        dict: Page object
    """
    try:
        page = notion.pages.retrieve(page_id=page_id)
        return page
    
    except Exception as e:
        print(f"Error retrieving page: {e}")
        return None


def extract_page_properties(page):
    """
    Extract readable properties from a page object.
    
    Args:
        page (dict): Page object from Notion API
    
    Returns:
        dict: Simplified properties
    """
    properties = {}
    
    for prop_name, prop_value in page["properties"].items():
        prop_type = prop_value["type"]
        
        if prop_type == "title":
            properties[prop_name] = prop_value["title"][0]["plain_text"] if prop_value["title"] else ""
        
        elif prop_type == "rich_text":
            properties[prop_name] = prop_value["rich_text"][0]["plain_text"] if prop_value["rich_text"] else ""
        
        elif prop_type == "select":
            properties[prop_name] = prop_value["select"]["name"] if prop_value["select"] else None
        
        elif prop_type == "multi_select":
            properties[prop_name] = [item["name"] for item in prop_value["multi_select"]]
        
        elif prop_type == "date":
            properties[prop_name] = prop_value["date"]["start"] if prop_value["date"] else None
        
        elif prop_type == "number":
            properties[prop_name] = prop_value["number"]
        
        elif prop_type == "checkbox":
            properties[prop_name] = prop_value["checkbox"]
        
        elif prop_type == "url":
            properties[prop_name] = prop_value["url"]
        
        elif prop_type == "email":
            properties[prop_name] = prop_value["email"]
        
        elif prop_type == "phone_number":
            properties[prop_name] = prop_value["phone_number"]
    
    return properties


def bulk_update_example():
    """
    Example: Bulk update multiple pages.
    """
    # Query for all "To Do" tasks
    filters = {
        "property": "Status",
        "select": {
            "equals": "To Do"
        }
    }
    
    tasks = query_database(DATABASE_ID, filter_params=filters)
    
    # Update each task to "In Progress"
    updated_count = 0
    for task in tasks:
        properties = {
            "Status": {
                "select": {
                    "name": "In Progress"
                }
            }
        }
        
        if update_page(task["id"], properties):
            updated_count += 1
    
    print(f"Updated {updated_count} tasks to 'In Progress'")
    return updated_count


def archive_page(page_id):
    """
    Archive (soft delete) a page.
    
    Args:
        page_id (str): The ID of the page
    
    Returns:
        dict: Archived page object
    """
    try:
        archived_page = notion.pages.update(
            page_id=page_id,
            archived=True
        )
        print(f"Archived page: {page_id}")
        posthog_client.capture(
            distinct_id=SCRIPT_USER_ID,
            event="page_archived",
            properties={},
        )
        return archived_page

    except Exception as e:
        print(f"Error archiving page: {e}")
        posthog_client.capture_exception(e, SCRIPT_USER_ID)
        return None


def get_database_info(database_id):
    """
    Retrieve database metadata and schema.
    
    Args:
        database_id (str): The ID of the database
    
    Returns:
        dict: Database object
    """
    try:
        database = notion.databases.retrieve(database_id=database_id)
        return database
    
    except Exception as e:
        print(f"Error retrieving database: {e}")
        return None


def print_database_schema(database_id):
    """
    Print the schema of a database.
    """
    database = get_database_info(database_id)
    
    if database:
        print(f"Database: {database['title'][0]['plain_text']}")
        print("\nProperties:")
        
        for prop_name, prop_config in database["properties"].items():
            prop_type = prop_config["type"]
            print(f"  - {prop_name}: {prop_type}")
            
            if prop_type == "select" and "select" in prop_config:
                options = [opt["name"] for opt in prop_config["select"]["options"]]
                print(f"    Options: {', '.join(options)}")
            
            elif prop_type == "multi_select" and "multi_select" in prop_config:
                options = [opt["name"] for opt in prop_config["multi_select"]["options"]]
                print(f"    Options: {', '.join(options)}")


def search_pages(query, filter_type=None):
    """
    Search for pages across workspace.
    
    Args:
        query (str): Search query
        filter_type (str): Filter by 'page' or 'database'
    
    Returns:
        list: Search results
    """
    try:
        search_params = {"query": query}
        
        if filter_type:
            search_params["filter"] = {"property": "object", "value": filter_type}
        
        response = notion.search(**search_params)
        results = response["results"]
        posthog_client.capture(
            distinct_id=SCRIPT_USER_ID,
            event="pages_searched",
            properties={
                "query_length": len(query),
                "filter_type": filter_type,
                "result_count": len(results),
            },
        )
        return results

    except Exception as e:
        print(f"Error searching: {e}")
        posthog_client.capture_exception(e, SCRIPT_USER_ID)
        return []


# Main execution examples
if __name__ == "__main__":
    print("Notion API Database Operations Examples\n")
    
    # Example 1: Query database
    print("1. Querying database...")
    all_tasks = query_database(DATABASE_ID)
    print(f"Total tasks: {len(all_tasks)}\n")
    
    # Example 2: Create new task
    print("2. Creating new task...")
    new_task = create_task_example()
    if new_task:
        print(f"Task ID: {new_task['id']}\n")
    
    # Example 3: Query with filters
    print("3. Querying with filters...")
    filtered_tasks = query_with_filters()
    print()
    
    # Example 4: Print database schema
    print("4. Database schema:")
    print_database_schema(DATABASE_ID)
    print()
    
    # Example 5: Search pages
    print("5. Searching pages...")
    search_results = search_pages("project", filter_type="page")
    print(f"Found {len(search_results)} pages matching 'project'")
