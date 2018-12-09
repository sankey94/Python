#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:03:25 2018

@author: student
"""
print("dac_sample_prog",__name__)
import convert_int
x=input('Enter number:')
y=x=input('Enter another number:')
print("dac_sample_prog",__name__)
x=convert_int.convert_to_int(x)
y=convert_int.convert_to_int(y)
print(convert_int.add(x,y))
#print(convert_int.multiply(x,y))
#if __name__=='__main__':
#    print('welcome to this place')
#    print('module')
#    print('convert_int', __name__)


