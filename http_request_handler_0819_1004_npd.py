# 代码生成时间: 2025-08-19 10:04:33
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured


# Define a custom Spider for handling HTTP requests
class HttpRequestSpider(scrapy.Spider):
    name = 'http_request_handler'
    allowed_domains = []  # Define allowed domains if needed

    def __init__(self, url, *args, **kwargs):
        super(HttpRequestSpider, self).__init__(*args, **kwargs)
        self.url = url

    def start_requests(self):
        """Start the requests to the given URL."""
        # Send the HTTP request to the specified URL
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        """Parse the response and extract data."""
        # Handle the response here
        # For example, you can extract data with response.css() or response.xpath()
        self.log('Finished request %s', response.url)
        # Return data or further process it

# Define a function to run the spider
def run_spider(url):
    try:
        # Create a CrawlerProcess with the project settings
        process = CrawlerProcess(get_project_settings())
        # Add the HttpRequestSpider to the process
        process.crawl(HttpRequestSpider, url=url)
        # Start the crawling process
        process.start()
    except NotConfigured as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == '__main__':
    url = 'http://example.com'  # Replace with the target URL
    run_spider(url)