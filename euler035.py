#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
import time

start = time.clock()

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

primes = sieve(10**6)
sum = 0
for i in primes:
    digits = list(str(i))
    circ = True
    for k in range(len(digits)):
        circular = digits[k:] + digits[:k]
        if not int(''.join(circular)) in primes:
            circ = False
            break
    if circ:
        sum += 1
        print sum, i

print sum

print time.clock()-start
