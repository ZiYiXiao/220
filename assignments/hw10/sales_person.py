"""
Name: Zi Yi Xiao
sales_person.py

Problem: This program encapsulates data for a sales person.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []
    def get_employee_id(self):
        return self.employee_id
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def enter_sale(self, sale):
        self.sales = sale.append
    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc = acc + sale.get_sales
        return acc
    def get_sales(self):
        return self.sales
    def met_quota(self, quota):
        if self.sales >= quota:
            return True
        else:
            return False
    def compare_to(self, other):
        self.sales = self.sales + [other]
        if other > self.sales:
            return - 1
        elif other < self.sales:
            return 1
        else:
            return 0
    def __str__(self):
        return "{self.employee_id}-{self.name}:{total_sales(self)}"
