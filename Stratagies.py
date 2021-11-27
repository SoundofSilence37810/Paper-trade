#Modules
import yfinance as yf

#Test function
def yFinance_test():

    #Set the ticker to CIBC
    cibc = yf.Ticker("CM.TO")

    #Get the stock information dictionary
    cibc.info

    print(cibc.info)

# Paper trade from past data
def paper_trade():
    pass

