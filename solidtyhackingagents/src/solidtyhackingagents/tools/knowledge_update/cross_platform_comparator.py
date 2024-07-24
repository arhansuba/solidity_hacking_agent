# cross_platform_comparator.py

import pandas as pd
import os
from typing import List

class CrossPlatformComparator:
    def __init__(self, platforms_dirs: List[str], output_file: str):
        self.platforms_dirs = platforms_dirs
        self.output_file = output_file
        self.data_frames = []

    def load_data(self):
        for dir_path in self.platforms_dirs:
            files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
            for file in files:
                file_path = os.path.join(dir_path, file)
                df = pd.read_json(file_path, orient='records', lines=True)
                self.data_frames.append(df)

    def compare_data(self):
        if len(self.data_frames) < 2:
            raise ValueError("At least two platforms' data are required for comparison.")
        
        # Combine all data frames into one for comparison
        combined_df = pd.concat(self.data_frames, keys=range(len(self.data_frames)))
        
        # Perform comparisons: Here we use groupby to compare different platforms
        comparison_result = combined_df.groupby(level=0).apply(lambda x: x.duplicated(keep=False))
        
        return comparison_result

    def save_comparison_results(self, comparison_result: pd.DataFrame):
        if not os.path.exists(os.path.dirname(self.output_file)):
            os.makedirs(os.path.dirname(self.output_file))
        
        comparison_result.to_json(self.output_file, orient='records', lines=True)

    def run(self):
        print("Loading data from platforms...")
        self.load_data()
        print("Comparing data...")
        comparison_result = self.compare_data()
        print("Saving comparison results...")
        self.save_comparison_results(comparison_result)
        print("Comparison complete.")

# Example usage
if __name__ == "__main__":
    platforms_dirs = ['data/platform1', 'data/platform2']
    output_file = 'data/comparison_results.json'
    
    comparator = CrossPlatformComparator(platforms_dirs, output_file)
    comparator.run()
