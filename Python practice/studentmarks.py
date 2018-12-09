#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 06:41:32 2018

@author: sanket
"""

marks=[]
a=int(input("Enter number of students:"))
for i in range(a):
    print("student{}".format(i),end="")
    i=(int(input("Enter marks")))
    marks.append(i)
#print(marks) 
r=tuple(marks)
print(r) 
a=max(r)
b=min(r)
print("High Score is {}".format(a))
print("Low Score is {}".format(b))  
#    marks+i
    