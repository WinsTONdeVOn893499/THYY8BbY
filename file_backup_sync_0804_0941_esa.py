# 代码生成时间: 2025-08-04 09:41:58
import os
import shutil
from scrapy.exceptions import NotConfigured

"""
文件备份和同步工具
该脚本使用Scrapy框架，通过定义Item和Pipeline实现文件的备份和同步功能。
"""

class FileBackupSync:
    def __init__(self, source_dir, backup_dir):
        """
        初始化函数
        :param source_dir: 源目录
        :param backup_dir: 备份目录
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir

    def backup_files(self):
        """
        备份文件
        """
        try:
            # 确保备份目录存在
            os.makedirs(self.backup_dir, exist_ok=True)

            # 遍历源目录中的所有文件
            for filename in os.listdir(self.source_dir):
                file_path = os.path.join(self.source_dir, filename)
                if os.path.isfile(file_path):
                    # 复制文件到备份目录
                    shutil.copy(file_path, self.backup_dir)
                    print(f"文件 {filename} 已备份到 {self.backup_dir}")
        except Exception as e:
            print(f"备份文件时出错：{e}")

    def sync_files(self):
        """
        同步文件
        """
        try:
            # 获取源目录和备份目录中的文件列表
            source_files = set(os.listdir(self.source_dir))
            backup_files = set(os.listdir(self.backup_dir))

            # 找出源目录中新增的文件
            new_files = source_files - backup_files
            for filename in new_files:
                file_path = os.path.join(self.source_dir, filename)
                if os.path.isfile(file_path):
                    # 复制文件到备份目录
                    shutil.copy(file_path, self.backup_dir)
                    print(f"文件 {filename} 已同步到 {self.backup_dir}")
        except Exception as e:
            print(f"同步文件时出错：{e}")


# 示例用法
if __name__ == "__main__":
    source_dir = "/path/to/source"
    backup_dir = "/path/to/backup"

    # 创建文件备份和同步工具实例
    file_backup_sync = FileBackupSync(source_dir, backup_dir)

    # 备份文件
    file_backup_sync.backup_files()

    # 同步文件
    file_backup_sync.sync_files()