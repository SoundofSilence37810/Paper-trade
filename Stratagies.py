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

    #print(price_info.columns)
    #print(price_info.columns)

    #print(price_info[3:])
    # print(price_info)
    #
    # for key in price_info:
    #     print(key,price_info[key][1])

    #Display a chart
    # plt.plot(price_info.index, price_info.iloc[:,[3]],price_info.index,price_info.iloc[:,[7]])
    # plt.title(ticker)
    # plt.xlabel=('Price')
    # plt.ylabel=('Year')
    # plt.show()

    #Loop through all the closing prices

    print(('Initial Price: {a}').format(a = price_info.iloc[:,[3]].values[0]))

    increase_flag = False
    decrease_flag = False

    total_number_of_increases = 0
    total_number_of_decreases = 0

    number_of_percent_increases = 0
    number_of_percent_decreases = 0

    number_increases_after_a_decrease = 0

    pivot_price = price_info.iloc[:,[3]].values[0]

    for closing_price in price_info.iloc[:,[3]].values:
        #Get the difference between the current closing price and the pivot value

        #The price of the stock has increased
        if(pivot_price < closing_price):

            #Set decrease flag to true
            if decrease_flag == True:
                decrease_flag = False
                number_increases_after_a_decrease +=1

            #Increase Increase Counter
            total_number_of_increases +=1

            percent_difference = ((closing_price - pivot_price) / pivot_price) * 100

            if(percent_difference > 3):
                #Number of criteria percent increaes
                number_of_percent_increases +=1
                pivot_price = closing_price
                print('Price Increase: {a}'.format(a = percent_difference))

        #The price of the stock has decreased
        elif(pivot_price > closing_price):

            #Increase Decrease Counter
            total_number_of_decreases +=1

            #Set decrease flag to true
            decrease_flag = True

            percent_difference = ((pivot_price - closing_price) / pivot_price) * 100

            if(percent_difference > 3):
                #Number of criteria percent decreases
                number_of_percent_decreases +=1
                pivot_price = closing_price
                print('Price Decrease: {a}'.format(a = percent_difference))

    #Questions answered
    print('Total number of price increases: {a}'.format(a = total_number_of_increases))
    print('Total number of price decreases: {a}'.format(a = total_number_of_decreases))

    #Questions answered
    print('Number of percent increases: {a}'.format(a = number_of_percent_increases))
    print('Number of percent decreases: {a}'.format(a = number_of_percent_decreases))

    #Questions answered
    print('3% increase after 3% decrease: {a}'.format(a = number_increases_after_a_decrease))

    # Paper trade from past data
def paper_trade():
    pass

# Determine the margin of safety
def mos():
    pass

# Determine the number of price fluctuations at a given percentage
def flucuations():
    #The date is the index so 1 is the first index/date
    pivot_index = 1

    #Start with the second index/date
    compare_index = 2

    #for each index = price_info.iloc[:,[3]]:
    #    pass


