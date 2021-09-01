"""
Name: Zi Yi Xiao
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = 20
    width = 5
    area = length * width
    print("Area =", area)


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def shooting_percentage():
    big = eval(input("Enter total shots: "))
    small = eval(input("Enter shots made: "))
    percentage = small/big * 100
    print("Shooting Percentage =", percentage)


def coffee():
    x = eval(input("Enter pounds: "))
    z = eval(input("Enter pounds: "))
    y = (10.50 * x) + (0.86 * z) + 1.50
    print("Total cost =", y)


def kilometers_to_miles():
    made = eval(input("Enter made: "))
    took = eval(input("Enter took: "))
    percentage = made/took * 100
    kilometers = eval(input("Enter kilometers: "))
    mile = kilometers/1.61
    print("Number of Miles =", mile)