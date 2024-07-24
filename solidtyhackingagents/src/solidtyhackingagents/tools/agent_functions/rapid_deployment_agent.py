# src/solidtyhackingagents/tools/rapid_deployment/rapid_deployment_agent.py

import yaml
import subprocess
from pathlib import Path

class RapidDeploymentAgent:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        """Load the configuration from the YAML file."""
        with open(self.config_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def deploy(self):
        """Perform rapid deployment tasks based on the loaded configuration."""
        deploy_tasks = self.config.get('deploy_tasks', [])
        
        for task in deploy_tasks:
            task_type = task.get('type')
            command = task.get('command')
            description = task.get('description', 'No description provided')
            
            print(f"Starting deployment task: {description}")
            
            if task_type == 'command':
                self.run_command(command)
            else:
                print(f"Unknown task type: {task_type}")
        
    def run_command(self, command: str):
        """Run a shell command and print its output."""
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e.stderr}")

    def run(self):
        """Run the rapid deployment process."""
        print("Starting rapid deployment process...")
        self.deploy()
        print("Rapid deployment process completed.")

if __name__ == "__main__":
    config_file = Path(__file__).parent.parent.parent / 'config' / 'rapid_deployment.yaml'
    agent = RapidDeploymentAgent(config_file)
    agent.run()
