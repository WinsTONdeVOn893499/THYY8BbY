# 代码生成时间: 2025-08-16 22:46:44
import scrapy
def get_system_metrics():
    """
    Retrieves system performance metrics
    """
    try:
        # Importing necessary modules
        import psutil
        import datetime
        
        # Getting CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Getting memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        
        # Getting disk usage
        disk_usage = psutil.disk_usage('/')
        disk_usage_percent = disk_usage.percent
        
        # Getting network statistics
        network_stats = psutil.net_io_counters()
        network_sent = network_stats.bytes_sent
        network_recv = network_stats.bytes_recv
        
        # Getting system uptime
        uptime = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.datetime.now() - uptime
        
        # Returning system metrics as a dictionary
        return {
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage': disk_usage_percent,
            'network_sent': network_sent,
            'network_recv': network_recv,
            'uptime': str(uptime)
        }
    except Exception as e:
        # Handling any exceptions and returning an error message
        return {'error': str(e)}

# Example usage of get_system_metrics function
if __name__ == '__main__':
    metrics = get_system_metrics()
    print(metrics)