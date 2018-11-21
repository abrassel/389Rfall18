Writeup 7 - Forensics I
======
1. JPEG

2. John Hancock Building, Chicago, Illinois

3. 2018:08:22 11:33:24.801

4. iPhone 8 back camera 3.99mm f/1.8

5. 539.5 m above Sea Level

6. You found the hidden message! CMSC389R-{look_I_f0und_a_str1ng}
CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

Flag: Congrats! Your flag is: CMSC389R-{dropping_files_is_fun}

The first step to figuring out what the binary does is opening it up in cutter.  I was reluctant to run the binary, not because I didn't trust you guys not to bork my OS, but because theoretically running unknown binaries is a pretty bad idea.  I opened it up in cutter, jumped to the main method, and observed that there was a write to some file in /tmp/.stego.  The main method also didn't seem to be making any other significant system calls, so I went ahead and ran it.  I foudn the generated file, and tried to run "file" on it to see what the type was.  I found that the OS couldn't recognize any information in it.

My next step then was to run exif on it, same problem. exiftools, however, caught that there was some sort of problem with byte alignment.  I initially dismissed that, thinking it would be a weird problem to have assigned, and popped open gdb to see if I could intercept the variable as it was printed to the image.  Unsurprisingly, this didn't seem particularly effective, so I revisited and took another look at what I could do.

I decided that that bad byte boundary could be an issue, and ran xxd to see what the file looked like.  I referenced the Wikipedia page for signatures for a jfif file (could see those bytes in xxd), and saw that the bytes almost matched, but were off by two.  I used tail -c +2 to shift over the file appropriately, and then file was able to recognize the image as a real image.  I changed the extension and opened it, saw the dinosaur and what was obviously steganography.

I ran steghide extract on it and tried the following passwords in sequence: dinosaur, dinosuar, Dinosaur, Dinosuar, brontosaurus, stegosaurus.  Finally, I was able to get the key, and that concluded my foray into steganography.
=======
1. 

2. 

3. 

4. 

5. 

6.

### Part 2 (55 pts)

*SUBMIT YOUR WRITEUP DETAILING YOUR APPROACH AND SOLUTION TO THIS PROBLEM HERE (>250 words). Dont forget to include the flag!*
