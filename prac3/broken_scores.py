"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def score_check(score):
    score = float(input("Enter score: "))
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif 100 >= score > 90:
            return "Excellent"
        elif 90 >= score > 50:
            return "Passable"
        else:
            return "Bad"

user_score = random.randint(1,100)
print(score_check(user_score))
