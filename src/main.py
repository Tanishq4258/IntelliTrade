from data_fetcher import get_stock_history
from plotting import plot_closing_price

def main():
    stock_symbol = input("Enter Name of stock you want the chart for: ")
    stock_data = get_stock_history(stock_symbol, period='1mo')

    if not stock_data.empty:
        print(f"Fetching data for {stock_symbol}...")
        print(stock_data['Close'].tail())
        plot_closing_price(stock_data, stock_symbol)
    else:
        print(f"Could not fetch data for {stock_symbol}. Please check the symbol.")

if __name__ == "__main__":
    main()