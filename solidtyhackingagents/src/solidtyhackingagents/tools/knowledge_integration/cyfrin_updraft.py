# cyfrin_updraft.py

import os
import json
import pandas as pd
from typing import List, Dict

class KnowledgeIntegration:
    def __init__(self, videos_dir: str, texts_dir: str, output_file: str):
        self.videos_dir = videos_dir
        self.texts_dir = texts_dir
        self.output_file = output_file
        self.video_data = []
        self.text_data = []

    def load_video_data(self):
        video_files = [f for f in os.listdir(self.videos_dir) if f.endswith('.json')]
        for file in video_files:
            with open(os.path.join(self.videos_dir, file), 'r') as f:
                self.video_data.extend(json.load(f))
    
    def load_text_data(self):
        text_files = [f for f in os.listdir(self.texts_dir) if f.endswith('.json')]
        for file in text_files:
            with open(os.path.join(self.texts_dir, file), 'r') as f:
                self.text_data.extend(json.load(f))
    
    def integrate_knowledge(self):
        video_df = pd.DataFrame(self.video_data)
        text_df = pd.DataFrame(self.text_data)
        
        # Ensure the keys used for merging match
        if 'video_id' not in video_df.columns or 'video_id' not in text_df.columns:
            raise KeyError("Both video and text data must have 'video_id' for integration.")

        # Merge data on 'video_id'
        integrated_df = pd.merge(video_df, text_df, on='video_id', how='left')

        return integrated_df

    def save_integrated_knowledge(self, integrated_df: pd.DataFrame):
        if not os.path.exists(os.path.dirname(self.output_file)):
            os.makedirs(os.path.dirname(self.output_file))
        
        integrated_df.to_json(self.output_file, orient='records', lines=True)

    def run(self):
        print("Loading video data...")
        self.load_video_data()
        print("Loading text data...")
        self.load_text_data()
        print("Integrating knowledge...")
        integrated_df = self.integrate_knowledge()
        print("Saving integrated knowledge...")
        self.save_integrated_knowledge(integrated_df)
        print("Knowledge integration complete.")

# Example usage
if __name__ == "__main__":
    videos_dir = 'data/videos'
    texts_dir = 'data/texts'
    output_file = 'data/integrated_knowledge.json'
    
    knowledge_integration = KnowledgeIntegration(videos_dir, texts_dir, output_file)
    knowledge_integration.run()
