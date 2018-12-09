#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 05:26:59 2018

@author: sanket
"""

def Wordchecker():
    word=input('Enter word to find in a file:')
    file1 = open("/home/sanket/fileread.txt","r") 
    a=file1.read()
    if word in a:
        print( word,True)
    else:
        print(False)
    
Wordchecker()