# 代码生成时间: 2025-09-03 13:02:41
import json
from scrapy import Request
from scrapy.http import Response
from scrapy.exceptions import DropItem


class ApiResponseFormatter:
    """
    A class used to format API responses into a standardized format.
    """

    def __init__(self, base_url, formatter_rules):
        """
        Initializes the ApiResponseFormatter with a base URL and a set of rules for formatting responses.
        :param base_url: The base URL of the API to be used for requests.
        :param formatter_rules: A dictionary of rules for formatting API responses.
        """
        self.base_url = base_url
        self.formatter_rules = formatter_rules

    def format_response(self, response):
        """
        Formats the API response according to the rules specified in the formatter_rules.
        :param response: The Response object received from the API call.
        :return: A formatted response or raises an error if formatting fails.
        """
        if not isinstance(response, Response):
            raise ValueError("response must be a scrapy Response object")

        # Check if response status is okay
        if response.status != 200:
            raise DropItem(f"API request failed with status code {response.status}")

        try:
            # Decode the JSON response
            api_response = response.json()
        except json.JSONDecodeError:
            raise DropItem("Invalid JSON response from API")

        # Apply the formatting rules to the API response
        formatted_response = {}
        for key, rule in self.formatter_rules.items():
            try:
                # Apply the rule to the response data
                formatted_response[key] = self.apply_rule(api_response, rule)
            except Exception as e:
                raise DropItem(f"Error formatting response with rule {rule}: {e}")

        return formatted_response

    def apply_rule(self, response_data, rule):
        "