"""
Name: Zi Yi Xiao
lab13.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Rectangle, Point
import time


def is_in_binary(search_val, values):
    mid = values[len(values) // 2]
    while mid and len(values) != 1:
        if mid > search_val:
            values = values[:(len(values) // 2)]
        else:
            values = values[(len(values) // 2)+1:]
    mid = values[len(values) // 2]
    if mid:
        return True
    else:
        return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if pos < lowest:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]


def rectangles(values):
    d = {}
    areas = []
    def get_area(rect):
        p1 = rect.getP1()
        p2 = rect.getP2()
        w = abs(p1.getX() - p2.getX())
        h = abs(p1.getY() - p2.getY())
        return w * h
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
    for i in range(len(areas)):
        values[i] = d[get_area(rect)]
    print(areas)


def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    def count_time(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))
    start = time.time()
    end = time.time()
    time_lapsed = end - start
    count_time(time_lapsed)
    i = 830
    j = 500
    if i > len(data):
        print("Alert!")
        return count_time(time_lapsed)
    elif j >= len(data):
        print("Warning!")
        return count_time(time_lapsed)
    else:
        pass


def main():
    # print(is_in_binary(3, [1, 2, 3]))
    # x = [3, 4, 1, 6]
    # selection_sort(x)
    # print(x)
    # x = [Rectangle(Point(0, 0), Point(20, 20))]
    # rectangles(x)
    # print(x)
    trade_alert("trades.txt")


main()
