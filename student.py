

class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return f"First name:{self.first_name}, Last name:{self.last_name}, ID:{self.id}"


    def __repr__(self):
        return f"<<{self.__str__()}>>"

if __name__ == "__main__"



# Simple example class usage (client code)
# first_name = input("First name: ")
# last_name = input("Last name: ")
# student_id = int(input("ID: "))
# s1 = Student(first_name, last_name, student_id)
# print(s1.first_name, "has ID", s1.id)


# Code Listing 11.7
# import math  # needed for sqrt (square root)
#
#
# class Point:
#
#
# """A Cartesian point (x, y) - all values are floats unless otherwise stated."""
#
#
# def __init__(self, x=0.0, y=0.0):
#
#
# """Initialise a point with x and y coordinates."""
#
# self.x = x
#
# self.y = y
#
#
# def distance(self, other):
#
#
# """Get the distance between self and another Point."""
#
# x_diff = self.x - other.x  # (x1 — x2)
#
# y_diff = self.y - other.y  # (y1 — y2)
#
# return math.sqrt(x_diff ** 2 + y_diff ** 2)
#
#
# def sum(self, other):
#
#
# """Get the vector sum of self and another Point, return a Point instance."""
#
# return Point(self.x + other.x, self.y + other.y)
#
#
# def __str__(self):