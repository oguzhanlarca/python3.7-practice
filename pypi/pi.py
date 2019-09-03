import os

from gpiozero import LED
from gpiozero import Button
from signal import pause
from time import sleep

red = LED(8)
blue = LED(7)

red_button = Button(3)
blue_button = Button(2)


def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        sleep(1)
        countdown(x-1)


def controll():
    red.on()
    blue.on()

    while True:
        if red_button.is_pressed:
            print("Red [ON/OFF] button pressed!")
            sleep(2)
            os.system('shutdown --poweroff --no-wall')
            countdown(59)
            #break

        if blue_button.is_pressed:
            print("Blue [Restart] button pressed!")
            sleep(2)
            os.system('shutdown --reboot --no-wall now')
            #break

#    red_button.wait_for_press()
#    print("Button is pressed")
#    sleep(1)
#    os.system('clear')


controll()
#pause()
