"""
Name: Zi Yi Xiao
three_door_game.py

Problem: This program writes a function for the game "Three Door Game".

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet (homeworklib.com)
to complete this program.
"""

import random
from graphics import GraphWin, Rectangle, Point, Text
from button import Button


def draw_button(button_text, point_one, point_two, win):
    outline = Rectangle(point_one, point_two)
    center = outline.getCenter()
    label = Text(center, button_text)
    outline.draw(win)
    label.draw(win)


def main():
    win = GraphWin("Three Doors Game", 400, 400)
    win.setCoords(0, 0, 10, 10)


    door1 = draw_button("Door 1", Point(1, 4), Point(3, 6), win)
    door2 = draw_button("Door 2", Point(4, 4), Point(6, 6), win)
    door3 = draw_button("Door 3", Point(7, 4), Point(9, 6), win)
    text1 = Text(Point(5, 8), "I have a secret door")
    text2 = Text(Point(5, 2), "Click to choose my secret door")
    text1.draw(win)
    text2.draw(win)
    pt = win.getMouse()
    while door1.is_clicked or door2.is_clicked(pt) or door3.is_clicked(pt):
        ans = random.randrange(1, 4)
        door1 = 1
        door2 = 2
        door3 = 3
        if door1 == ans and door1.is_clicked(pt) == True:
            door1.color_button("green")
            door1.set_label("green")
            text1 = Text(Point(5, 8), "You win!")
            text2 = Text(Point(5, 2), "Click to close")
            text1.draw(win)
            text2.draw(win)
        else:
            door1.color_button("red")
            door1.set_label("red")
            text1 = Text(Point(5, 8), "You lose!")
            text2 = Text(Point(5, 2), "{ans} is my secret door")
            text1.draw(win)
            text2.draw(win)
        if door2 == ans and door2.is_clicked(pt) == True:
            door2.color_button("green")
            door2.set_label("green")
            text1 = Text(Point(5, 8), "You win!")
            text2 = Text(Point(5, 2), "Click to close")
            text1.draw(win)
            text2.draw(win)
        else:
            door2.color_button("red")
            door2.set_label("red")
            text1 = Text(Point(5, 8), "You lose!")
            text2 = Text(Point(5, 2), "{ans} is my secret door")
            text1.draw(win)
            text2.draw(win)
        if door3 == ans and door3.is_clicked(pt) == True:
            door3.color_button("green")
            door3.set_label("green")
            text1 = Text(Point(5, 8), "You win!")
            text2 = Text(Point(5, 2), "Click to close")
            text1.draw(win)
            text2.draw(win)
        else:
            door3.color_button("red")
            door3.set_label("red")
            text1 = Text(Point(5, 8), "You lose!")
            text2 = Text(Point(5, 2), "{ans} is my secret door")
            text1.draw(win)
            text2.draw(win)
        pt = win.getMouse()

    draw_button.undraw()

    win.getMouse()
    win.close()
    return Button


if __name__ == '__main__':
    main()
