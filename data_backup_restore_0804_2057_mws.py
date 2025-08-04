# 代码生成时间: 2025-08-04 20:57:34
import os
import json
from scrapy import signals
from scrapy.exceptions import NotConfigured
from twisted.python.failure import Failure


# 数据备份恢复类
class DataBackupRestore:
    """
    用于数据备份和恢复的类。
    """
    def __init__(self, backup_dir='backups', data_dir='data'):
        self.backup_dir = backup_dir
        self.data_dir = data_dir
        self._check_directories()

    def _check_directories(self):
        """检查备份和数据目录是否存在，不存在则创建。"""
        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)

    def backup(self, filename, data):
        """
        备份数据。
        :param filename: 备份文件的名称
        :param data: 要备份的数据
        """
        try:
            with open(os.path.join(self.backup_dir, filename), 'w') as f:
                json.dump(data, f)
        except Exception as e:
            raise NotConfigured(f'备份数据失败: {e}')

    def restore(self, filename):
        """
        恢复数据。
        :param filename: 要恢复的备份文件的名称
        """
        try:
            with open(os.path.join(self.backup_dir, filename), 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise NotConfigured(f'备份文件 {filename} 不存在')
        except Exception as e:
            raise NotConfigured(f'恢复数据失败: {e}')


# Scrapy 扩展
class DataBackupRestoreExtension:
    """
    Scrapy 扩展，用于在爬虫关闭时自动备份数据。
    """
    def __init__(self, stats):
        self.stats = stats
        self.backup_restore = DataBackupRestore()

    @classmethod
    def from_crawler(cls, crawler):
        """
        从爬虫中提取并初始化扩展。
        """
        extension = cls(crawler.stats)
        crawler.signals.connect(extension.spider_closed, signal=signals.spider_closed)
        return extension

    def spider_closed(self):
        """爬虫关闭时调用，备份数据。"""
        if self.stats.get_value('item_scraped_count', 0) > 0:
            try:
                self.backup_restore.backup('data_backup.json', {'items_scraped': self.stats.get_value('item_scraped_count', 0)})
            except NotConfigured as e:
                self._log_failure(e)

    def _log_failure(self, failure):
        "