import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Get the stock data
ticker = "GOOGL"
start_date = datetime.datetime.now() - pd.Timedelta(days=365)
end_date = datetime.datetime.now()
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Create the line chart
fig, ax = plt.subplots()
ax.plot(stock_data['Close'], label='Google Stock Price')
ax.set_title('Google Stock Price Over Past Year')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()

# Display the chart in Streamlit
st.pyplot(fig)