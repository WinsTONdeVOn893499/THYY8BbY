# 代码生成时间: 2025-10-10 02:35:19
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

# 定义Item
class MyItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

# 定义Spider
class MySpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/']

    def parse(self, response):
        # 提取数据
        item = MyItem()
        item['url'] = response.url
        item['title'] = response.css('title::text').get()
        item['content'] = response.css('body::text').get()

        # 保存数据到ORM
        # 此处假设有一个ORM框架，如Django ORM
        # from myapp.models import MyModel
        # my_model = MyModel(url=item['url'], title=item['title'], content=item['content'])
        # my_model.save()

        yield item

# 主函数
def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(MySpider)
    process.start()

if __name__ == '__main__':
    main()
