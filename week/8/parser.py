#!/usr/bin/env python2

import sys
from struct import unpack_from
import struct
from itertools import count as infcount
WORD = (4, '<L')
DWORD = (8, '<Q')
DOUBLE = (8, '<d')
def STRING(length):
    return (length, '%ds' % (length,))
MAGIC = 0xDEADBEEF
VERSION = 0x1
PNG_MAGIC = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'

SECTION_PNG = 0x1
SECTION_DWORDS = 0x2
SECTION_UTF8 = 0x3
SECTION_DOUBLES = 0x4
SECTION_WORDS = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_ASCII = 0x9

lookup = [
    '','PNG', 'DWORDS', 'UTF8', 'DOUBLES',
    'WORDS', 'COORD', 'REFERENCE', '','ASCII']

def bork(msg):
    sys.exit(msg)

def read(length, code):
    read.count += length
    return unpack_from(code, data, offset=read.count - length)[0]
read.count = 0

with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()
    
magic, version, timestamp = [read(*WORD) for x in xrange(3)]
author = read(*STRING(8))
scount = read(*WORD)

# check to make sure header is valid
if magic != MAGIC:
    bork("magic is wrong")

if version != VERSION:
    bork("version is wrong")

if timestamp > 2**31 - 1:
    bork("timestamp is negative")

try:
    author.decode('ascii')
except UnicodeDecodeError:
    bork('string is not valid ascii')
    
if scount == 0:
    bork("section count <= 0")

#print the header
print '--------HEADER---------'

print 'magic:\t\t0x%x' % ( magic,)
print 'version:\t%d' % (version,)
print 'timestamp:\t0x%x' % (timestamp,)
print 'author:\t\t%s' % (author,)
print 'scount:\t\t%d' % (scount,)



for section in infcount():
    try:
        stype, slen  = read(*WORD), read(*WORD)
        print 'section: %d, stype: %s' % (section, lookup[stype]), '\n-----------------------------\n'

        if stype == SECTION_PNG:
            with open('section_%d.png' % (section,), 'wb') as image:
                image.write(str(PNG_MAGIC + read(*STRING(slen))))
            vals = 'Printing Image!'


        elif stype == SECTION_DWORDS:
            vals = [read(*DWORD) for dword in xrange(slen/8)] 
        elif stype == SECTION_UTF8:
            try:
                vals = unicode(read(*STRING(slen)), 'utf-8')
            except (UnicodeDecodeError,UnicodeEncodeError):
                bork('invalide utf-8 string')
        elif stype == SECTION_DOUBLES:
            vals = [read(*DOUBLE) for double in xrange(slen/8)]
        elif stype == SECTION_WORDS:
            vals = [read(*WORD) for word in xrange(slen/4)]
        elif stype == SECTION_COORD:
            if slen != 16:
                bork('incorrect slen for a coord section')
            vals = [read(*DOUBLE), read(*DOUBLE)]
        elif stype == SECTION_REFERENCE:
            if slen != 4:
                bork('incorrect slen for a reference section')
            vals = read(*WORD)
            if vals not in range(scount):
                bork('invalid svalue for the given range')
        elif stype == SECTION_ASCII:
            vals = read(*STRING(slen))
        else:
            bork ('not a valid type')

        print vals
    except (struct.error, IndexError):
        break
