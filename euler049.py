#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
import time
import sys
import itertools

start = time.clock()

def sieve(l, k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)

    for i in xrange(l):
        s.discard(i)

    return sorted(s)

primes = sieve(1000, 10000)
c = 0

for i in primes:
    if c > 1:
        break
    for s in range(1, int((10000-i)/2.0)):
        if i+s in primes and i+2*s in primes:
            t1 = set(itertools.permutations(str(i)))
            t2 = tuple(str(i+s))
            t3 = tuple(str(i+2*s))
            if t2 in t1 and t3 in t1:
                print i, i+s, i+2*s
                c += 1

print time.clock()-start
