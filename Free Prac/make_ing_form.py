#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 16:31:06 2018

@author: student
"""

def make_ing_form(word):
    if word.endswith('ie'):
        return word[:-2]+'ying'
    elif word.endswith('e'):
        return word+'ing'
    
    return word+'ing'

while True:
    word = input('Enter a word: ')
    print('ing form of', word, 'is', make_ing_form(word))
