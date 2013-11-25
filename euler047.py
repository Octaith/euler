#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
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

def factors(n):
    f = 0
    for i in primes:
        if i**2 > n:
            return f+1
        pf = False
        while not n%i:
            pf = True
            n /= i
        if pf:
            f += 1
        if n == 1:
            return f
    return f


primes = sieve(100000)

cons = 0
i = 0
while True:
    i += 1
    if factors(i) == 4:
        cons += 1
        if cons == 4:
            print i-3
            break
    else:
        cons = 0

print time.clock()-start
