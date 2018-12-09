#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 08:32:40 2018

@author: student
"""

def minion_game(s):
    # your code goes here
    n = len(s)
    stuart = 0
    kevin = 0
    for i in range(n):
        if s[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print ('Kevin', kevin)
    elif stuart > kevin:
        print ('Stuart', stuart)
    else:
        print ('Draw')
minion_game('BANANA')