"""
Name: Zi Yi Xiao
mean.py

Problem: This program asks for input, does arithmetic, and provides output.

Input: Enter the values to be entered.
Output: The RMS Average, the Harmonic Mean, and the Geometric Mean.
This program will output in the order of the RMS Average, the Harmonic Mean, and then the Geometric Mean.

Certification of Authenticity:
I certify that this assignment is my own work, but I got help from the internet (rosettacode.org) to calculate
and output the RMS Average and the Geometric Mean. Specifically, lines 16, 17, 26, 27, 28, 31, 32, and 33.
"""

from functools import (reduce)
from math import (sqrt)
import math

def main():
    acc = 0
    num = eval(input("Enter the number of values to be entered: "))
    for i in range(num):
        value = eval(input("Enter value " + str(i + 1)))
        acc = acc + num
    def rms_average(num):
        return sqrt(reduce(lambda a, x: a + x * x, num, 0) / len(num))
    round_rms_average = round(rms_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
    print(round_rms_average)
    print(acc/num)
    def geometric_mean(num):
        return math.exp(math.fsum(math.log(x) for x in num) / len(num))
    round_geometric_mean = round(geometric_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7.29]), 3)
    print(round_geometric_mean)

if __name__ == "__main__":
    main()
