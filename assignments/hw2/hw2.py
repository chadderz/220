"""
Name: <Margaux Walz>
<hw2>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper = eval(input("What is the upper bound?"))
    upper1 = upper + 1
    x = range(3, upper1, 3)
    list1 = list(x)
    sum1 = sum(list1)
    print("Sum of threes is", sum1)


def multiplication_table():
    for row in range(1, 11):
        for column in range(1, 11):
            multiple = row * column
            print(multiple, end="\t")
        print()


def triangle_area():
    a_int = eval(input("enter side a length:"))
    b_int = eval(input("enter side b length:"))
    c_int = eval(input("enter side c length:"))
    perim = (a_int + b_int + c_int)
    half_perim = perim / 2
    area = math.sqrt(half_perim * (half_perim - a_int) * (half_perim - b_int) * (half_perim - c_int))
    print("area is:", area)


def sum_squares():
    low_range = eval(input("Enter lower range:"))
    up_range = eval(input("Enter upper range:"))
    low_rang_sq = low_range * low_range
    limit = up_range + 1
    x_sqrt = range(low_range, limit)
    sum_1 = sum(x_sqrt)
    print(sum_1)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    for equation in range(1, exponent):
        squared = base * base
        print(squared)



if __name__ == '__main__':
    pass
