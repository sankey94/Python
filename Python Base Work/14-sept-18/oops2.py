#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 10:21:55 2018

@author: student
"""

class Car:
    no_of_tyres=4
    steering_type='Manual'
    def move_steering(self,direction):
        self.direction=direction
        print('car is moving in {} direction'.format(direction))
    
audi=Car()
merc=Car()
merc.color='black'

print(audi.no_of_tyres)

print(merc.no_of_tyres)
print(merc.color)
merc.no_of_tyres=5
print(merc.no_of_tyres)

nano=Car()
print(nano.no_of_tyres)
nano.move_steering('left')
print(nano.direction)