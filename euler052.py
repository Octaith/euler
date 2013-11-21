#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
import time
import itertools

start = time.clock()

def checker(n):
    ns = set(str(n))
    if len(str(n)) == len(ns):
        flag = True
        for i in xrange(2, 7):
            candidate = set(str(n*i))
            if candidate != ns:
                flag = False
                break
        if flag:
            return True
    return False

i = 1
while True:
    if checker(i):
        print i
        break
    i += 1
    
print time.clock()-start
