import pandas as pd

def calculate_simple_moving_average(data: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Calculates the Simple Moving Average (SMA) for the closing price.

    Args:
        data (pd.DataFrame): The DataFrame containing the stock data.
        window (int): The number of periods (days) to include in the average.

    Returns:
        pd.DataFrame: The original DataFrame with a new column for the SMA.
    """
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    return data