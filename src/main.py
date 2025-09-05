from data_fetcher import get_stock_history, get_stock_currency, get_stock_news
from plotting import plot_closing_price, live_plot_data
from analysis import calculate_simple_moving_average, calculate_exponential_moving_average, calculate_rsi
from portfolio import Portfolio
import threading
import matplotlib.pyplot as plt

def fetch_and_print_news(symbol):
    """Fetches and prints news articles."""
    print("\n------------------------------")
    print("Fetching Latest News for", symbol)
    print("------------------------------")
    news_articles = get_stock_news(symbol)
    
    if news_articles:
        for i, article in enumerate(news_articles[:5]):
            print(f"{i+1}. {article['title']}")
            print(f"   - {article['summary']}")
            print(f"   - Link: {article['url']}")
            print("-" * 20)
    else:
        print("No news articles found or an error occurred.")

def main():
    initial_budget = float(input("Enter your initial investment budget: "))
    my_portfolio = Portfolio(initial_budget)

    while True:
        action = input("\nEnter 'chart' to view a stock chart, 'buy' to buy a stock, 'sell' to sell a stock, 'value' to check your portfolio, or 'exit' to quit: ")

        if action.lower() == 'exit':
            break
        
        stock_symbol = ""
        
        if action.lower() in ['chart', 'buy', 'sell']:
            stock_symbol = input("Enter stock symbol: ").upper()
            try:
                currency = get_stock_currency(stock_symbol)
                if not currency:
                    print("Invalid stock symbol. Please try again.")
                    continue
            except Exception:
                print("Invalid stock symbol. Please try again.")
                continue
        else:
            currency = ""
        
        if action.lower() == 'chart':
            print("\nSelect time period:")
            print("1. Today (1-minute intervals) - Live-ish")
            print("2. Last 7 Days (30-minute intervals)")
            print("3. Last 1 Month (Daily)")
            print("4. Last 1 Year (Weekly)")
            print("5. Last 5 Years (Weekly)")
            print("6. All Time (Monthly)")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                live_plot_data(stock_symbol, currency)
                fetch_and_print_news(stock_symbol)
            else:
                period = '1mo'
                interval = '1d'
                if choice == '2': period, interval = '7d', '30m'
                elif choice == '3': period, interval = '1mo', '1d'
                elif choice == '4': period, interval = '1y', '1wk'
                elif choice == '5': period, interval = '5y', '1wk'
                elif choice == '6': period, interval = 'max', '1mo'
                else: print("Invalid choice. Defaulting to 1 month (Daily).")
                
                stock_data = get_stock_history(stock_symbol, period=period, interval=interval)
                
                if not stock_data.empty:
                    stock_data_with_indicators = calculate_simple_moving_average(stock_data)
                    stock_data_with_indicators = calculate_exponential_moving_average(stock_data_with_indicators)
                    stock_data_with_indicators = calculate_rsi(stock_data_with_indicators)
                    latest_price = stock_data_with_indicators['Close'].iloc[-1]
                    plot_closing_price(stock_data_with_indicators, stock_symbol, latest_price, currency)
                    fetch_and_print_news(stock_symbol)
                else:
                    print(f"Could not fetch data for {stock_symbol}. Please check the symbol.")
        
        elif action.lower() == 'buy':
            quantity = int(input("Enter quantity to buy: "))
            current_price_data = get_stock_history(stock_symbol, period='1d', interval='1m')
            if not current_price_data.empty:
                current_price = current_price_data['Close'].iloc[-1]
                my_portfolio.buy(stock_symbol, quantity, current_price)
            else:
                print("Could not get current price. Purchase failed.")
        
        elif action.lower() == 'sell':
            if stock_symbol in my_portfolio.holdings:
                quantity = int(input("Enter quantity to sell: "))
                current_price_data = get_stock_history(stock_symbol, period='1d', interval='1m')
                
                if not current_price_data.empty:
                    current_price = current_price_data['Close'].iloc[-1]
                    my_portfolio.sell(stock_symbol, quantity, current_price)
                else:
                    print("Could not get current price. Sell failed.")
            else:
                print(f"You do not hold any shares of {stock_symbol}.")
        
        elif action.lower() == 'value':
            current_prices = {}
            if my_portfolio.holdings:
                print("Fetching current prices for your holdings...")
                for symbol in my_portfolio.holdings:
                    price_data = get_stock_history(symbol, period='1d', interval='1m')
                    if not price_data.empty:
                        current_prices[symbol] = price_data['Close'].iloc[-1]
                    else:
                        current_prices[symbol] = 0
                
                total_value = my_portfolio.get_portfolio_value(current_prices)
                print(f"\nTotal Portfolio Value: {currency} {total_value:.2f}")
                print("Current Holdings:", my_portfolio.holdings)
            else:
                print("Your portfolio is currently empty.")
        else:
            print("Invalid action. Please enter 'chart', 'buy', 'sell', 'value', or 'exit'.")
        
        if action.lower() != 'value':
            print("\nCurrent Portfolio Cash:", f"{my_portfolio.cash:.2f}")
            print("Current Holdings:", my_portfolio.holdings)
        
if __name__ == "__main__":
    main()