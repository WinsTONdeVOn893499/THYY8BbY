# 代码生成时间: 2025-10-11 19:15:49
import sqlite3
from scrapy.exceptions import DropItem


# 定义一个Scrapy Item
class UserItem(scrapy.Item):
    first_name = scrapy.Field()
    last_name = scrapy.Field()


# 定义一个Scrapy Pipeline，用于防止SQL注入
class SQLInjectionPipeline(object):
    """
    Pipeline for preventing SQL injection by parameterized queries.
    """

    def __init__(self):
        # 初始化数据库连接（这里使用SQLite作为示例）
        self.conn = sqlite3.connect('users.db', check_same_thread=False)
        self.cur = self.conn.cursor()
        # 创建表（如果不存在）
        self.create_table()

    def create_table(self):
        """
        Create a SQLite table to store user data.
        """
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT
        )''')
        self.conn.commit()

    def process_item(self, item, spider):
        """
        This method is called for every item pipeline.
        """
        try:
            # 使用参数化查询防止SQL注入
            self.cur.execute("INSERT INTO users (first_name, last_name) VALUES (?, ?)", 
                            (item['first_name'], item['last_name']))
            self.conn.commit()
            # 返回item，使pipeline继续处理
            return item
        except sqlite3.IntegrityError:
            # 如果发生唯一性约束错误（例如重复的用户名），则丢弃该item
            raise DropItem("Duplicate item found. Item: %s" % item)
        except Exception as e:
            # 处理其他所有可能的异常
            spider.logger.error('Error while processing item: %s', e)
            raise e

    def close_spider(self, spider):
        """
        This method is called when the spider is closed.
        """
        # 关闭数据库连接
        self.cur.close()
        self.conn.close()
