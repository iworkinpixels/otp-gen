OTP Gen
===============================

This is a one time pad generator powered by the hardware random number generator in the raspberry pi, made to work on the Adafruit Internet of Things thermal printer kit.  Enjoy, but remember that even if you receive further notice to the contrary,
**THIS IS NOT SECURE**.

The one time pad algorithm means that you have to somehow securely transmit something that is (at a minimum) exactly as long as every message you ever intend to send on the network.  If you can do that, you have a secure channel.  Just sent your messages over that channel and call it a day. One time pads are mathematically completely secure, but practically they cannot be implemented in a way that can take advantage of this security.  In addition, there is no way to recover from an error, so whether there was noise in the transmission, or the enemy is bit-flipping incoming messages, you will never have any way of knowing.

That having been said, I have done everything in my power to ensure that the pads are actually random, and that they are never used twice, so it should be a good learning exercise to see what I have missed. This is meant as an excuse to get people excited (and knowledgable) about cryptography. You are responsible for all of the consequences, and your mileage may vary considerably.

There is an example one time pad included (otp.txt) if you just want to mess around with one.  It goes without saying that you should never, ever use any part of any published otp to encrypt anything that you don't want to be public.

As always, pull requests are welcome if you'd like to take a crack at hardening this script (and the pi that it runs on) to make it more secure.

TODO:
* File Deletion:  What's a good way to securely delete a file which resides on a micro SD card? (or should you burn your SD card after use?) [Here](http://www.cyberciti.biz/tips/linux-how-to-delete-file-securely.html) are some ideas.
* Deployment:  If you're going to burn your SD card after use, this would be better as an image file that you could write to your SD card, plug it in, and go.
* Secure RAM: Does python have the ability to lock memory to keep it from being written to disk?
* Documentation: It would be cool if this script would print instructions for how to operate a one time pad on startup, and perhaps a vigenere table as well.
