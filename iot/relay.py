#!/usr/bin/python3.7

# A simple Python application for controlling a relay board from a Raspberry Pi

__author__ =  "Oguzhan Ince"
__email__ =   "cu.oguzhan@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-09-17"
__doc__ =     "Class to operate at least 3 relays"

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
    print(time, "## Dis kapi acildi.")
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
