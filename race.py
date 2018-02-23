#!/usr/bin/python

# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import RPi.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment
import time
import datetime

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(29, GPIO.IN)

# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()

# Initialize the display. Must be called once before using the display.
display.begin()

# Keep track of the colon being turned on or off.
colon = False

# Run through different number printing examples.
print('Press Ctrl-C to quit.')

running = 0 
while(True):
  LEDStart = GPIO.input(12)
  LEDStop1 = GPIO.input(13)
  LEDStop2= GPIO.input(15)
  print LEDStart,LEDStop1,LEDStop2

  if running == 0 :
    if LEDStart == 0 :
      running = 1
      starttime = datetime.datetime.now()
    else :
      continue
  else :
    if LEDStop1 == 1 or LEDStop2 == 1 :
      running = 0
      continue

  t1 = datetime.datetime.now()
  display.clear()
  diff = t1-starttime
  print diff

  temp = diff.seconds+diff.microseconds/1000000.0
  print temp 
  # Print a floating point number to the display.
  display.print_float(temp, decimal_digits=3)
  display.write_display()
  time.sleep(0.1)
