#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import time
import math

start = time.clock()

def triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            pyth = a**2+b**2
            c = math.sqrt(pyth)
            if c == int(c):
                if a+b+c == 1000:
                    print '%s^2 + %s^2 = %s^2 (a+b+c = %s)' % (a,b,int(c),a+b+c)
                    return int(a*b*c)

print triplet()

print time.clock()-start
