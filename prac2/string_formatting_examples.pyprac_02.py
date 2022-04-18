"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# TODO: Use string formatting (.format() or f-strings) to produce the output:
# 1922 Gibson L-5 CES for about $16,035!

import math
print("{} {} for about ${}!".format(year,name,math.ceil(cost)))


# TODO: Using a for loop with the range function and string formatting,
# produce the following right-aligned output (DO NOT use a list):
#   0
#  50
# 100
# 150


numbers = [0, 50, 100, 150]


for i, number in enumerate(numbers, 1):
    print(f"{number:>3}")
