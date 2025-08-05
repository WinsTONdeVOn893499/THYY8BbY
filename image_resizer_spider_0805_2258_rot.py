# 代码生成时间: 2025-08-05 22:58:11
import os
import scrapy
from PIL import Image
from scrapy.crawler import CrawlerProcess

"""
Image Resizer Spider

This spider is designed to resize images in a specified directory.
It includes error handling and is structured for easy understanding and maintenance.
"""

class ImageResizerSpider(scrapy.Spider):
    name = 'image_resizer'
    allowed_domains = []
    start_urls = []

    def __init__(self, input_dir='', output_dir='', image_size=(800, 600), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.image_size = image_size

    def parse(self, response):
        # Check if the input directory exists
        if not os.path.exists(self.input_dir):
            raise ValueError(f"Input directory '{self.input_dir}' does not exist.")

        # Check if the output directory exists, create if not
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        # List all files in the input directory
        for file_name in os.listdir(self.input_dir):
            file_path = os.path.join(self.input_dir, file_name)
            # Check if the file is an image
            if self.is_image(file_path):
                self.resize_image(file_path)

    def is_image(self, file_path):
        """
        Check if the file is an image.
        Supported formats: jpg, jpeg, png, gif.
        """
        img_formats = ('.jpg', '.jpeg', '.png', '.gif')
        if file_path.lower().endswith(img_formats):
            return True
        return False

    def resize_image(self, file_path):
        """
        Resize the image and save it to the output directory.
        """
        try:
            with Image.open(file_path) as img:
                resized_img = img.resize(self.image_size, Image.ANTIALIAS)
                output_file_path = os.path.join(
                    self.output_dir, os.path.basename(file_path))
                resized_img.save(output_file_path)
                self.logger.info(f"Image resized and saved to {output_file_path}")
        except IOError as e:
            self.logger.error(f"Error resizing image {file_path}: {e}")

# Example usage
if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ImageResizerSpider, input_dir='path_to_input_directory',
                   output_dir='path_to_output_directory', image_size=(800, 600))
    process.start()