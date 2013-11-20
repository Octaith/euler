#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
import time

start = time.clock()

sum = 0
for i in xrange(1, 1000000):
    d = str(i)
    b = bin(i)[2:]
    if d == d[::-1]:
        if b == b[::-1]:
            sum += i

print sum        

print time.clock()-start
