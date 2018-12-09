#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:47:15 2018

@author: student
"""
class Container():
    start_serial_code = 'ZRMUM01'
    container_size = '220 x 140'
    capacity_in_tons = 1030
    def __init__(self, serial_code):
        self.serial_code = Container.start_serial_code + str(serial_code)

    def 

c1 = Container(720)
c1.contents = 'Books'

c2 = Container(721)
c2.contents = 'Fish'

c3 = Container(722)
print(c1.serial_code, c2.serial_code, c3.serial_code)
print(c1.contents, c2.contents)
