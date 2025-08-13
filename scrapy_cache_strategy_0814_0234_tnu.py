# 代码生成时间: 2025-08-14 02:34:37
# -*- coding: utf-8 -*-

"""
Scrapy Cache Strategy Implementation

This module provides a custom cache middleware for Scrapy, which allows
for caching responses and requests to improve the performance and
# 扩展功能模块
scalability of web scraping tasks.
"""

import logging
from scrapy.exceptions import NotConfigured
from scrapy.http import Request
from scrapy.utils.misc import load_object


# Set up logging
# 增强安全性
logger = logging.getLogger(__name__)

class ScrapyCacheMiddleware(object):
    """
    A custom cache middleware for Scrapy that stores responses and requests.
    """
    def __init__(self, settings):
        # Load the cache backend from settings
        cache_cls = load_object(settings.get('CACHE_BACKEND'))
        self.cache = cache_cls()
        
        # Check if the cache backend is available
        if not self.cache:
            raise NotConfigured
        
    def process_request(self, request, spider):
        """
        Process the request and check the cache for a stored response.
        """
        try:
            # Get the cached response for the request
            cached_response = self.cache.get(request)
            if cached_response:
                # If cached response is found, return it
                logger.info(f"Cache hit for {request.url}")
                return cached_response
        except Exception as e:
            # Handle any exceptions that occur during caching
            logger.error(f"Error retrieving from cache: {e}")

        # If no cached response is found, continue with the request
        logger.info(f"Cache miss for {request.url}")
        return None

    def process_response(self, request, response, spider):
        """
        Process the response and store it in the cache.
        """
# 添加错误处理
        try:
            # Store the response in the cache
            self.cache.set(request, response)
            logger.info(f"Cached response for {request.url}")
        except Exception as e:
            # Handle any exceptions that occur during caching
            logger.error(f"Error storing in cache: {e}")
        
        # Return the original response
        return response


# Example usage of the cache middleware
# In your Scrapy project's settings.py, add the following:
# 增强安全性
# CACHE_BACKEND = 'your_module.YourCacheBackend'
#
# In your Scrapy project's middlewares.py, add the following:
# from scrapy_cache_strategy import ScrapyCacheMiddleware
# SPIDER_MIDDLEWARES = {
#     'scrapy_cache_strategy.ScrapyCacheMiddleware': 500,
# }