# 代码生成时间: 2025-09-08 17:43:11
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request


# 定义订单项目结构
class OrderItem(Item):
    order_id = Field()
    product_name = Field()
    quantity = Field()
    price = Field()
    total = Field()

# 订单处理蜘蛛
class OrderProcessingSpider(Spider):
    name = 'order_processing'
    allowed_domains = ['example.com']  # 假设订单信息在example.com上
    start_urls = ['https://example.com/orders']

    def parse(self, response):
        """解析订单页面"""
        orders = response.css('div.order')
        for order in orders:
            loader = ItemLoader(item=OrderItem(), selector=order)
            loader.add_css('order_id', 'span.order-id::text')
            loader.add_css('product_name', 'span.product-name::text')
            loader.add_css('quantity', 'span.quantity::text')
            loader.add_css('price', 'span.price::text')
            loader.add_css('total', 'span.total::text')
            yield loader.load_item()

        # 分页处理
        next_page = response.css('a.next-page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def close(self, reason):
        """关闭时要执行的操作"""
        if reason == 'finished':
            self.log('订单处理完成')
        else:
            self.log('订单处理异常关闭', level=logging.ERROR)

# 运行爬虫
def run_spider():
    process = CrawlerProcess()
    process.crawl(OrderProcessingSpider)
    process.start()

if __name__ == '__main__':
    run_spider()