# 代码生成时间: 2025-08-19 01:59:10
# -*- coding: utf-8 -*-

"""
A responsive spider using Scrapy framework.
This spider is designed to handle responsive layouts by
emulating different viewport sizes.
"""

import scrapy
from scrapy.linkextractors import LinkExtractor
# 扩展功能模块
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider
from scrapy.http import Request
import random

class ResponsiveSpider(CrawlSpider):
    name = 'responsive_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/']
# NOTE: 重要实现细节

    # Define the link extractor with the rule to follow links
    link_extractor = LinkExtractor(allow=('/article/',))
    rules = (
        Rule(link_extractor, callback='parse_article', follow=True),
    )
# FIXME: 处理边界情况

    def __init__(self, *args, **kwargs):
        super(ResponsiveSpider, self).__init__(*args, **kwargs)
        # Initialize viewport sizes for responsive layout testing
        self.viewport_sizes = [
            (320, 480),  # Mobile
# 优化算法效率
            (768, 1024),  # Tablet
            (1024, 768),  # Small desktop
            (1280, 800),  # Large desktop
            (1366, 768),  # Typical laptop
            (1920, 1080),  # Large screen
# NOTE: 重要实现细节
        ]

    def start_requests(self):
        """
        Send out requests with different viewport sizes.
# 扩展功能模块
        This method is overridden from CrawlSpider to customize the request.
        """
        for url in self.start_urls:
            for width, height in self.viewport_sizes:
                yield Request(
                    url=url,
                    callback=self.parse_start_url,
                    meta={'viewport': {'width': width, 'height': height}},
                    dont_filter=True
                )

    def parse_start_url(self, response):
        """
        Parse the start URL with different viewport sizes.
        This method handles the initial page and extracts links.
        """
        # Log the viewport size for debugging purposes
        self.logger.info(f"Viewing {response.url} with viewport size {response.meta['viewport']}")
        # Follow the rules and extract links
        return super().parse_start_url(response)

    def parse_article(self, response):
        """
        Parse an article page.
        This method is the callback for article links.
        """
        # Extract article content
        title = response.css('h1::text').get()
        body = response.css('p::text').getall()
        yield {
            'title': title,
            'body': body,
            'url': response.url,
            'viewport': response.meta['viewport']
        }

    def closed(self, reason):
        """
        Handle spider closure.
# NOTE: 重要实现细节
        This method is called when the spider is closed.
        """
        if reason == 'finished':
            self.logger.info('Spider finished successfully')
        else:
# NOTE: 重要实现细节
            self.logger.error(f'Spider closed due to {reason}')
# 扩展功能模块
