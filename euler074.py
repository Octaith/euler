# coding: utf-8
'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
import time
from math import factorial
start = time.clock()

f = [factorial(n) for n in xrange(10)]


def chain(n, ch=[]):
    if not ch:
        ch = [n]
    s = ch[-1]
    digits = list(str(s))
    fdigits = [f[int(d)] for d in digits]
    s = sum(fdigits)
    if len(ch) > 1 and s in ch:
        return len(ch), ch
    ch.append(s)
    return chain(n, ch)

limit = 10**6
print sum(chain(i)[0] == 60 for i in xrange(1, limit+1))

print '{:1.3f}s'.format(time.clock()-start)
