import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

ticker = input("Enter a stock symbol (e.g., AAPL, INFY.NS, TCS.NS): ")
data = yf.download(ticker, period="1mo", interval="1d")  # 1 month of data

if data.empty:
    print("No data found for the given symbol. Please check the ticker.")
else:
    # Calculate daily percentage return
    data['Daily Return (%)'] = data['Close'].pct_change() * 100

    # Plot the closing price
    plt.figure(figsize=(8,4))
    plt.plot(data.index, data['Close'], label='Closing Price')
    plt.title(f"Last Month Closing Price for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot daily returns
    plt.figure(figsize=(8,4))
    plt.plot(data.index, data['Daily Return (%)'], marker='o', linestyle='-', label='Daily Return %')
    plt.title(f"Daily Returns (%) for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Daily Return (%)")
    plt.grid(True)
    plt.legend()
    plt.show()

    print("\nSummary Stats:")
    print(data[['Close', 'Daily Return (%)']].describe())
