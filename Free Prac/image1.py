#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:59:49 2018

@author: student
"""
import numpy as np
from matplotlib import pyplot as plt

img = plt.imread('puppy.jpg')
print(type(img))

img = img[50:350, 250:600]

plt.imshow(img)

#print(help(plt.imread))