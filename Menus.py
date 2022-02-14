# All menus will be placed in this module

from Stratagies import *

# Main Menu
def main_menu():
    # Set up text menu here
    print('\nMAIN MENU\n\n')
    print('1 - Price Chart\n')
    print('2 - Moving Average\n')
    print('3 - MOS\n')
    print('4 - What if?\n')
    print('5 - Quit\n')
    # Get input from the user
    mainmenuinput: int = input('Menu Option: ')

    return int(mainmenuinput)

def process_menu_choice(menuchoice:int):

    print(menuchoice)

    # Display a price chart for a stock ticker symbol
    if menuchoice == 1:
        # Get input from the user
        tickersymbol = input('Please enter a stock symbol: ')

        price_chart(tickersymbol)
