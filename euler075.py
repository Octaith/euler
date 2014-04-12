# coding: utf-8
'''
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
from fractions import gcd
from math import sqrt
import time
from collections import defaultdict
start = time.clock()


def generate():
    result = 0
    for m in xrange(1, int(sqrt(limit/2))):
        for n in xrange(1, m):
            # http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
            if (m-n) % 2 == 1 and gcd(m, n) == 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                p = a + b + c
                while p <= limit:
                    tris[p] += 1
                    if tris[p] == 1:
                        result += 1
                    if tris[p] == 2:
                        result -= 1
                    p += a + b + c
    return result

limit = 1500000
tris = defaultdict(int)
print generate()

print '{:1.3f}s'.format(time.clock()-start)
