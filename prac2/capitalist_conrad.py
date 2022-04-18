"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random
from typing import TextIO

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = random.randint(1, 100)
DATE = 0

out_file = open('capitalist_conrad.txt', 'w')
price = INITIAL_PRICE
date = DATE
print("Starting price: ${:,.2f}".format(price), file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    date += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On Day {}, price is ${:,.2f}".format(date, price), file=out_file)


else:
    out_file.close()
