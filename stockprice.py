import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Stock Prices of Ethereum, Bitcoin and Dogecoin


Shown are the stock closing price and volume.

Ethereum (Eth-USD)

""")

#define ticker symbol
tickerSymbol = 'ETH-USD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2020-4-15', end='2021-4-16')
#Open high, low, close, volume, dividends, stock splits

#st.line_chart(tickerDf.High)
#st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
#st.line_chart(tickerDf.Dividends)


st.write("""

Bitcoin (BTC-USD)

""")

#define ticker symbol
tickerSymbol = 'BTC-USD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2012-4-15', end='2021-4-15')

#Open high, low, close, volume, dividends, stock splits

#st.line_chart(tickerDf.High)
#st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
#st.line_chart(tickerDf.Dividends)

st.write("""

Dogecoin (DOGE-USD)

""")

#define ticker symbol
tickerSymbol = 'DOGE-USD'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2012-4-15', end='2021-4-15')

#Open high, low, close, volume, dividends, stock splits

#st.line_chart(tickerDf.High)
#st.line_chart(tickerDf.Low)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
#st.line_chart(tickerDf.Dividends)
