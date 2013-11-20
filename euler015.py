#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''
import time
import math

start = time.clock()

n = 40
k = 20

print math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print time.clock()-start
