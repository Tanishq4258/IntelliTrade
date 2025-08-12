# src/plotting.py

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
from data_fetcher import get_stock_history

def plot_closing_price(data: pd.DataFrame, symbol: str, latest_price: float):
    """
    Plots the closing price, available indicators, and the latest price.
    """
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-', label='Closing Price')

    if 'SMA_20' in data.columns:
        plt.plot(data.index, data['SMA_20'], linestyle='-', label='20-Day SMA')

    plt.annotate(
        f'Latest Price: ${latest_price:.2f}',
        xy=(data.index[-1], latest_price),
        xytext=(5, 20),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='black')
    )

    plt.title(f'{symbol} Closing Price & 20-Day SMA')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.show()

def live_plot_data(symbol: str):
    """
    Simulates a live-updating graph for the current day's stock price.
    """
    from matplotlib import style
    style.use('fivethirtyeight')
    
    fig, ax = plt.subplots(figsize=(10, 5))

    def animate(i):
        data = get_stock_history(symbol, period='1d', interval='1m')

        if not data.empty:
            ax.clear()
            ax.plot(data.index, data['Close'], marker='o', linestyle='-', label='Closing Price')
            ax.set_title(f'{symbol} Live Intraday Price')
            ax.set_xlabel('Time')
            ax.set_ylabel('Price')
            ax.grid(True)
            ax.legend()
        else:
            ax.clear()
            ax.text(0.5, 0.5, "No data available.", ha='center', va='center', transform=ax.transAxes)
            ax.set_title(f'{symbol} Live Intraday Price')

    ani = animation.FuncAnimation(fig, animate, interval=60000)
    plt.show()