#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
from hashlib import sha512
import string

hashes = frozenset(open('hashes', 'r').read().split('\n'))
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

found = 0
for word in open('probable-v2-top1575.txt', 'r'):
    word = word.strip()
    for salt in salts:
        if sha512(salt + word).hexdigest() in hashes:
            print 'Salt: %s\tPwd: %s' % (salt, word)
            found += 1

print 'Number of hashes: %s\tNumber found: %s' % (len(hashes) - 1, found)
