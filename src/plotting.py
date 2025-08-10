import matplotlib.pyplot as plt
import pandas as pd

def plot_closing_price(data: pd.DataFrame, symbol: str):
    """
    Plots the closing price from a DataFrame.
    """
    plt.figure(figsize=(10,5))
    
    plt.plot(data.index, data['Close'], marker='o', linestyle='-', label='Closing Price')
    
    if 'SMA_20' in data.columns:
        plt.plot(data.index, data['SMA_20'], color='orange', label='20-Day SMA')
    
    plt.title(f'{symbol} Closing price - Last {len(data)} days')   
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.show()