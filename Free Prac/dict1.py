#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 14:41:38 2018

@author: student
"""
d = {'money': 5500, 'cards': 3, 'candies': 17, 'vcards': 5, 'money1': 500, 123: 'money3', 1234: 'cards'}

if 123 in d:
    print(d[123])

for item in d:
    print(item, " --> ", d[item])
print('**' * 10)
for k, v in d.items():
    print(k, '....', v)
    
d['candies'] = 56
d['candies'] += 5
print(d)
'''
for item in d.keys():
    print(item)

for item in d.values():
    print(item)
'''

d2 = { 'money': 6000, 'cards': {'visa':2, 'amex':1, 'master':0}, 'candies': 14}
