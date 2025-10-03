# 代码生成时间: 2025-10-03 22:41:51
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class DigitalSignatureTool:
    """数字签名工具，用于生成签名和验证签名。"""

    def __init__(self, private_key_path=None, public_key_path=None):
        """初始化数字签名工具，加载私钥和公钥。

        :param private_key_path: 私钥文件路径
        :param public_key_path: 公钥文件路径
        """
        self.private_key = self.load_private_key(private_key_path) if private_key_path else None
        self.public_key = self.load_public_key(public_key_path) if public_key_path else None

    def load_private_key(self, private_key_path):
        """从文件加载私钥。

        :param private_key_path: 私钥文件路径
        :return: 私钥对象
        """
        if not private_key_path or not os.path.exists(private_key_path):
            raise FileNotFoundError('私钥文件不存在')

        with open(private_key_path, 'rb') as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        return private_key

    def load_public_key(self, public_key_path):
        """从文件加载公钥。

        :param public_key_path: 公钥文件路径
        :return: 公钥对象
        """
        if not public_key_path or not os.path.exists(public_key_path):
            raise FileNotFoundError('公钥文件不存在')

        with open(public_key_path, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key

    def sign(self, data):
        """对数据进行签名。

        :param data: 待签名的数据（字节串）
        :return: 签名（字节串）
        """
        if not self.private_key:
            raise ValueError('未加载私钥，无法签名')

        return self.private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def verify(self, data, signature):
        """验证签名的有效性。

        :param data: 待验证的数据（字节串）
        :param signature: 签名（字节串）
        :return: 布尔值，表示签名是否有效
        """
        if not self.public_key:
            raise ValueError('未加载公钥，无法验证')

        try:
            self.public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception as e:
            print(f'签名验证失败：{e}')
            return False

# 示例用法
if __name__ == '__main__':
    tool = DigitalSignatureTool('private_key.pem', 'public_key.pem')

    # 待签名的数据
    data = b'Hello, World!'

    # 对数据进行签名
    signature = tool.sign(data)
    print(f'签名：{signature.hex()}')

    # 验证签名的有效性
    is_valid = tool.verify(data, signature)
    print(f'签名验证结果：{is_valid}')
