from data_fetcher import get_exchange_rate
class Portfolio:
    def __init__(self, initial_cash, base_currency):
        self.cash = initial_cash
        self.base_currency = base_currency
        self.holdings = {}
        print(f"Portfolio initialized with {self.cash:.2f} {self.base_currency}.")

    def buy(self, symbol, quantity, price, stock_currency):
        cost = quantity * price
        
        # Convert cost to the portfolio's base currency
        if stock_currency != self.base_currency:
            exchange_rate = get_exchange_rate(stock_currency, self.base_currency)
            cost *= exchange_rate
            print(f"Converted cost to {self.base_currency} at rate {exchange_rate:.2f}.")

        if cost > self.cash:
            print("Not enough cash to make this purchase.")
            return False
        
        self.cash -= cost
        if symbol in self.holdings:
            self.holdings[symbol]['quantity'] += quantity
        else:
            self.holdings[symbol] = {'quantity': quantity, 'buy_price': price, 'currency': stock_currency}

        print(f"Bought {quantity} of {symbol} at {price:.2f} {stock_currency}. Remaining cash: {self.cash:.2f} {self.base_currency}")
        return True

    def sell(self, symbol, quantity, price, stock_currency):
        if symbol not in self.holdings or self.holdings[symbol]['quantity'] < quantity:
            print("Not enough shares to sell.")
            return False
        
        # Convert revenue to the portfolio's base currency
        revenue = quantity * price
        if stock_currency != self.base_currency:
            exchange_rate = get_exchange_rate(stock_currency, self.base_currency)
            revenue *= exchange_rate
            print(f"Converted revenue to {self.base_currency} at rate {exchange_rate:.2f}.")

        self.cash += revenue
        self.holdings[symbol]['quantity'] -= quantity
        
        if self.holdings[symbol]['quantity'] == 0:
            del self.holdings[symbol]

        print(f"Sold {quantity} of {symbol} at {price:.2f} {stock_currency}. New cash: {self.cash:.2f} {self.base_currency}")
        return True

    def get_portfolio_value(self, current_prices):
        total_value = self.cash
        for symbol, data in self.holdings.items():
            stock_value = data['quantity'] * current_prices.get(symbol, 0)
            
            # Convert holding value to the portfolio's base currency
            if data['currency'] != self.base_currency:
                exchange_rate = get_exchange_rate(data['currency'], self.base_currency)
                stock_value *= exchange_rate
            
            total_value += stock_value
        return total_value