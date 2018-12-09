#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:34:10 2018

@author: student
"""
from math import pi

def calc_area(radius):
    return pi*radius**2
def calc_circumference(radius):
    return 2*pi*radius

circle1_name = 'C1'
circle1_radius = 4.2

circle2_name = 'C2'
circle2_radius = 3.9

circle3_name = 'C3'
circle3_radius = 5.1
circle4_name = 'C4'
circle4_radius = 5

circumferences = []
for i in range(50):
    circumferences.append(calc_circumference(circle1_radius))

#circle2_circumference = calc_circumference(circle2_radius)
#print(circle2_circumference)
#print(circumferences)


''' better way??? '''
circumferences = []
circles = [ ['C1', 4.2], ['C2', 3.9], ['C3', 5.1]]
for i in range(3):
    circumferences.append(calc_circumference(circles[i][1]))
print(circumferences)

''' using custom datatype '''
class Circle:
    pass

circle1 = Circle()
circle2 = Circle()
circle1.radius = 4.2
circle1.name = 'C1'

print(calc_circumference(circle1.radius))

