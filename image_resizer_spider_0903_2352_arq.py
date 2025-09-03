# 代码生成时间: 2025-09-03 23:52:21
{
    """
    Image Resizer Spider is a Scrapy-based script designed to download and resize images.
# 添加错误处理
    """

    import os
    from PIL import Image
# 扩展功能模块
    from scrapy.crawler import CrawlerProcess
    from scrapy.spiders import CrawlSpider, Rule
    from scrapy.linkextractors import LinkExtractor
    from scrapy.selector import Selector
    from scrapy.http import Request
    from scrapy.exceptions import DropItem
# 改进用户体验

    class ImageResizerSpider(CrawlSpider):
        name = 'image_resizer'
        allowed_domains = []  # Define allowed domains
        start_urls = []  # Define start URLs
        download_delay = 1  # Define download delay

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.image_urls = set()

        def parse(self, response):
            # Check if the response is a success
            if not response.ok:
                self.logger.error(f"Failed to retrieve {response.url}")
                return

            # Add image URLs to the set
            for image_url in response.css('img::attr(src)').getall():
                if image_url not in self.image_urls:
                    self.image_urls.add(image_url)
                    yield response.follow(image_url, self.download_image, meta={'image_url': image_url})

            # Follow links to other pages
            yield from self.follow_links(response)

        def follow_links(self, response):
            # Extract links from the page
            link_extractor = LinkExtractor()
            links = link_extractor.extract_links(response)

            # Follow links to other pages
            for link in links:
                yield Request(url=link.url, callback=self.parse)

        def download_image(self, response):
            # Check if the response is an image
            if 'image' not in response.headers['Content-Type']:
                self.logger.error(f"Not an image: {response.url}")
# NOTE: 重要实现细节
                return

            # Save the image to disk
            self.logger.info(f"Downloading image: {response.url}")
            image_path = self.save_image(response)

            # Resize the image
            self.resize_image(image_path)
# 改进用户体验

        def save_image(self, response):
            # Define the image directory
            image_dir = 'images'
# FIXME: 处理边界情况
            if not os.path.exists(image_dir):
                os.makedirs(image_dir)

            # Save the image to disk
            image_path = os.path.join(image_dir, os.path.basename(response.url))
            with open(image_path, 'wb') as f:
                f.write(response.body)
            return image_path

        def resize_image(self, image_path):
            # Open the image
            image = Image.open(image_path)

            # Define the new size
            new_size = (800, 600)

            # Resize the image
            image = image.resize(new_size, Image.ANTIALIAS)

            # Save the resized image
            image.save(image_path)
            self.logger.info(f"Resized image: {image_path}")

    # Run the spider
    def run_spider():
        process = CrawlerProcess()
        process.crawl(ImageResizerSpider)
        process.start()

    if __name__ == '__main__':
        run_spider()
}