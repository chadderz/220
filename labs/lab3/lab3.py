"""
Name: <Margaux Walz>
<lab3>lab.py

Problem: <This program uses nested loops to determine the averages of traffic data>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def traffic():
    roads_surveyed = eval(input("How many roads were surveyed?"))
    surveyed_1 = roads_surveyed + 1
    for i in range(1, surveyed_1):
        print("How many days was road", i, end=" ")
        days_surveyed = eval(input("traveled?"))
        days_1 = days_surveyed + 1
        for days in range(1, days_1):
            print("How many cars traveled on day", days, end="?")
            cars_traveled = eval(input(" "))



