# 代码生成时间: 2025-09-18 01:47:36
import json
from scrapy.exceptions import NotConfigured

"""
Config Manager for Scrapy, allows you to manage configuration files easily.
This module provides a simple way to load, save, and update configurations.
"""

class ConfigManager:
    def __init__(self, file_path):
        """Initialize the ConfigManager with a file path."""
        self.file_path = file_path
        self.configs = self._load_configs()

    def _load_configs(self):
        """Load configurations from a JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise NotConfigured(f"Configuration file not found at {self.file_path}")
        except json.JSONDecodeError as e:
            raise NotConfigured(f"Error reading configuration file: {e}")

    def _save_configs(self):
        """Save configurations to a JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.configs, file, indent=4)
        except Exception as e:
            raise NotConfigured(f"Error writing configuration file: {e}")

    def get_config(self, key):
        """Get a configuration value by key."""
        return self.configs.get(key)

    def set_config(self, key, value):
        """Set a configuration value."""
        self.configs[key] = value
        self._save_configs()

    def remove_config(self, key):
        """Remove a configuration value by key."""
        if key in self.configs:
            del self.configs[key]
            self._save_configs()
            return True
        return False

# Example usage:
# config_manager = ConfigManager('path/to/config.json')
# config_manager.set_config('timeout', 10)
# print(config_manager.get_config('timeout'))
# config_manager.remove_config('timeout')
