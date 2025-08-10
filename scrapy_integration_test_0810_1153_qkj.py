# 代码生成时间: 2025-08-10 11:53:40
import unittest
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
from scrapy.spiders import Spider
from scrapy.item import Item
from scrapy.exceptions import CloseSpider


# Define the Item class
class ExampleItem(Item):
    example_field = fields.String()


# Define a sample Spider which inherits from Scrapy Spider
class ExampleSpider(Spider):
    name = "example_spider"
    start_urls = ["http://example.com"]

    def parse(self, response):
        item = ExampleItem()
        item["example_field"] = "example_value"
        yield item


# Define the Scrapy CrawlerProcess
class ScrapyIntegrationTest(unittest.TestCase):
    def setUp(self):
        # Create settings
        self.settings = Settings()
        self.settings.setmodule("scrapy_settings")

        # Create CrawlerProcess with settings
        self.process = CrawlerProcess(self.settings)

    def test_spider(self):
        # Instantiate the spider
        spider = ExampleSpider()

        # Add the spider to the CrawlerProcess
        self.process.crawl(spider)

        # Start the crawl. This will also close the spider when done.
        try:
            self.process.start()
        except CloseSpider as e:
            self.fail(f"Spider closed unexpectedly: {e}")

        # Check that the spider has been closed properly
        self.assertTrue(spider.closed)

        # If you need to access the items collected by the spider, you can do so:
        # self.assertEqual(len(self.process.spider.crawler.stats.get_value("item_scraped_count")), 1)


# Run the tests
if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)