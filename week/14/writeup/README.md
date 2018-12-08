Writeup 10 - Crypto II
=====

Name: Alexander Brassel
Section: 0401

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Alexander Brassel

## Assignment 10 Writeup

### Part 1 (70 Pts)

At first I thought that I might be able to exploit some vulnerable PHP.  However, I soon realized that the weakness was not properly sanitizing the SQL input (the hint on the project page helped a lot with that).  I switched tracks, then, and started working on crafting a payload to exploit improper sanitization.  I recognized that the GET request ?id=<num> probably looked something like "get * from * where id='num'" in the back-end.  Therefore, if I used something like "0' or '1=1", then the query would be replaced with "get * from * where id='0' or '1=1'", which would produce all possible pages.  It worked like a charm, and I got the following flag:
CMSC38R-{y0U-are_the_5ql_n1nja}


### Part 2 (30 Pts)

For the first level, I tried sticking in some HTML source code and I noticed that it modified the source of the document.  Therefore, it stood to reason that I could break out of the tag and call a script.  I did this using "h1> <script> alert(); </script>".

For the second level, I had to learn how to embed javascript in images.  I actually accomplished this level by creating a malicious link and clicking on it.  I did this using <a href="javascript:alert()"> test </a>.

For the third level, I looked at the source code because I was stuck.  I saw there that I could modify /static/level3/cloud generation line.  I broke out of src using ', then added an onclick to produce an alert when clicked.  I did this using 3' onclick='alert()';

For the fourth level, I had a lot of issue on figuring out how to break out since I'm not a web developer and not very familiar with what this stuff looks like on the back end.  I figured out that I could use a ') to break out of the call and then call my own code before resuming to catch the trailing input.  I did t his using 3""');alert();('.

For the fifth level, I noticed taht the thing that you put in the encoded GET request became the content of the next link that you would try to advance to.  I took advantage of this by replacing the next link with an alert instead.  javascript:alert().

Finally, I figured out what to do with this, but was unable to get it working due to some unknown error not relating to my comprehension.  I generated a webpage at "cs.umd.edu/~abrassel/cmsc389r" which contains the text "alert();".  I then circumvented the filter by capitalizing an arbitrary letter in http.  However, it was unable to recognize the page for some reason (I promise that it exists).
