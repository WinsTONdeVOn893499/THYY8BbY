# 代码生成时间: 2025-08-02 17:04:38
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.item import Item, Field
import random
import string
import json

# 定义Item结构
class TestDataItem(Item):
    name = Field()
    email = Field()
    age = Field()
    gender = Field()

# 创建测试数据生成器类
class TestDataGenerator:
    def __init__(self, num_records=100):
        self.num_records = num_records

    def generate_random_string(self, length=10):
        """生成随机字符串"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def generate_random_email(self):
        """生成随机邮箱"""
        return f"{self.generate_random_string(8)}@example.com"

    def generate_random_age(self):
        """生成随机年龄(18-100)"""
        return random.randint(18, 100)

    def generate_random_gender(self):
        "