# cross_platform_comparison_dashboard.py

import os
import matplotlib.pyplot as plt
import pandas as pd
import json

class CrossPlatformComparisonDashboard:
    def __init__(self, data_file='data/cross_platform_comparison.json'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if not os.path.isfile(self.data_file):
            raise FileNotFoundError(f"Data file {self.data_file} not found.")
        
        with open(self.data_file, 'r') as file:
            data = json.load(file)
        
        return pd.DataFrame(data)

    def plot_comparison(self):
        df = self.data
        platforms = df['platform'].unique()

        plt.figure(figsize=(12, 8))
        for platform in platforms:
            platform_data = df[df['platform'] == platform]
            plt.plot(platform_data['date'], platform_data['metric'], label=platform)

        plt.xlabel('Date')
        plt.ylabel('Metric Value')
        plt.title('Cross-Platform Comparison Over Time')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        plt.savefig('output/cross_platform_comparison_dashboard.png')
        plt.show()

# Example usage
if __name__ == "__main__":
    dashboard = CrossPlatformComparisonDashboard()
    dashboard.plot_comparison()
