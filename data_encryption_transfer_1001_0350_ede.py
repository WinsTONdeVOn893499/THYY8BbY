# 代码生成时间: 2025-10-01 03:50:27
import os
import logging
from cryptography.fernet import Fernet

# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataEncryptionTransfer:
    """
    数据加密传输工具类。
    这个类提供了数据加密和解密的功能，
    可以用于安全地传输敏感数据。
    """

    def __init__(self, key=None):
        """
        初始化函数，生成或加载加密密钥。
        :param key: 密钥字符串，如果为None，则生成新的密钥。
        """
        if key is None:
            self.key = Fernet.generate_key()
            self.cipher_suite = Fernet(self.key)
            logger.info("Generated a new encryption key.")
        else:
            self.key = key
            self.cipher_suite = Fernet(self.key)
            logger.info("Loaded an existing encryption key.")

    def encrypt_data(self, data):
        """
        加密数据。
        :param data: 待加密的数据，必须是字符串。
        :return: 加密后的数据。
        """
        try:
            encrypted_data = self.cipher_suite.encrypt(data.encode())
            logger.info("Data encrypted successfully.")
            return encrypted_data
        except Exception as e:
            logger.error(f"Failed to encrypt data: {e}")
            raise

    def decrypt_data(self, encrypted_data):
        """
        解密数据。
        :param encrypted_data: 待解密的加密数据。
        :return: 解密后的原始数据。
        """
        try:
            decrypted_data = self.cipher_suite.decrypt(encrypted_data).decode()
            logger.info("Data decrypted successfully.")
            return decrypted_data
        except Exception as e:
            logger.error(f"Failed to decrypt data: {e}")
            raise

    def save_key(self, file_path):
        """
        保存密钥到文件。
        :param file_path: 密钥文件的路径。
        """
        try:
            with open(file_path, 'wb') as key_file:
                key_file.write(self.key)
            logger.info(f"Encryption key saved to {file_path}.")
        except Exception as e:
            logger.error(f"Failed to save key: {e}")
            raise

    def load_key(self, file_path):
        """
        从文件加载密钥。
        :param file_path: 密钥文件的路径。
        """
        try:
            with open(file_path, 'rb') as key_file:
                self.key = key_file.read()
            self.cipher_suite = Fernet(self.key)
            logger.info(f"Encryption key loaded from {file_path}.")
        except Exception as e:
            logger.error(f"Failed to load key: {e}")
            raise

# 示例用法
if __name__ == '__main__':
    det = DataEncryptionTransfer()
    key_path = 'encryption_key.key'
    
    # 保存密钥
    det.save_key(key_path)
    
    # 加密数据
    data_to_encrypt = "Sensitive Data"
    encrypted_data = det.encrypt_data(data_to_encrypt)
    print(f"Encrypted: {encrypted_data}")
    
    # 加载密钥
    det.load_key(key_path)
    
    # 解密数据
    decrypted_data = det.decrypt_data(encrypted_data)
    print(f"Decrypted: {decrypted_data}")