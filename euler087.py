def sieve(k):
    s = set(range(3, k, 2))
    s.add(2)

    for i in range(3, k, 2):
        if i in s:
            for j in range(i ** 2, k, i * 2):
                s.discard(j)
    return sorted(s)

limit = 50 * 10**6
primes = sieve(int(limit**0.5))


def uptofifty(p):
    return [i ** p for i in primes if i ** p < limit]

results = set()

for c in uptofifty(4):
    for b in uptofifty(3):
        for a in uptofifty(2):
            r = a + b + c
            if r < limit:
                results.add(r)

print len(results)
