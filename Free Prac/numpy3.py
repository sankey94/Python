#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:42:16 2018

@author: student
"""
import numpy as np
a = np.arange(100)
a = np.arange(100).reshape(10,10)
a.sum()
a[1:3]
a[1:3,3:7]
a[::-1]
a = np.arange(3,30,3).reshape(3,3)
a[a<15]
a[(a<15) & (a>6)]
