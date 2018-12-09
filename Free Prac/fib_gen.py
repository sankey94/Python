#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:18:16 2018

@author: student
"""

def fib_gen(max):
    first, second = 0, 1
    while first < max:
        print(first)
        first, second = second, first + second

#fib_gen(15)


def fib_gen1(max):
    first, second = 0, 1
    while first < max:
        yield first
        first, second = second, first + second

gen = fib_gen1(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
    