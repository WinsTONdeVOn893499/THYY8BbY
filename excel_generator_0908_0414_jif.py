# 代码生成时间: 2025-09-08 04:14:12
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd


# 定义一个Scrapy项目中用于生成Excel文件的Spider类
class ExcelGeneratorSpider(scrapy.Spider):
    '''
    Excel生成器Spider，用于从给定的网站抓取数据并存储到Excel文件中。
    '''
    name = 'excel_generator'
    allowed_domains = []  # 设置允许抓取的域名
    start_urls = []  # 设置初始URL列表

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_settings = get_project_settings()
        self.data = []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''
        解析响应并提取数据的方法。
        这里需要根据具体的网站和数据结构进行实现。
        '''
        # 示例：提取网页中的数据
        self.data.extend(response.css('div::text').getall())

    def closed(self, reason):
        '''
        当Spider关闭时调用，用于保存数据到Excel文件。
        '''
        # 将数据转换为DataFrame
        df = pd.DataFrame(self.data, columns=['Data'])
        # 创建Workbook和Worksheet
        wb = Workbook()
        ws = wb.active
        # 将DataFrame添加到Worksheet
        for r in dataframe_to_rows(df, index=False, header=True):
            ws.append(r)
        # 保存Workbook
        wb.save('output.xlsx')
        self.log('Excel file saved to output.xlsx')

# 启动Scrapy爬虫
def run_crawler():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ExcelGeneratorSpider)
    process.start()

if __name__ == '__main__':
    run_crawler()