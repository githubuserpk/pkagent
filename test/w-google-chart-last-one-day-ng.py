import streamlit as st
import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

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
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=stock_data.index, y='Close', data=stock_data, ax=ax)
    ax.set_title(f"{ticker} Stock Price ({start_date} to {end_date})")
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')

    # Custom formatter function
    def format_date(x, pos=None):
        try:
            return pd.to_datetime(x).strftime('%m-%d %H:%M')
        except (AttributeError, ValueError):
            return ''  # Return empty string if conversion fails

    # Format x-axis labels to display date and hour
    ax.xaxis.set_major_formatter(plt.FuncFormatter(format_date))
    plt.xticks(rotation=45)

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