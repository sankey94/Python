#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:27:59 2018

@author: student
"""
def your_gcd(num1, num2):
    if num1 < num2:
        smaller_num = num1
    else:
        smaller_num = num2
    for i in range(1, smaller_num+1):
        if num1%i == 0 and num2%i == 0:
            hcf = i
    return hcf

def my_gcd(num1, num2):
    for i in range(1, min(num1, num2)+1):
        if num1%i == 0 and num2%i == 0:
            hcf = i
    return hcf
    
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
result = your_gcd(num1, num2)
print(result)
result = my_gcd(num1, num2)
print(result)