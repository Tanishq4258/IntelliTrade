import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation
from data_fetcher import get_stock_history

def plot_closing_price(data: pd.DataFrame, symbol: str, latest_price: float, currency: str): # ADD CURRENCY
    """
    Plots the closing price, available indicators, and the latest price.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(10, 8))
    
    ax1.plot(data.index, data['Close'], marker='o', linestyle='-', label='Closing Price')
    if 'SMA_20' in data.columns:
        ax1.plot(data.index, data['SMA_20'], linestyle='-', label='20-Day SMA')
    if 'EMA_20' in data.columns:
        ax1.plot(data.index, data['EMA_20'], linestyle='-', label='20-Day EMA')

    ax1.annotate(
        f'Latest Price: {currency} {latest_price:.2f}', # UPDATE THIS LINE
        xy=(data.index[-1], latest_price),
        xytext=(5, 20),
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='black')
    )
    ax1.set_title(f'{symbol} Closing Price, SMA & EMA')
    ax1.set_ylabel('Price')
    ax1.grid(True)
    ax1.legend()
    
    if 'RSI_14' in data.columns:
        ax2.plot(data.index, data['RSI_14'], linestyle='-', label='RSI (14)')
        ax2.axhline(70, linestyle='--', alpha=0.5, color='red')
        ax2.axhline(30, linestyle='--', alpha=0.5, color='green')
        ax2.set_title('Relative Strength Index (RSI)')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('RSI')
        ax2.grid(True)
        ax2.legend()
        
    plt.tight_layout()
    plt.show()


# live_plot_data function
# live_plot_data function
def live_plot_data(symbol: str):
    """
    Simulates a live-updating graph for the current day's stock price.
    This function will continuously fetch new data and redraw the plot.
    """
    import matplotlib.animation as animation
    from data_fetcher import get_stock_history, get_stock_currency
    from matplotlib import style

    style.use('fivethirtyeight')
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Fetch the currency once, outside the animation loop
    currency = get_stock_currency(symbol)

    def animate(i):
        data = get_stock_history(symbol, period='1d', interval='1m')

        if not data.empty:
            current_price = data['Close'].iloc[-1]
            ax.clear()
            ax.plot(data.index, data['Close'], marker='o', linestyle='-', label='Closing Price')
            ax.set_title(f'{symbol} Live Intraday Price - Current Price: {currency} {current_price:.2f}')
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