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
import time
import json
start = time.clock()


def scale(tr, m):
    return sorted([x*m for x in tr])

tops = {}
def triangle(p):
    if p % 2:
        return 0
    top = 0
    variants = 0
    for k in gen_asc:
        if k > p:
            break
        if not p % k:
            # m = p/k
            # print p, k, gen[k], m, scale(gen[k], m)
            # variants.append(gen[k])
            tops[p] = k
            variants += 1
            if variants > 1:
                return 0
    return variants


def triple(m, n):
    '''http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple'''
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    p = a + b + c
    return {p: (a, b, c)}


def generate():
    for m in xrange(1, limit):
        for n in xrange(1, m):
            if (m-n) % 2 and gcd(m, n) == 1:
                t = triple(m, n)
                gen.update(t)
                if t.keys()[0] > limit:
                    print len(gen)
                else:
                    continue
                break
        else:
            continue
        break

limit = 1500000
# limit = 100000
s = 0
gen = {}
generate()
gen_asc = sorted(gen.keys())
res = 0
itime = time.clock()
for i in xrange(1, limit+1):
    res += triangle(i) == 1
    if not i % 10000:
        print '{:10d}k{:10.3f}{:10.3f}'.format(i/1000, time.clock()-itime, time.clock()-start)
        itime = time.clock()

with open('tops.json', 'w') as f:
    stop = sorted(tops)
    for k in stop:
        f.write('{};{}\n'.format(k, tops[k]))

print res
print '{:1.3f}s'.format(time.clock()-start)
