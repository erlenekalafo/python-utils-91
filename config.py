import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        # Load default configuration
        config = self.load_json(self.default_config_path)
        # Update with user configuration if it exists
        user_config = self.load_json(self.user_config_path)
        if user_config:
            config.update(user_config)
        return config

    def load_json(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return {}

# Default paths for the configuration files
DEFAULT_CONFIG_PATH = 'default_config.json'
USER_CONFIG_PATH = 'user_config.json'

# Example of how to use the ConfigLoader
if __name__ == '__main__':
    config_loader = ConfigLoader(DEFAULT_CONFIG_PATH, USER_CONFIG_PATH)
    print(config_loader.config)  # Display loaded configuration