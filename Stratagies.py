#Modules
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

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

    stock_financials = ticker_object.financials

    print(stock_financials)
#ticker_object.
    #print(ticker_object.dividends)

    #print(ticker_object.info)

    #print(price_info.loc[:,["Close"]])

    #Create a new simple moving average column
    price_info["sm_50"] = price_info.iloc[:,2].rolling(window=50).mean()

    #Set the iLOC(Index Location) after the first 50 rows
    price_info = price_info.iloc[50:]

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

    percentage_increase_decrease = 35

    increase_flag = False
    decrease_flag = False

    total_number_of_increases = 0
    total_number_of_decreases = 0

    number_of_percent_increases = 0
    number_of_percent_decreases = 0

    number_increases_after_a_decrease = 0

    pivot_price = price_info.iloc[:,[3]].values[0]

    #Loops through all the closing price values
    for closing_price in price_info.iloc[:,[3]].values:
        #Get the difference between the current closing price and the pivot value

        #The price of the stock has increased
        if(pivot_price < closing_price):

            #Increase Increase Counter
            total_number_of_increases +=1

            percent_difference = ((closing_price - pivot_price) / pivot_price) * 100

            if(percent_difference > percentage_increase_decrease ):
                #Number of criteria percent increaes
                number_of_percent_increases +=1
                pivot_price = closing_price
                print('Price Increase: {a}'.format(a = percent_difference))

                #Set decrease flag to true
                if decrease_flag == True:
                    decrease_flag = False
                    number_increases_after_a_decrease +=1

        #The price of the stock has decreased
        elif(pivot_price > closing_price):

            #Increase Decrease Counter
            total_number_of_decreases +=1



            percent_difference = ((pivot_price - closing_price) / pivot_price) * 100

            if(percent_difference > percentage_increase_decrease ):

                #Set decrease flag to true
                decrease_flag = True

                #Number of criteria percent decreases
                number_of_percent_decreases +=1
                pivot_price = closing_price
                print('Price Decrease: {a}'.format(a = percent_difference))

    #Questions answered
    print('\nTotal number of price increases: {a}'.format(a = total_number_of_increases))
    print('Total number of price decreases: {a}'.format(a = total_number_of_decreases))

    #Questions answered
    print('\nNumber of {b} percent increases: {a}'.format(a = number_of_percent_increases, b=percentage_increase_decrease))
    print('Number of {b} percent decreases: {a}'.format(a = number_of_percent_decreases, b=percentage_increase_decrease))

    #Questions answered
    print('\n{b}% increase after {b}% decrease: {a}'.format(a = number_increases_after_a_decrease, b=percentage_increase_decrease ))

    #Question answered
    win_percent = (number_increases_after_a_decrease/number_of_percent_decreases)*100

    print('Percentage of wins: {a}'.format(a=win_percent))

    # Paper trade from past data
def paper_trade():
    pass

# Determine the margin of safety
# Yahoo finance only has four years of data
def mos(ticker:str) -> tuple:

    #Fixes compatibility issues with yahoo finance
    yf.pdr_override()

    #Set the ticker_object to ticker
    ticker_object = yf.Ticker(ticker)

    #Get the financial informaiton from Yahoo Finance
    stock_financials = ticker_object.financials

    print(stock_financials)

    #Information Needed for MOS Calculation
    #1. Annual Total Revenue

    percentgrowth = 0

    numberOfYears = 0

    lastYearsRevenue = 0

    growthRate = 0

    accumulatedGrowthRate = 0

    #Calculate the growth rate, Yahoo Finance Only Shows the Past Four Years
    for year in stock_financials.iloc[15:16,:].values:

        #
        for totalRevenue in reversed(year):
            if numberOfYears > 0:
                growthRate = (totalRevenue-lastYearsRevenue)/totalRevenue

            #Move this information to a log in the future
            print(f'Year: {numberOfYears+1} Revenue: {totalRevenue} GrowthRate: {abs(growthRate*100)}')

            #Get the accumulated growth rate
            accumulatedGrowthRate = accumulatedGrowthRate + abs(growthRate*100)

            #Save last years revenue
            lastYearsRevenue = totalRevenue

            #Increase the index number
            numberOfYears +=1

    growthRate = accumulatedGrowthRate/(numberOfYears-1)

    #Move output from this funcion
    print(f'\nWARNING: YAHOO DATA IS SOMETIMES WRONG!')
    print(f'\nGrowth rate is {growthRate} over {numberOfYears} years.')

    #Return the growth rate and over how many years the calculation was done for
    return growthRate, numberOfYears

