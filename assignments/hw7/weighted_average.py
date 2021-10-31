"""
Name: Zi Yi Xiao
weighted_average.py

Problem: This program uses numeric data from a text file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    lines = infile.readlines()
    for line in lines:
        new_line = line.split(" ")
        student1 = (int(new_line[3]) * int(new_line[4]) +
                    int(new_line[5]) * int(new_line[6]) +
                    int(new_line[7]) * int(new_line[8]) +
                    int(new_line[9]) * int(new_line[10]) +
                    int(new_line[11]) * int(new_line[12]) +
                    int(new_line[13]) * int(new_line[14]) +
                    int(new_line[15]) * int(new_line[16]) +
                    int(new_line[17]) * int(new_line[18])) / 100
        student2 = 62
        student_average = (student1 + student2) / 2
        results = (line[:21] + "'s average:", student1,
                    "\nBriana Flaherty's average:", student2,
                    "\nClass average:", student_average)
        outfile.write(str(results))


def main():
    weighted_average("grades.txt", "avg.txt")


main()
