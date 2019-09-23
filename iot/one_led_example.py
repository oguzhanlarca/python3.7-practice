#!/usr/bin/env python3.7

# This example is worse than c pi libs.
# You should work with gpiozero...

__author__ =  "oguzhanlarca"
__email__ =   "cu.oguzhan@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-09-21"

import RPi.GPIO as GPIO
import time

LedPin = 11  # pin11

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)  # Set LedPin high(+3.3V) to off led

colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00,
          0x00FFFF, 0xFF00FF, 0xFFFFFF, 0x9400D3]

pins = {'pin_R': 11, 'pin_G': 12, 'pin_B': 13}  # pins is a dict

for i in pins:
        GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
        GPIO.output(pins[i], GPIO.HIGH)  # Set pins to high(+3.3V) to off led
        
p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)
p_B = GPIO.PWM(pins['pin_B'], 2000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)
p_B.start(0) 

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)  # led off
    p_R.stop()
    p_G.stop()
    p_B.stop()
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
        GPIO.cleanup()
    GPIO.cleanup()
    if __name__ == '__main__':
        setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
 
def setColor(col):   # For example : col = 0x112233
    R_val = (col & 0x110000) >> 16
    G_val = (col & 0x001100) >> 8
    B_val = (col & 0x000011) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
    p_G.ChangeDutyCycle(100-G_val)
    p_B.ChangeDutyCycle(100-B_val)


try:
    while True:
        for col in colors:
            setColor(col)
            time.sleep(1.0)
except KeyboardInterrupt:
        destroy()
        

def loop():
    print(' ')
    while True:
        print('\n[ON]')
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(3)
        print('[OFF]')
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(3)
   
loop()

