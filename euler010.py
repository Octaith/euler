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

def is_prime(n):
    for i in primes:
        if i>math.sqrt(n):
            break
        if n%i == 0:
            return False
    return True

i, sum = 3, 2
while i < 2*10**6:
    if is_prime(i):
        primes.append(i)
        sum += i
    i += 2

print sum

print time.clock()-start
