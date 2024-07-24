# trend_analysis_utils.py

import pandas as pd

def calculate_moving_average(df: pd.DataFrame, column: str, window: int) -> pd.Series:
    """
    Calculate the moving average for a given column in a DataFrame.
    """
    return df[column].rolling(window=window).mean()

def identify_trends(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Identify trends in a given column of the DataFrame.
    """
    trends = df[[column]].copy()
    trends['Trend'] = trends[column].diff().fillna(0)
    return trends

def visualize_trends(df: pd.DataFrame, column: str) -> None:
    """
    Visualize trends in a given column of the DataFrame.
    """
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(df[column], label='Original')
    plt.plot(df['Trend'], label='Trend', linestyle='--')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Trend Analysis')
    plt.legend()
    plt.show()
