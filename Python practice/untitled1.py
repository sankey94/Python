#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 06:26:56 2018

@author: sanket
"""

numbers={}
def main():
    
    while True:
        i=int(input("Enter number"))
        j=i**2+5
        numbers[i]=j
        print(numbers)
        
        
main()