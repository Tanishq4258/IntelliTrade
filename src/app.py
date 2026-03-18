from flask import Flask, request, jsonify
from flask_cors import CORS
from graph_fetcher import get_chart_base64
from stock_price_fetcher import get_live_price, get_stock_info, get_stock_news

app = Flask(__name__)
# Enable CORS for the Node.js frontend to interact seamlessly
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    symbol = data.get('symbol', 'AAPL')
    period = data.get('period', '1Y')
    indicators = data.get('indicators', [])
    
    chart_img, rsi_img = get_chart_base64(symbol, period, indicators)
    
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
    data = get_stock_news(symbol)
    return jsonify(data)

@app.route('/api/stock-info', methods=['GET'])
def stock_info():
    symbol = request.args.get('symbol', 'AAPL')
    data = get_stock_info(symbol)
    if "error" in data:
        return jsonify(data), 400
    return jsonify(data)

if __name__ == '__main__':
    print("=========================================")
    print("IntelliTrade Flask REST API Started")
    print("➜ Connects to the Node.js Dashboard")
    print("=========================================")
    app.run(host='0.0.0.0', port=5000, debug=True)