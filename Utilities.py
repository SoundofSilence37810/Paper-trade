#Utilities Module
#Using yahoo_fin

import yahoo_fin.stock_info as si

#Get a list of all stock symbols for a particular market
def get_all_stock_symbols(exchange:str):

    tickers = si.tickers_sp500()
    #tickers  =si.get_data("nflx")

    print(tickers)

