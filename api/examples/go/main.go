package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

// NotionClient represents a client for the Notion API
type NotionClient struct {
	apiKey    string
	baseURL   string
	httpClient *http.Client
}

// NewNotionClient creates a new instance of NotionClient
func NewNotionClient(apiKey string) *NotionClient {
	return &NotionClient{
		apiKey:    apiKey,
		baseURL:   "https://api.notion.com/v1",
		httpClient: &http.Client{},
	}
}

// CreatePage creates a new page in Notion
func (c *NotionClient) CreatePage(parentID string, properties map[string]interface{}) (map[string]interface{}, error) {
	payload := map[string]interface{}{
		"parent": map[string]string{
			"database_id": parentID,
		},
		"properties": properties,
	}

	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("POST", c.baseURL+"/pages", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	req.Header.Set("Notion-Version", "2022-06-28")
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, _ := ioutil.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(respBody, &result)
	return result, nil
}

// QueryDatabase queries a Notion database
func (c *NotionClient) QueryDatabase(databaseID string, filter map[string]interface{}) ([]map[string]interface{}, error) {
	payload := map[string]interface{}{
		"filter": filter,
	}

	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("POST", c.baseURL+"/databases/"+databaseID+"/query", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	req.Header.Set("Notion-Version", "2022-06-28")
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, _ := ioutil.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(respBody, &result)

	if results, ok := result["results"].([]interface{}); ok {
		var pages []map[string]interface{}
		for _, item := range results {
			if page, ok := item.(map[string]interface{}); ok {
				pages = append(pages, page)
			}
		}
		return pages, nil
	}
	return nil, nil
}

// GetPage retrieves a specific page from Notion
func (c *NotionClient) GetPage(pageID string) (map[string]interface{}, error) {
	req, _ := http.NewRequest("GET", c.baseURL+"/pages/"+pageID, nil)
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	req.Header.Set("Notion-Version", "2022-06-28")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, _ := ioutil.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(respBody, &result)
	return result, nil
}

// UpdatePage updates a page in Notion
func (c *NotionClient) UpdatePage(pageID string, properties map[string]interface{}) (map[string]interface{}, error) {
	payload := map[string]interface{}{
		"properties": properties,
	}

	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("PATCH", c.baseURL+"/pages/"+pageID, bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	req.Header.Set("Notion-Version", "2022-06-28")
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, _ := ioutil.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(respBody, &result)
	return result, nil
}

// ArchivePage archives a page in Notion
func (c *NotionClient) ArchivePage(pageID string) (map[string]interface{}, error) {
	payload := map[string]bool{"archived": true}
	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("PATCH", c.baseURL+"/pages/"+pageID, bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	req.Header.Set("Notion-Version", "2022-06-28")
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, _ := ioutil.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(respBody, &result)
	return result, nil
}

// Search searches for pages and databases in Notion
func (c *NotionClient) Search(query string) (map[string]interface{}, error) {
	payload := map[string]string{"query": query}
	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("POST", c.baseURL+"/search", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+c.apiKey)
	req.Header.Set("Notion-Version", "2022-06-28")
	req.Header.Set("Content-Type", "application/json")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	respBody, _ := ioutil.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(respBody, &result)
	return result, nil
}

// Example usage
func main() {
	apiKey := os.Getenv("NOTION_API_KEY")
	if apiKey == "" {
		fmt.Println("NOTION_API_KEY environment variable not set")
		return
	}

	client := NewNotionClient(apiKey)

	// Create a new page
	properties := map[string]interface{}{
		"Title": map[string]interface{}{
			"title": []map[string]string{
				{"text": {"content": "Go API Test"}},
			},
		},
		"Status": map[string]interface{}{
			"status": map[string]string{"name": "In Progress"},
		},
	}

	databaseID := os.Getenv("NOTION_DATABASE_ID")
	if newPage, err := client.CreatePage(databaseID, properties); err == nil {
		fmt.Printf("Created page: %v\n", newPage["id"])
	} else {
		fmt.Printf("Error creating page: %v\n", err)
	}

	// Query database
	filter := map[string]interface{}{
		"property": "Status",
		"status": map[string]string{"equals": "In Progress"},
	}

	if pages, err := client.QueryDatabase(databaseID, filter); err == nil {
		fmt.Printf("Found %d pages\n", len(pages))
	} else {
		fmt.Printf("Error querying database: %v\n", err)
	}
}
