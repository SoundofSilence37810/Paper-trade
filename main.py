# import statements
import sys
import datetime as dt

# import without dot notation
from typing import Tuple, Union, Any

from Stratagies import *
from Utilities import *
from Menus import *

import yfinance as yf

def main() -> int:

    # Local Variables
    running = 1
    # Application Info
    print(f'Paper Trades Application - For Educational Purposes Only')

    # Main program loop
    while running == 1:

        menuchoice: int = main_menu()

        process_menu_choice(menuchoice)

        if menuchoice == 5:
            running = 0

        # For now lets just break
        break

    return 0


if __name__ == '__main__':
    sys.exit(main())
