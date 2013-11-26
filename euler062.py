#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
from __future__ import division
import time
import itertools

start = time.clock()

cubes = set()
for i in xrange(1, 10000):
    cubes.add(i**3)

for i in cubes:
    t = sorted(list(str(i)))
    l = []
    for j in cubes:
        t2 = sorted(list(str(j)))
        if t == t2:
            l.append(j)
    if len(l) == 5:
        print sorted(l)[0]
        break

print time.clock()-start
