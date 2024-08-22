import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
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

    # Filter data to start from 10 AM
    stock_data = stock_data.between_time('10:00', '23:59')

    # Create the line chart using Plotly
    fig = px.line(stock_data, x=stock_data.index, y='Close', title=f"{ticker} Stock Price", labels={'x': 'Time', 'Close': 'Price'})
    fig.update_layout(
        xaxis_title='Time',
        yaxis_title='Price',
        xaxis=dict(tickformat='%H:%M', tickangle=0),  # Flat x-axis labels
        title={'x': 0.5},  # Center the title
        hovermode='x'
    )

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
            st.plotly_chart(fig)
        else:
            st.write("Unable to display chart. Please try a different ticker or time range.")