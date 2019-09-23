#!/usr/bin/python3.7

# A simple Python application for controlling a relay board from a Raspberry Pi
# The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# The relay is connected to one of the Pi's GPIO ports, then is defined as an Output device
# in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

__author__ =  "oguzhanlarca"
__email__ =   "cu.oguzhan@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-09-17"
__doc__ =     "Class to operate at least 1 relay"

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

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 21

# create a relay object.
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay = OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

def set_relay(status):
    if status:
        print(time, "## Role durumu: ACIK")
        relay.on()
    else:
        print(time, "## Role durumu: KAPALI")
        relay.off()

def main_loop():
    # start by turning the relay off
    # but it seems turning the relay ON wtf?
    set_relay(False)
    print(time, "## Role durumu degisti..")
    sleep(1)
    sys.exit(0)

if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
       # turn the relay off
        print("\n", time, "## Keyboard Interrupt Signal Detected !")
        set_relay(False)
        print(time, "## Exiting application\n")
        # exit the application
        sys.exit(0)
