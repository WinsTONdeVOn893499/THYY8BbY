# 代码生成时间: 2025-08-31 07:43:51
import scrapy
def check_response_size(response, min_size=1000):
    # 检查响应体大小是否符合预期
    return len(response.body) >= min_size

class ResponsiveSpider(scrapy.Spider):
    name = 'responsive_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com']

    def parse(self, response):
        # 检查响应是否有效
        if not check_response_size(response):
            self.logger.error('响应体过小，可能页面未完全加载。')
            return

        # 在这里处理响应数据，例如提取信息
        # 例如：提取页面标题
        title = response.css('title::text').get()

        # 假设我们根据页面的某些特征来判断是否为响应式设计
        # 这里只是一个示例，实际中需要根据具体情况来判断
        is_responsive = response.css('meta[name=viewport]::attr(content)').get() is not None

        # 输出结果
        yield {
            'title': title,
            'is_responsive': is_responsive,
        }
