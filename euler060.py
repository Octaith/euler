# coding: utf-8
'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from itertools import permutations, combinations
import time
start = time.clock()


def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s), s


def isprime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def is_prime(n):
    if n < primes[-1]:
        return n in primeset
    else:
        return isprime(n)


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


results = []
def intersect(todepth, nums={}, newset={}):
    if newset:
        for b in candidates.keys():
            newnums = set(nums)
            if b in nums:
                break
            newnums.add(b)
            if candidate(newnums):
                if len(newnums) == todepth:
                    print 'found: sum({}) = {}, elapsed {:1.2f}s'.format(sorted(list(newnums)), sum(newnums), time.clock()-start)
                    result = {
                        'result': sorted(list(newnums)),
                        'sum': sum(newnums)
                        }
                    results.append(result)
                else:
                    inter = newset & set(candidates[b])
                    if inter and len(newnums) < todepth:
                        intersect(todepth,  nums=newnums, newset=inter)
    else:
        for a in candidates.keys():
            if candidates[a]:
                intersect(todepth, nums={a}, newset=set(candidates[a]))


primes, primeset = sieve(10**4)
print len(primes), 'primes'
candidates = find_candidates(1250)
print len(candidates), 'candidates'
intersect(5)
best = sorted(results, key=lambda x: x['sum'])[0]
print 'and the winner is', best['sum']
