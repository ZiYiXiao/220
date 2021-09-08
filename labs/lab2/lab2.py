"""
Name: Zi Yi Xiao
lab2.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def sum_of_threes():
    bound = eval(input("Total: "))
    acc = 0
    for i in range(0, bound+1, 3):
        acc = acc + i
    print(acc)


def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            h * l
        print()


def triangle_area():
    import math
    a = eval(input("Enter a: "))
    b = eval(input("Enter b: "))
    c = eval(input("Enter c: "))
    s = (a + b + c) / 2
    x = s * (s - a) * (s - b) * (s - c)
    A = math.sqrt(x)
    print(A)


def sumSquares():
    lower = eval(input("Enter lower base: "))
    middle = eval(input("Enter middle base: "))
    upper = eval(input("Enter upper base: "))
    exp = eval(input("Enter exp: "))
    answer = lower ** exp + middle ** exp + upper ** exp
    print(answer)


def power():
    base = eval(input("Enter base: "))
    exp = eval(input("Enter exp: "))
    answer = base ** exp
    print(base, "^", exp, "=", answer)