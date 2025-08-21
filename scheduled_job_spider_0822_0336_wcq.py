# 代码生成时间: 2025-08-22 03:36:16
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
import logging
import os

# 配置日志
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

class ScheduledJobSpider(scrapy.Spider):
    name = "scheduled_job"
    allowed_domains = []
    start_urls = []

    def __init__(self, job_func=None, *args, **kwargs):
        super(ScheduledJobSpider, self).__init__(*args, **kwargs)
        self.job_func = job_func

    def start_requests(self):
        # 检查是否提供了任务函数
        if not self.job_func:
            raise ValueError("Job function is required")
        # 执行任务函数
        self.job_func()
        self.crawler.engine.close_spider(self, "Job completed")

# 任务函数示例：打印当前时间
def print_current_time():
    from datetime import datetime
    print("Current time: ", datetime.now())

# 定时任务调度器
class Scheduler:
    def __init__(self, interval, job_func):
        self.interval = interval  # 定时任务间隔（秒）
        self.job_func = job_func  # 任务函数
        self.process = None

    def start(self):
        # 开始定时任务
        self.process = reactor.addSystemEventTrigger(
            'before', 'shutdown', self.stop
        )
        reactor.callWhenRunning(self._run)

    def _run(self):
        # 执行任务函数，并在指定间隔后再次执行
        self.job_func()
        reactor.callLater(self.interval, self._run)

    def stop(self):
        # 停止定时任务
        reactor.removeSystemEventTrigger(self.process)

# 主函数
def main():
    job_func = print_current_time  # 任务函数
    interval = 10  # 定时任务间隔（秒）

    # 创建调度器
    scheduler = Scheduler(interval, job_func)
    scheduler.start()

    # 启动Scrapy处理器
    process = CrawlerProcess(get_project_settings())
    process.crawl(ScheduledJobSpider, job_func=job_func)
    process.start()
    reactor.run()

if __name__ == '__main__':
    main()