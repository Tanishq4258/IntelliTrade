class Portfolio:
    def __init__(self, initial_cash):
        self.cash = initial_cash
        self.holdings = {}
        print(f"Portfolio initialized with {self.cash:.2f} cash.")
    
    def buy(self, symbol, quantity, price):
        cost = quantity * price
        if cost > self.cash:
            print("Not enough cash to make this purchase.")
            return False
        self.cash -=cost
        if symbol in self.holdings:
            self.holdings[symbol]['quantity'] += quantity
        else:
            self.holdings[symbol] = {'quantity': quantity, 'buy_price': price}

        print(f"Bought {quantity} of {symbol} at {price:.2f}. Remaining cash: {self.cash:.2f}")
        return True

    def sell(self, symbol, quantity, price):
        if symbol not in self.holdings or self.holdings[symbol]['quantity'] < quantity:
            print("Not enough shares to sell.")
            return False

        self.cash += quantity * price
        self.holdings[symbol]['quantity'] -= quantity

        if self.holdings[symbol]['quantity'] == 0:
            del self.holdings[symbol]

        print(f"Sold {quantity} of {symbol} at {price:.2f}. New cash: {self.cash:.2f}")
        return True

    def get_portfolio_value(self, current_prices):
        total_value = self.cash
        for symbol, data in self.holdings.items():
            if symbol in current_prices:
                total_value += data['quantity'] * current_prices[symbol]
        return total_value