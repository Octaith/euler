#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''
import time
import json

start = time.clock()

with open('words.txt', 'r') as f:
    words = json.load(f)

def wordscore(w):
    s = 0
    for i in w:
        s += ord(i)-64
    return s

def triangles(limit):
    n, l = 0, []
    while n<limit:
        n += 1
        l.append(0.5*n*(n+1))
    return l

tr = triangles(200)

sum = 0
for i in words:
    ws = wordscore(i)
    if ws in tr:
        sum += 1

print sum

print time.clock()-start
