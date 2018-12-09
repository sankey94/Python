#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:07:05 2018

@author: student
"""

def employees_old(e, c, age, dept='IT', sal=0):
    name = input('Enter name of empl: ')
    print('Name of empl is',name)
    print('emp id:', e)
    print('dept is:', dept)
    print('Salary is:', sal)

def employees1(e, *info, dept='IT', sal=0):
    print(e)
    print('all other non keyword argument', info)
    
def employees2(*args, dept='IT', sal=0):
    #print(e)
    print('all other non keyword argument', args)
    print('Department ->', dept)
    
def employees3(*args, **other_info):
    #print(e)
    print('all other non keyword argument', args)
    print('keyword arguments -> ', other_info)

def employees(*args, **kwargs):
    #print(e)
    print('all other non keyword argument', args)
    print('Salary -> ', kwargs["sal"])
    print('Course -> ', args[1])
    
empl_id = 101
#employees(empl_id)
course = 'dbda'
#employees(empl_id, course)
#employees(empl_id, course, dept='ADMIN', sal=12000)
employees(empl_id, course, 25, 'pune', dept='Admin', sal=15000)
