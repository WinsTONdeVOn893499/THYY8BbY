# 代码生成时间: 2025-07-31 09:26:04
import os
import sys
from PIL import Image
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Spider
from scrapy.item import Field, Item
from scrapy.exceptions import CloseSpider


# Define the image item structure with a field for the image file
class ImageItem(Item):
    image = Field()


# Define the Spider class for resizing images
class ImageResizerSpider(Spider):
    name = 'image_resizer'
    allowed_domains = []
    start_urls = []
    custom_settings = {
        'IMAGES_STORE': '/path/to/your/images',  # Define where to store resized images
    }

    def __init__(self, *args, **kwargs):
        # Initialize the spider with a list of image paths
        self.image_paths = kwargs.get('images', [])
        self.resized_images = []
        super(ImageResizerSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # Iterate over the image paths and resize each image
        for image_path in self.image_paths:
            try:
                with Image.open(image_path) as img:
                    # Define the new image size
                    new_size = (800, 600)
                    
                    # Resize the image
                    img = img.resize(new_size, Image.ANTIALIAS)
                    
                    # Get the image file name and path
                    image_name = os.path.basename(image_path)
                    
                    # Save the resized image to the specified path
                    new_image_path = os.path.join(self.custom_settings['IMAGES_STORE'], image_name)
                    img.save(new_image_path)
                    
                    # Add the resized image path to the list
                    self.resized_images.append(new_image_path)
            except IOError as e:
                self.logger.error(f'Error resizing image {image_path}: {e}')
                raise CloseSpider(f'Error resizing image {image_path}')

        # Return the list of resized images
        yield ImageItem(image=self.resized_images)


# Function to run the spider with a list of images
def run_spider(images):
    process = CrawlerProcess()
    process.crawl(ImageResizerSpider, images=images)
    process.start()

# Example usage:
if __name__ == '__main__':
    image_paths = ['/path/to/image1.jpg', '/path/to/image2.jpg']  # Replace with your image paths
    run_spider(image_paths)