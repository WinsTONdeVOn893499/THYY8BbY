# 代码生成时间: 2025-09-14 10:50:48
import scrapy
def __init__(self):
    # Initialize the scheduler
    self.scheduler = scrapy.crawler.CrawlerProcess()

    self.crawl_times = 0

    self.start_urls = [
        "http://example.com",
        "http://example.org",
    ]

    self.interval = 60  # Interval in seconds

    def schedule_next_job(self):
        # Schedule the next job
        self.crawl_times += 1
        if self.crawl_times < 10:  # Limit the number of crawls
            next_run = scrapy.utils.misc.estimate_next_run(self.interval, self.crawl_times)
            self.scheduler.schedule(next_run, self.run_spider, self.start_urls)
        else:
            print("Crawl limit reached. Stopping the scheduler.")
            self.scheduler.stop()

    def run_spider(self, start_urls):
        # Define the Spider class
        class MySpider(scrapy.Spider):
            name = "my_spider"
            start_urls = start_urls

            def parse(self, response):
                # Your parsing logic here
                print(f"Crawled {response.url}")
                # Here you can extract data or follow links

        # Run the spider
        self.scheduler.crawl(MySpider)
        self.schedule_next_job()

    def start(self):
        # Start the scheduler
        self.run_spider(self.start_urls)
        self.scheduler.start()

if __name__ == "__main__":
    scheduler = scheduled_job_spider()
    scheduler.start()