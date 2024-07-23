# rapid_deployment_config.py

import os
import json

class RapidDeploymentConfig:
    def __init__(self, config_file='config/rapid_deployment_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get_deployment_settings(self):
        return self.config.get('deployments', {})

    def get_deployment(self, deployment_name):
        deployments = self.get_deployment_settings()
        return deployments.get(deployment_name, {})

    def update_deployment(self, deployment_name, settings):
        deployments = self.get_deployment_settings()
        deployments[deployment_name] = settings
        self.config['deployments'] = deployments
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    rapid_deployment_config = RapidDeploymentConfig()
    print(rapid_deployment_config.get_deployment_settings())
