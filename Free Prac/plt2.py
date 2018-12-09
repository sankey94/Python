#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:53:20 2018

@author: student
"""

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(2,20,2)
y = np.arange(1,10)

x = np.arange(0, 3*np.pi, 0.1)
x = np.sin(x)
y = np.cos(x)

plt.plot(x,y)

plt.xlabel('x data')
plt.ylabel('x data')
plt.title('Sample ploting')
plt.show()
