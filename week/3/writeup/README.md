Writeup 3 - OSINT II, OpSec and RE
======

Name: Alexander Brassel
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Alexander Brassel

## Assignment 3 Writeup

### Part 1 (100 pts)

Dear Mr Krueger,

We've identified three separate security lapses that allowed us to gain access to your server.  Please find our writeup on the aforementioned errors attached below.

The first and most immediate security vulnerability is the apparent lack of protection against port scanning from outside parties.  This is an issue because attackers are able to use tools such as "nmap" to determine which ports are open and available for attack.  It's difficult to defend against such attacks, since you cannot prevent a 3rd party user from trying a port to see if it is open without incurring other undesirable consequences.  However, many antiviruses can detect such attacks in real time.  For example, you can see an example of this feature working so well on Bitdefender that a user is actually having to tone it down. https://security.stackexchange.com/questions/74584/port-scan-detected-and-blocked-bitdefender-2014

The second vulnerability we were able to exploit is the combination of your exceptionally weak password in conjuction with lax social media presence.  The issue with the server password is two-fold.  First, it is listed on common databases (such as Rock You) that keep records of commonly used passwords.  You are advised to avoid the use of such passwords because, despite them being easy to remember, they essentially put you on the short list of easily crackable accounts.  To compound matters, it's advised to not use passwords that are heavily related to your interests.  For example, your Instagram account is largely concerned with pokemon, which might incentize a hacker to use a pokemon related password dictionary, which would result in your password being cracked in seconds.  The simultaneous resolution to both of these problems is to use a password manager such as [LastPass](https://www.lastpass.com/business-password-manager).  A password manager generates cryptographically secure login credentials and spares you the trouble of having to remember them.  This could be of great use to you.

Finally, the third vulnerability is your lack of rate limiting on incoming brute force attacks.  Most common devices that you see or use - such as smartphones - have an increasing delay between allowed login attempts.  This prevents brute force attacks by making them increasingly time consuming.  [Fail2Ban](https://en.wikipedia.org/wiki/Fail2ban) is a good resource for this.

Let me know if you would like any additional assistance on protecting your site!

Best,
Alex