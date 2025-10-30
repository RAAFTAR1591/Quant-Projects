import yfinance as yf
import matplotlib.pyplot as plt


ticker = input ("Enter a stock ticker symbol: ")

data = yf.download(ticker, period="5d", interval="15m")

if data.empty:
    print("No data found for the given ticker symbol.")
else:
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], marker='o', linestyle='-')
    plt.title(f'5-Day Stock Price for {ticker.upper()} (15-Minute Intervals)')
    plt.xlabel('Date and Time')
    plt.ylabel('Closing Price (USD)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()
    plt.show()
    print(data[['Close']])
