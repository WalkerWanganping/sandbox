"""
CP1404 Prac_6
Name:Wang Anping
"""
from prac6.car import Car

MENU = """Menu: 
d) Drive 
r) Refuel 
q) Quit"""

def main():
    """Demo test code to show how to use car class."""
    name = input("Please enter your name")
    new_car = Car(name, 100)
    print(new_car,"\n", MENU)

    choice = input("Please enter your choice").lower()
    while choice != "q":
        if choice == "d":
            distance = int(input("Please enter how many kilometer do you want to drive"))
            while distance <= 0:
                print("distance must be over zero!")
                distance = int(input("Please enter how many kilometer do you want to drive"))
            remain_distance = new_car.drive(distance)
            print("car will drive {}km".format(remain_distance), end=" ")
            print("")
            if new_car.fuel == 0:
                print("but no foul left", end=" ")
        elif choice == "r":
            new_add_fuel = int(input("How many fuel do you want to add?"))
            while new_add_fuel < 0:
                print("new add fuel must be over zero!")
                new_add_fuel = int(input("How many fuel do you want to add?"))
            new_car.add_fuel(new_add_fuel)
            print("{} units of fuel is added!".format(new_add_fuel))
        else:
            print("Invalid choice!")
        print(new_car)
        print(MENU)
        choice = input("Please enter your choice").lower()
    print(f"SEE U {new_car.name}!")


main()