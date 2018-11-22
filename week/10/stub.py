#!/usr/bin/env python2
# from the git repo
import md5py
from socket import socket

host = '142.93.118.186'
port = 1234

s = socket()
s.connect((host, port))
#####################################
### STEP 1: Calculate forged hash ###
#####################################

message = 'test'    # original message here

s.recv(1024)
s.send('1\n')
s.recv(1024)
s.send(message + '\n')

legit = s.recv(1024).split(': ')[2].strip()      # a legit hash of secret + message goes here, obtained from signing a message

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'the cake is a lie'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(legit)
print(fake_hash)

def test(string):
    if 'let me see' in string:
        print '\n'.join(string.split('\n')[2:7]), '\n\n\n'


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
padding = '\\x80' # trailing 1
length  = '\\x20' # length of 'test'


# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
pre_padding_length = 64 - 1 - 1 - len(message)
#for i in range(pre_padding_length-6, pre_padding_length-16, -1):
for i in range(0, 64):
    payload = message + padding + length + malicious

    # send `fake_hash` and `payload` to server (manually or with sockets)
    # REMEMBER: every time you sign new data, you will regenerate a new secret!
    test(s.recv(1024))
    s.send('2\n')
    test(s.recv(1024))
    s.send(fake_hash + '\n')
    test(s.recv(1024))
    s.send(payload + '\n')
    padding += '\\x00'

