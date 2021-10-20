"""
Name: Zi Yi Xiao
lab7.py

Problem: This program writes various functions.

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet (geeksforgeeks.org)
to write the function 'encode_better()'.
"""


def cash_conversion():
    x = eval(input("Enter an integer: "))
    print("${:.2f}".format(x))


def encode():
    st = input("Enter the message to be encoded: ")
    key = eval(input("Enter integer key value: "))
    acc = ""
    for c in st:
        ci = ord(c) - ord("a")
        ni = ci + key
        nu = ni + ord("a")
        nc = chr(nu)
        acc = acc + nc
    print(acc)


def sphere_area():
    def sphere_volume(radius):
        return radius
    return sphere_volume


def sum_n():
    natural_numbers = [1, 2, 3, 4]
    for i in natural_numbers:
        return i + 1


def sum_n_cubes():
    natural_numbers = [1, 2, 3, 4]
    for i in natural_numbers:
        return i ** 3


def encode_better():
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
        string = input("Enter the message to be encoded: ")
        keyword = input("Enter the key: ")
        key = generate_key(string, keyword)
        cipher_texts = cipher_text(string, key)
        print(cipher_texts)


def main():
    cash_conversion()
    # encode()
    # sphere_area()
    # sum_n()
    # sum_n_cubes()
    # encode_better()


main()
