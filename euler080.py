'''
Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
'''

import time

start = time.clock()

from decimal import *

getcontext().prec = 105


def sqrt_digits_sum(n):
    prec_sqrt = Decimal(n).sqrt()
    digits = sum(map(int, str(int(prec_sqrt * 10 ** 99))))
    if int(prec_sqrt) == prec_sqrt:
        digits = 0
    return digits

s = 0
for i in range(1, 101):
    s += sqrt_digits_sum(i)

print(s)

print(time.clock()-start)
