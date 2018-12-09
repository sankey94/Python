#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 12:06:09 2018

@author: student
"""
import random
class Employees:
    sal_hike1=1.08
    def __init__(self,empnm,empid,empsal):
        self.empnm = empnm
        self.empid=empid
        self.empsal=empsal
        
    def Display(self):
        print(self.empid, self.empnm, self.empsal)
        
    def sal_hike(self):
        self.empsal+=self.empsal*Employees.sal_hike1
        print(self.empsal)

'''
for i in range(5):
    if __name__=='__main__' :
        empnm=input("Enter name:")
        empid=int(input("Enter id:"))
        empsal=int(input("Enter Salary:"))
        emp1=Employees(empnm,empid,empsal)
        emp2=Employees(empnm,empid,empsal)
        emp3=Employees(empnm,empid,empsal)
        emp4=Employees(empnm,empid,empsal)
        emp1.Display()
        
 #       emp1.sal_hike()
   #     emp1.Display()
#for i in range(2):
#       emp1.sal_hike()
#       emp1.Display()
       
'''       
       
names=['shalini','lini','sanket','bh','gsygs']
employees=[]
for i in range(2):
    empnm=random.choice(names)
    emp=Employees(empid,empnm,empsal)
    employees.append(emp)
print(employees[0].empsal)
employees[0].sal_hike()
print(employees[0].empsal)
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
     

    
        