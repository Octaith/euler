#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''
from __future__ import division
import time

start = time.clock()

def bouncy(n):
    t = list(str(n))
    if t != sorted(t) and t != sorted(t, reverse=True):
        return True
    return False

b = 0
i = 0

while True:
    i += 1
    if bouncy(i):
        b += 1
    if b/i > 0.99:
        break

print i-1

print time.clock()-start
