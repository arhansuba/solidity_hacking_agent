# agent_config.py

import os
import json

class AgentConfig:
    def __init__(self, config_file='config/agent_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get_agent_settings(self):
        return self.config.get('agents', {})

    def get_agent(self, agent_name):
        agents = self.get_agent_settings()
        return agents.get(agent_name, {})

    def update_agent(self, agent_name, settings):
        agents = self.get_agent_settings()
        agents[agent_name] = settings
        self.config['agents'] = agents
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    agent_config = AgentConfig()
    print(agent_config.get_agent_settings())
