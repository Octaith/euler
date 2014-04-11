from fractions import Fraction
from math import log10, floor


def expand(n):
    if n == 0:
        return 0
    result = Fraction(1, 2 + expand(n-1))
    return result

hits = 0
for n in xrange(1, 1001):
    print n
    frac = 1 + expand(n)
    num = floor(log10(frac.numerator))
    den = floor(log10(frac.denominator))
    hits += num > den

print hits
