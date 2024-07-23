# report_utils.py

import pandas as pd

def generate_summary_report(df: pd.DataFrame, output_file: str) -> None:
    """
    Generate a summary report of the DataFrame and save to a file.
    """
    summary = df.describe(include='all')
    with open(output_file, 'w') as file:
        file.write(summary.to_string())

def generate_comparison_report(df1: pd.DataFrame, df2: pd.DataFrame, output_file: str) -> None:
    """
    Generate a comparison report between two DataFrames and save to a file.
    """
    comparison = df1.compare(df2)
    with open(output_file, 'w') as file:
        file.write(comparison.to_string())
