<?php
/**
 * Notion AI Resources - PHP CRUD Operations
 * Complete guide to Create, Read, Update, Delete operations using Notion API
 */

// Configure your Notion API key
define('NOTION_API_KEY', 'your-api-key-here');
define('NOTION_API_URL', 'https://api.notion.com/v1');
define('DATABASE_ID', 'your-database-id-here');

class NotionClient {
    private $apiKey;
    private $apiUrl;
    
    public function __construct($apiKey) {
        $this->apiKey = $apiKey;
        $this->apiUrl = NOTION_API_URL;
    }
    
    /**
     * Make API request to Notion
     */
    private function makeRequest($endpoint, $method = 'GET', $data = null) {
        $url = $this->apiUrl . $endpoint;
        
        $headers = [
            'Authorization: Bearer ' . $this->apiKey,
            'Notion-Version: 2022-06-28',
            'Content-Type: application/json'
        ];
        
        $options = [
            'http' => [
                'header' => implode("\r\n", $headers),
                'method' => $method,
            ]
        ];
        
        if ($data) {
            $options['http']['content'] = json_encode($data);
        }
        
        $context = stream_context_create($options);
        $response = file_get_contents($url, false, $context);
        
        return json_decode($response, true);
    }
    
    /**
     * CREATE - Add new page to database
     */
    public function createPage($databaseId, $properties) {
        $data = [
            'parent' => ['database_id' => $databaseId],
            'properties' => $properties
        ];
        
        return $this->makeRequest('/pages', 'POST', $data);
    }
    
    /**
     * READ - Query database
     */
    public function queryDatabase($databaseId, $filter = null, $sorts = null) {
        $data = ['database_id' => $databaseId];
        
        if ($filter) {
            $data['filter'] = $filter;
        }
        
        if ($sorts) {
            $data['sorts'] = $sorts;
        }
        
        return $this->makeRequest('/databases/' . $databaseId . '/query', 'POST', $data);
    }
    
    /**
     * READ - Retrieve single page
     */
    public function getPage($pageId) {
        return $this->makeRequest('/pages/' . $pageId);
    }
    
    /**
     * UPDATE - Modify page properties
     */
    public function updatePage($pageId, $properties) {
        $data = ['properties' => $properties];
        
        return $this->makeRequest('/pages/' . $pageId, 'PATCH', $data);
    }
    
    /**
     * DELETE - Archive page
     */
    public function deletePage($pageId) {
        $data = ['archived' => true];
        
        return $this->makeRequest('/pages/' . $pageId, 'PATCH', $data);
    }
}

// Example Usage
$notion = new NotionClient(NOTION_API_KEY);

// Create example
$newPage = $notion->createPage(DATABASE_ID, [
    'Title' => [
        'title' => [
            [
                'type' => 'text',
                'text' => ['content' => 'New AI Project']
            ]
        ]
    ],
    'Status' => [
        'status' => ['name' => 'In Progress']
    ],
    'Priority' => [
        'select' => ['name' => 'High']
    ]
]);

echo "Created page: " . $newPage['id'] . "\n";

// Read example - Query with filter
$results = $notion->queryDatabase(DATABASE_ID, [
    'property' => 'Status',
    'status' => ['equals' => 'In Progress']
]);

echo "Found " . count($results['results']) . " pages\n";

// Update example
if (!empty($results['results'])) {
    $pageId = $results['results'][0]['id'];
    
    $updated = $notion->updatePage($pageId, [
        'Priority' => [
            'select' => ['name' => 'Critical']
        ]
    ]);
    
    echo "Updated page: " . $pageId . "\n";
}

// Delete example
// $notion->deletePage($pageId);
// echo "Deleted page: " . $pageId . "\n";

?>
