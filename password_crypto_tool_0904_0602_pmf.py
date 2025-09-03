# 代码生成时间: 2025-09-04 06:02:51
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Password Crypto Tool using Python and Scrapy framework.
This tool provides basic functionality for password encryption and decryption.
"""

import hashlib
import base64
from scrapy.utils.project import get_project_settings


class PasswordCryptoTool:
    """Class for password encryption and decryption."""

    def __init__(self, algorithm='sha256'):
        """Initialize the crypto tool with a specific algorithm."""
        self.algorithm = algorithm

    def encrypt(self, password):
        """Encrypt the given password using the specified algorithm."""
        if not password:
            raise ValueError("Password cannot be empty.")

        # Use hashlib to generate a hash of the password
        hashed_password = hashlib.new(self.algorithm)
        hashed_password.update(password.encode('utf-8'))

        # Encode the hash as a base64 string for storage
        encoded_password = base64.b64encode(hashed_password.digest()).decode('utf-8')

        return encoded_password

    def decrypt(self, encoded_password):
        """Decrypt the given encoded password."""
        if not encoded_password:
            raise ValueError("Encoded password cannot be empty.")

        # Decode the base64 string to get the hash
        decoded_hash = base64.b64decode(encoded_password)

        # Hash the decoded data using the same algorithm
        hashed_password = hashlib.new(self.algorithm)
        hashed_password.update(decoded_hash)

        # Convert the hash to a string
        original_password = hashed_password.hexdigest()

        return original_password

# Example usage:
if __name__ == '__main__':
    tool = PasswordCryptoTool()
    password = 'secret'

    encrypted_password = tool.encrypt(password)
    print(f'Encrypted password: {encrypted_password}')

    try:
        decrypted_password = tool.decrypt(encrypted_password)
        print(f'Decrypted password: {decrypted_password}')
    except ValueError as e:
        print(f'Error: {e}')