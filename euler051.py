#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
import time
import itertools

start = time.clock()

def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

primes = sieve(10**6)

def eight_prime_family(prime, rd):
  c=0
  for digit in '0123456789':
    n = int(prime.replace(rd, digit))
    if (n>100000 and n in primes):
      c=c+1
  return c==8
 
for prime in primes:
  if (prime>100000):
    s = str(prime)
    last_digit = s[5:6]
    if (s.count('0')==3 and eight_prime_family(s,'0') \
     or s.count('1')==3 and last_digit != '1' and eight_prime_family(s,'1') \
     or s.count('2')==3 and eight_prime_family(s,'2')):
       print s
       break


print time.clock()-start
