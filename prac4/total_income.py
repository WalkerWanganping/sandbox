"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_forms(incomes, month_numbers):
    """This function will print report based on incomes"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_numbers + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:5.2f} Total: ${:5.2f}".format(month, income, total))


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_numbers = int(input("How many months? "))

    for month in range(1, month_numbers + 1):
        income = int(input("Enter income for month {}:$".format(month)))
        incomes.append(income)

    print_forms(incomes, month_numbers)


main()
