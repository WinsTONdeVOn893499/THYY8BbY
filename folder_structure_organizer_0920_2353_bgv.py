# 代码生成时间: 2025-09-20 23:53:05
import os
import shutil
from scrapy.exceptions import NotConfigured

"""
Folder Structure Organizer using Scrapy

This script is designed to organize a folder's structure by:
1. Moving files into a specified subfolder based on their extensions.
2. Renaming files according to a naming convention if needed.
3. Ensuring the directories exist before moving files.
"""

class FolderStructureOrganizer:
    def __init__(self, root_folder, extension_map=None):
        """
        Initialize the Folder Structure Organizer.

        :param root_folder: The path to the root folder to be organized.
        :param extension_map: A dictionary mapping file extensions to their respective subfolder names.
        """
        self.root_folder = root_folder
        self.extension_map = extension_map if extension_map else {}

    def ensure_directory(self, path):
        "