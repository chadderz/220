"""
Name: Margaux Walz
hw3.py

Problem: Solve math problems using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def average():
    num_grades = eval(input("How many grades will you enter? "))
    sum_grades = 0
    for i in range(num_grades):
        grade_num = float(input("Enter grade:"))
        sum_grades += grade_num
    average = sum_grades / num_grades
    print("Average is:", average)


average()


def tip_jar():
    tip_amt = 0
    sum_tip = 0
    for i in range(1, 6):
        tip_amt = float(input("how much would you like to donate? "))
        sum_tip += tip_amt
    print("total tips: ", sum_tip)


tip_jar()


def newton():
    sqr_num = eval(input("What number do you want to square root? "))
    appr_times = eval(input("How many times should we improve the approximation? "))
    approx = range(sqr_num, 10000, sqr_num)
    float(approx)
    for i in range(1, appr_times+1):
         approx - (approx + (sqr_num/approx)) / 2
    print(approx)


newton()

def sequence():
    num_terms = eval(input("How many terms would you like?"))
    num_limit = num_terms + 1
    for i in range(1, num_limit):
        print((i - 1) + (i % 2))


sequence()

def pi():
    number = eval(input("How many terms in the series? "))
    total = 1
    numer = 0
    denom = 0
    for i in range(number):
        num = i * (2.0 - (i % 2.0))
        denom = i * (1.0 + (i % 2.0))
    total *= numer/denom
    answer = total * 2
    print(answer)


pi()


if __name__ == '__main__':
    pass
