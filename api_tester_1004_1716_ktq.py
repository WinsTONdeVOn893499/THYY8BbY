# 代码生成时间: 2025-10-04 17:16:48
import scrapy
import json
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from urllib.parse import urlencode

# API测试工具
class ApiTester:
    """用于测试API的工具类"""

    def __init__(self, base_url):
        """初始化API测试工具

        Args:
            base_url (str): API的基础URL
        """
        self.base_url = base_url
        self.process = CrawlerProcess()

    def request(self, method, endpoint, params=None, headers=None, body=None):
        """发送请求到API

        Args:
            method (str): 请求方法（GET, POST, PUT, DELETE等）
            endpoint (str): 端点URL
            params (dict, optional): 查询参数. Defaults to None.
            headers (dict, optional): 请求头. Defaults to None.
            body (str, optional): 请求体. Defaults to None.

        Returns:
            dict: API响应的数据
        """
        url = self.base_url + endpoint

        if params:
            url += '?' + urlencode(params)

        callback = self._parse_response

        if method.upper() == 'GET':
            request = Request(url, callback=callback, headers=headers)
        elif method.upper() == 'POST':
            request = Request(url, callback=callback, method='POST', headers=headers, body=body)
        else:
            raise ValueError('Unsupported HTTP method')

        self.process.crawl(request)
        return self.process.start()

    def _parse_response(self, response):
        """解析响应数据

        Args:
            response (Response): Scrapy的响应对象
        """
        try:
            data = json.loads(response.body)
        except json.JSONDecodeError as e:
            print(f'Error parsing JSON: {e}')
            data = {}
        return data

# 示例用法
if __name__ == '__main__':
    tester = ApiTester('https://api.example.com/')
    params = {'key': 'value'}
    response_data = tester.request('GET', 'endpoint', params=params)
    print(response_data)
