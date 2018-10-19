Writeup 3 - Pentesting I
======

Name: Alexander Brassel
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Alexander Brassel

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag is CMSC389R-{p1ng_as_a_$erv1c3}
I used the following sequence of inputs in order to obtain the flag.  First, I logged into the interactive prompt.  Then, I dropped into a new shell.  Once I dropped into my shell, I navigated to the home directory using "cd /home".  Then, I cat'd the contents of the flag.txt file after determining that it existed using "ls -a" (just in case the flag was hidden).

It's worth mentioning that I was also able to find the other flag on the cgi-bin/stats directory.  I've since been informed that this is worth zero additional credit, and for that, I am sad :(

in the spirit of part 1 is supposed to be asking, I'll talk about low-level implementation details of my shell.  The first thing to note is that nc'ing into cornerstoneairlines.co 45 greets you with an IP prompt.  My first question was "well, what is this supposed to do?"  So I used it to view the uptime of a local address "192.168.1.1".  It gave me information back.  Ok great.

I floundered blindly for a bit, just testing out different inputs on it.  "What if I just replaced it with a command?  No output.   What if I tried to buffer overflow it?  Nothing."  Then I decided it would probably be a good idea to look up vulnerabilities in the linux ping command.

This quickly revealed that you could append multiple commands after the input in order to execute arbitrary input on the server, thus achieving command injection.  So, I tried to print out the current directory using "192.168.1.1; ls".  It worked as expected.  I then tried without the IP address and was able to observe still valid input.  So far, so good.

Next, I tried to change the directory.  No dice - it only allowed one operation.  Ok, next step, what happens if we chain together inputs?  That worked.  So I cd'd into the home directory and printed out the contents.  I was greeted with the flag input, so I relogged and printed out the flag.

I would recommend that Fred use an OPSEC secure technology instead of the ping command.  Using "ps-aux" i was able to identify where Fred was executing the ping command from, which included an arbitrary evaluation of user input.  Using an opsec recommended approach would have solved all of the unfortunate issues he faced here.  It's also not a bad idea to password protect your network interfaces anyway.

### Part 2 (55 pts)
shell.py 

shell.py runs a state-of-the-art interfacing system with Fred's uptime measurement server.

Using this one of a kind piece of software, you can perform the following actions:

* help - view this dialogue menu
* quit - exit the interface (but why would you want to do that?)
* pull <destination> <local> - pull a file from destination to the local path
* shell - start the even more state of the art shell
* secret - additional functionality for only the most advanced users

But what's this about shell?  Wouldn't you like to know.

Shell is a fully-functioning bash-like service that allows you to fully take control of Fred's machine as a root user.  Using this sophisticated command, you can finally live out your fantasies of being the one and only Fred Krueger.  You can cat files, change directories, and even do anything that you could ever want to a *read-only* operating system.  Seriously why does he only have read privileges.

Best of luck!

To begin your spiritual awakening, run "python3 shell.py".  Careful, with great power comes great aesthetics.