# 代码生成时间: 2025-10-13 18:25:08
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BlockChain Node Manager
This module provides functionality to manage blockchain nodes.
It includes adding, removing, and querying nodes.
"""

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import NotConfigured


# Define a custom Spider for managing blockchain nodes
class BlockchainNodeSpider(scrapy.Spider):
    '''
    Spider to manage blockchain nodes.
    It allows adding, removing, and querying nodes.
    '''
    name = 'blockchain_node'
    allowed_domains = ['blockchain.com']
    start_urls = ['http://blockchain.com']

    def __init__(self):
        self.nodes = []
        self.node_id = 1
        self.node_info = {}
        super().__init__()

    def parse(self, response):
        # Extract nodes from the website
        nodes = response.xpath('//div[@class="node"]//text()').getall()
        for node in nodes:
            # Process each node and add to the list
            self.process_node(node)

    def process_node(self, node):
        try:
            # Validate and process the node data
            node_id = self.node_id
            self.node_id += 1
            self.nodes.append(node)
            self.node_info[node_id] = {'node': node, 'status': 'active'}
            yield {'node_id': node_id, 'node': node, 'status': 'active'}
        except Exception as e:
            self.logger.error(f'Error processing node {node}: {e}')

    def add_node(self, node):
        try:
            if node not in self.nodes:
                self.nodes.append(node)
                self.node_id += 1
                self.node_info[self.node_id] = {'node': node, 'status': 'active'}
                self.logger.info(f'Node {node} added successfully')
            else:
                self.logger.warning(f'Node {node} already exists')
        except Exception as e:
            self.logger.error(f'Error adding node {node}: {e}')

    def remove_node(self, node):
        try:
            if node in self.nodes:
                self.nodes.remove(node)
                self.logger.info(f'Node {node} removed successfully')
            else:
                self.logger.warning(f'Node {node} not found')
        except Exception as e:
            self.logger.error(f'Error removing node {node}: {e}')

    def query_node(self, node):
        try:
            if node in self.nodes:
                node_info = self.node_info[self.nodes.index(node)]
                self.logger.info(f'Node {node} info: {node_info}')
                return node_info
            else:
                self.logger.warning(f'Node {node} not found')
        except Exception as e:
            self.logger.error(f'Error querying node {node}: {e}')

# Example usage
if __name__ == '__main__':
    process = CrawlerProcess()
    spider = BlockchainNodeSpider()
    process.crawl(spider)
    process.start()
