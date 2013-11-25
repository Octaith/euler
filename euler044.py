#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''
import time
import itertools
import operator

start = time.clock()

def pentagonal(n):
    return n*(3*n-1)/2

p = set(pentagonal(i) for i in xrange(1,3000))

cp = itertools.combinations(p, 2)

for i in cp:
    if operator.add(*i) in p and abs(operator.sub(*i)) in p:
        print abs(operator.sub(*i))
        break

print time.clock()-start