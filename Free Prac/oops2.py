#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 09:54:18 2018

@author: student
"""
'''
import random
from math import pi

class Circle:
    def __init__(self):
        self.radius = random.uniform(2,8)
    def calc_circumference(self):
        return 2*pi*self.radius
    def calc_area(self):
        return pi*self.radius**2

circumferences = []
for i in range(10):
    circle = Circle()
    circumferences.append(circle.calc_circumference())

print(circumferences)
'''

import random
from math import pi

class Circle:
    def __init__(self, color='Blue'):
        self.color = color
        self.radius = random.uniform(2,8)
    def calc_circumference(self):
        return 2*pi*self.radius
    def calc_area(self):
        return pi*self.radius**2

circumferences = []
for i in range(1000):
    circle = Circle('Red')
    circumferences.append(circle.calc_circumference())
print(circumferences)

new_circle = Circle('Orange')
print(new_circle.color, new_circle.calc_circumference())
