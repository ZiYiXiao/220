"""
Name: Zi Yi Xiao
lab10.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build():
    return list(range(1, 10))


def display(board):
    for i in range(3):
        n = i * 3
        print(board[n], board[n + 1], board[n + 2], sep="|")
        print(10 * "-")


def place(board, pos, piece):
    if piece == "X" or piece == "O":
        board[pos - 1] = piece


def legal(board, pos):
    if board[pos - 1] == pos:
        return True
    return False


def isWon(board, piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n + 1] != piece:
            continue
        if board[n + 2] != piece:
            continue
        return True
    for i in range(3):
        if board[i] != piece:
            continue
        if board[i + 3] != piece:
            continue
        if board[i + 6] != piece:
            continue
        return True
    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False


def over(board):
    if isWon(board, "X"):
        return True
    elif isWon(board, "O"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True


def play():
    board = build()
    while True:
        display(board)
        pos = eval(input("Enter position: "))
        if legal(board, pos):
            place(board, pos, "X")
            display(board)
        if over(board):
            if isWon(board, "X"):
                print("X Wins")
                break
            if isWon(board, "O"):
                print("O Wins")
                break
            print("Tie")
            break

        display(board)
        pos = eval(input("Enter position: "))
        if legal(board, pos):
            place(board, pos, "O")
            display(board)
        if over(board):
            if isWon(board, "X"):
                print("X Wins")
                break
            if isWon(board, "O"):
                print("O Wins")
                break
            print("Tie")
            break


def main():
    play()


main()
