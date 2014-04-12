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
from math import floor
import fractions
import time
start = time.clock()


def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return s


def phi(n):
    if n in primes:
        o['primes'] += 1
        return n-1
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount


o = {'primes': 0}
candidates = {}
t = 1*10**4
primes = sieve(t)
i = time.clock()
for n in xrange(2, t+1):
    candidates[n] = n/phi(n)
    if not n % 1000:
        print '{:1d}/{:1d}/{:1.3f}'.format(n, t, time.clock()-i)
        i = time.clock()

print max(candidates.iterkeys(), key=lambda x: candidates[x])
print 'optimized'
print o

print '{:1.3f}s'.format(time.clock()-start)
