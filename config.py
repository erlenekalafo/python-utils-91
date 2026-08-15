import json
import os

class ConfigLoader:
    def __init__(self, default_config_path=None):
        self.default_config_path = default_config_path or "default_config.json"
        self.config = self.load_config()

    def load_config(self):
        config = self.load_defaults()
        env_config = self.load_env_vars()
        config.update(env_config)
        return config

    def load_defaults(self):
        if not os.path.exists(self.default_config_path):
            return {}
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_env_vars(self):
        env_config = {}
        for key, value in os.environ.items():
            if key.startswith('APP_'):
                config_key = key[4:].lower()
                env_config[config_key] = value
        return env_config

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.get('some_setting', 'default_value'))
