"""
Name: Zi Yi Xiao
lab4.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can add a square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to add a square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to add squares
    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 10, p.getY() - 10), Point(p.getX() + 10, p.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    win = GraphWin("Rectangle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    r = Rectangle(p1, p2)
    r.draw(win)
    length = abs(p1.getX() - p2.getX())
    width = abs(p1.getY() - p2.getY())
    area = length * width
    perimeter = 2 * (length + width)
    inst_pt = Point(400 / 2, 400 - 10)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)
    inst_pt = Point(400 / 2, 400 - 30)
    instructions = Text(inst_pt, "The perimeter is: " + str(perimeter))
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 400, 400)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r = (x2 - x1) ** 2 + (y2 - y1) ** 2
    r = math.sqrt(r)
    c = Circle(p1, r)
    c.draw(win)
    circumference = 2 * math.pi * r
    inst_pt = Point(400 / 2, 400 - 10)
    instructions = Text(inst_pt, "The radius is: " + str(r))
    instructions.draw(win)
    inst_pt = Point(400 / 2, 400 - 30)
    instructions = Text(inst_pt, "The circumference is: " + str(circumference))
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        num = 4
        denominator = 1 + 2 * i
        fraction = (num / denominator) * ((-1) ** i)
        acc = acc + fraction
    print(math.pi - acc)


def main():
    squares()
    # rectangle()
    # circle()
    # pi2()


main()
