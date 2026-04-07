# © 2024 Tanishq Chhabra. All rights reserved.
# Made by Tanishq Chhabra for IntelliTrade Project

import yfinance as yf
import matplotlib
matplotlib.use('Agg') # Needed to prevent GUI popups in web servers
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

def get_chart_base64(symbol, period='1Y', indicators=None):
    if indicators is None:
        indicators = []
        
    stock = yf.Ticker(symbol)
    
    # Translate frontend period (1D, 1W, 1M, 1Y) to yfinance format
    yf_period = '1y'
    if period == '1D': yf_period = '1d'
    elif period == '1W': yf_period = '5d'
    elif period == '1M': yf_period = '1mo'
    else: yf_period = '1y'
        
    stock_data = stock.history(period=yf_period)
    
    if stock_data.empty:
        return None, None
        
    # Main Plot
    plt.figure(figsize=(10, 5))
    
    # Dark Mode Aesthetic Match
    plt.style.use('dark_background')
    plt.gca().set_facecolor('#0d1117')
    plt.gcf().set_facecolor('#0d1117')
    
    plt.plot(stock_data.index, stock_data['Close'], marker='', linestyle='-', color='#00ff88', linewidth=2)
    
    # Add SMA/EMA if requested
    if 'SMA' in indicators:
        sma = stock_data['Close'].rolling(window=20).mean()
        plt.plot(stock_data.index, sma, color='#f0c040', label='SMA 20', linestyle='--')
    if 'EMA' in indicators:
        ema = stock_data['Close'].ewm(span=20, adjust=False).mean()
        plt.plot(stock_data.index, ema, color='#ff4d4d', label='EMA 20', linestyle=':')
        
    plt.title(f'{symbol} Price ({period})', color='white')
    plt.xlabel('Date', color='gray')
    plt.ylabel('Price', color='gray')
    plt.grid(True, color='#30363d')
    plt.legend()
    
    # Save Main Plot to Base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    buf.seek(0)
    chart_img = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    
    rsi_img = None
    if 'RSI' in indicators:
        # Calculate RSI
        delta = stock_data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        plt.figure(figsize=(10, 3))
        plt.gca().set_facecolor('#0d1117')
        plt.gcf().set_facecolor('#0d1117')
        
        plt.plot(stock_data.index, rsi, color='#f0c040', linewidth=2)
        plt.axhline(70, linestyle='--', color='red', alpha=0.5)
        plt.axhline(30, linestyle='--', color='green', alpha=0.5)
        
        plt.title('Relative Strength Index (14)', color='white')
        plt.grid(True, color='#30363d')
        plt.ylim(0, 100)
        
        rsi_buf = io.BytesIO()
        plt.savefig(rsi_buf, format='png', bbox_inches='tight', transparent=True)
        rsi_buf.seek(0)
        rsi_img = base64.b64encode(rsi_buf.getvalue()).decode('utf-8')
        plt.close()
        
    return chart_img, rsi_img

if __name__ == "__main__":
    # Backward compatibility for direct terminal usage
    matplotlib.use('TkAgg') # Re-enable UI popups for terminal
    stock_symbol = input("Enter Name of stock you want last 1 month chart for: ")
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period='1mo')
    print(stock_data['Close'].tail())
    plt.style.use('default')
    plt.figure(figsize=(10,5))
    plt.plot(stock_data.index, stock_data['Close'], marker='o', linestyle='-')
    plt.title(f'{stock_symbol} Closing price - Last 30 days')   
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()
