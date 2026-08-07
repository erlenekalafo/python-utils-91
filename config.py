import json
import os

class ConfigLoader:
    def __init__(self, default_config_path=None):
        self.default_config_path = default_config_path or 'default_config.json'
        self.config = {}  # to hold the loaded config
        self.load_defaults()

    def load_defaults(self):
        if os.path.exists(self.default_config_path):
            with open(self.default_config_path, 'r') as file:
                self.config = json.load(file)
        else:
            raise FileNotFoundError(f'Default config file not found: {self.default_config_path}')

    def load_from_file(self, custom_config_path):
        if os.path.exists(custom_config_path):
            with open(custom_config_path, 'r') as file:
                custom_config = json.load(file)
                self.config.update(custom_config)
        else:
            raise FileNotFoundError(f'Custom config file not found: {custom_config_path}')

    def get_setting(self, key, default=None):
        return self.config.get(key, default)

# Usage example
if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get_setting('example_setting', 'default_value'))
    loader.load_from_file('custom_config.json')
    print(loader.get_setting('another_setting', 'default_value'))