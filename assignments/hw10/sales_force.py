"""
Name: Zi Yi Xiao
sales_force.py

Problem: This program encapsulates data for a sales person.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []
    def add_data(self, file_name):
        infile = open(file_name, "r")
        print(self.sales_people + infile.read().split())
    def quota_report(self, quota):
        self.sales_people = []
        if self.sales_people >= quota:
            return True
        if self.sales_people < quota:
            return False
        return self.sales_people
    def top_seller(self):
        return max(self.sales_people)
    def individual_sales(self, employee_id):
        return employee_id(SalesPerson)
