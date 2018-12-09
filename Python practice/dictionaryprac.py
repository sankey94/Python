#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 05:45:22 2018

@author: sanket
"""

people={'sanket':'blue','chetna':'red','ravi':'red','anki':'violet'}
print(people)
people['sanket']='black'
print(people)
del people['sanket']
print(people)
for key,value in sorted(people.items()):
    print(key+"->" ,end=" ")
    print(value)
    
