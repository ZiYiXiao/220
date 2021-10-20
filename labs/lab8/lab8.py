"""
Name: Zi Yi Xiao
lab8.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    i = 1
    for line in infile:
        new_line = line.split()
        for word in new_line:
            outfile.write(str(i) + " " + word + "\n")
            i += 1


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for line in infile:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write("".join(new_line) + "\n")


def calc_check_sum(isbn):
    acc = 0
    isbn = str(isbn)
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10 - i)
        acc = acc + num
    return acc % 11


def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        outfile.write(line + "\n")


def encode(message, key):
    acc = ""
    for c in message:
        ci = ord(c) - ord("a")
        ni = ci + key
        nu = ni + ord("a")
        nc = chr(nu)
        acc = acc + nc
    return acc


def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line + "\n")


def encode_better(string, key):
    def generate_key(string, key):
        acc = ""
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
        return (acc.join(key))

    def cipher_text(string, key):
        acc = ""
        cipher_texts = []
        for i in range(len(string)):
            x = (ord(string[i]) + ord(key[i])) % 97
            x += ord('a')
            cipher_texts.append(chr(x))
        return (acc.join(cipher_texts))

    if __name__ == "__main__":
        string = open(string, "r")
        keyword = open(key, "w")
        key = generate_key(string, keyword)
        cipher_texts = cipher_text(string, key)
        return cipher_texts


def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        new_line = encode_better(line, pad)
        outfile.write(new_line + "\n")


def main():
    # number_words("walrus.txt", "new_walrus.txt")
    # hourly_wages("hourly_wages.txt", "new_hourly_wages.txt")
    # calc_check_sum()
    # send_message("file.txt", "bob")
    # send_safe_message("file.txt", "bob", 5)
    send_uncrackable_message("file.txt", "bob", "pad.txt")


main()
