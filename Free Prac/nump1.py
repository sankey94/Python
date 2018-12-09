#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:32:34 2018

@author: student
"""
import numpy as np
import time

a1 = np.arange(1000000)
a2 = np.arange(1000000)
lst1 = list(range(1000000))
lst2 = list(range(1000000))

start = time.time()

res = [ x+y for x,y in zip(lst1, lst2) ]
print(res)
print('Time taken for adding list: ', (time.time() - start)*1000)

start = time.time()

res = a1 + a2
print(res)
print('Time taken for adding numpy array: ', (time.time() - start)*1000)

