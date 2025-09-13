# 代码生成时间: 2025-09-14 07:18:19
import os
from PIL import Image
from scrapy.exceptions import DropItem

"""
图片尺寸批量调整器

这个脚本用于批量调整指定目录下所有图片的尺寸。
"""

class ImageSizeAdjuster:
    def __init__(self, folder_path, target_width, target_height):
        """
        初始化图片尺寸调整器
        :param folder_path: 要处理的图片文件夹路径
        :param target_width: 目标宽度
        :param target_height: 目标高度
        """
        self.folder_path = folder_path
        self.target_width = target_width
        self.target_height = target_height

    def adjust_image_sizes(self):
        """
        批量调整图片尺寸
        """
        for filename in os.listdir(self.folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(self.folder_path, filename)
                try:
                    self.process_image(file_path)
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    def process_image(self, file_path):
        """
        处理单个图片
        :param file_path: 图片文件路径
        """
        with Image.open(file_path) as img:
            # 调整图片尺寸
            resized_img = img.resize((self.target_width, self.target_height), Image.ANTIALIAS)
            # 保存调整后的图片
            resized_img.save(file_path)
            print(f"Adjusted image size for {file_path}")

    def run(self):
        """
        运行图片尺寸调整器
        """
        self.adjust_image_sizes()

# 示例用法
if __name__ == '__main__':
    adjuster = ImageSizeAdjuster('path/to/your/images', 800, 600)  # 指定文件夹路径和目标尺寸
    adjuster.run()