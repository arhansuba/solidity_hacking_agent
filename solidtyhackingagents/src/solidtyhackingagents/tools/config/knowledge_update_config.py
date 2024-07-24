# knowledge_update_config.py

import os
import json

class KnowledgeUpdateConfig:
    def __init__(self, config_file='config/knowledge_update_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get_update_settings(self):
        return self.config.get('updates', {})

    def get_update(self, update_name):
        updates = self.get_update_settings()
        return updates.get(update_name, {})

    def update_setting(self, update_name, settings):
        updates = self.get_update_settings()
        updates[update_name] = settings
        self.config['updates'] = updates
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    knowledge_update_config = KnowledgeUpdateConfig()
    print(knowledge_update_config.get_update_settings())
