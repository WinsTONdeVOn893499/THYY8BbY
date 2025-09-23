# 代码生成时间: 2025-09-24 01:17:34
import hashlib
# 扩展功能模块
"""
哈希值计算工具
"""

class HashCalculator:
    def __init__(self):
        """初始化哈希计算器"""
# 优化算法效率
        self.hash_functions = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }

    def calculate_hash(self, data, algorithm='md5'):
        """计算给定数据的哈希值

        Args:
            data (str): 要计算哈希值的数据
            algorithm (str): 哈希算法，如 'md5', 'sha1', 'sha256', 'sha512'

        Returns:
            str: 计算得到的哈希值

        Raises:
            ValueError: 如果指定的算法不支持
# 优化算法效率
        """
        if algorithm not in self.hash_functions:
            raise ValueError(f'Unsupported algorithm: {algorithm}')

        hash_func = self.hash_functions[algorithm]
        hash_obj = hash_func(data.encode('utf-8'))
        return hash_obj.hexdigest()


def main():
# FIXME: 处理边界情况
    """主函数，用于演示哈希计算器的使用方法"""
# 优化算法效率
    calculator = HashCalculator()

    # 演示计算字符串的哈希值
    test_string = 'Hello, World!'
    print(f'MD5 Hash of "{test_string}": {calculator.calculate_hash(test_string)}')

    # 演示计算空字符串的哈希值
    print(f'SHA1 Hash of empty string: {calculator.calculate_hash('', algorithm='sha1')}')

    # 演示处理不支持的算法
    try:
        calculator.calculate_hash('', algorithm='unsupported')
    except ValueError as e:
        print(e)
# 增强安全性

if __name__ == '__main__':
    main()