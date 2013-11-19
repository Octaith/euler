#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''
import time

start = time.clock()

number = 2**1000
digits = list(str(number))
sum = 0
for i in digits:
    sum += int(i)

print sum

print time.clock()-start
