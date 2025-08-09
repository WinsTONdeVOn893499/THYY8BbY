# 代码生成时间: 2025-08-10 05:44:16
import scrapy


# 定义排序算法类
class SortingAlgorithmsSpider(scrapy.Spider):
    '''
    该类实现了基本的排序算法，用于对数组进行排序。
    包括冒泡排序、选择排序、插入排序和快速排序。
    '''
    name = 'sorting_algorithms'
    allowed_domains = []  # 由于这是一个独立的排序算法实现，所以不需要设置domains
    start_urls = []  # 同上，不需要设置start_urls

    def __init__(self):
        # 初始化一个示例数组
        self.array = [64, 34, 25, 12, 22, 11, 90]

    def bubble_sort(self):
        """冒泡排序算法实现"""
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    # 交换两个元素的位置
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        return self.array

    def selection_sort(self):
        """选择排序算法实现"""
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j
            # 交换最小元素和第i个元素的位置
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
        return self.array

    def insertion_sort(self):
        """插入排序算法实现"""
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j]:
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j+1] = key
        return self.array

    def quick_sort(self, low, high):
        """快速排序算法实现"""
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi-1)
            self.quick_sort(pi+1, high)

    def partition(self, low, high):
        """快速排序中的分区操作"""
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        return i+1

    def start_requests(self):
        """Scrapy引擎启动时会调用此方法"""
        # 调用排序算法并打印结果
        print("Original array: ", self.array)
        print("Sorted array by bubble sort: ", self.bubble_sort())
        print("Sorted array by selection sort: ", self.selection_sort())
        print("Sorted array by insertion sort: ", self.insertion_sort())
        print("Sorted array by quick sort: ", self.quick_sort(0, len(self.array)-1))

# 运行排序算法
if __name__ == '__main__':
    sorting_spider = SortingAlgorithmsSpider()
    sorting_spider.start_requests()