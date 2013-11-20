#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

# Number of divisors
def factors(n):
    s = 1
    t = math.sqrt(n)
    for i in xrange(2, int(t)+1):
        if n%i == 0:
            s += 2
    if t == int(t): s -= 1
    return s

# Sum of divisors
def d(n):
    s = 1
    t = math.sqrt(n)
    for i in xrange(2, int(t)+1):
        if n%i == 0:
            s += i + n/i
    if t == int(t): s -= t
    return s

# Sieve of Eratosthenes - list primes <k
def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)
