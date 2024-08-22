import streamlit as st
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

def plot_stock_price(ticker, start_date, end_date):
    """Plots the stock price for the specified date range, showing hour by hour data."""

    # Fetch stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date + timedelta(days=1), interval="1h")

    # Check if we have data
    if stock_data.empty:
        st.write("No data available for the specified period.")
        return None

    # Ensure index is datetime
    stock_data.index = pd.to_datetime(stock_data.index)

    # Create the line chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(stock_data.index, stock_data['Close'], linewidth=2, color='#1a73e8')  # Google blue color
    ax.set_title(f"{ticker} Stock Price", fontsize=16, fontweight='bold')
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Price', fontsize=12)

    # Format x-axis to show hours
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Show every hour
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.xticks(rotation=45, ha='right')

    # Add gridlines
    ax.grid(True, linestyle='--', alpha=0.7)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Adjust layout
    plt.tight_layout()

    return fig

# Streamlit app
st.title("Stock Price Viewer")

# User input for ticker
ticker = st.text_input("Enter stock ticker (e.g., GOOGL):", "GOOGL")

# Date pickers for start and end dates
start_date = st.date_input("Start date", datetime.now().date() - timedelta(days=7))
end_date = st.date_input("End date", datetime.now().date())

if st.button("Show Stock Price"):
    if start_date > end_date:
        st.write("Error: End date must fall after start date.")
    else:
        fig = plot_stock_price(ticker, start_date, end_date)
        if fig:
            st.pyplot(fig)
        else:
            st.write("Unable to display chart. Please try a different ticker or time range.")