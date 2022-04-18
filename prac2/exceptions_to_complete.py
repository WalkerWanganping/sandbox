"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        print("Valid result is:", result)
        # put the print here to make the code could ask for integer without termination
    except ValueError:  # when input is not an integer, the code below except will run
        print("Please enter a valid integer.")
