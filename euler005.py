#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import time

start = time.clock()

# Greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Least common multiple
def lcm(a, b):
    return abs(a*b)/gcd(a,b)

n = 1
for i in range(1,21):
    n = lcm(n, i)

print n

print time.clock()-start
