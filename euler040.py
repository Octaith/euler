#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
import time

start = time.clock()

limit = 1000000
n = [0]

i = 1

while len(n) < limit+1:
    for j in str(i):
        n.append(j)
    i += 1

s = 1
for i in [1,10,100,1000,10000,100000,1000000]:
    s *= int(n[i])

print s

print time.clock()-start
