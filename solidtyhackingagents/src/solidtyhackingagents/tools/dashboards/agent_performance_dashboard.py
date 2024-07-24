# agent_performance_dashboard.py

import os
import matplotlib.pyplot as plt
import pandas as pd
import json

class AgentPerformanceDashboard:
    def __init__(self, data_file='data/agent_performance.json'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if not os.path.isfile(self.data_file):
            raise FileNotFoundError(f"Data file {self.data_file} not found.")
        
        with open(self.data_file, 'r') as file:
            data = json.load(file)
        
        return pd.DataFrame(data)

    def plot_performance(self):
        df = self.data
        agents = df['agent'].unique()

        plt.figure(figsize=(12, 8))
        for agent in agents:
            agent_data = df[df['agent'] == agent]
            plt.plot(agent_data['date'], agent_data['performance'], label=agent)

        plt.xlabel('Date')
        plt.ylabel('Performance')
        plt.title('Agent Performance Over Time')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig('output/agent_performance_dashboard.png')
        plt.show()

# Example usage
if __name__ == "__main__":
    dashboard = AgentPerformanceDashboard()
    dashboard.plot_performance()
