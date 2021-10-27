"""
Name: Zi Yi Xiao
lab9.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Circle, Point, Text
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList():
    acc = 0
    list1 = [1, 2, 3, 4]
    for i in range(0, len(list1)):
        acc = acc + list1[i]
    print(acc)


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = str(float(strList[i]))


def writeSumOfSquares(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        squareEach()
        sumList()
        toNumbers()
        outfile.write("Sum of squares = " + str(sum) + "\n")


def starter():
    weight = eval(input("Enter the weight: "))
    numWins = eval(input("Enter the number of wins: "))
    if 150 <= weight < 160:
        print("You should start.")
    if numWins >= 5:
        print("You should start.")
    else:
        print("You should not start.")
    if weight > 199:
        print("You should start.")
    if numWins > 20:
        print("You should start.")


def leapYear():
    year = eval(input("Enter the year: "))
    if year % 400 == 0:
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circleOverlap():
    win = GraphWin("Circle Overlap", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    r1 = math.sqrt(r1)
    c1 = Circle(p1, r1)
    c1.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    x3 = p3.getX()
    x4 = p4.getX()
    y3 = p3.getY()
    y4 = p4.getY()
    r2 = (x4 - x3) ** 2 + (y4 - y3) ** 2
    r2 = math.sqrt(r2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    dist = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    if dist < r1 + r2:
        inst_pt = Point(400 / 2, 400 - 10)
        instructions = Text(inst_pt, "The circles overlap.")
        instructions.draw(win)
    else:
        inst_pt = Point(400 / 2, 400 - 10)
        instructions = Text(inst_pt, "The circles do not overlap.")
        instructions.draw(win)

    win.getMouse()
    win.close()


def main():
    nums = [5, 2, -3]
    addTen(nums)
    print(nums)
    # nums = [3, 5.7, 2]
    # squareEach(nums)
    # print(nums)
    # sumList()
    # strList = ["3", "5.7", "2"]
    # toNumbers(strList)
    # print(strList)
    # writeSumOfSquares("input.txt", "output.txt")
    # starter()
    # leapYear()
    # circleOverlap()


main()
