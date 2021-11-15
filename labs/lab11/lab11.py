"""
Name: Zi Yi Xiao
lab11.py

Problem: This program writes a function for Hangman.

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet
(github.com/jasmin-30/Hangman) to complete this program.
"""

import random

wordlist_filename = "words.txt"


def load_words():
    infile = open(wordlist_filename, "r")
    line = infile.readline()
    wordlist = line.split()
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    c = 0
    for i in letters_guessed:
        if i in secret_word:
            c += 1
    if c == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    s = []
    for i in secret_word:
        if i in letters_guessed:
            s.append(i)
    ans = ""
    for i in secret_word:
        if i in s:
            ans += i
        else:
            ans += "_ "
    return ans


def get_available_letters(letters_guessed):
    import string
    ans = list(string.ascii_lowercase)
    for i in letters_guessed:
        ans.remove(i)
    return "".join(ans)


def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    global letters_guessed
    mistake_made = 0
    letters_guessed = []

    while 8 - mistake_made > 0:
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            break
        else:
            print("You have", 8 - mistake_made, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            guess = str(input("Please guess a letter: ")).lower()
            if guess in letters_guessed:
                print("You have already guessed that letter:", get_guessed_word(secret_word, letters_guessed))
            elif guess in secret_word and guess not in letters_guessed:
                letters_guessed.append(guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(guess)
                mistake_made += 1
                print("That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
        if 8 - mistake_made == 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
        else:
            continue


secret_word = choose_word(wordlist).lower()
hangman(secret_word)
