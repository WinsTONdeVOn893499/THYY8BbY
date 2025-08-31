# 代码生成时间: 2025-09-01 07:22:47
import os
import shutil
from scrapy.exceptions import NotConfigured


class FolderStructureOrganizer:
    def __init__(self, source_folder, destination_folder):
        """
        初始化文件夹结构整理器。

        :param source_folder: 源文件夹路径
        :param destination_folder: 目标文件夹路径
        """
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def check_folders(self):
        """
        检查源文件夹和目标文件夹是否存在，如果不存在则创建。
        """
        if not os.path.exists(self.source_folder):
            raise NotConfigured(f"源文件夹 {self.source_folder} 不存在。")
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

    def organize(self):
        """
        整理文件夹结构，将源文件夹中的所有文件移动到目标文件夹。
        """
        self.check_folders()
        for item in os.listdir(self.source_folder):
            source_path = os.path.join(self.source_folder, item)
            destination_path = os.path.join(self.destination_folder, item)
            if os.path.isfile(source_path):
                try:
                    shutil.move(source_path, destination_path)
                    print(f"文件 {item} 已移动到 {destination_folder}")
                except Exception as e:
                    print(f"移动文件 {item} 时发生错误：{e}")
            elif os.path.isdir(source_path):
                # 递归整理子文件夹
                self.organize_subfolder(source_path, destination_path)

    def organize_subfolder(self, source_path, destination_path):
        """
        递归整理子文件夹。

        :param source_path: 子文件夹的源路径
        :param destination_path: 子文件夹的目标路径
        """
        # 如果目标路径不存在，则创建它
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        # 递归整理子文件夹中的文件
        for item in os.listdir(source_path):
            source_item_path = os.path.join(source_path, item)
            destination_item_path = os.path.join(destination_path, item)
            if os.path.isfile(source_item_path):
                try:
                    shutil.move(source_item_path, destination_item_path)
                    print(f"文件 {item} 已移动到 {destination_item_path}")
                except Exception as e:
                    print(f"移动文件 {item} 时发生错误：{e}")


# 使用示例
if __name__ == '__main__':
    source_folder = '/path/to/source/folder'
    destination_folder = '/path/to/destination/folder'
    organizer = FolderStructureOrganizer(source_folder, destination_folder)
    organizer.organize()
