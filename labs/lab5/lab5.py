"""
Name: Zi Yi Xiao
lab5.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    tri = Polygon(p1, p2, p3)
    tri.draw(win)
    side1 = abs(p1.getX() - p2.getX())
    side2 = abs(p2.getX() - p3.getX())
    side3 = abs(p1.getX() - p3.getX())
    perimeter = side1 + side2 + side3
    area = (side1 * side2 * side3) / 2
    inst_pt = Point(500 / 2, 500 - 10)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)
    inst_pt = Point(500 / 2, 500 - 30)
    instructions = Text(inst_pt, "The perimeter is: " + str(perimeter))
    instructions.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(200, 240), 5)
    green_box = red_box.clone()
    green_box.move(0, 30)
    blue_box = red_box.clone()
    blue_box.move(0, 60)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)
    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    s = eval(input("Input a string: "))  # Input a string: 'Hello world'
    print(s[0])
    print(s[len(s) - 1])
    print(s[2:6])
    print(s[::len(s) - 1])
    print(s[0:3] * 10)
    for i in range(len(s)):
        print(s[i])
    print(len(s))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    print("x =", values[1] + values[3])
    print("x =", values[0] + values[2])
    print("x =", values[1] * 5)
    print("x =", values[2:5])
    print("x =", values[2], ",", values[3], ",", values[0])
    print("x =", values[2], ",", values[0], ",", values[5])
    print("x =", values[0] + values[2] + float("7.2"))
    print("x =", str(len(values)))


def another_series():
    acc = 0
    series = eval(input("Input number of terms: "))  # Input number of terms: 10
    for i in range(series):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc = acc + y
    print("\nSum = " + str(acc))


def main():
    triangle()
    # color_shape()
    # process_string()
    # process_list()
    # another_series()


main()