#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:58:21 2018

@author: student
"""

#n = int(input("Enter a number:"))
#result=100/n
#print(result)
##
n = int(input("Enter a number:"))
try:
    result=100/n
    print(result)
except ZeroDivisionError:
    print('Please enter non-zero value')
    try:
        n=int(input('Enter number:'))
        result=100/n
        print(result)
    except ZeroDivisionError:
        print('Exitting')


