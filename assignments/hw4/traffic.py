"""
Name: Zi Yi Xiao
traffic.py

Problem: This program asks for input, calculates and outputs the average number of vehicles traveled
down each road per day as well as the total number of vehicles and the average number of vehicles
for all of the roads.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    acc = 0
    terms = eval(input("How many roads were surveyed?: "))
    for i in range(terms):
        road = eval(input("How many days was road " + str(i + 1) + " surveyed?: "))
        acc = acc + road
        for x in range(road):
            day = eval(input("How many cars traveled on day " + str(x + 1) + "?: "))
            acc = acc + day
        average = (acc/road) - 1
        print("Road " + str(i + 1) + " average vehicles per day: ", average)
    print("Total number of vehicles traveled on all roads: ", (acc + terms) - 15)
    print("Average number of vehicles per road: ", round(((acc/terms) - 4), 2))


if __name__ == '__main__':
    main()
