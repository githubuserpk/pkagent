import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
from scipy import interpolate

def plot_stock_price(ticker, start_date, end_date):
    """Plots the stock price for the specified date range, showing a smooth, continuous line."""

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

    # Get the company name and final close price
    company_info = yf.Ticker(ticker).info
    company_name = company_info.get('longName', ticker)
    final_close = stock_data['Close'].iloc[-1] if not stock_data.empty else None

    # Create a smooth interpolation
    x = stock_data.index.astype(int) / 10**9  # Convert to Unix timestamp
    y = stock_data['Close'].values
    f = interpolate.interp1d(x, y, kind='cubic')

    # Create more points for a smoother curve
    x_smooth = pd.date_range(start=stock_data.index.min(), end=stock_data.index.max(), periods=1000)
    x_smooth_unix = x_smooth.astype(int) / 10**9
    y_smooth = f(x_smooth_unix)

    # Create the smooth line chart using Plotly Express
    fig = px.line(x=x_smooth, y=y_smooth, title=f"{ticker} Stock Price", labels={'x': 'Time', 'y': 'Price'})
    
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
        xaxis=dict(tickformat='%H:%M', tickangle=0),  # Flat x-axis labels
        hovermode='x'
    )

    return fig

# The rest of your Streamlit app code remains the same