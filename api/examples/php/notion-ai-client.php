<?php
/**
 * Notion AI API Client for PHP
 * Simple client for solopreneurs using PHP
 */

class NotionAIClient {
    private $token;
    private $apiUrl = 'https://api.notion.com/v1';
    private $version = '2022-06-28';
    
    public function __construct($token) {
        $this->token = $token;
    }
    
    private function request($method, $endpoint, $data = null) {
        $ch = curl_init($this->apiUrl . $endpoint);
        
        $headers = [
            'Authorization: Bearer ' . $this->token,
            'Notion-Version: ' . $this->version,
            'Content-Type: application/json'
        ];
        
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        
        if ($method === 'POST') {
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        } elseif ($method === 'PATCH') {
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PATCH');
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        }
        
        $response = curl_exec($ch);
        curl_close($ch);
        
        return json_decode($response, true);
    }
    
    public function queryDatabase($databaseId, $filter = null) {
        $data = [];
        if ($filter) {
            $data['filter'] = $filter;
        }
        return $this->request('POST', "/databases/{$databaseId}/query", $data);
    }
    
    public function createPage($parentId, $properties) {
        $data = [
            'parent' => ['database_id' => $parentId],
            'properties' => $properties
        ];
        return $this->request('POST', '/pages', $data);
    }
    
    public function updatePage($pageId, $properties) {
        $data = ['properties' => $properties];
        return $this->request('PATCH', "/pages/{$pageId}", $data);
    }
}

// Usage example
$token = getenv('NOTION_TOKEN');
$databaseId = getenv('NOTION_DATABASE_ID');

$client = new NotionAIClient($token);

// Query database
$results = $client->queryDatabase($databaseId);
echo "Found " . count($results['results']) . " pages\n";

// Create a new page
$newPage = $client->createPage($databaseId, [
    'Name' => [
        'title' => [
            ['text' => ['content' => 'New Task from PHP']]
        ]
    ]
]);
echo "Created page: " . $newPage['id'] . "\n";

?>
