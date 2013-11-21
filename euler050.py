#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
import time

start = time.clock()
limit = 10**6

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

def primesum(p):
    s = []
    n = 0
    for i in p:
        n += i
        s.append(n)
    return s

primes = sieve(limit)
primesums = primesum(primes)

n, m = 0, 0
for i in xrange(n, len(primesums)):
    for j in xrange(i-n-1, 0, -1):
        t = primesums[i]-primesums[j]
        if t>limit:
            break
        if t in primes:
            n = i-j
            if t>m:
                m = t

print m

print time.clock()-start
