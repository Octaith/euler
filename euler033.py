#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
import time
import fractions

start = time.clock()

m = []
for n in xrange(10, 100):
    for d in xrange(10, 100):
        t = fractions.Fraction(n, d)
        for i in xrange(1,10):
            if str(i) in str(n) and str(i) in str(d):
                tn = str(n).replace(str(i), '')
                td = str(d).replace(str(i), '')
                if tn and td:
                    tn, td = int(tn), int(td)
                    if tn > 0 and td > 0 and tn != td and tn < td:
                        ti = fractions.Fraction(tn, td)
                        if ti == t:
                            m.append(t)
                            print '%s/%s (%s crossed) == %s/%s' % (tn, td, i, n, d)

mm = m[0]
for i in m[1:]:
    mm *= i

print mm

print time.clock()-start
