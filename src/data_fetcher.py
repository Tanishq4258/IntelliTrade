import yfinance as yf
import pandas as pd

def get_stock_history(symbol: str, period: str = '1mo', interval: str = '1d') -> pd.DataFrame:
    """
    Fetches historical stock data for a given symbol, period, and interval.
    
    Args:
        symbol (str): The stock symbol (e.g., 'AAPL', 'SUZLON.NS').
        period (str): The time period for the data (e.g., '1mo', '6mo', '1y').
        interval (str): The interval for the data points (e.g., '1d', '1wk', '1m').
    
    Returns:
        pd.DataFrame: A DataFrame containing the historical stock data.
    """
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period=period, interval=interval)
    return stock_data