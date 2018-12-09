#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 05:54:34 2018

@author: sanket
"""
#def addvalue():
#   
import sys 
def get_details():
    
    s=input('Enter phone no:')
    return s

def phoneadd():
    key=input('Enter name:')
    value=get_details()
    info[key] = value
    return info
def display():
        print(info)
     
        
        
info={}        
while True:
    print('Select operations below:')
    print('1.Add user')
    print('2.Find number as a whole')
    print('3.Find number as numbers in')
    print('4.Display Data')
    ch=int(input('Enter choice:'))
    
    if ch==1:
        phoneadd()
    elif ch==2:
        search_phone=int(input("Enter number to be searched:"))
        for key,value in info.items():
            if search_phone==value:
               # key=info[phone]
               print(key)
               
    elif ch==3:
        count=0
        a='5'
        for key,value in info():
            #print (key,value)
            if a in value and key>2:
                print(key)
                

    
        print(count)
            
        display()
    elif ch==4:
        display()


    else:
        sys.exit("Exitting......")
    
    