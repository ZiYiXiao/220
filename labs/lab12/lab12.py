"""
Name: Zi Yi Xiao
lab12.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Zi Yi"
    except:
        pass


def read_data(filename):
    infile = open(filename, "r")
    line = infile.readline()
    lst = line.split(" ")
    return lst


def is_in_linear(value, lst):
    i = 0
    while i < len(lst):
        if i in value:
            i += 1
    if i == len(value):
        return True
    else:
        return False


def good_input():
    x = eval(input("Enter a number from 1 to 10: "))
    if x <= 10 and x >= 1:
        print(x)
    while x > 10 or x < 1:
        x = eval(input("Number must be between 1 and 10. Enter another number: "))
        if x <= 10 and x >= 1:
            print(x)
    return x


def num_digits():
    x = eval(input("Enter a positive integer: "))
    while x > 0:
        i = 0
        while x > 0:
            i += 1
            x //= 10
            print(x)
            x = eval(input("Enter a positive integer: "))


def hi_lo_game():
    number = randint(1, 100)
    guesses = 0
    x = eval(input("Guess a number: "))
    while x != number and guesses < 7:
        if x > number:
            print("Your guess is higher than the number.")
        elif number > x:
            print("Your guess is lower than the number.")
        guesses += 1
        x = eval(input("Guess a number: "))
    if x == number:
        print("You win in", guesses, "guesses!")
    else:
        print("Sorry, you lose. The number was", number)


def main():
    find_and_remove_first(["1", "2", "3", "4", "5"], "5")
    # read_data("dataSorted.txt")
    # is_in_linear("5", ["1", "2", "3", "4", "5"])
    # good_input()
    # num_digits()
    # hi_lo_game()


main()
