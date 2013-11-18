#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

start = time.clock()

a = 999
b = 999
p = []
while a>99:
    m = a*b
    if b<a:
        a -= 1
        b = 999
    b -= 1
    if str(m)[::-1] == str(m):
        #print '%s × %s = %s' % (a, b, m)
        p.append(m)

print max(p)
print time.clock()-start
