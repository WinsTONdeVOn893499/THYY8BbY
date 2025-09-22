# 代码生成时间: 2025-09-22 18:44:27
import os
from PIL import Image
from scrapy import signals
from scrapy.exceptions import NotConfigured


class ImageSizeAdjuster:
    """
    Image Size Adjuster
    A tool for resizing images using the Python Imaging Library (PIL).
    
    Attributes:
        target_size (tuple): The target size for the images.
        quality (int): The quality of the output image.
    """
    def __init__(self, target_size=(300, 300), quality=85):
        self.target_size = target_size
        self.quality = quality
        
    def adjust_image_size(self, image_path, output_path):
        """
        Adjust the size of the image.
        
        Args:
            image_path (str): The file path of the image to resize.
            output_path (str): The file path where the resized image will be saved.
        
        Raises:
            FileNotFoundError: If the specified image file does not exist.
            IOError: If there is an issue reading or writing the image file.
        """
        try:
            with Image.open(image_path) as img:
                img = img.resize(self.target_size, Image.ANTIALIAS)
                img.save(output_path, quality=self.quality)
        except FileNotFoundError:
            print(f"Error: The file {image_path} does not exist.")
        except IOError as e:
            print(f"Error: An I/O error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Usage example
if __name__ == '__main__':
    image_resizer = ImageSizeAdjuster(target_size=(800, 600), quality=90)
    image_paths = [
        'path/to/image1.jpg',
        'path/to/image2.jpg',
        # Add more image paths as needed
    ]
    output_dir = 'path/to/output/directory'
    
    for image_path in image_paths:
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        image_resizer.adjust_image_size(image_path, output_path)