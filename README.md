# 🤖 IntelliTrade – AI-Powered Trading Assistant

Driven by a passion for automated finance, IntelliTrade is a personal long-term project aimed at leveraging AI to provide intelligent, data-driven suggestions to a human trader. It is a companion to help analyze and interpret stock market data, not an automated system for guaranteed profit.

This project is in active development, with a focus on building a robust backend for data fetching, analysis, and visualization.

---

🚀 Features Implemented So Far
        
        ✅ Modular & Scalable Architecture: The project has been refactored into a clean src/ directory with dedicated modules for data fetching, analysis, and plotting.
        
        ✅ Advanced Technical Indicators: Can calculate and plot a Simple Moving Average (SMA), Exponential Moving Average (EMA), and the Relative Strength Index (RSI).
        
        ✅ Dynamic Data Visualization: Plots a live-updating intraday graph and static charts for user-selected time periods (day, week, month, year).
        
        ✅ Live Data & News Integration: Fetches live-ish intraday price data and displays the latest financial news and sentiment from a news API.
        
        ✅ Currency Handling: Automatically detects and displays the correct currency (e.g., USD, INR) for the selected stock.
        
        ✅ Multi-threading for Performance: Uses multi-threading to fetch news articles simultaneously while the graphs are being plotted, providing a smoother user experience.
        
        ✅ Professional Candlestick Charts: Replaced basic line charts with industry-standard candlestick visualization using `mplfinance`.
        
        ✅ Portfolio Simulator: Integrated a mock trading engine with a $10,000 starting balance for paper trading stocks.
        
        ✅ AI-Powered News Summaries: Leverages Google Gemini AI to condense market news into concise, 2-sentence insights.
        
        ✅ Production-Ready Architecture: Optimized for cloud deployment (Render/Railway) with dynamic API routing and gunicorn support.
  

    
---

## 📊 Sample Output

![Sample Stock Chart](images/progress_18-03-2026.png)
![Sample Stock Chart](images/progress2_18-03-2026.png)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-blue?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-green?style=for-the-badge&logo=matplotlib&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

---

## 🛣️ Roadmap

        [x] Add support for candlestick charts.

        [ ] Implement custom date range selection for data fetching and plotting.

        [ ] Implement machine learning for price prediction.

        [x] Implement portfolio and budgeting logic to track mock investments.

        [ ] Connect to a real broker API for live or paper trading (simulated trading).

        [x] Build a full web dashboard (v1.0 complete).

---

## 🛠️ How to Run

To get IntelliTrade up and running on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Tanishq4258/IntelliTrade.git](https://github.com/Tanishq4258/IntelliTrade.git)
    cd IntelliTrade
    ```

2.  **(Optional but Recommended) Create and activate a Python virtual environment:**
    Using a virtual environment helps isolate your project's dependencies and prevents conflicts with other Python projects.
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    Ensure you have a `requirements.txt` file in your project's root directory.
    Then, install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Backend API Server:**
    
    Our newly integrated Flask Server wraps the fetchers into REST endpoints over port 5000:
    ```bash
    python src/app.py
    ```
    *(If you prefer the old terminal method for testing charts, run `python src/services/graph_service.py` directly).*

5.  **Run the Frontend Dashboard (Node.js/Express):**

    Navigate to the `frontend` directory, install dependencies, and start the server:
    ```bash
    cd frontend
    npm install
    npm start
    ```
    Then, open [http://localhost:3000](http://localhost:3000) in your web browser. The dashboard will automatically fetch data from `http://localhost:5000/api` based on the backend API contract.

---

## 👨‍💻 Author

Tanishq Chhabra
Just getting started. IntelliTrade may take months or years to complete — but it’s happening. 🚀

---

## 📌 License

**All rights reserved.**

This is a personal project by Tanishq Chhabra. You may not copy, modify, distribute, or reuse any part of this code or content without explicit written permission from the author.
