#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 12:22:33 2018

@author: student
"""
import random
class Employee:
    salary_hike = 1.08 # class attribute
    def __init__(self, n):
        self.name = n
        self.emp_id = int(input('Enter emp_id: '))
        self.salary = int(input('Enter salary: '))

    def apply_hike(self):
        self.salary = self.salary * Employee.salary_hike
'''
emp1 = Employee('Aakash')
emp2 = Employee('Mohan')
emp3 = Employee('Ajay')
emp4 = Employee('Jatin')
emp5 = Employee('Mohit')
print(emp1.salary)
emp1.apply_hike()
print(emp1.salary)
'''

names = ['Aakash', 'Mohit', 'Mohan', 'Ajay', 'John', 'Bob', 'Jatin']
employees = []
for i in range(2):
    name = random.choice(names)
    emp = Employee(name)
    employees.append(emp)

print(employees[0].salary)
employees[0].apply_hike()
print(employees[0].salary)

