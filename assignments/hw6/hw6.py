"""
Name: Margaux Walz
hw6.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def cash_converter():
    int1 = eval(input("enter an integer: "))
    print("That is ${:,.2f}".format(int1))


def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    encrypt = ""
    for char in message:
        num = ord(char) + key
        encrypt += chr(num % 128)
    return encrypt


def sphere_area(radius):
    area = 4 * math.pi * radius ** 2
    print(area)


def sphere_volume(radius):
    volume = (4/3) * (math.pi * radius ** 3)
    print(volume)


def sum_n(number):
    sum1 = 0
    sum2 = 0
    for val in range(1, number+1):
        sum2 = sum1 + val
    print(sum2)


def sum_n_cubes(number):
    sum1 = 0
    for i in range(1, number+1):
        sum1 += i ** 3
    return sum1


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
