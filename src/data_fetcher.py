import yfinance as yf
import pandas as pd
import requests

# NOTE: Replace with your actual Alpha Vantage API key
API_KEY = "PLL9MS92UTGD2AE2"

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

def get_stock_currency(symbol: str) -> str:
    """
    Fetches the currency of a stock.
    
    Args:
        symbol (str): The stock symbol (e.g., 'AAPL', 'SUZLON.NS').
    
    Returns:
        str: The currency of the stock (e.g., 'USD', 'INR').
    """
    stock = yf.Ticker(symbol)
    currency = stock.info.get('currency')
    return currency

def get_stock_news(symbol: str) -> list:
    """
    Fetches news headlines and summaries for a given stock symbol.
    
    Args:
        symbol (str): The stock symbol (e.g., 'AAPL', 'SUZLON.NS').
    
    Returns:
        list: A list of news articles with headline and summary.
    """
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={API_KEY}'
    try:
        response = requests.get(url)
        data = response.json()
        
        articles = data.get('feed', [])
        news_list = []
        for article in articles:
            news_list.append({
                "title": article.get('title', 'No Title'),
                "summary": article.get('summary', 'No Summary'),
                "url": article.get('url', '#')
            })
        return news_list
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
    
def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """
    Fetches the exchange rate between two currencies using a virtual pair.
    """
    pair = f"{from_currency}{to_currency}=X"
    try:
        data = yf.Ticker(pair).history(period='1d')
        if not data.empty:
            return data['Close'].iloc[-1]
    except Exception:
        pass
    return 1.0 # Return 1.0 if currencies are the same or rate is not found
    