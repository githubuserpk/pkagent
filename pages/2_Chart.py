import streamlit as st
import numpy as np
import pandas as pd

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

import seaborn as sns


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


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



# Get the stock data
ticker = "GOOGL"
start_date = datetime.datetime.now() - pd.Timedelta(days=365)
end_date = datetime.datetime.now()
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Resample data to daily frequency if needed
stock_data = stock_data.resample('D').mean()

# Create the line chart
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=stock_data.index, y='Close', data=stock_data, ax=ax)
ax.set_title('Google Stock Price Over Past Year')
ax.set_xlabel('Date')
ax.set_ylabel('Price')

# Display the chart in Streamlit
st.pyplot(fig)