"""
CP1404 Prac_6
Name:Wang Anping
"""

from prac6.guitar import Guitar

def main():
    guitar_list = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        guitar_to_add = Guitar(guitar_name, guitar_year, guitar_cost)
        guitar_list.append(guitar_to_add)
        print(guitar_to_add, "added.")
        guitar_name = input("Name: ")
    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitar_list:
        guitar_list.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitar_list):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i + 1, guitar, vintage_string))
    else:
        print("BYE")

main()