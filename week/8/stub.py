#!/usr/bin/env python2

import sys
import struct


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1
WORD = (4, "<L"])
DWORD = (8, "<Q")
DOUBLE = (8, "<Q")
STRING = (8, "s")

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

def readline(length, code):
    struct.unpack(code, data[readline.cur:length])
    readline.cur += code
readline.cur = 0 # init line counter

def is_ascii(string):
    return all(ord(c) < 128 for c in s)

def header(args):
    magic, version, timestamp, author, nsects = args

    if magic != MAGIC:
        bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

    print("MAGIC: %s" % hex(magic2))

    if version != VERSION:
        bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

    print("VERSION: %d" % int(version))

    if timestamp > 2**31 - 1:
        bork("Bad timestamp!  Got %d" % (int(timestamp),))

    print("TIMESTAMP: %d" % timestamp)
    
    if not is_ascii(author):
        bork("Bad author! Got %s" % (author,))

    if nsects <= 0:
        bork("Bad section count!  Got %d" % (nsects))

    print("-------  BODY  -------")
    targets += ([(section, [WORD, WORD])] * nsects)

def section(args):
    stype, slen = args

    if slen > 0:
        payload = readline(slen, '' + slen + 's') # check for overflow

    if stype == SECTION_PNG:
        payload = PDF_SIGNATURE + payload
        with open('image%d.png' % (section.count,),'w') as img:
            img.write(payload)

        section.count += 1
    elif stype == SECTION_UTF8:
        pass
    elif stype == SECTION_DOUBLES:
        pass
    elif stype == SECTION_WORDS:
        pass
    elif stype == SECTION_COORD:
        pass
    elif stype == SECTION_REFERENCE:
        pass
    elif stype == SECTION_ASCII:
        pass
section.count = 0    

    

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
targets = [
    (header, [WORD,WORD,WORD,STRING,WORD])
    ]
print("------- HEADER -------")
while targets:
    func, codes = targets.pop()
    items = []
    for (length, code) in codes:
        items.append(readline(length, code))
    func(items)
