# coding: utf-8
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9) = 6.

n   Relatively Prime    φ(n)    n/φ(n)
2   1                   1       2
3   1,2                 2       1.5
4   1,3                 2       2
5   1,2,3,4             4       1.25
6   1,5                 2       3
7   1,2,3,4,5,6         6       1.1666...
8   1,3,5,7             4       2
9   1,2,4,5,7,8         6       1.5
10  1,3,7,9             4       2.5

It can be seen that n = 6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''
from __future__ import division
from functools import reduce
from operator import mul
from math import floor, sqrt
import time
start = time.clock()


def phi(n):
    primes = set(fac(n))
    factors = [1-1/p for p in primes if not n % p]
    product = reduce(mul, factors, 1)
    return int(n*product)


def fac(n):
    '''http://rosettacode.org/wiki/Prime_decomposition#Python'''
    step = lambda x: 1 + x*4 - (x//2)*2
    maxq = long(floor(sqrt(n)))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    res = []
    if q <= maxq:
        res.extend(fac(n//q))
        res.extend(fac(q))
    else:
        res = [n]
    return res


candidates = {}
t = 10**6
i = time.clock()
for n in xrange(2, t+1):
    candidates[n] = n/phi(n)
    if not n % 50000:
        print '{:1d}/{:1d}/{:1.3f}'.format(n, t, time.clock()-i)
        i = time.clock()

print max(candidates.iterkeys(), key=lambda x: candidates[x])

print '{:1.3f}s'.format(time.clock()-start)
