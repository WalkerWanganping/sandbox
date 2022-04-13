"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def temp_change_cel(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))

def temp_change_fah(fahrenheit):
    celsius = (fahrenheit - 32) / 9.0 * 5
    print("Result: {:.2f} C".format(celsius))

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        temp_change_cel(celsius)
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        temp_change_fah(fahrenheit)
    else:
        print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
print("Thank you.")



