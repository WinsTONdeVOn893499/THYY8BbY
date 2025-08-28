# 代码生成时间: 2025-08-29 07:57:41
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured
from scrapy.utils.project import get_project_settings

class MemoryUsageSpider(scrapy.Spider):
    name = 'memory_usage'
    allowed_domains = []  # 留空，因为不需要爬取特定域的内容
    start_urls = []  # 留空，因为不需要爬取特定页面

    def __init__(self, *args, **kwargs):
        super(MemoryUsageSpider, self).__init__(*args, **kwargs)
        self.process = None
        if not self.settings.get('MEMORY_USAGE_ENABLED'):
            raise NotConfigured('Memory usage monitoring is not enabled.')
        self.process = psutil.Process()

    def start_requests(self):
        # 此方法留空，因为不需要发出请求
        pass

    def parse(self, response):
        # 此方法留空，因为不需要解析响应
        pass

    def closed(self, reason):
        # 在关闭spider时，收集内存使用情况
        self.log('Spider closed. Reason: %s' % reason)
        if self.process:
            self.log('Memory usage: %s' % self.process.memory_info().rss)

# 设置文件
class MemoryUsageSettings(object):
    def get_project_settings(self):
        return get_project_settings()

    def get(self, setting):
        if setting == 'MEMORY_USAGE_ENABLED':
            return True  # 这里可以根据需要调整为False来禁用内存使用监控
        return self.get_project_settings().get(setting)

# 运行爬虫
if __name__ == '__main__':
    process = CrawlerProcess(settings=MemoryUsageSettings())
    try:
        process.crawl(MemoryUsageSpider)
        process.start()
    except KeyboardInterrupt:
        pass
    finally:
        process.stop()