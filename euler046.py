#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import time
import math

start = time.clock()

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

primes = sieve(10000)

for i in xrange(9, 10000, 2):
    if i not in primes:
        flag = True
        for p in primes:
            if p >= i:
                break
            for s in xrange(1, int(math.sqrt(i-p))+1):
                if p+2*s**2 == i:
                    flag = False
                    break
        if flag:
            print i
            break

print time.clock()-start
