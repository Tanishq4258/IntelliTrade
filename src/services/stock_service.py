# © 2024 Tanishq Chhabra. All rights reserved.
# Made by Tanishq Chhabra for IntelliTrade Project

import yfinance as yf

def get_live_price(symbol):
    stock = yf.Ticker(symbol)
    try:
        # Prefer fast dict info
        info = stock.info
        price = info.get('currentPrice') or info.get('regularMarketPrice')
        prev_close = info.get('previousClose')
        
        if not price:
            # Fallback to history
            hist = stock.history(period='1d')
            price = hist['Close'].iloc[-1]
            prev_close = stock.history(period='5d')['Close'].iloc[-2]
            
        change = ((price - prev_close) / prev_close) * 100 if prev_close else 0
        currency = info.get('currency', 'USD')
        
        # Determine currency symbol
        curr_symbol = '₹' if currency == 'INR' else '$' if currency == 'USD' else currency
        
        return {
            "price": price,
            "change": change,
            "currency": curr_symbol
        }
    except Exception as e:
        return {"error": str(e)}

def get_stock_info(symbol):
    stock = yf.Ticker(symbol)
    try:
        info = stock.info
        price_data = get_live_price(symbol)
        
        market_cap = info.get('marketCap')
        # Format millions / billions / trillions
        if market_cap:
            if market_cap >= 1e12:
                mc_formatted = f"{market_cap / 1e12:.2f}T"
            elif market_cap >= 1e9:
                mc_formatted = f"{market_cap / 1e9:.2f}B"
            elif market_cap >= 1e6:
                mc_formatted = f"{market_cap / 1e6:.2f}M"
            else:
                mc_formatted = str(market_cap)
        else:
            mc_formatted = "N/A"
            
        return {
            "name": info.get('shortName', symbol),
            "price": price_data.get('price', 0),
            "change_pct": price_data.get('change', 0),
            "market_cap": mc_formatted,
            "currency": price_data.get('currency', '$')
        }
    except Exception as e:
        return {"error": str(e)}

def get_stock_news(symbol):
    stock = yf.Ticker(symbol)
    articles = []
    try:
        news = stock.news
        for item in news[:5]:
            articles.append({
                "title": item.get('title', 'Market Update'),
                "source": item.get('publisher', 'News Source'),
                "sentiment": "Neutral", # yfinance doesn't provide sentiment out of box, so stubbing
                "url": item.get('link', '#')
            })
    except Exception as e:
        print(f"News fetch failed: {e}")
    return articles

if __name__ == "__main__":
    # Backward compatibility for direct terminal usage
    stock_symbol = input("Enter Name of stock you want the Live value for: ")
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period='1d')
    print("Live price for ", stock_symbol, "is: ", stock_data['Close'].iloc[-1])