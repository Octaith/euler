#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import time
import math

start = time.clock()

baseexp = []

with open('base_exp.txt', 'r') as f:
    for i in f:
        baseexp.append(i.replace('\n', '').split(','))

largest = [0, 0]
c = 0
for i in baseexp:
    a, x = int(i[0]), int(i[1])
    c += 1
    if x*math.log10(a) > largest[1]:
        largest[0] = c
        largest[1] = x*math.log10(a)

print largest

print time.clock()-start
