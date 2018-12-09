#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 15:50:43 2018

@author: student
"""

def correct(s):
    print(s.split())
    return ' '.join(s.split()).replace('.', '. ')

s = 'python    is fun.and  it is     actually a  fun.End'
print(correct(s))
