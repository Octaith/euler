#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import time
import math

start = time.clock()
facts = [math.factorial(i) for i in range(10)]

sum = 0
for i in xrange(3, facts[-1]):
    s = 0
    for j in str(i):
        s += facts[int(j)]
    if s == i:
        sum += i

print sum

print time.clock()-start
