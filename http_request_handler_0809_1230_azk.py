# 代码生成时间: 2025-08-09 12:30:41
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured


# 定义一个HTTP请求处理器
class HttpRequestHandler:
    def __init__(self, url):
        """
        初始化HTTP请求处理器

        参数:
            url (str): 要请求的URL地址
        """
        self.url = url
        self.process = CrawlerProcess(get_project_settings())

    def fetch(self):
        """
        发送HTTP请求并获取响应

        返回:
            response (scrapy.Response): HTTP响应对象
        """
        try:
            # 创建一个Spider，用于发送请求
            class MySpider(Spider):
                name = 'my_spider'
                start_urls = [self.url]

                def parse(self, response):
                    return {
                        'status_code': response.status,
                        'body': response.body.decode('utf-8')
                    }

            # 启动CrawlerProcess，发送请求
            self.process.crawl(MySpider)
            self.process.start()

            # 获取响应结果
            for result in self.process.results:
                yield result

        except Exception as e:
            # 错误处理
            yield {
                'error': str(e)
            }

    def fetch_all(self):
        """
        发送HTTP请求并获取所有响应

        返回:
            results (list): 所有响应结果的列表
        """
        results = []
        for result in self.fetch():
            results.append(result)
        return results


# 示例用法
if __name__ == '__main__':
    url = 'http://example.com'
    handler = HttpRequestHandler(url)
    results = handler.fetch_all()
    for result in results:
        print(result)