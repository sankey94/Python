#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:33:23 2018

@author: student
"""
class Student:
    start_stud_id = 100 #class atrribute
    def get_fullname(self):
        return self.firstname + " " + self.lastname
    def __init__(self, name='NA', last='NA', phone='0'):
        self.firstname = name
        self.lastname = last
        self.email = name + '.' + last + '@cdac.com'
        self.phone = phone
        self.stud_id = Student.start_stud_id + 1
        Student.start_stud_id += 1
    def stud_details(self):
        print(self.stud_id, ":", self.get_fullname())
    def print_start_stud_id(self):
        print(Student.start_stud_id)

print(Student.start_stud_id)
s1 = Student('Aakash', 'Sharma', '+91 9836467')
s1.stud_details()
s = [Student(), Student()]
s1.print_start_stud_id()
