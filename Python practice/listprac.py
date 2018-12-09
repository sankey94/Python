#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 05:12:06 2018

@author: sanket
"""
#cust=['name', 'address', 'age', 'college name']
#value=int(input("Enter no values:"))
#for i in range(1,value):
#    cust.append(input("Enter value:"))
#print(cust)
#cust.remove(input("Enter element to remove:"))
#print(cust)
months=['Jan','Feb','Mar','April','May','June','July','August','September','October','November','December']
for i in months:
    print(i, end=",")
while True:
    month=(input("Which batch do you want to appear? :"))
    if month=='Jan' or month=='jan' :
        print(months[:5])
    if month=='July':
        print(months[6:-1])
    x=input("Do you want to continue:")
    if(x!='y'):
        break;