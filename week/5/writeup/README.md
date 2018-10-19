Writeup 5 - Binaries I
======

Name: Alexander Brassel
Section: 0401

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Alexander Brassel

## Assignment 5 Writeup

Let's start from the beginning - the best part, if the Star Wars franchise is anything to go by.  I began with the memset function as it's easier and I wanted to get a feel for assembly coding, particularly with intel syntax.

First, I treated it as an abstract problem - what's the general process?  Make a for loop and add to each position.  I've taken 216, I know that I can do this.  So I looked up the syntax for conditional jumps and moving and arithmetic operations and kind of mentally formed a thought on how I might go about doing this.

Then, I took a look at the hint and decided that it couldn't hurt to look up the instructions given.  Lo and behold, rep stosb seemed to magically do what I wanted - copy a byte, move to the next byte in dest, and copy there.  However, I wasn't really sure how to give it arguments.

I asked on Piazza after a couple of internet searches didn't seem to yield anything too useful.  I suppose that in a real life situation you could look up the documentation again as I did later, assuming that you were more comfortable with assembly.  I found that I just needed to set my registers appropriately in order for the stosb call to have access to them.

In order to do this, I moved the registers into the appropriate locations (see my attached code for an example of me doing this), then executed rep stosb, which runs until ecx contains 0, which I accomplished by moving rdx into rcx.

Two issues presented themselves during this step.  The first issue was "how do I match the size of the values stored?"  In order to do this, I used the lowest bits of the rdi rsi register and copied them into the byte operand (al) for stosb only.

Next, the more pressing question - how do I find my input arguments?  I found by searching through the slides that there were a pre-defined set of registers that correspond with specific input arguments.  I simply picked the right ones and re-arranged them as necessary to fit the rep stosb function.

Next, I moved to my_strncpy.  This one I knew I couldn't use rep for, because I needed to move the current byte being copyied at each stage, but I knew that stosb would probably still be useful.  I took a look at the loop command - when does it terminate?  When rcx is 0.  great - I can copy the count into that register, no problem.

Next, how do i do the copy operation at each step of the loop?  Well the logical solution would be to get the offset start - current_countdown.  I was stuck on this for a while, since yasm throws a pretty inscrutable error about an effective invalid address.  My first thought was that I had used incorrect syntax for addressing, so I spent quite a while trawling the web, trying to find the correct way to write an offset dereference.  Then, I found that there was a much simpler problem - offset addressing appears not to permit subtraction.  Ok, fine.  I added a second register that counted up as the other counted down.

Finally, now that I'm done, I have to double check to make sure that I've obeyed x86 rules.  I checked the slide about which variables you can and can't clobber and verified that none of the registers I had (ab)used were the reserved ones.  Done!