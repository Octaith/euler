#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''
import time

start = time.clock()

keylog = []
with open('keylog.txt', 'r') as f:
    for i in f:
        keylog.append(i.replace('\n',''))

def check(n):
    s = str(n)
    for i in keylog:
        t1 = s.find(i[0])
        t2 = s.find(i[1], t1)
        t3 = s.find(i[2], t2)
        if t1 == -1 or t2 == -1 or t3 == -1 or not t1 < t2 < t3:
            return False
    return True

n = 0
while True:
    n+=1
    if check(n):
        print n
        break

print time.clock()-start
