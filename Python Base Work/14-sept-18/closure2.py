#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:16:11 2018

@author: student
"""

def conversion_price(currency):
    def price(qty):
        return qty*currency
    return price

dollar_to_rupees=conversion_price(70)
pound_to_rupees=conversion_price(90)

print(dollar_to_rupees(30))
print(pound_to_rupees(30))





def make_multiplier_of(n):
    def multiplier(x):
        return  x*n
    return multiplier
times3=make_multiplier_of(3)
times5=make_multiplier_of(5)
times6=make_multiplier_of(6)

print(times3(7))
print(times5(7))