from data_fetcher import get_stock_history, get_stock_currency # ADD NEW IMPORT
from plotting import plot_closing_price, live_plot_data
from analysis import calculate_simple_moving_average, calculate_exponential_moving_average, calculate_rsi

def main():
    stock_symbol = input("Enter Name of stock you want the chart for: ")

    print("\nSelect time period:")
    print("1. Today (1-minute intervals) - Live-ish")
    print("2. Last 7 Days (30-minute intervals)")
    print("3. Last 1 Month (Daily)")
    print("4. Last 1 Year (Weekly)")
    print("5. Last 5 Years (Weekly)")
    print("6. All Time (Monthly)")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        live_plot_data(stock_symbol)
        return

    period = '1mo'
    interval = '1d'

    if choice == '2':
        period = '7d'
        interval = '30m'
    elif choice == '3':
        period = '1mo'
        interval = '1d'
    elif choice == '4':
        period = '1y'
        interval = '1wk'
    elif choice == '5':
        period = '5y'
        interval = '1wk'
    elif choice == '6':
        period = 'max'
        interval = '1mo'
    else:
        print("Invalid choice. Defaulting to 1 month (Daily).")

    stock_data = get_stock_history(stock_symbol, period=period, interval=interval)
    currency = get_stock_currency(stock_symbol) # CALL NEW FUNCTION

    if not stock_data.empty:
        print(f"Fetching data for {stock_symbol}...")
        stock_data_with_indicators = calculate_simple_moving_average(stock_data)
        stock_data_with_indicators = calculate_exponential_moving_average(stock_data_with_indicators)
        stock_data_with_indicators = calculate_rsi(stock_data_with_indicators)
        latest_price = stock_data_with_indicators['Close'].iloc[-1]
        plot_closing_price(stock_data_with_indicators, stock_symbol, latest_price, currency) # PASS CURRENCY
    else:
        print(f"Could not fetch data for {stock_symbol}. Please check the symbol.")

if __name__ == "__main__":
    main()