#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:10:26 2018

@author: student
"""
from oops3 import Car

class GermanCar(Car):
    pass

polo = GermanCar()
polo.no_of_tyres = 7
print(polo.no_of_tyres)
