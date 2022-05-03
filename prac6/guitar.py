"""
CP1404 Prac_6
Name:Wang Anping
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """make a class of code for texting guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize guitars."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the information of a guitar."""
        return "{}, {}year, ${:2f}".format(self.name, self.year, self.cost)

    def __lt__(self, other):
        """Help list guitar by year"""
        return self.year < other.year

    def is_vintage(self):
        """Determine if the guitar is greater than 50 years."""
        return self.get_age() >= VINTAGE_AGE

    def get_age(self):
        """Get the guitar age."""
        return CURRENT_YEAR - self.year