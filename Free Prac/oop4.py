#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 11:14:27 2018

@author: student
"""
import random
class Employee:
    def __init__(self, name, location='Mumbai'):
        self.emp_id = random.randint(100, 1000)
        self.name = name
        self.location = location
    
    def set_designation(self, d):
        self.designation = d
        
if __name__ == '__main__':
    emp1 = Employee('Aakash', 'Pune')
    emp1.set_designation('Manager')
    print(emp1.designation)
    
    print(emp1.location)

    emp2 = Employee('Suraj')
    print(emp2.location)
