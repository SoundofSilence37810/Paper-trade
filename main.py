#import statements
import sys

#import without dot notation
from Stratagies import *
from Utilities import *

import yfinance as yf

def main() -> int:

    #Application Info
    print(f'Paper Trades Application - For Educational Purposes Only')

    #Get input from the user
    ticker_symbol = input('Please enter a stock symbol: ')

    #Check to make certain the ticker symbol exists

    #get_all_stock_symbols('test')

    #If the ticker symbol is valid or blank
    if ticker_symbol:
        yFinance_test(ticker_symbol)
    else:
        yFinance_test('CM.TO')

    #End program with error code zero
    return 0

if __name__ == '__main__':
    sys.exit(main())