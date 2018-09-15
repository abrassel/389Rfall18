##Part 1

The first step I took to learning about kruegster1990 was going over to inteltechniques and doing a username search.
I found several helpful resources.  He had posted a writeup in the UMDSEC twitsy page.  Aditionally, there was a reddit account corresponding the same handle (which was entirely empty), a tweet about cute dogs, and a link to his instagram page, as well as a link to twitter.

I was able to visit his proper twitter page and find out that his real name was Fred Kreuger (1).
Next, I attempted to uncover more information about him using wayback on his reddit page.  It didn't come up with anything interesting, so I moved on.  Next, I trowled through the instagram and twitter pages and determined that this user seems to have two interests: traveling, and pokemon.

Afterwards, I moved to the website that he had linked in his bio.  Spytox came up with a potential email at kruegster@tutanota.com, and the About page on his website confirmed that this was, indeed, his email. A quick look noted that tutanoga is a website that hosts some sort of secure emails, so I gave up there.  Also, I probably shouldn't try to hack them.

I was able to find IPs associated with the website in one of two ways.  The first way was by looking at the page under construction.  Unfortunately, the wayback machine didn't seem to return any results for this portion either so I just used the actual IP that it gave back.

The first IP address I found was 142.93.117.193.  Using nslookup, I was able to determine that the other page of his website was hosted at 142.93.118.186.  I went through the source code of the website and found the  CMSC389R-{h1dden_fl4g_in_s0urce}  flag in the source code.

Next, I decided to use the wfuzz routine to find all subdirectories and folders on each website.  On 142.93.117.193 I found the following .git repo which contains this flag: CMSC389R-{y0u_found_th3_g1t_repo}. I also was able to find the /secret file with the following flag: 
	Congrats!  Your first flag is: 
	CMSC389R-{fly_th3_sk1es_w1th_u5}.  I decided to use wget to read through the html manually.

I took a look at the headers I received when I queried the web page, and I was able to determine that their server is running Apache/2.4.18 on Ubuntu.

Finally, I decided to see what ports besides 80 were running on each of those IP addresses.  After running nmap, I was able to find several ports on 142.93.117.193, which had an EthernetIP-1, rxapi, waste, and something else that didn't look super helpful.  1942.93.118.186 only came up with ssh and html.  I took a look at the waste folder 1337 and was greeted with the login prompt. On to part 2.

##Part 2

Unfortunately, I spent quite a while going down the wrong path here.  Before I had realized that there was an open port at 1337 I developed a script that opened several different python instances with different guesses for usernames and tried to brute force the ssh using the rock you database.  This ran for like 10 to 15 minutes before I realized that there was another port open.

Then, I found the 1337 port.  Using nc, I was able to log in and play around for a second.  Then, I drew on my 417 knowledge, and modified my earlier python and bash script to run using a tcp socket instead on 1337.  I went through the rock you sheet concurrently testing with the different usernames, and was eventually able to find the "pokemon" password, "kruegster" username.  Should have guessed, considering the contents of the instagram account.

Next, I logged into the server, and browsed around looking for hidden directories briefly.  Nothing showed up, so I moved to the home directory, since presumably he'd store his files there.  Found the flight records.  Realized that every single one of them were decoy flags, so I got stuck for a bit.

Then, going on the piazza hint, I decided to browse through his social media pages again.  Going through his instagram and reading the comments, I found the page with the flight ticket number AAC27670.  This matched with the file name of one of the flag containing files, so I opened that and pasted the contents here as follows.  CMSC389R-{c0rn3rstone-air-27670}.

Use find.py <username> to run the brute forcer
