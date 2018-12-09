#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 08:46:55 2018

@author: student
"""
''' closure is a function which remembers the values in
enclosing scope even if they are not in memory'''
def outer():
    x = 10
    a = 8
    b = 18
    print(hex(id(x)), hex(id(a)))
    def inner(y):
        return x+y+a
    return inner

local_fun = outer()
print(type(local_fun))
print(local_fun(50))
print(local_fun.__closure__)

''' Closures are used as function factories.. which returns 
new and specialised functions '''

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x,exp) 
        #Python creates a closure to refer to exp obj
    return raise_to_exp

square = raise_to(2)
cube = raise_to(3)
print(square(5), cube(5))
