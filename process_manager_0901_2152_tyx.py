# 代码生成时间: 2025-09-01 21:52:45
import psutil
from scrapy import signals
from scrapy.exceptions import NotConfigured

"""
Process Manager: A Scrapy extension to manage processes.
# NOTE: 重要实现细节

This extension allows you to manage processes within your Scrapy project.
It provides functionality to start, stop, and monitor processes.
"""

class ProcessManager:
    def __init__(self, stats):
        """Initialize the Process Manager."""
        self.stats = stats
        self.processes = {}
# 扩展功能模块

    def start_process(self, name, cmdline):
        """Start a process."""
        try:
            # Start the process using subprocess
            process = subprocess.Popen(cmdline, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Store the process in the dictionary
            self.processes[name] = process
            self.stats.set_value('process_started', name)
        except Exception as e:
            # Handle any exceptions that occur while starting the process
            self.stats.inc_value('process_start_error', name)
            raise e

    def stop_process(self, name):
        """Stop a process."""
        if name in self.processes:
            try:
                # Terminate the process
                self.processes[name].terminate()
# 改进用户体验
                # Wait for the process to finish
# 增强安全性
                self.processes[name].wait()
                del self.processes[name]
                self.stats.set_value('process_stopped', name)
# TODO: 优化性能
            except Exception as e:
                # Handle any exceptions that occur while stopping the process
                self.stats.inc_value('process_stop_error', name)
                raise e
        else:
            raise ValueError(f"Process '{name}' not found.")

    def monitor_processes(self):
        """Monitor all processes."""
        for name, process in self.processes.items():
            try:
                # Check if the process is still running
                if process.poll() is not None:
                    # Process has finished, remove it from the dictionary
                    del self.processes[name]
                    self.stats.set_value('process_finished', name)
            except Exception as e:
                # Handle any exceptions that occur while monitoring the process
                self.stats.inc_value('process_monitor_error', name)
# FIXME: 处理边界情况
                raise e

# Register the extension
def setup_extension(crawler):
    if not crawler.settings.get('PROCESS_MANAGER_ENABLED'):
        raise NotConfigured
    # Create a new instance of the Process Manager
# NOTE: 重要实现细节
    process_manager = ProcessManager(crawler.stats)
    # Connect the process manager to the spider signals
    crawler.signals.connect(process_manager.start_process, signal=signals.spider_opened)
    crawler.signals.connect(process_manager.stop_process, signal=signals.spider_closed)
    crawler.signals.connect(process_manager.monitor_processes, signal=signals.engine_started)
    crawler.extensions.append(process_manager)

# Set up the extension
setup_extension(crawler)