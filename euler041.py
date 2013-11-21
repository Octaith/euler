#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
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

# number is divisible by 3 if and only if the digit sum of the number is divisible by 3
# only n = 4, 7 could be primes
pandigital = set(str(i) for i in range(1,8))
primes = sieve(7654321)

for i in primes[::-1]:
    if set(str(i)) == pandigital:
        print i
        break

print time.clock()-start
