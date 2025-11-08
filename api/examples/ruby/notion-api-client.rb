# Notion API Ruby Client
# Complete examples for Notion API operations

require 'http'
require 'json'

class NotionClient
  def initialize(api_key)
    @api_key = api_key
    @base_url = 'https://api.notion.com/v1'
  end

  private def headers
    {
      'Authorization' => "Bearer #{@api_key}",
      'Notion-Version' => '2022-06-28',
      'Content-Type' => 'application/json'
    }
  end

  private def make_request(method, endpoint, body = nil)
    uri = URI("#{@base_url}#{endpoint}")
    http = HTTP.headers(headers)
    
    response = case method
               when :get
                 http.get(uri)
               when :post
                 http.post(uri, json: body)
               when :patch
                 http.patch(uri, json: body)
               end
    
    JSON.parse(response.body.to_s)
  end

  # CREATE - Add new page to database
  def create_page(database_id, properties)
    body = {
      parent: { database_id: database_id },
      properties: properties
    }
    make_request(:post, '/pages', body)
  end

  # READ - Query database
  def query_database(database_id, filter: nil, sorts: nil)
    body = { database_id: database_id }
    body[:filter] = filter if filter
    body[:sorts] = sorts if sorts
    make_request(:post, "/databases/#{database_id}/query", body)
  end

  # READ - Get page
  def get_page(page_id)
    make_request(:get, "/pages/#{page_id}")
  end

  # READ - Get page content
  def get_page_blocks(page_id)
    make_request(:get, "/blocks/#{page_id}/children")
  end

  # UPDATE - Modify page
  def update_page(page_id, properties)
    body = { properties: properties }
    make_request(:patch, "/pages/#{page_id}", body)
  end

  # DELETE - Archive page
  def archive_page(page_id)
    body = { archived: true }
    make_request(:patch, "/pages/#{page_id}", body)
  end

  # SEARCH - Find pages
  def search(query, type: 'page')
    body = {
      query: query,
      filter: { value: type, property: 'object' }
    }
    make_request(:post, '/search', body)
  end
end

# Example Usage
if __FILE__ == $0
  client = NotionClient.new(ENV['NOTION_API_KEY'])
  
  # Create page
  new_page = client.create_page(
    ENV['DATABASE_ID'],
    {
      'Title' => {
        'title' => [{
          'type' => 'text',
          'text' => { 'content' => 'Ruby API Test' }
        }]
      },
      'Status' => {
        'status' => { 'name' => 'In Progress' }
      }
    }
  )
  
  puts "Created page: #{new_page['id']}"
  
  # Query database
  results = client.query_database(
    ENV['DATABASE_ID'],
    filter: {
      'property' => 'Status',
      'status' => { 'equals' => 'In Progress' }
    }
  )
  
  puts "Found #{results['results'].length} pages"
end
