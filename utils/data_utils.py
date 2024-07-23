# data_utils.py

import pandas as pd
import json

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.
    """
    return pd.read_csv(file_path)

def save_to_json(data: dict, file_path: str) -> None:
    """
    Save a dictionary to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def merge_dataframes(df1: pd.DataFrame, df2: pd.DataFrame, on: str) -> pd.DataFrame:
    """
    Merge two DataFrames on a specified column.
    """
    return pd.merge(df1, df2, on=on)
