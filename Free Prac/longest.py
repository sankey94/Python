#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:25:45 2018

@author: student
"""
def find_longest_word(lst):
    l = 0
    for i in lst:
        if l < len(i):
            l = len(i)
    return l

''' Alternate way '''
def find_longest_word1(lst):
    return len(max(lst, key=len))

lst = ['Aakash', 'abc', 'Muralidhar', 'xyz']
print(find_longest_word1(lst))
