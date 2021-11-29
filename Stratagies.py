#Modules
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Test function
def yFinance_test(ticker:str):

    #Fixes compatibility issues with yahoo finance
    yf.pdr_override()

    #Set the ticker_object to ticker
    ticker_object = yf.Ticker(ticker)

    #Get the stock information pandas dataframe
    stock_info = ticker_object.info

    #Get the price information as a pandas dataframe
    price_info = ticker_object.history(period="max")

    #ticker_object.
    #print(ticker_object.dividends)

    #print(ticker_object.info)

    #print(price_info.loc[:,["Close"]])

    #Create a new simple moving average column
    price_info["sm_50"] = price_info.iloc[:,2].rolling(window=50).mean()

    #Set the iLOC(Index Location) after the first 50 rows
    price_info = price_info.iloc[50:]

    print(price_info.columns)
    #print(price_info.columns)

    #print(price_info[3:])
    # print(price_info)
    #
    # for key in price_info:
    #     print(key,price_info[key][1])

    #Display a chart
    plt.plot(price_info.index, price_info.iloc[:,[3]],price_info.index,price_info.iloc[:,[7]])
    plt.title(ticker)
    plt.xlabel=('Price')
    plt.ylabel=('Year')
    plt.show()

# Paper trade from past data
def paper_trade():
    pass

# Determine the margin of safety
def mos():
    pass

# Determine the number of price flucuations at a given percentage
def flucuations():
    pass

