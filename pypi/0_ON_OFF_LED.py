#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

gbp_11 = 11 # GPIO.BOARD pin 11 with 3.3 VDC pin 1
gbp_8 = 8 # TxD pin 8

def setup():
    print(' ')
    GPIO.setmode(GPIO.BOARD)       	# Numbers GPIOs by physical location
    GPIO.setup(gbp_11, GPIO.OUT)   	# Set gbp_11 mode is output
    GPIO.output(gbp_11, GPIO.HIGH) 	# Set gbp_11 high(+3.3V) to off led
    GPIO.setup(gbp_8, GPIO.OUT)   	# Set gbp_8 mode is output
    GPIO.output(gbp_8, GPIO.HIGH) 	# Set gbp_8 high(+3.3V) to off led

def online():
    #while True:
    print('\n[WHITE ON  | RED OFF]')
    GPIO.output(gbp_11, GPIO.LOW) # Led on
    GPIO.output(gbp_8, GPIO.LOW) # Led OFF

def offline():
    print('[WHITE OFF | RED ON]')
    GPIO.output(gbp_11, GPIO.HIGH) # Led off
    GPIO.output(gbp_8, GPIO.HIGH) # Led ON

def destroy():
    GPIO.output(gbp_11, GPIO.HIGH) # Turn off
    GPIO.output(gbp_8, GPIO.LOW) # Turn off
    GPIO.cleanup()
    
def main():
	setup()
	online()
	time.sleep(3)
	offline()
	time.sleep(3)
	destroy()
     
if __name__ == "__main__":
	main()
	print(' ')

