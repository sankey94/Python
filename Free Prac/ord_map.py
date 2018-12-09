#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = 'python is fun'
#lst = []
#for c in s:
#    lst.append(ord(c))
#print(lst)

print(list(map(ord, s)))

def surname_based(name):
    return name.split()[1]

students = ['Aakash Sharma', 'Vinay Kumar', 'Jatin Doshi']

print(students)
students.sort(key=surname_based, reverse=False)
print(students)

''' second approach '''
print('**' * 20)
students = ['Aakash Sharma', 'Vinay Kumar', 'Jatin Doshi']
students.sort(key=lambda x: x.split()[1], reverse=True)
print(students)

employees = [ ['Aakash', 53000], ['Vinay', 67000], ['Jatin', 61000] ]
employees.sort(key=lambda x: x[1])
print(employees)

