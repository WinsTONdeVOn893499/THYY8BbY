# 代码生成时间: 2025-10-02 16:21:50
import psutil
import os

# 定义MemoryUsageAnalyzer类，用于分析内存使用情况
class MemoryUsageAnalyzer:
    """
    MemoryUsageAnalyzer is a class that analyzes the memory usage of a process.
    It provides methods to get the memory usage in different formats and
    to check if the memory usage exceeds a specified threshold.
    """

    def __init__(self, pid):
        """
        Initialize the MemoryUsageAnalyzer with the process ID.
        :param pid: The process ID of the process to analyze.
        """
        self.pid = pid
        self.process = psutil.Process(pid)

    def get_memory_info(self):
        """
        Get the memory usage information of the process in bytes.
        :return: A tuple containing the memory usage in bytes and the peak memory usage.
        """
        try:
            mem_info = self.process.memory_info()
            return mem_info.rss, mem_info.peak_wset
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error: {e}")
            return None, None

    def get_memory_usage_percentage(self):
        """
        Get the memory usage percentage of the process.
        :return: The memory usage percentage or None if an error occurs.
        """
        try:
            return self.process.memory_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"Error: {e}")
            return None

    def is_memory_usage_exceeded(self, threshold):
        """
        Check if the memory usage exceeds a specified threshold.
        :param threshold: The memory usage threshold in bytes.
        :return: True if the memory usage exceeds the threshold, False otherwise.
        """
        rss, _ = self.get_memory_info()
        return rss > threshold if rss is not None else None

# Example usage
if __name__ == '__main__':
    pid = os.getpid()  # Get the current process ID
    analyzer = MemoryUsageAnalyzer(pid)

    mem_info = analyzer.get_memory_info()
    if mem_info:
        print(f"Memory usage: {mem_info[0] / (1024 * 1024):.2f} MB")
        print(f"Peak memory usage: {mem_info[1] / (1024 * 1024):.2f} MB")

    mem_usage_percentage = analyzer.get_memory_usage_percentage()
    if mem_usage_percentage:
        print(f"Memory usage percentage: {mem_usage_percentage:.2f}%")

    threshold = 100 * 1024 * 1024  # 100 MB
    if analyzer.is_memory_usage_exceeded(threshold):
        print(f"Memory usage exceeded the threshold of {threshold / (1024 * 1024):.2f} MB")
    else:
        print("Memory usage is within the threshold")
