# © 2024 Tanishq Chhabra. All rights reserved.
# Made by Tanishq Chhabra for IntelliTrade Project

import yfinance as yf

stock_symbol = input("Enter Name of stock you want the Live value for: ")
stock = yf.Ticker(stock_symbol)
stock_data = stock.history(period='1d') #1d means 1 day
print("Live price for ", stock_symbol, "is: ", stock_data['Close'])