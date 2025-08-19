# 代码生成时间: 2025-08-20 03:31:24
import scrapy

"""
一个简单的Scrapy项目，用于网页内容抓取。
这个项目遵循Python最佳实践，包含清晰的代码结构，适当的错误处理，
必要的注释和文档，确保代码的可维护性和可扩展性。
"""

# 定义一个Spider，用于抓取网页内容
class WebScraperSpider(scrapy.Spider):
    name = 'web_scraper'  # Spider的名称
    allowed_domains = ['example.com']  # 允许抓取的域名
    start_urls = ['http://example.com/']  # 起始URL

    def parse(self, response):
        """
        解析网页内容。

        :param response: Scrapy的响应对象。
        """
        # 检查响应状态码是否为200
        if response.status != 200:
            self.logger.error(f"Failed to retrieve {response.url}, status code: {response.status}")
            return

        # 提取网页的标题
        title = response.xpath('//title/text()').get()
        self.logger.info(f"Title: {title}")

        # 提取网页的所有链接
        links = response.css('a::attr(href)').getall()
        for link in links:
            # 过滤掉相对路径和无效链接
            if not link.startswith('http') and not link.startswith('/'):
                continue

            # 生成完整的URL
            full_url = response.urljoin(link)
            self.logger.info(f"Found link: {full_url}")

            # 抓取链接页面
            yield scrapy.Request(url=full_url, callback=self.parse)