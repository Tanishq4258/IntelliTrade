from data_fetcher import get_stock_history
from plotting import plot_closing_price
from analysis import calculate_simple_moving_average

def main():
    stock_symbol = input("Enter Name of stock you want the chart for: ")
    stock_data = get_stock_history(stock_symbol, period='3mo')

    if not stock_data.empty:
        print(f"Fetching data for {stock_symbol}...")
        stock_data_with_sma = calculate_simple_moving_average(stock_data)
        plot_closing_price(stock_data_with_sma, stock_symbol)
    else:
        print(f"Could not fetch data for {stock_symbol}. Please check the symbol.")

if __name__ == "__main__":
    main()