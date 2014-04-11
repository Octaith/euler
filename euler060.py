# coding: utf-8
'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from itertools import permutations, combinations
import os
import time
import random
import sys
start = time.clock()


def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s), s


def is_probable_prime(n, k=7):
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


def is_prime(n):
    if n < primes[-1]:
        return n in primeset
    else:
        print n, 'prob'
        return is_probable_prime(n)


def int_concat(list):
    return int(''.join(str(n) for n in list))


def candidate(x):
    mutations = [is_prime(int_concat(i)) for i in permutations(x, 2)]
    if all(mutations):
        return True
    return False


def find_candidates(lim):
    test = primes[:lim]
    s = {}
    for x in test:
        s[x] = [y for y in test if candidate([x, y])]
    return s


def intersect(todepth, depth=2, nums={}, newset={}):
    # print '| '*depth, len(nums), sorted(list(nums))
    if len(nums) == todepth and candidate(nums):
        print sorted(list(nums))
        print sum(nums)
        print time.clock()-start
        os._exit(0)
    if newset:
        for a in newset:
            for b in candidates.keys():
                if candidate([a, b]):
                    inter = set(candidates[b]) & set(candidates[b])
                    newnums = set(nums)
                    if len(inter) and depth < todepth and b not in newnums:
                        newnums.add(b)
                        intersect(todepth, depth=len(newnums), nums=newnums, newset=inter)
    else:
        for a, b in combinations(candidates.keys(), 2):
            inter = set(candidates[a]) & set(candidates[b])
            if inter:
                intersect(todepth, depth=depth, nums={a, b}, newset=inter)


primes, primeset = sieve(10**6)
print len(primes), 'primes'
candidates = find_candidates(125)
print len(candidates), 'candidates'
print intersect(4)
