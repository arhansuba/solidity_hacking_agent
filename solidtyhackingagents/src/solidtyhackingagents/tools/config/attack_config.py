# attack_config.py

import os
import json

class AttackConfig:
    def __init__(self, config_file='config/attack_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get_attack_settings(self):
        return self.config.get('attacks', {})

    def get_attack(self, attack_name):
        attacks = self.get_attack_settings()
        return attacks.get(attack_name, {})

    def update_attack(self, attack_name, settings):
        attacks = self.get_attack_settings()
        attacks[attack_name] = settings
        self.config['attacks'] = attacks
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    attack_config = AttackConfig()
    print(attack_config.get_attack_settings())
