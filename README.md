# 🤖 IntelliTrade – AI-Powered Trading Assistant (Phase 1)

Driven by a passion for automated finance, **IntelliTrade** is a personal long-term project aimed at leveraging AI to make intelligent, hands-free trading decisions, learning autonomously from stock data and financial news.

This is **Phase 1**, where the initial focus is on:
- Fetching live stock market data (Indian & Global).
- Visualizing it in clean, user-friendly graphs.
- Allowing interactive input from the user.

---

## 🚀 Features So Far

- ✅ Fetches **live stock data** using `yfinance`.
- ✅ Accepts **user input** for stock symbols (e.g., `AAPL`, `SUZLON.NS`).
- ✅ Plots last 30 days of **daily closing prices** as a line graph using `matplotlib`.
- ✅ Clear, beginner-friendly Python code with full documentation.

---

## 📊 Sample Output

![Sample Stock Chart](images/sample_chart.png)

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-blue?style=for-the-badge&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-green?style=for-the-badge&logo=matplotlib&logoColor=white)

---

## 🛣️ Roadmap

- [ ] Add support for **candlestick charts**.
- [ ] Implement **custom date range** selection for data fetching and plotting.
- [ ] Integrate various **technical indicators** (e.g., RSI, MACD, Moving Averages) into charts and data.
- [ ] Develop **news sentiment analysis** using Natural Language Processing (NLP) to gauge market sentiment.
- [ ] Begin implementing **machine learning models** for stock price prediction.
- [ ] Explore connecting to a **real broker API** for live or paper trading (simulated trading).
- [ ] Build a full **web dashboard** for user interaction and visualization (possibly using Flask, React, or similar web frameworks).

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
    Ensure you have a `requirements.txt` file in your project's root directory with `yfinance` and `matplotlib` listed (as you've done).
    Then, install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    *(Currently, your core scripts are `graph_fetcher.py` and `stock_price_fetcher.py` within the `src/` directory. As the project evolves, you will likely use `main.py` as your primary entry point after refactoring.)*

    To run the stock chart plotter:
    ```bash
    python src/graph_fetcher.py
    ```
    To run the live price fetcher:
    ```bash
    python src/stock_price_fetcher.py
    ```
    Follow the on-screen prompts to enter stock symbols.

---

## 👨‍💻 Author

Tanishq Chhabra
Just getting started. IntelliTrade may take months or years to complete — but it’s happening. 🚀

---

## 📌 License

**All rights reserved.**

This is a personal project by Tanishq Chhabra. You may not copy, modify, distribute, or reuse any part of this code or content without explicit written permission from the author.
