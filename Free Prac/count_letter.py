#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:34:22 2018

@author: student
"""

s = 'python is fun. lets learn python'

count = 0
for letter in s:
    if letter == 'n':
        count += 1
print(count)
