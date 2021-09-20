"""
Name: Zi Yi Xiao
interest.py

Problem: This program computes the monthly interest charge on a credit card account.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    print("This program computes the monthly interest charge on a credit card account.")
    annual = eval(input("Input the annual interest rate: "))
    billing = eval(input("Input the number of days in the billing cycle: "))
    balance = eval(input("Input the net balance shown on the statement: "))
    payment = eval(input("Input the net payment received: "))
    day = eval(input("Input the day of the billing cycle in which the payment was made: "))
    end = billing - day
    calculation1 = balance * billing
    calculation2 = payment * end
    calculation3 = calculation1 - calculation2
    average = calculation3 / billing
    monthly = annual / 12
    interest = average * monthly
    print("The monthly interest charge is: ", interest)

if __name__ == "__main__":
    main()
