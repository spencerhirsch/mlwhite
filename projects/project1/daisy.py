import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker_symbol = "^DJI"  # Ticker symbol for Dow Jones Industrial Average

# Define the start and end dates for the historical data
start_date = "1999-01-22"
end_date = "2024-03-21"

# Fetch historical data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save data to CSV file
data.to_csv("dji.csv")
