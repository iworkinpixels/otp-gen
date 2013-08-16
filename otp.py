#!/usr/bin/python
#
# OTP (or any other text file) printer.  Push the button to
# print another copy of the file.

from __future__ import print_function
import RPi.GPIO as GPIO
import sys, os, random, getopt, re
import subprocess, time, Image, socket
from Adafruit_Thermal import *

ledPin       = 18
buttonPin    = 23
holdTime     = 2     # Duration for button hold (shutdown)
tapTime      = 0.01  # Debounce time for button taps
printer      = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
printer.setLineHeight(23) # So graphical chars fit together

# Called when button is briefly tapped.  Prints one copy of the OTP.
def tap():
  GPIO.output(ledPin, GPIO.HIGH)  # LED on while working
  otp = file("/ramdisk/otp.txt")
  printer.feed(3)
  for line in otp:
    printer.println(line)  
  printer.feed(3)
  file.close(otp)
  GPIO.output(ledPin, GPIO.LOW)

# Called when button is held down.  Invokes shutdown process.
def hold():
  GPIO.output(ledPin, GPIO.HIGH)
  subprocess.call(["shutdown", "-h", "now"])
  GPIO.output(ledPin, GPIO.LOW)

# Initialization

# Use Broadcom pin numbers (not Raspberry Pi pin numbers) for GPIO
GPIO.setmode(GPIO.BCM)

# Enable LED and button (w/pull-up on latter)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED on while working
GPIO.output(ledPin, GPIO.HIGH)

# Processor load is heavy at startup; wait a moment to avoid
# stalling during greeting.
time.sleep(30)

# Show IP address (if network is available)
try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        printer.println('My IP address is ' + s.getsockname()[0])
        printer.boldOn()
        printer.println('Why am I on a network?!')
        printer.boldOff()
        printer.feed(3)
except:
        printer.boldOn()
        printer.println('Network is unreachable. Good.')
        printer.boldOff()
        printer.feed(3)

printer.println('Press the button once for each')
printer.println('copy of the keying materials.')
printer.println('Then, securely erase everything.')

# Print greeting image
printer.printImage(Image.open('gfx/hello.png'), True)
printer.feed(3)
GPIO.output(ledPin, GPIO.LOW)

# Poll initial button state and time
prevButtonState = GPIO.input(buttonPin)
prevTime        = time.time()
tapEnable       = False
holdEnable      = False

# Main loop
while(True):
  # Poll current button state and time
  buttonState = GPIO.input(buttonPin)
  t           = time.time()

  # Has button state changed?
  if buttonState != prevButtonState:
    prevButtonState = buttonState   # Yes, save new state/time
    prevTime        = t
  else:                             # Button state unchanged
    if (t - prevTime) >= holdTime:  # Button held more than 'holdTime'?
      # Yes it has.  Is the hold action as-yet untriggered?
      if holdEnable == True:        # Yep!
        hold()                      # Perform hold action (usu. shutdown)
        holdEnable = False          # 1 shot...don't repeat hold action
        tapEnable  = False          # Don't do tap action on release
    elif (t - prevTime) >= tapTime: # Not holdTime.  tapTime elapsed?
      # Yes.  Debounced press or release...
      if buttonState == True:       # Button released?
        if tapEnable == True:       # Ignore if prior hold()
          tap()                     # Tap triggered (button released)
          tapEnable  = False        # Disable tap and hold
          holdEnable = False
      else:                         # Button pressed
        tapEnable  = True           # Enable tap and hold actions
        holdEnable = True

  # LED blinks while idle, for a brief interval every 2 seconds.
  # Pin 18 is PWM-capable and a "sleep throb" would be nice, but
  # the PWM-related library is a hassle for average users to install
  # right now.  Might return to this later when it's more accessible.
  if ((int(t) & 1) == 0) and ((t - int(t)) < 0.15):
    GPIO.output(ledPin, GPIO.HIGH)
  else:
    GPIO.output(ledPin, GPIO.LOW)
