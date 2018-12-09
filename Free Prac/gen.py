#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:56:33 2018

@author: student
"""

def simple_generator():
    print('Hi')
    yield 'Hello'
    x = 10
    y = x + 5
    print(y)
    yield 'World'
    yield x
    
ret = simple_generator()
print(type(ret))

print(next(ret))
print(next(ret))

for i in ret:
    print(i)
