# noinspection SpellCheckingInspection
"""
Name: <Margaux Walz>
<hw1>.py

Problem: <This program solves different math problems using python>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length*width*height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter the players total shots: "))
    made = eval(input("Enter how many shots the player made: "))
    percentage = made/total*100.0
    print("Shooting Percentage =", percentage)


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    price = pounds*10.50*0.86+1.50
    print("Your total is:", price)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel? "))
    miles = kilometers/1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    pass
