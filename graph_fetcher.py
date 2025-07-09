# © 2024 Tanishq Chhabra. All rights reserved.
# Made by Tanishq Chhabra for IntelliTrade Project

import yfinance as yf
import matplotlib.pyplot as plt

stock_symbol = input("Enter Name of stock you want last 1 month chart for: ")
stock = yf.Ticker(stock_symbol)

stock_data = stock.history(period='1mo') #1mo means 1 month

print(stock_data['Close'].tail())

plt.figure(figsize=(10,5)) #blank canvas for the graph
plt.plot(stock_data.index, stock_data['Close'], marker='o', linestyle='-')
plt.title(f'{stock_symbol} Closing price - Last 30 days')   
plt.xlabel('Date')
plt.ylabel('Price')
plt.grid(True)
plt.show()
