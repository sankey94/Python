#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:05:46 2018

@author: student
"""
def overlapping1(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
    return False

''' Alternate way '''
def overlapping2(lst1, lst2):
    return True if set(lst1) & set(lst2) else False    

lst1 = [1,2,3,4,5]
lst2 = [9,8,7,6,5]
print(overlapping2(lst1,lst2))
lst2 = [9,8,7,6]
print(overlapping2(lst1,lst2))

