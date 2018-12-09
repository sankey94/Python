#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:40:19 2018

@author: student
"""
try:
    with open('stud_info.csv', 'r') as stud_info:
        salaries = []
        for rec in stud_info:
            salaries.append(int(rec.split(',')[3]))
        print(sum(salaries)/len(salaries))
except Exception as err:
    print(err)


try:
    with open('stud_info.csv', 'r') as stud_info:
        salaries = []
        for rec in stud_info.readlines():
            salaries.append(int(rec.split(',')[3]))
        print(sum(salaries)/len(salaries))
except Exception as err:
    print(err)
    