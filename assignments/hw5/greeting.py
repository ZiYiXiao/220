"""
Name: Zi Yi Xiao
greeting.py

Problem: This program displays an animated arrow shooting through a heart.

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet to display an animated arrow
shooting through a heart. I got help from the sites: pythonforfun.in, geeksforgeeks.org
"""

import turtle
win = turtle.Screen()
win.setup(width=400, height=400)
win.title("Valentine's Greeting Card")
win.tracer(0)
red = turtle.Turtle()
red.width(1)
red.ht()
black = turtle.Turtle()
black.speed(0)
black.width(1)
black.ht()
turtle.penup()
turtle.setposition(-80, -100)
turtle.pendown()
turtle.write("Happy Valentine's Day!", font=("Verdana", 15, "normal"))
turtle.penup()
turtle.setposition(-82, -140)
turtle.pendown()
turtle.write("(click the red x button to close)", font=("Verdana", 10, "normal"))
turtle.ht()


def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)


def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()


def arrow():
    black.fillcolor('black')
    black.begin_fill()
    for side in range(1):
        black.forward(75)
        black.left(90)
        black.forward(5)
        black.right(135)
        black.forward(7.5)
        black.right(90)
        black.forward(7.5)
        black.right(135)
        black.forward(5)
        black.left(90)
        black.forward(75)
        black.right(90)
        black.forward(0.6066)
        black.right(90)
        black.end_fill()


black.penup()
black.goto(-200, 100)
black.pendown()

heart()

while True:
    black.clear()
    arrow()
    win.update()
    black.forward(1)
