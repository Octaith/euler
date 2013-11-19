#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import time
import json

start = time.clock()

def namescore(n):
    score = 0
    for c in n:
        score += ord(c)-64
    return score

with open('names.txt', 'r') as f:
    names = json.load(f)

names = sorted(names)

c, sum = 0, 0
for name in names:
    c += 1
    sum += c*namescore(name)

print sum

print time.clock()-start
