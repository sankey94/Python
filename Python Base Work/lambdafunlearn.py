#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:49:20 2018

@author: student
"""
#
#def square(x):
#    return x**2
#res=map(square,[1,2,3,4,5,6,7,8,9])
#print(next(res))
#print(next(res))
#print(next(res))
#print(next(res))
#print(next(res))
# 
#
#for i in res:
#    print(i)



#lst=["23","3","45"]
#new_lst=list(map(int,lst))
#print(new_lst)

def surname_based(name):
    return name.split()[1]
s='python is fun'
student=['Akash Sharma','Ronak Vora','Ritesh Vedak','Virendra Risbud']
print(student)
student.sort(key=surname_based)
print(student)
print('**'*20)
'''Second approach'''

student=['Akash Sharma','Ronak Vora','Ritesh Vedak','Virendra Risbud']
print(student)
student.sort(key=lambda x: x.split()[1],reverse=False)
print(student)
employees=[['Akash',200000],['Vinay',60000],['Jatin',100001]]
print(employees)
print('**'*30)
employees.sort(key=lambda x: x[1],reverse=False)
print(employees)
