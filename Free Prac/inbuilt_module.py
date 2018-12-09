#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import pi

def calc_area1(radius):
    return pi*radius**2

def calc_circumference1(radius):
    return 2*pi*radius

r = int(input('Enter radius of a circle: '))
print('Area ==>', calc_area1(r))
print('Circumferece ==>', calc_circumference1(r))

''' Alternate way '''
import math
def calc_area(radius):
    return math.pi*math.pow(radius, 2)

def calc_circumference(radius):
    return 2*math.pi*radius

r = int(input('Enter radius of a circle: '))
print('Area ==>', calc_area(r))
print('Circumferece ==>', calc_circumference(r))
