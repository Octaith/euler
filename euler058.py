#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''
from __future__ import division
import time
import random
import sys

start = time.clock()

def is_probable_prime(n, k = 7):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in xrange(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

pnums = 0
i = 3
while pnums/(2*i-1) > 0.1 or pnums < 1:
    b = i**2
    for j in xrange(4):
        if is_probable_prime(b-j*(i-1)):
            pnums += 1
    i += 2
print i
print time.clock()-start
