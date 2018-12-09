# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def prime(num):
    p_nos = []
    for i in range(2, num+1):
        found = 0
        for j in range(2, i):
            if i % j == 0:
                found = 1
        if found == 0:
            p_nos.append(i)
    return p_nos

def another_function(num):        
        return list(range(num))
    
#print(another_function(5))
#print(another_function(7))

final_list = []
final_list.append(prime(5))
final_list.append(prime(7))
final_list.append(prime(8))
print(final_list)

'''
option = 'yes'
while option == 'yes':
    num = int(input('Enter a number: '))
    func1(num)
    option = input("continue? ")
'''
