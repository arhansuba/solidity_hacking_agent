# trend_analysis_config.py

import os
import json

class TrendAnalysisConfig:
    def __init__(self, config_file='config/trend_analysis_config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file {self.config_file} not found.")
        
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        
        return config

    def get_trend_settings(self):
        return self.config.get('trends', {})

    def get_trend(self, trend_name):
        trends = self.get_trend_settings()
        return trends.get(trend_name, {})

    def update_trend(self, trend_name, settings):
        trends = self.get_trend_settings()
        trends[trend_name] = settings
        self.config['trends'] = trends
        self.save_config()

    def save_config(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

# Example usage
if __name__ == "__main__":
    trend_analysis_config = TrendAnalysisConfig()
    print(trend_analysis_config.get_trend_settings())
