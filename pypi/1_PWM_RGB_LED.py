#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gpiozero
import time

singleLED = gpiozero.PWMLED(14)
rgbLED = gpiozero.RGBLED(16, 20, 21)

# turn on the RGB LED
rgbLED.color = (1,0,0) # red
time.sleep(1)
rgbLED.color = (0,1,0) # green
time.sleep(1)
rgbLED.color = (0,0,1) # blue
time.sleep(1)
rgbLED.color = (1, 1, 1) # bright white
time.sleep(1)
rgbLED.color = (.01, .01, .01) # dim white
time.sleep(1)
rgbLED.off()

# turn on LED
singleLED.value = .01 # dim
time.sleep(1)
singleLED.value = 1 # bright
time.sleep(1)
singleLED.off()

# blink clock
import datetime
timenow = datetime.datetime.now()
rgbLED.color = (timenow.hour/24, timenow.minute/60, timenow.second/60)
singleLED.pulse(background = True) # single LED pulses the seconds

time.sleep(15)
singleLED.off()
rgbLED.off()

