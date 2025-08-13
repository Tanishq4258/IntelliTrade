# src/analysis.py

import pandas as pd

def calculate_simple_moving_average(data: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Calculates the Simple Moving Average (SMA) for the closing price.
    """
    data[f'SMA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def calculate_exponential_moving_average(data: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    Calculates the Exponential Moving Average (EMA) for the closing price.
    """
    data[f'EMA_{window}'] = data['Close'].ewm(span=window, adjust=False).mean()
    return data

def calculate_rsi(data: pd.DataFrame, window: int = 14) -> pd.DataFrame:
    """
    Calculates the Relative Strength Index (RSI) for the closing price.
    """
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    data[f'RSI_{window}'] = rsi
    
    return data