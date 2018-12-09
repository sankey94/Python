#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:48:41 2018

@author: student
"""


def square(x):
    return x**2

res = map(square, [1,2,3,4,5])

#print(next(res))
#print(next(res))
#print(next(res))
#print(next(res))
#print(next(res))

for i in res:
    print(i)
    

lst = ["23", "3", "45"]
new_lst = list(map(int, lst))
print(new_lst)

