#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import time
import math

start = time.clock()

# a^2 + b^2 == c^2
sols = {}
for c in xrange(1, 1000):
    for b in xrange(1, c):
        a = math.sqrt(c**2-b**2)
        if a == int(a):
            a = int(a)
            s = a+b+c
            if s<1000:
                if not s in sols:
                    sols[s] = 0
                sols[s] +=1
m = (0,0)
for i in sols:
    if sols[i] > m[1]:
        m = (i, sols[i])

print m[0]

print time.clock()-start
