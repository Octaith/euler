#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

primes = sieve(10**6)
primes2 = set(primes)
discard = ('0','2','4','6','8','11','33','77','99')

for i in primes:
    for d in discard:
        if i>100 and d in str(i):
            primes2.discard(i)

print int((len(primes)-len(primes2))*1000.0/len(primes))/10.0, '% primes filtered'

def trunkator(n):
    for i in range(len(str(n))):
        yield int(str(n)[i:])
        yield int(str(n)[:i+1])

interesting = []
for p in primes2:
    flag = True
    for i in trunkator(p):
        if i not in primes2:
            flag = False
    if flag and p > 7:
        interesting.append(p)

print interesting
print len(interesting)
print sum(interesting)

print time.clock()-start
