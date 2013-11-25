#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
import time

start = time.clock()

c = 0
for a in xrange(1, 100):
    for b in xrange(1, 100):
        if len(str(a**b)) == b:
            c += 1

print c

print time.clock()-start
