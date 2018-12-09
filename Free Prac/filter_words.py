#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:32:05 2018

@author: student
"""

def filter_long_words(word_list, n):
    new_lst = []
    for word in word_list:
        if n < len(word):
            new_lst.append(word)
    return new_lst

''' Alternate way '''
def filter_long_words1(word_list, n):
    return [ word for word in word_list if len(word)>n ]

lst = ['Aakash', 'abc', 'Muralidhar', 'xyz']
print(filter_long_words(lst, 5))
