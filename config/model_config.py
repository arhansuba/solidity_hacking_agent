# model_config.py

import os
import json

class ModelConfig:
    def __init__(self, config_file='config/model_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get_model_settings(self):
        return self.config.get('models', {})

    def get_model(self, model_name):
        models = self.get_model_settings()
        return models.get(model_name, {})

    def update_model(self, model_name, settings):
        models = self.get_model_settings()
        models[model_name] = settings
        self.config['models'] = models
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    model_config = ModelConfig()
    print(model_config.get_model_settings())
