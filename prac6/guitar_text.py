"""
CP1404 Prac_6
Name:Wang Anping
"""

from prac6.guitar import Guitar

CURRENT_YEAR = 2022


def run_tests():
    """Tests for Guitar class."""

    name = "Gibson L-5 CES"
    year = 1922
    cost = 11451.4
    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 810)


    print(f"{guitar.name} get_age() - Expected {100}. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {9}. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected {False}. Got {other.is_vintage()}")

run_tests()