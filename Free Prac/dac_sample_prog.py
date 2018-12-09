#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 14:52:52 2018

@author: student
"""
import my_math

if __name__ == '__main__':
    x = input('Enter a number: ')
    y = input('Enter another number: ')
    x = my_math.convert_to_int(x)
    y = my_math.convert_to_int(y)
    
    print(my_math.add(x,y))
    print("dac_sample_prog", __name__)
