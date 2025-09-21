# 代码生成时间: 2025-09-22 02:14:31
import scrapy
def bubble_sort(arr):
    """
    实现冒泡排序算法，对列表进行排序
    :param arr: 需要排序的列表
    :type arr: List[int]
    :return: 排序后的列表
    :rtype: List[int]
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def insertion_sort(arr):
    """
    实现插入排序算法，对列表进行排序
    :param arr: 需要排序的列表
    :type arr: List[int]
    :return: 排序后的列表
    :rtype: List[int]
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def selection_sort(arr):
    """
    实现选择排序算法，对列表进行排序
    :param arr: 需要排序的列表
    :type arr: List[int]
    :return: 排序后的列表
    :rtype: List[int]
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def quick_sort(arr):
    """
    实现快速排序算法，对列表进行排序
    :param arr: 需要排序的列表
    :type arr: List[int]
    :return: 排序后的列表
    :rtype: List[int]
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
def main():
    # 测试数据
    test_data = [64, 34, 25, 12, 22, 11, 90]
    
    # 冒泡排序
    sorted_data = bubble_sort(test_data.copy())
    print("冒泡排序结果：", sorted_data)
    
    # 插入排序
    sorted_data = insertion_sort(test_data.copy())
    print("插入排序结果：", sorted_data)
    
    # 选择排序
    sorted_data = selection_sort(test_data.copy())
    print("选择排序结果：", sorted_data)
    
    # 快速排序
    sorted_data = quick_sort(test_data.copy())
    print("快速排序结果：", sorted_data)
    
if __name__ == "__main__":
    main()