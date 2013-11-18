#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import time
import math

start = time.clock()

primes = [2]

def is_prime(n):
    for i in primes:
        if i>math.sqrt(n):
            break
        if n%i == 0:
            return False
    return True

found_primes = 1
i = 3
while found_primes < 10001:
    if is_prime(i):
        found_primes += 1
        primes.append(i)
    i += 2

print i

print time.clock()-start
