"""
Name: <Margaux Walz>
<lab1>.py

Problem: <This program finds the monthly interest rate given user inputted information>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_interest_rate():
    interest_rate = eval(input('What percent is your annual interest rate?'))
    num_days = eval(input('How many days are in your billing cycle?'))
    previous_bal = eval(input('What is your previous balance?'))
    payment_amt = eval(input('How much are you paying?'))
    day_cycle = eval(input('What day is it in the billing cycle?'))
    step_1 = previous_bal * num_days
    step_2 = payment_amt * (num_days - day_cycle)
    step_3 = step_1 - step_2
    avg_daily_balance = step_3 - num_days
    interest_rate_decimal = interest_rate / 100
    monthly_interest = avg_daily_balance * (interest_rate_decimal / 12)
    monthly_interest_rounded = round(monthly_interest,2)
    print('Your monthly interest is $', monthly_interest_rounded, '!')
