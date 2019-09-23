#!/usr/bin/python3.7

# A simple Python application for controlling a relay board from a Raspberry Pi
# The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# The relay is connected to one of the Pi's GPIO ports, then is defined as an Output device
# in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

__author__ =  "Oguzhan Ince"
__email__ =   "cu.oguzhan@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-09-17"
__doc__ =     "Class to operate at least 3 relays"

# Useful documentation:
# https://gpiozero.readthedocs.io/en/stable/installing.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/api_output.html
# https://gpiozero.readthedocs.io/en/stable/api_input.html

# Replacement code if GPIOzero doesn't work...
# https://www.adafruit.com/product/2348
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/circuitpython-raspi
# https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi

import os
import sys

from datetime import date
from datetime import datetime
from gpiozero import LED
from gpiozero import Button
from gpiozero import OutputDevice

from signal import pause
from time import sleep

time = datetime.now()

red = LED(8)
blue = LED(7)
white = LED(20)

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 21

# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay = OutputDevice(RELAY_PIN, active_high=False, initial_value=False)


red_button = Button(16)
blue_button = Button(3)
bell_button = Button(2)

def countdown(x):
    if x == 0:
        print(time, "Done!")
        return
    else:
        print(time, x, "...")
        sleep(1)
        countdown(x-1)


def doorbell():
    # TO-DO:
    # When the door bell button push: led blinks until door relay goes on
    print(time, "## Door [Bell] button pressed!")
    # then toggle the relay every second until the app closes
    toggle_relay()   
    white.off()
    sleep(1)
    
    toggle_relay()
    white.on()
    sleep(1)
    
    toggle_relay()
    white.off()
    sleep(1)
    
    toggle_relay()
    white.on()
    sleep(1)
   
    toggle_relay()
    white.off()
    sleep(1)

def shutdown():
    print(time, "## Red [ON/OFF] button pressed!")
    sleep(1)
    os.system('shutdown --poweroff --no-wall')
    countdown(59)

def reboot():
    print(time, "## Blue [Restart] button pressed!")
    sleep(1)
    countdown(3)
    os.system("shutdown --reboot --no-wall now")

def set_relay(status):
    if status:
        print(time, "## Setting relay: ON")
        relay.on()
    else:
        print(time, "## Setting relay: OFF")
        relay.off()

def toggle_relay():
    print(time, "## Toggling relay")
    relay.toggle()


def main_loop():
    # start by turning the relay off
    set_relay(False) #
    
    red.on()   #on/off led 
    blue.on()  #restart led
    white.on() #doorbell led
    
    while True:
        if blue_button.is_pressed:
            reboot()

        if red_button.is_pressed:
            shutdown()

        if bell_button.is_pressed:
            doorbell()

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # turn the leds off
        red.off()
        blue.off()
        white.off()
        # turn the relay off
        print("\n", time, "## Keyboard Interrupt Signal Detected !")
        set_relay(False)
        print(time, "## Exiting application\n")
        # exit the application
        sys.exit(0)
