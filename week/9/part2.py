#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import re

parser = re.compile("Find me the (\w+) hash of (\w+)")

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while True:
    data = s.recv(1024)
    is_match = parser.search(data)

    if not is_match:
        print data
        break
    hash_type, target = is_match.groups()

    guess = getattr(hashlib, hash_type)(target).hexdigest()
    s.send(guess + '\n')

# close the connection
s.close()
