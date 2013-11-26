#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''
import time
import json
import sys
import itertools

start = time.clock()

commonwords = set(["the","be","to","of","and","a","in","that","have","I","it","for","not","on","with","he","as","you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will","my","one","all","would","there","their","what","so","up","out","if","about","who","get","which","go","me","when","make","can","like","time","no","just","him","know"])

with open('cipher1.txt', 'r') as f:
    cipher = json.load(f)

#print cipher

def decode(key):
    #print 'decoding with', key
    str = ''
    key = list(key)
    for i in xrange(len(key)):
        key[i] = ord(key[i])
    c = 0
    for i in cipher:
        str += chr(i ^ key[c])
        c += 1
        if c == len(key):
            c = 0
    return str



variants = itertools.permutations('abcdefghijklmnopqrstuvwxyz', 3)

mk = ''
for i in variants:
    t = decode(i)
    cw = 0
    for w in commonwords:
        if w in t:
            cw += 1
    if cw > 0.5*len(commonwords):
        mk = i
        print '%s words decoded with key %s' % (cw, i)
        print t
        break

t = decode(mk)
c = 0
for i in t:
    c += ord(i)

print c

print time.clock()-start
