# 代码生成时间: 2025-09-16 13:13:15
import os
import shutil
from scrapy.exceptions import NotConfigured

"""
Folder Structure Organizer
This script will organize files in a given directory based on
file extensions into subdirectories.
"""

class FolderStructureOrganizer:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.extensions = {
            '.txt': 'Text Files',
            '.log': 'Log Files',
            '.pdf': 'PDF Documents',
            '.docx': 'Word Documents',
            '.xlsx': 'Excel Spreadsheets',
            '.png': 'Image Files',
            '.jpg': 'Image Files',
            '.jpeg': 'Image Files',
            '.mp3': 'Audio Files',
            '.mp4': 'Video Files',
        }

    def organize(self):
        """
        Organize files in the root directory into subdirectories
        based on their extensions.
        """
        if not os.path.exists(self.root_dir):
            raise NotConfigured(f"The directory '{self.root_dir}' does not exist.")

        for item in os.listdir(self.root_dir):
            full_path = os.path.join(self.root_dir, item)
            if os.path.isfile(full_path):
                self.move_file(full_path)

    def move_file(self, file_path):
        """
        Move a file to the appropriate subdirectory based on its extension.
        """
        extension = self.get_extension(file_path)
        if extension:
            dest_dir = os.path.join(self.root_dir, self.extensions[extension])
            self.create_directory(dest_dir)
            shutil.move(file_path, dest_dir)
            print(f'Moved {file_path} to {dest_dir}')
        else:
            print(f'Skipped {file_path}, no extension found.')

    def get_extension(self, file_path):
        """
        Extract the extension from a file path.
        """
        _, ext = os.path.splitext(file_path)
        return ext.lower()

    def create_directory(self, path):
        """
        Create a directory if it does not exist.
        """
        if not os.path.exists(path):
            os.makedirs(path)
            print(f'Created directory {path}')


if __name__ == '__main__':
    # Define the root directory to organize
    root_directory = '/path/to/your/directory'

    # Create an instance of FolderStructureOrganizer and organize the directory
    try:
        organizer = FolderStructureOrganizer(root_directory)
        organizer.organize()
    except NotConfigured as e:
        print(e)
    except Exception as e:
        print(f'An error occurred: {e}')
