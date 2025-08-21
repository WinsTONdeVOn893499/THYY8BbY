# 代码生成时间: 2025-08-21 15:26:50
import re
from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from scrapy.item import Field
from scrapy.exceptions import CloseSpider
from datetime import datetime
from typing import List, Dict


# 日志项的字段定义
class LogItem(ItemLoader):
    url = Field()
    level = Field()
    message = Field()
    timestamp = Field()

    # 定义日志项字段解析规则
    def default_input_processor(self, out):
        return out.strip()


# 日志解析工具类
class LogParser(Spider):
    name = 'log_parser'
    allowed_domains = []
    start_urls = []
    custom_settings = {
        'LOG_ENABLED': True,
        'LOG_FILE': 'path_to_log_file.log'
    }

    def __init__(self):
        super().__init__()
        self.log_file_path = self.custom_settings.get('LOG_FILE')

    def start_requests(self):
        if self.log_file_path is None:
            raise CloseSpider('Log file path is not provided in settings.')
        yield Request(self.log_file_path, callback=self.parse_log)

    def parse_log(self, response):
        if not response.body:
            raise CloseSpider('Log file is empty.')

        log_entries = self.parse_log_entries(response.text)
        for entry in log_entries:
            yield LogItem(item={'url': response.url}, response=entry)

    def parse_log_entries(self, log_content: str) -> List[Dict[str, str]]:
        """
        解析日志文件内容。

        :param log_content: 日志文件内容。
        :return: 解析后的日志项列表。
        """
        log_entries = []
        pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) (\w+) - (.+)')

        for line in log_content.split('
'):
            match = pattern.match(line)
            if match:
                timestamp, level, message = match.groups()
                log_entries.append({
                    'timestamp': self.convert_timestamp(timestamp),
                    'level': level,
                    'message': message
                })
            else:
                self.logger.warning(f'Unrecognized log line format: {line}')

        return log_entries

    def convert_timestamp(self, timestamp_str: str) -> datetime:
        """
        将日志时间戳字符串转换为datetime对象。

        :param timestamp_str: 需要转换的日志时间戳字符串。
        :return: datetime对象。
        """
        return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
