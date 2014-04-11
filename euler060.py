#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
import time
from itertools import combinations, permutations
from math import factorial
import progressbar

start = time.clock()


def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s), s

primes, primeset = sieve(10**6)
toobig = lambda x: x > primes[-1]


def int_concat(list):
    result = int(''.join(str(n) for n in list))
    if toobig(result):
        print result
        raise ValueError('too big')
    return result


def remarkable(x):
    mutations = [int_concat(i) in primeset for i in permutations(x, 2)]
    if all(mutations):
        return sum(x)
    return False


def remarkable_set(n):
    lim = 150
    test = primes[:lim]
    total = factorial(lim)/(factorial(n)*factorial(lim-n))
    step = total/10000
    count = 0

    widgets = [
        progressbar.Percentage(), '    ',
        progressbar.SimpleProgress(sep='/'), '    ',
        progressbar.FileTransferSpeed(unit=''), '    ',
        progressbar.ETA()
    ]

    pbar = progressbar.ProgressBar(maxval=total, widgets=widgets).start()

    for i in combinations(test, n):
        if remarkable(i):
            pbar.finish()
            print 'Found!'
            print i
            return remarkable(i)
        if not count % step:
            pbar.update(count)
        count += 1

print remarkable_set(4)

print time.clock()-start
