"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    else:
        pass

    fraction = numerator / denominator
    print(fraction)
except ValueError:  # ValueError occurs here while any input is not a number
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # ZeroDivisionError occurs when input of denominator is 0
    print("Cannot divide by zero!")
print("Finished.")