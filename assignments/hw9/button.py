"""
Name: Zi Yi Xiao
button.py

Problem: This program encapsulates data for a button shown in GUI.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Rectangle, Point, Text


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.text = ""
    def get_shape(self):
        return self.shape
    def get_label(self):
        return self.label
    def get_text(self):
        return self.text
    def set_text(self, label):
        self.text = label
    def draw_button(button_text, point_one, point_two):
        win = GraphWin("Three Doors Game", 400, 400)
        outline = Rectangle(point_one, point_two)
        center = outline.getCenter()
        label = Text(center, button_text)
        outline.draw(win)
        label.draw(win)
    def draw(self, draw_button, button_text, point_one, point_two):
        win = GraphWin("Three Doors Game", 400, 400)
        draw_button(button_text, point_one, point_two, win)
        draw_button.draw(win)
    def undraw(self, draw_button, button_text, point_one, point_two):
        win = GraphWin("Three Doors Game", 400, 400)
        draw_button(button_text, point_one, point_two, win)
        draw_button.undraw()
    def is_clicked(self, point, draw_button, door1, door2, door3):
        win = GraphWin("Three Doors Game", 400, 400)
        door1.is_clicked = draw_button("Door 1", Point(1, 4), Point(3, 6), win)
        door2.is_clicked = draw_button(Point(4, 4), Point(6, 6))
        door3.is_clicked = draw_button(Point(7, 4), Point(9, 6))
        if point == door1.is_clicked or door2.is_clicked or door3.is_clicked:
            return True
        else:
            return False
    def color_button(self, color, draw_button, button_text, point_one, point_two):
        win = GraphWin("Three Doors Game", 400, 400)
        draw_button(button_text, point_one, point_two, win)
        pt = win.getMouse()
        if draw_button.is_clicked(pt):
            draw_button.color_button(color)
            draw_button.set_label(color)
        else:
            draw_button.color_button(color)
            draw_button.set_label(color)
    def set_label(self, label):
        self.text.update = label
