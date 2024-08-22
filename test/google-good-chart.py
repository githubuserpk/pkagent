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
        xaxis=dict(tickformat='%H:%M', tickangle=0),  # Flat x-axis labels
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