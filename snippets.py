#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

# Number of divisors
def factors(n):
    s = 1
    t = math.sqrt(n)
    for i in xrange(2, int(t)+1):
        if n%i == 0:
            s += 2
    if t == int(t): s -= 1
    return s

# Sum of divisors
def d(n):
    s = 1
    t = math.sqrt(n)
    for i in xrange(2, int(t)+1):
        if n%i == 0:
            s += i + n/i
    if t == int(t): s -= t
    return s

# Sieve of Eratosthenes - list primes <k
def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

# Miller-Rabin primality test
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