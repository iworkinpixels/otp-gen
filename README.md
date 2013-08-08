OTP Gen
===============================

This is a one time pad generator powered by the hrng in the raspberry pi, made to work on the Adafruit Internet of Things thermal printer kit.  Enjoy, but remember that even if you receive further notice to the contrary,
**THIS IS NOT SECURE**.

The security of one time pads is completely dependent on you having total physical control over all copies of the pad at all times.  If you could do that, you would just hand messages to each other and call it a day.  As it is, if anyone wants into your messages bad enough, they will go beat up one of your dudes immediately after the secure courrier drops off his copies of the pads, and then pretend to be him for as long as it takes for someone else in the network to make the mistake of messaging him.

That having been said, I have done everything in my power to ensure that the pads are actually random, and that they are never used twice, so it should be a good learning exercise to see what I missed.

This is meant as an excuse to get people excited (and knowledgable) about cryptography.  

As always, pull requests are welcome if you'd like to take a crack at hardening this script (and the pi that it runs on) to make it more secure.

TODO:
* File Deletion:  What's a good way to securely delete a file which resides on a micro SD card? (or should you burn your SD card after use?) [Here](http://www.cyberciti.biz/tips/linux-how-to-delete-file-securely.html) are some ideas.
* Deployment:  If you're going to burn your SD card after use, this would be better as an image file that you could write to your SD card, plug it in, and go.
* Secure RAM: Does python have the ability to lock memory to keep it from being written to disk?
* Documentation: It would be cool if this script would print instructions for how to operate a one time pad on startup, and perhaps a vigenere table as well.
