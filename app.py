import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt6


# Fetch historical stock data
def fetch_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end)


# Calculate the Relative Strength Index (RSI)
def calculate_rsi(data, period=14):
    # Calculate price changes
    delta = data['Close'].diff()

    # Calculate gains and losses
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()

    # Calculate RSI
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


# Calculate Simple Moving Averages (SMA)
def calculate_moving_averages(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()  # 20-day SMA
    data['SMA_50'] = data['Close'].rolling(window=50).mean()  # 50-day SMA


# Plot closing price, SMAs, and RSI
def plot_data(data, ticker):
    # Plot closing price and moving averages
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA_20'], label='20-Day SMA', color='orange')
    plt.plot(data['SMA_50'], label='50-Day SMA', color='green')
    plt.title(f"{ticker} Price and Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

    # Plot RSI
    plt.figure(figsize=(14, 7))
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
    plt.title(f"{ticker} RSI")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()


# Main execution
if __name__ == "__main__":
    ticker = "AAPL"  # Stock ticker symbol
    start_date = "2020-01-01"  # Start date for data
    end_date = "2023-01-01"  # End date for data

    # Fetch stock data
    data = fetch_data(ticker, start_date, end_date)

    # Calculate indicators
    data['RSI'] = calculate_rsi(data)  # Calculate RSI
    calculate_moving_averages(data)  # Calculate SMAs

    # Plot results
    plot_data(data, ticker)
