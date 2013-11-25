#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''
import time
import sys

start = time.clock()

def sequence(n):
    #print '\n===', n, '==='
    while True:
        r = 0
        for i in str(n):
            r += int(i)**2
        #sys.stdout.write(str(n)+' ')
        if r == 1 or r == 89:
            return r
        n = r

c = 0
for i in xrange(2, 10**7):
    if not i%(10**4):
        sys.stdout.write('\r'+str(i*100.0/10**7)+' %')
    t = sequence(i)
    if t == 89:
        c += 1

print '\n\n',c

print time.clock()-start
