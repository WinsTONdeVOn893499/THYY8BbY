# 代码生成时间: 2025-08-25 18:50:04
import os
from scrapy.utils.project import get_project_settings
# 定义一个函数用于批量重命名文件

def batch_rename_files(directory, prefix, extension):
    """
    批量重命名指定目录下的文件。
    
    参数:
    directory (str): 文件所在的目录。
    prefix (str): 要添加的前缀。
    extension (str): 文件的扩展名。
    """
    # 检查目录是否存在
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # 获取目录下所有文件
    files = os.listdir(directory)
    
    # 遍历所有文件
    for index, file in enumerate(files, start=1):
        # 构造新文件名
        new_filename = f"{prefix}{index}{extension}"
        
        # 构造旧文件路径和新文件路径
        old_file_path = os.path.join(directory, file)
        new_file_path = os.path.join(directory, new_filename)
        
        # 重命名文件
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file}' to '{new_filename}'")
        except OSError as e:
            print(f"Error renaming '{file}' to '{new_filename}': {e}")

# 以下是使用示例
if __name__ == '__main__':
    # 指定目录
    directory = "path/to/your/files"
    
    # 文件前缀
    prefix = "new_"
    
    # 文件扩展名
    extension = ".txt"
    
    # 调用批量重命名函数
    batch_rename_files(directory, prefix, extension)