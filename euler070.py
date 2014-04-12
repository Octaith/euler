# coding: utf-8
'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''
from __future__ import division
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


def interesting(n, p):
    n = sorted(list(str(n)))
    p = sorted(list(str(p)))
    return n == p

candidates = {}
t = 10**7
left = t**0.5 - 1000
right = t**0.5 + 1000
primes = sieve(10000)

'''http://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-φn-is-a-permutation-of-n/'''
for a in primes:
    for b in primes:
        if left < a < right and left < b < right:
            n = a*b
            p = (a-1)*(b-1)
            if n < t and interesting(n, p):
                candidates[n] = n/p

print len(candidates), 'candidates'
winner = min(candidates.iterkeys(), key=lambda x: candidates[x])
print winner, candidates[winner]

print '{:1.3f}s'.format(time.clock()-start)
