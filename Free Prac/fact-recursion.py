#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:22:34 2018

@author: student
"""

def fact(num):
    if num == 0 or num == 1:
        return num
    return num*fact(num-1)

result = fact(6)
print(result)

#********************************

def fact(num):
    if num == 0 or num == 1:
        return num
    return num*fact(num-1)

num = int(input('Enter a number: '))
result = fact(num)
print(result)
