#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time

start = time.clock()

def collatz(n):
    seq = [n]
    i = n
    while i>1:
        if i%2 == 0:
            i = i/2
            seq.append(i)
        else:
            i = 3*i+1
            seq.append(i)
    return len(seq)

longest = 0

for i in xrange(1, 10**6):
    chain = collatz(i)
    if chain > longest:
        print '%s gives %s elements' % (i, chain)
        longest = chain

print time.clock()-start
