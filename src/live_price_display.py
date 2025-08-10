# live_price_display.py

import yfinance as yf
import time
import os

def get_live_price(symbol):
    """
    Fetches the current price of a stock.
    """
    try:
        ticker = yf.Ticker(symbol)
        # Check if the ticker symbol exists
        if not ticker.info:
            return None
        price = ticker.info.get('currentPrice')
        return price
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    stock_symbol = input("Enter the stock symbol for a live price feed: ")

    # Check for a valid symbol before starting the loop
    initial_price = get_live_price(stock_symbol)
    if not initial_price:
        print("Invalid stock symbol. Please try again.")
        return # Exit the function and end the script

    try:
        while True:
            # Clear the terminal for a cleaner display
            os.system('cls' if os.name == 'nt' else 'clear')

            price = get_live_price(stock_symbol)

            if price:
                print(f"Stock: {stock_symbol}")
                print(f"Live Price: ${price}")
            else:
                print(f"Could not fetch price for {stock_symbol}.")
                # Since we already checked the symbol, this might indicate
                # a temporary network error. We can continue the loop.

            # Wait for 0.2 seconds before the next update
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nStopping the live price feed.")

if __name__ == "__main__":
    main()