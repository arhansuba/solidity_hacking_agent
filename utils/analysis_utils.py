# analysis_utils.py

import pandas as pd

def summarize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarize the given DataFrame with basic statistics.
    """
    summary = df.describe(include='all')
    return summary

def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the correlation matrix for the given DataFrame.
    """
    corr_matrix = df.corr()
    return corr_matrix

def detect_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Detect outliers in the specified column of the DataFrame.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]
    return outliers
