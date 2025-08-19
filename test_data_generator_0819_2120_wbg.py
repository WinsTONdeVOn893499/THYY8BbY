# 代码生成时间: 2025-08-19 21:20:59
import scrapy
def generate_test_data(count):
    """
    生成指定数量的测试数据。
    :param count: 需要生成的测试数据数量
    :return: 测试数据列表
    """
    test_data = []
    for i in range(count):
        try:
            # 这里可以根据需要生成不同的测试数据
            test_data.append({
                "id": i + 1,
                "name": "Test User " + str(i + 1),
                "email": "testuser" + str(i + 1) + "@example.com",
                "age": 20 + i
            })
        except Exception as e:
            print(f"Error generating test data: {e}")
    return test_data

# 测试函数
if __name__ == "__main__":
    count = 10  # 需要生成的测试数据数量
    test_data_list = generate_test_data(count)
    print(f"Generated {count} test data items: {test_data_list}")