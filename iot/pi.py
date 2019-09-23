#!/usr/bin/python3.7

# The application uses the GPIO Zero library (https://gpiozero.readthedocs.io/en/stable/)
# in GPIO Zero: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

__author__ =  "oguzhanlarca"
__email__ =   "cu.oguzhan@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-09-21"

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

#red_button = Button(16)
#blue_button = Button(3)
bell_button = Button(2)

#def countdown(x):
#    if x == 0:
#        print(time, "## Done!")
#        return
#    else:
#        print(time,"## ", x,)
#        sleep(1)
#        countdown(x-1)


def doorbell():
    # TO-DO:
    # When the door bell button push: led blinks until door relay goes on
    print(time, "## Bell button pressed!")
   
    white.on()
    sleep(1)

    white.off()
    sleep(1)

    white.on()
    sleep(1)
   
    white.off()
    sleep(1)

#def shutdown():
#    print(time, "## Red [ON/OFF] button pressed!")
#    sleep(1)
#    os.system('shutdown --poweroff --no-wall')
#    countdown(59)

#def reboot():
#    print(time, "## Blue [Restart] button pressed!")
#    sleep(1)
#    countdown(3)
#    os.system("shutdown --reboot --no-wall now")

def main_loop():   
    red.on()   #on/off led 
    blue.on()  #restart led
    white.on() #doorbell led
    
    while True:
#        if blue_button.is_pressed:
#            reboot()

#        if red_button.is_pressed:
#            shutdown()

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

        print("\n", time, "## Keyboard Interrupt Signal Detected !")

        print(time, "## Exiting application\n")
        # exit the application
        sys.exit(0)
