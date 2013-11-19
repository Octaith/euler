#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
import time

start = time.clock()

numbers = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    10: 'ten',
    20: 'twenty',
    30: 'thirty',
    40: 'fourty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninty',
    100: 'hundred',
    1000: 'thousand',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: ''
}

def read(n):
    r = ''
    if n == 1000:
        r = numbers[1] + numbers[1000]
    elif 100 <= n < 1000:
        q = n/100
        r = numbers[q] + numbers[100]
        q = n%100
        if 0 < q < 20:
            r += 'and' + numbers[q]
        elif q == 0:
            r += numbers[0]
        else:
            q = n%100/10*10
            r += 'and' + numbers[q]
            q = n%100%10
            r += numbers[q]
    elif n<100:
        if n < 20:
            r += numbers[n]
        else:
            q = n/10*10
            r += numbers[q]
            q = n%10
            r += numbers[q]
    print n, r
    return len(r)

sum = 0
for i in xrange(1,1001):
    sum += read(i)

print sum

print time.clock()-start
