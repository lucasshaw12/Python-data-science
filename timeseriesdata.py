#! python3

#  Timeseries data

##############
# Time series analysis techniques
##############

import yfinance as yf
import pandas as pd
import numpy as np
ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='5d')
# print(df)
# print(df['Close'])

##############
# Calculating percentage changes
##############
# print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1, keys=['Close', '2DaysShift']))  # Calculating percentage changes...
# ... by comparing the close date from the close date 2 days earlier using 'shift(2)'.
# print((df['Close'] - df['Close'].shift(2)) / df['Close'].shift(2))  # percentage change from two days earlier to now.
df['2DaysRise'] = np.log(df['Close'] / df['Close'].shift(2))  # Calculate 2 day change using natural logarithm
# print(df[['Close', '2DaysRise']])

##############
# Rolling average calculations
##############

df['2DaysAvg'] = df['Close'].shift(1).rolling(2).mean()
# print(df[['Close', '2DaysAvg']])

##############
# Percentage change of Rolling average
##############

df['2DaysAvgRise'] = np.log(df['Close'] / df['2DaysAvg'])
# print(df[['Close', '2DaysRise', '2DaysAvgRise']])

##############
# Multivariate Time Series
##############

stocks = pd.DataFrame()
tickers = ['MSFT', 'TSLA', 'GM', 'AAPL', 'ORCL', 'AMZN']
for ticker in tickers:
    tkr = yf.Ticker(ticker)
    hist = tkr.history(period='5d')
    hist = pd.DataFrame(hist[['Close']].rename(columns={'Close': ticker}))
    if stocks.empty:
        stocks = hist
    else:
        stocks = stocks.join(hist)
# print(stocks)

##############
# Processing multivariate Time Series
##############

stocks_to_keep = []
for i in stocks.columns:
    if stocks[stocks[i]/stocks[i].shift(1) < .97].empty:
        stocks_to_keep.append(i)
# print(stocks_to_keep)
# print(stocks[stocks_to_keep])

##############
# Analysing dependencies between variables
##############

ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')
print(df)
df = df[['Close', 'Volume']].rename(columns={'Close': 'Price'})  # Change column name from 'Close' to 'Price'
df['priceRise'] = np.log(df['Price'] / df['Price'].shift(1))  # show percentage change in price over past 2 days
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))  # show percentage change in volume over past 2 days
print(df)
print(df[abs(df['priceRise']) > .05])  # Show which 'price' values go over 5% change +/-
print(df['volumeRise'].mean().round(4))  # Average volume change over entire series
print(df[abs(df['priceRise']) > .05]['volumeRise'].mean().round(4))  # Average volume change for row with above average changes in price











