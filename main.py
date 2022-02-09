#import statements
import sys
import datetime as dt

#import without dot notation
from typing import Tuple, Union, Any

from Stratagies import *
from Utilities import *
from Menus import *

import yfinance as yf

def main() -> int:

    #Local Variables
    running = 1
    #Application Info
    print(f'Paper Trades Application - For Educational Purposes Only')

    #Main program loop
    while running == 1:

        #Set up text menu here
        print('\nMAIN MENU\n\n')
        print('1 - Price Chart\n')
        print('2 - Moving Average\n')
        print('3 - MOS\n')
        print('4 - What if?\n')
        print('5 - Quit\n')
        #Get input from the user
        mainMenuInput = input('Menu Option: ')

        if mainMenuInput == 5:
            running = 0

        #Get input from the user
        ticker_symbol = input('Please enter a stock symbol: ')

        #For now lets just break
        break
    #Print Price Chart
    if mainMenuInput == 1:
        pass
    #Print Simple Moving Average
    elif mainMenuInput == 2:
        pass
    #Calculate the MOS price
    elif mainMenuInput == 3:
        pass
    #What if scenarios
    elif mainMenuInput == 3:
        pass
    else:
        pass

    #Check to make certain the ticker symbol exists

    #get_all_stock_symbols('test')

    #If the ticker symbol is valid or blank
    if ticker_symbol:
        #dailyPriceIncreaseDecrease(ticker_symbol, 5)

        #Testing
        #yFinance_test(ticker_symbol)

        mos(ticker_symbol)
    else:
        yFinance_test('CM.TO')

    val: tuple[int, int] = mos('CM.TO)')

    #End program with error code zero
    return 0

if __name__ == '__main__':
    sys.exit(main())