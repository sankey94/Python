#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:15:14 2018

@author: student
"""

class Employee:
    emp_id=0
    def set_designation(self,designation):
        self.designation=designation
        
if __name__=='__main__':
    emp1=Employee()
    print(emp1.emp_id)

    emp1.set_designation('manager')
    print(emp1.emp_id)

    
    
    
    
    
    
    
    
