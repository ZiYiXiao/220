"""
Name: Zi Yi Xiao
vigenere.py

Problem: This program implements the Vigenere cipher.

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet (geeksforgeeks.org)
to implement the Vigenere cipher.
"""

from graphics import GraphWin, Point, Text, Rectangle, Entry


def main():
    win_width = 400
    win_height = 400
    win = GraphWin("Vigenere", win_width, win_height)
    win.setBackground("white")

    message_pt = Point(win_width / 2 - 60, win_height / 2 - 100)
    message = Text(message_pt, "Message to code: ")
    message.setTextColor("black")

    keyword_pt = message_pt.clone()
    keyword_pt.move(0, 30)
    keyword = Text(keyword_pt, "Enter Keyword: ")
    keyword.setTextColor("black")

    message.draw(win)
    keyword.draw(win)

    message_box = Entry(Point(270, 100), 20)
    keyword_box = message_box.clone()
    keyword_box.move(0, 30)
    message_box.draw(win)
    keyword_box.draw(win)

    num_clicks = 1

    inst_pt = Point(200, 266)
    instructions = Text(inst_pt, "Encode")
    instructions.draw(win)

    for i in range(num_clicks):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX() - 0.001, p.getY() - 0.001),
                          Point(p.getX() + 0.001, p.getY() + 0.001))
        shape.undraw()
        shape.draw(win)

        def cipher_text(message, key):
            cipher_texts = []
            for i in range(len(message)):
                x = (ord(message[i]) + ord(key[i])) % 26
                x += ord('A')
                cipher_texts.append(chr(x))
            return ("".join(cipher_texts))

        def generate_key(message, key):
            for i in range(len(message) - len(key)):
                key.append(key[i % len(key)])
            return ("".join(key))

        if __name__ == "__main__":
            message = str(message)
            keyword = str(keyword)
            key = generate_key(message, keyword)
            cipher_texts = cipher_text(message, key)
            instructions.setText(cipher_texts)

    inst_pt = Point(200, 256)
    instructions = Text(inst_pt, "Resulting Message:\n")
    instructions.draw(win)
    inst_pt = Point(200, 376)
    instructions = Text(inst_pt, "Click Anywhere to Close Window")
    instructions.draw(win)

    win.getMouse()
    win.close()


main()
