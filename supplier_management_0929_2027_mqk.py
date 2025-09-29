# 代码生成时间: 2025-09-29 20:27:02
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider
from scrapy.utils.project import get_project_settings

"""
供应商管理系统
这个程序使用Scrapy框架来管理供应商信息
"""

class SupplierManager(scrapy.Spider):
    name = 'supplier_manager'
    allowed_domains = []  # 定义允许爬取的域
    start_urls = []    # 初始URL列表

    def __init__(self):
        self.suppliers = []  # 存储供应商信息的列表
        self.settings = get_project_settings()
        self.log_level = self.settings.get('LOG_LEVEL')

    def start_requests(self):
        """
        发送初始请求
        """
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        解析网页，处理供应商信息
        """
        try:
            # 假设供应商信息在一个表格中，且表格的class为'supplier-table'
            supplier_table = response.css('table.supplier-table::text').getall()
            for supplier in supplier_table:
                self.process_supplier(supplier)
        except Exception as e:
            self.logger.error(f'解析出错: {e}', level=self.log_level)
            raise CloseSpider('解析失败')

    def process_supplier(self, supplier_info):
        """
        处理单个供应商信息
        """
        try:
            # 假设供应商信息格式为'Name, Contact, Email'
            parts = supplier_info.split(',')
            name, contact, email = parts[0].strip(), parts[1].strip(), parts[2].strip()
            supplier = {'name': name, 'contact': contact, 'email': email}
            self.suppliers.append(supplier)
        except Exception as e:
            self.logger.error(f'处理供应商信息出错: {e}', level=self.log_level)

    def closed(self, reason):
        """
        爬虫关闭时执行的操作
        """
        self.logger.info(f'爬取结束, 共找到 {len(self.suppliers)} 个供应商')
        self.save_suppliers()

    def save_suppliers(self):
        """
        保存供应商信息到文件
        """
        with open('suppliers.json', 'w') as file:
            import json
            json.dump(self.suppliers, file, indent=4)

# 使用Scrapy CrawlerProcess运行爬虫
def run_spider():
    process = CrawlerProcess()
    process.crawl(SupplierManager)
    process.start()

if __name__ == '__main__':
    run_spider()