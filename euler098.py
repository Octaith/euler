#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
'''
import json
from collections import defaultdict
from itertools import permutations, combinations
import time

start = time.clock()

with open('words.txt') as f:
    words = json.load(f)


def is_number_square(n):
    return int(n**0.5) == n**0.5


def is_word_square(word, substitutions):
    n = [str(substitutions[letter]) for letter in word]
    if n[0] == '0':
        return False
    n = int(''.join(n))
    if is_number_square(n):
        # print '{} {} = {}^2'.format(word, n, int(n**0.5))
        return n


def letters_list(word):
    return [letter for letter in word]


def all_substitutions(word):
    letters = letters_list(word)
    letter_count = len(set(letters))
    letter_subs = sorted(set(letters))
    if letter_count > 10:
        yield False
    subs = permutations(numbers, letter_count)
    for sub in subs:
        dsub = {letter_subs[i]: x for i, x in enumerate(sub)}
        if is_word_square(word, dsub):
            yield dsub


def pairable():
    pairs = defaultdict(list)
    for word in words:
        letters = letters_list(word)
        fingerprint = ''.join(sorted(letters))
        pairs[fingerprint].append(word)
    candidates = {x: pairs[x] for x in pairs if len(pairs[x]) > 1}
    print len(candidates), 'candidates'
    return candidates


def check_pairs():
    for i in pairs.values():
        for pair in combinations(i, 2):
            for result, word in check_pair(pair):
                if result:
                    print ' and '.join(pair), 'is a square anagram word pair, max', result, word
                    mpair[result] = word


def check_pair(pair):
    for sub in all_substitutions(pair[0]):
        if sub and is_word_square(pair[1], sub):
            yield is_word_square(pair[0], sub), pair[0]
            yield is_word_square(pair[1], sub), pair[1]
    yield False, None


mpair = {}
numbers = range(10)
pairs = pairable()
check_pairs()
m = max(mpair.keys())
print m, mpair[m]

print time.clock()-start
