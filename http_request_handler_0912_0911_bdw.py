# 代码生成时间: 2025-09-12 09:11:21
import scrapy
def http_request_handler(url, method='GET', headers=None, body=None):
    '''
    HTTP请求处理器
    :param url: 请求的URL地址
    :param method: 请求方法，默认为GET
    :param headers: 请求头部，字典格式
    :param body: 请求体，适用于POST请求
    :return: 响应内容
    '''
    # 检查请求方法是否合法
    if method.upper() not in ['GET', 'POST', 'PUT', 'DELETE']:
        raise ValueError('Invalid request method')

    # 初始化Scrapy的Request对象
    request = scrapy.Request(url=url, method=method, headers=headers, body=body)

    # 创建Scrapy的Spider对象
    class SimpleSpider(scrapy.Spider):
        name = 'simple_spider'
        start_urls = [url]

    spider = SimpleSpider()

    try:
        # 发送请求并获取响应
        response = scrapy.Request(url=url, method=method, headers=headers, body=body)
        yield response
    except Exception as e:
        # 捕获并处理异常
        print(f'Error occurred: {e}')
        # 可在这里记录日志，返回错误响应等

# 示例用法
def main():
    url = 'http://example.com'
    method = 'GET'
    headers = {'User-Agent': 'Mozilla/5.0'}
    body = None
    for response in http_request_handler(url, method, headers, body):
        print(response.status)
        print(response.body)

if __name__ == '__main__':
    main()