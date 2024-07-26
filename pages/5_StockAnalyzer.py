import streamlit as st


option = st.selectbox(
    'Select the stock from your Portfolio?',
    ('Google', 'Apple', 'Microsoft', 'Gold'))
st.write('You selected:', option)

#portfolio_start_amount str '£1000'
st.write('Portfolio investment: £1000')
st.write('Start date: 1 Jul 2024')