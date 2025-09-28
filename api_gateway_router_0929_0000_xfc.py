# 代码生成时间: 2025-09-29 00:00:37
import json
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.spiders import Spider
from w3lib.url import canonicalize_url


class ApiGatewayRouter:
    def __init__(self, settings):
        """
        Initializes the ApiGatewayRouter
        :param settings: Scrapy settings
        """
        self.settings = settings
        self.routes = self.load_routes()

    def load_routes(self):
        """
        Loads the API routes from the settings
        :return: A dictionary of routes
        """
        try:
            routes = self.settings.get('API_ROUTES')
            if routes:
                return json.loads(routes)
            else:
                raise NotConfigured('API_ROUTES setting is not configured.')
        except json.JSONDecodeError:
            raise NotConfigured('Invalid JSON format for API_ROUTES setting.')

    def route(self, request, spider):
        """
        Routes the request to the appropriate spider based on the URL
        :param request: The Scrapy Request object
        :param spider: The Scrapy Spider object
        :return: The spider that will handle the request
        """
        url = canonicalize_url(request.url)
        for route in self.routes:
            if url.startswith(route['prefix']):
                return self.routes[route]['spider']
        raise ValueError(f"No spider found for URL: {url}")

    def handle_request(self, request):
        """
        Handles the request by routing it to the appropriate spider
        :param request: The Scrapy Request object
        :return: The response from the spider
        """
        try:
            spider_name = self.route(request, None)
            spider_cls = SpiderLoader(spider_name).load()
            spider = spider_cls()
            return spider.handle_request(request)
        except Exception as e:
            return {'error': str(e)}


class SpiderLoader:
    def __init__(self, spider_name):
        self.spider_name = spider_name

    def load(self):
        """
        Loads the spider class based on the spider name
        :return: The spider class
        """
        try:
            spider_cls = globals()[self.spider_name]
            return spider_cls
        except KeyError:
            raise ValueError(f"Spider not found: {self.spider_name}")


# Example usage
# settings = {'API_ROUTES': json.dumps({'/api/v1/users': {'spider': 'UserSpider', 'prefix': '/api/v1/users'}}})
# api_gateway_router = ApiGatewayRouter(settings)
# request = Request(url="https://example.com/api/v1/users")
# response = api_gateway_router.handle_request(request)
# print(response)