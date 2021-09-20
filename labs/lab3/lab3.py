"""
Name: Zi Yi Xiao
lab3.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    acc = 0
    num = eval(input("Enter the number of grades: "))
    for i in range(num):
        hw = eval(input("Enter your grade on HW " + str(i + 1)))
        acc = acc + hw
    print("Your average grade is: ", acc/num)


def tip_jar():
    acc = 0
    for i in range(5):
        donate = eval(input("Donate Amount " + str(i + 1)))
        acc = acc + donate
    print("Total Amount: ", acc)


def newton():
    x = eval(input("What is x: "))
    refine = eval(input("Enter how many times to improve the approximation: "))
    approx = x / 2
    for i in refine():
    print(approx = (approx + (x / approx)) / 2)


def sequence():
    y = 1 + (i // 2 * 2)
    end = eval(input("End: "))
    for i in range(1, end+1)
    print(1 + (i // 2 * 2))


def pi():
    terms = eval(input("The number of terms in the series: "))
    fraction = (pi / 2) = (2 / 1) * (2 / 3) * (4 / 3) * (4 / 5) * (6 / 5) * (6 / 7) * (8 / 7)
    acc = 1
    for i in range(terms):
        num = 2 + (i // 2 * 2)
        denom = 1 + ((i + 1) // 2 * 2)
        acc * fraction
    print(acc * 2)
