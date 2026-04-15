from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from core.portfolio import Portfolio
from services.graph_service import get_chart_base64
from services.stock_service import get_live_price, get_stock_info, get_stock_news
from services.ai_service import summarize_news

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Enable CORS for the Node.js frontend to interact seamlessly
CORS(app)

# In-memory Portfolio for MVP (Simple state management for a single-user demo)
# In production, this would be backed by a database.
user_portfolio = Portfolio(initial_cash=1000000.0, base_currency='INR')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    symbol = data.get('symbol', 'AAPL')
    period = data.get('period', '1Y')
    indicators = data.get('indicators', [])
    chart_type = data.get('chart_type', 'candle')
    
    chart_img, rsi_img = get_chart_base64(symbol, period, indicators, chart_type)
    
    if chart_img is None:
        return jsonify({"error": "Failed to generate chart. Ensure symbol is valid."}), 400
        
    return jsonify({
        "chart_image": chart_img,
        "rsi_image": rsi_img
    })

@app.route('/api/live-price', methods=['GET'])
def live_price():
    symbol = request.args.get('symbol', 'AAPL')
    data = get_live_price(symbol)
    if "error" in data:
        return jsonify(data), 400
    return jsonify(data)

@app.route('/api/news', methods=['GET'])
def news():
    symbol = request.args.get('symbol', 'AAPL')
    articles = get_stock_news(symbol)
    
    # Generate AI Summary
    summary = summarize_news(articles)
    
    return jsonify({
        "summary": summary,
        "articles": articles
    })

@app.route('/api/stock-info', methods=['GET'])
def stock_info():
    symbol = request.args.get('symbol', 'AAPL')
    data = get_stock_info(symbol)
    if "error" in data:
        return jsonify(data), 400
    return jsonify(data)

# --- Portfolio Endpoints ---

@app.route('/api/portfolio/status', methods=['GET'])
def portfolio_status():
    return jsonify({
        "cash": user_portfolio.cash,
        "currency": user_portfolio.base_currency,
        "holdings": user_portfolio.holdings
    })

@app.route('/api/portfolio/buy', methods=['POST'])
def portfolio_buy():
    data = request.json
    symbol = data.get('symbol')
    quantity = data.get('quantity', 1)
    price = data.get('price')
    currency = data.get('currency', 'USD')
    
    if not symbol or not price:
        return jsonify({"error": "Symbol and price are required"}), 400
        
    success = user_portfolio.buy(symbol, quantity, price, currency)
    if success:
        return jsonify({"message": f"Successfully bought {quantity} shares of {symbol}"})
    return jsonify({"error": "Insufficient funds or transaction failed"}), 400

@app.route('/api/portfolio/sell', methods=['POST'])
def portfolio_sell():
    data = request.json
    symbol = data.get('symbol')
    quantity = data.get('quantity', 1)
    price = data.get('price')
    currency = data.get('currency', 'USD')
    
    if not symbol or not price:
        return jsonify({"error": "Symbol and price are required"}), 400
        
    success = user_portfolio.sell(symbol, quantity, price, currency)
    if success:
        return jsonify({"message": f"Successfully sold {quantity} shares of {symbol}"})
    return jsonify({"error": "Insufficient holdings or transaction failed"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Typical PaaS environments like Render/Railway set special env vars
    # We default debug=True for local, but False if FLASK_ENV is production
    debug_mode = os.environ.get('FLASK_DEBUG', 'true').lower() == 'true'
    
    print("=========================================")
    print(f"IntelliTrade Flask REST API Started on port {port}")
    print(f"Debug Mode: {'Enabled' if debug_mode else 'Disabled'}")
    print("➜ Connects to the Node.js Dashboard")
    print("=========================================")
    
    app.run(host='0.0.0.0', port=port, debug=debug_mode)