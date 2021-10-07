"""
Name: Zi Yi Xiao
lab6.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    print(last + ', ' + first)


def company_name():
    internet_domain_name = input("Enter internet domain name: ")
    domains = internet_domain_name.split(".")
    print(domains[1])


def initials():
    name = eval(input("How many names to input?: "))
    for i in range(name):
        first = input("Enter the first name of student " + str(i + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        first_initial = first[0]
        last_initial = last[0]
        print(first + "'s initials are " + first_initial + last_initial)


def names():
    # Input this list of names: Randall Alexander, Tony Leclerc, RoxAnn Stalvey, Walter Blair
    list_names = input("Enter people's names, separated by commas: ")
    name = list_names.split(" ")
    print("The initials are", end=" ")
    for i in range(len(name)):
        initial = name[i]
        print(initial[0].upper(), end=" ")


def thirds():
    # Input the sentence: The quick brown fox jumps over the lazy dog
    sentences = eval(input("How many sentences to input?: "))
    for i in range(sentences):
        sentence = input("Enter sentence " + str(i + 1) + ": ")
        print(sentence[2::3])


def pig_latin():
    acc = 0
    # Input the sentence: The time has come
    sentence = input("Enter sentence: ")
    words = sentence.split(" ")
    for word in words:
        acc = acc + len(word)
        output = word[1:] + word[0] + "ay"
        print(output.lower(), end=" ")


def main():
    name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # pig_latin()


main()
