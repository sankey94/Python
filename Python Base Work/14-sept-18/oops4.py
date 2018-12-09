#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:34:06 2018

@author: student
"""
import random
class Employee:
    def __init__(self,name,location='Mumbai'):
        self.emp_id=random.randint(100,1000)
        self.name=name
        self.location=location
    def set_designation(self,d):
        self.designation=d
        
if __name__=='__main__':
    emp1=Employee('Aakash')
    emp1.set_designation('manager')
    print(emp1.designation)
    
    emp2=Employee('suraj')
    print(emp2.location)
    
    
    