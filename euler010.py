#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math
import time

start = time.clock()

primes = [2]

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

primes = sieve(2000000)

print sum(primes)

print time.clock()-start