# Determine the number of price fluctuations at a given percentage
def flucuations():
    #The date is the index so 1 is the first index/date
    pivot_index = 1

    #Start with the second index/date
    compare_index = 2

    #for each index = price_info.iloc[:,[3]]:
    #    pass

#Calculates the number of days the price increased for a given stock verses a price decrease with a given percentage
def dailyPriceIncreaseDecrease(ticker:str, percent:int):
    #Fixes compatibility issues with yahoo finance
    yf.pdr_override()

    #Set the ticker_object to ticker
    ticker_object = yf.Ticker(ticker)

    #Get the stock information pandas dataframe
    stock_info = ticker_object.info

    #Get the price information as a pandas dataframe
    price_info = ticker_object.history(period="max")

    #Loop through all the closing prices

    print(('Initial Price: {a}').format(a = price_info.iloc[:,[3]].values[0]))

    percentage_increase_decrease = percent

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

            #Increase Increase Counter
            total_number_of_increases +=1

            percent_difference = ((closing_price - pivot_price) / pivot_price) * 100

            if(percent_difference > percentage_increase_decrease ):
                #Number of criteria percent increaes
                number_of_percent_increases +=1
                pivot_price = closing_price
                print('Price Increase: {a}'.format(a = percent_difference))

                #Set decrease flag to true
                if decrease_flag == True:
                    decrease_flag = False
                    number_increases_after_a_decrease +=1

        #The price of the stock has decreased
        elif(pivot_price > closing_price):

            #Increase Decrease Counter
            total_number_of_decreases +=1



            percent_difference = ((pivot_price - closing_price) / pivot_price) * 100

            if(percent_difference > percentage_increase_decrease ):

                #Set decrease flag to true
                decrease_flag = True

                #Number of criteria percent decreases
                number_of_percent_decreases +=1
                pivot_price = closing_price
                print('Price Decrease: {a}'.format(a = percent_difference))

    #Questions answered
    print('\nTotal number of price increases: {a}'.format(a = total_number_of_increases))
    print('Total number of price decreases: {a}'.format(a = total_number_of_decreases))

    #Questions answered
    print('\nNumber of {b} percent increases: {a}'.format(a = number_of_percent_increases, b=percentage_increase_decrease))
    print('Number of {b} percent decreases: {a}'.format(a = number_of_percent_decreases, b=percentage_increase_decrease))

    #Questions answered
    print('\n{b}% increase after {b}% decrease: {a}'.format(a = number_increases_after_a_decrease, b=percentage_increase_decrease ))

    #Question answered
    win_percent = (number_increases_after_a_decrease/number_of_percent_decreases)*100

    print('Percentage of wins: {a}'.format(a=win_percent))

#Pick a date to buy a stock, number of shares, and purchase date
#def mos(ticker:str, numberOfShares:int, dateOfPurchase:datetime, ) -> tuple:
#    pass


def price_chart(tickersymbol: str):
    #Fixes compatibility issues with yahoo finance
    yf.pdr_override()

    #Set the ticker_object to ticker
    ticker_object = yf.Ticker(tickersymbol)

    #Get the stock information pandas dataframe
    stock_info = ticker_object.info

    #Get the price information as a pandas dataframe
    price_info = ticker_object.history(period="max")

    #print(price_info[3:])
    # print(price_info)
    #
    # for key in price_info:
    #     print(key,price_info[key][1])

    #Display a chart
    #plt.plot(price_info.index, price_info.iloc[:,[3]],price_info.index,price_info.iloc[:,[7]])
    #plt.title(tickersymbol)
    #plt.xlabel=('Price')
    #plt.ylabel=('Year')
    #plt.show()




