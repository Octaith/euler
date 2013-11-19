#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
import time

start = time.clock()

def fact(n):
    if n == 1: return 1
    return n*fact(n-1)

sum = 0
for i in str(fact(100)):
    sum += int(i)

print sum

print time.clock()-start
