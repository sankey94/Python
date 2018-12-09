#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:40:32 2018

@author: student
"""
#
#try:
#    with open('/home/student/NSE-INFY.csv','r') as infy:
#        close=[]
#        for line in infy:
#            closing_price=line.split(',')[5]
#            if closing_price == 'Close':
#                continue
#            close.append(float(closing_price))
#        print(sum(close)/len(close))
#except IOError as err:
#   print('File not found -->',err)
#   
#   

try:
    with open('/home/student/NSE-INFY.csv','r') as infy:
        #close=[]
        #        year = datetime.date.today().year
        d={}
        for line in infy:
            closing_price=line.split(',')[5]
            if closing_price == 'Close':
                continue
           # close.append(float(closing_price))
            date=line.split(',')[0]
            year=date.split('-')[0]
            if year in d:
                d[year].append(float(closing_price))
            else:
                d[year]=[float(closing_price)]
        for item in d:
           print('close price for {} is {}'.format(item,sum(d[item])/len(d[item])))
       # print('Close price for 2018 is {}'.format(sum()))
    print(year)
        #print(sum(close)/len(close))
except IOError as err:
   print('File not found -->',err)

        