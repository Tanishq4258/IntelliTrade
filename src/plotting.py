import matplotlib.pyplot as plt
import pandas as pd

def plot_closing_price(data: pd.DataFrame, symbol: str):
    """
    Plots the closing price from a DataFrame.
    """
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-')
    plt.title(f'{symbol} Closing price - Last {len(data)} days')   
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()