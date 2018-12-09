#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:39:18 2018

@author: student
"""

from math import pi

def calc_area(radius):
    return pi*radius**2
def cal_circumference(radius):
    return 2*pi*radius

circle1_name='c1'
circle1_radius=4.2

circle2_name='c2'
circle2_radius=3.9

circle3_name='c3'
circle3_radius=5.1

circle4_name='c4'
circle4_radius=5

circumferences=[]
for i in range(50):
    circumferences.append(cal_circumference(circle1_radius))


#circle2_circumference=calc-circumference(circle2_radius)
#print(circle2_circumference)
#print(circumferences)

'''better way'''

circumferences=[]
circles=[['c1',4.2],['c2',3.9],['c3',5.1]]    
for i in range(3):
    circumferences.append(cal_circumference(circles[i][1]))
print(circumferences)
'''using custom datatype'''
class Circle:
    pass
circle1= Circle()
circle2=Circle()
circle1.radius=4.2
circle1.name='c1'
print(cal_circumference(circle1.radius))    
