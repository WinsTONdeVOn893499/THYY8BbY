# 代码生成时间: 2025-08-09 17:28:10
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider, Request
from scrapy.exceptions import NotConfigured
from urllib.parse import urlparse
from validators import url as validate_url


class URLValidatorSpider(Spider):
    name = 'url_validator'
    start_urls = [
        # Define the URLs to be validated here
        'https://www.example.com',
        'https://www.google.com',
        'htp://www.fakeurl.com',  # Invalid URL for testing
    ]

    def parse(self, response):
        # This method will not be used as we are directly checking URLs in start_requests
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.check_url_validity)

    def check_url_validity(self, response):
        # Check if the URL is valid using the validators library
        if validate_url(response.url):
            self.log(f"URL '{response.url}' is valid.")
        else:
            self.log(f"URL '{response.url}' is invalid.",
                     level=scrapy.log.ERROR)

    def log(self, message, level=None, **kwargs):
        # Custom log method to handle logging
        super().log(message, level=level, **kwargs)


# Crawler process setup
def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (compatible; URLValidatorSpider/1.0)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
    })
    process.crawl(URLValidatorSpider)
    process.start()

if __name__ == '__main__':
    main()

# Note: The validators library is required for this script to work.
#       Install it using `pip install validators` before running the script.