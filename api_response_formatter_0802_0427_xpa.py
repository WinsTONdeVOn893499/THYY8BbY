# 代码生成时间: 2025-08-02 04:27:33
import json
from scrapy.http import Response

"""
API响应格式化工具
"""

class ApiResponseFormatter:
    """
    用于格式化API响应的工具类
    """

    def __init__(self, response):
        self.response = response

    def format_response(self):
        """
        格式化API响应

        返回：
            dict -- 格式化后的响应数据
        """
        try:
            content = self.response.body
            # 假设响应内容是JSON格式
            formatted_data = json.loads(content)
            return formatted_data
        except json.JSONDecodeError:
            raise ValueError("响应内容不是有效的JSON格式")
        except Exception as e:
            raise Exception(f"格式化响应时出现错误：{e}")

    def format_response_as_dict(self):
        """
        将格式化后的响应数据转换为字典

        返回：
            dict -- 格式化后的响应数据字典
        """
        formatted_data = self.format_response()
        return formatted_data

# 示例用法
if __name__ == '__main__':
    # 假设我们有一个Scrapy Response对象
    class MockResponse:
        def __init__(self, body):
            self.body = body

    mock_response = MockResponse('{"key": "value"}')
    formatter = ApiResponseFormatter(mock_response)
    try:
        formatted_data = formatter.format_response_as_dict()
        print(formatted_data)
    except Exception as e:
        print(f"错误：{e}")