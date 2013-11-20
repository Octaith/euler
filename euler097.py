#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.
'''
import time

start = time.clock()

a = 2
for i in xrange(1, 7830457):
    a = (2 * a) % 10**10

a *= 28433
a += 1
print a % 10**10

print time.clock()-start
