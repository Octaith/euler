#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
import time
import sys

start = time.clock()

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

print 'generating one million primes'
primes = sieve(10**6)
print 'starting with %s primes' % len(primes)
circs = set()

def circulate(s):
    for i in range(len(s)):
        yield s[i:] + s[:i]

c = 0
c_step = len(primes)/79
for i in primes:
    if not c%c_step:
        sys.stdout.write('.')
    c+=1
    if i not in circs:
        digits = str(i)
        circ = True
        for k in circulate(digits):
            if not int(k) in primes:
                circ = False
                break
        if circ:
            for k in circulate(digits):
                circs.add(int(k))

print len(circs)

print time.clock()-start
