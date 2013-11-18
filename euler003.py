#!/usr/bin/env python
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
import time

start = time.clock()

n = 600851475143
d = 2
while d*d < n:
    if n%d == 0:
        n /= d
        print 'divided by %s and got %s' % (d, n)
    d += 1

print n
print time.clock()-start
