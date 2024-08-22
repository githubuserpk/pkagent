import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from scipy import interpolate

def plot_stock_price(ticker, start_date, end_date, interval):
    """Plots the stock price for the specified date range."""
    
    # Fetch stock data
    stock_data = yf.download(ticker, start=start_date, end=end_date + timedelta(days=1), interval=interval)

    # Check if we have data
    if stock_data.empty:
        st.write("No data available for the specified period.")
        return None

    # Ensure index is datetime
    stock_data.index = pd.to_datetime(stock_data.index)

    # Get the company name and final close price
    company_info = yf.Ticker(ticker).info
    company_name = company_info.get('longName', ticker)
    final_close = stock_data['Close'].iloc[-1] if not stock_data.empty else None

    # Create the line chart using Plotly Express
    fig = px.line(stock_data, x=stock_data.index, y='Close', title=f"{ticker} Stock Price", labels={'x': 'Time', 'Close': 'Price'})
    
    # Add annotations for company name and final close price
    if final_close is not None:
        fig.add_annotation(
            x=stock_data.index[0],  # Position it at the start of the data
            y=final_close,
            text=f"{company_name}<br>Close: ${final_close:.2f}",
            showarrow=False,
            align='left',
            xref='x',
            yref='y',
            bgcolor='white',
            bordercolor='black',
            borderwidth=1,
            opacity=0.8
        )

    fig.update_layout(
        xaxis_title='Time',
        yaxis_title='Price',
        hovermode='x'
    )

    return fig

# Streamlit app
st.title("Stock Price Viewer")

# User input for ticker
ticker = st.text_input("Enter stock ticker (e.g., GOOGL):", "GOOGL")

# Define date ranges and intervals
date_ranges = {
    "1D": (datetime.now() - timedelta(days=1), "1m"),
    "5D": (datetime.now() - timedelta(days=5), "15m"),
    "1 Month": (datetime.now() - timedelta(days=30), "1h"),
    "Last 6M": (datetime.now() - timedelta(days=180), "1d"),
    "Last 1 Yr": (datetime.now() - timedelta(days=365), "1d")
}

# Create tabs
tabs = st.tabs(["1D", "5D", "1 Month", "Last 6M", "Last 1 Yr"])

for label, tab in zip(date_ranges.keys(), tabs):
    with tab:
        start_date, interval = date_ranges[label]
        end_date = datetime.now()
        fig = plot_stock_price(ticker, start_date, end_date, interval)
        if fig:
            st.plotly_chart(fig)
        else:
            st.write("Unable to display chart. Please try a different ticker or time range.")