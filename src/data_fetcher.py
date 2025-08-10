import yfinance as yf
import pandas as pd

def get_stock_history(symbol: str, period: str = '1mo') -> pd.DataFrame:
    """
    Fetches historical stock data for a given symbol and period.
    """
    stock = yf.Ticker(symbol)
    stock_data = stock.history(period=period)
    return stock_data