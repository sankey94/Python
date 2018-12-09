#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:38:28 2018

@author: student
"""

def employee(city, name='Aakash', age=18):
    print(city, '-> name =', name, 'and age =', age)
        
employee('Pune')
employee('Pune', age=27)
employee('Pune', 'Ajay')
employee('Pune', 'Jatin', 25)



def employee2(*args, **kwargs):
    print(args)
    print(kwargs['age'])

employee2('Pune', 'Ajit', '+91 926346', age=26, profession='IT professional')
#employee2('Pune', 27)
#employee2('Pune')
#employee2('Pune', 'Jatin', 25)
