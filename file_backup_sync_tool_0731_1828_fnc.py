# 代码生成时间: 2025-07-31 18:28:41
import os
import shutil
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import NotConfigured

"""
File Backup and Sync Tool
This tool is designed to backup and sync files using Python and Scrapy framework.
It follows best practices for code structure, error handling, and documentation.
"""

class FileBackupSyncTool:
    def __init__(self, source_path, target_path):
        """
        Initialize the FileBackupSyncTool with source and target paths.
        Args:
            source_path (str): The path to the source directory.
            target_path (str): The path to the target directory.
        """
        self.source_path = source_path
        self.target_path = target_path
        self.settings = get_project_settings()
        
        # Check if the source and target paths exist
        if not os.path.exists(self.source_path):
            raise NotConfigured("Source path does not exist: {}".format(self.source_path))
        if not os.path.exists(self.target_path):
            raise NotConfigured("Target path does not exist: {}".format(self.target_path))
            
    def backup_files(self):
        """
        Backup files from the source directory to the target directory.
        This method creates a timestamped backup directory in the target path.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = os.path.join(self.target_path, "backup_{}".format(timestamp))
        os.makedirs(backup_dir, exist_ok=True)
        for filename in os.listdir(self.source_path):
            file_path = os.path.join(self.source_path, filename)
            if os.path.isfile(file_path):
                shutil.copy(file_path, backup_dir)
        print("Backup completed successfully.")
        
    def sync_files(self):
        """
        Synchronize files between the source and target directories.
        This method updates the target directory with any changes from the source directory.
        """
        for filename in os.listdir(self.source_path):
            file_path = os.path.join(self.source_path, filename)
            target_file_path = os.path.join(self.target_path, filename)
            if os.path.isfile(file_path):
                if not os.path.exists(target_file_path):
                    shutil.copy(file_path, self.target_path)
                else:
                    file_mtime = os.path.getmtime(file_path)
                    target_file_mtime = os.path.getmtime(target_file_path)
                    if file_mtime > target_file_mtime:
                        shutil.copy(file_path, self.target_path)
        print("Sync completed successfully.")

# Example usage
if __name__ == "__main__":
    source_path = "/path/to/source/directory"
    target_path = "/path/to/target/directory"
    tool = FileBackupSyncTool(source_path, target_path)
    tool.backup_files()
    tool.sync_files()