#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:07:59 2018

@author: student
"""
n = int(input('Enter a number: '))
result = 100/n
print(result)


n = int(input('Enter a number: '))
try:
    result = 100/n
except ZeroDivisionError:
    print('Please enter non-zero value')
    try:
        n = int(input('Enter a number: '))
        result = 100/n
    except ZeroDivisionError:
        print('Rahene do tumse nahi ho payega')
print(result)
