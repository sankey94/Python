#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:54:44 2018

@author: student
"""
import random
from math import pi
class Circle:
    def __init__(self,color='Blue'):
        self.color = color
        self.radius=random.randint(2,8)
    def calc_area(self):
        return pi*self.radius**2
    def cal_circumference(self):
        return 2*pi*self.radius
    #class attributes

circumferences=[]
for i in range(10):

    circle=Circle('Red')
    circle.radius=random.uniform(1.1,5.1)
    circumferences.append(circle.cal_circumference())
print(circumferences)


new_circle=Circle('Red')
circumferences.append(circle.cal_circumference())
print(new_circle.color,new_circle.cal_circumference())
    
#
#
#import random
#class Employee:
#    def __init__(self,name,location='Mumbai'):
#        self.emp_id=random.randint(100,1000)
#        self.name=name
#        self.location=location
#    def set_designation(self,d):
#        self.designation=d
#        
#if __name__=='__main__':
#    emp1=Employee('Aakash')
#    emp1.set_designation('manager')
#    print(emp1.designation)
#    
#    emp2=Employee('suraj')
#    print(emp2.location)
#    