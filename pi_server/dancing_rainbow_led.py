#!/usr/bin/python

import RPi.GPIO as GPIO
import time


# No buzzer function yet
def main():
    red = 4
    green = 23
    blue = 24
    buzzer = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    GPIO.setup(blue, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)

    GPIO.output(red, False)
    GPIO.output(green, False)
    GPIO.output(blue, False)
    GPIO.output(buzzer, False)
    for _ in range(5):
        GPIO.output(red, True)
        time.sleep(.2)
        GPIO.output(green, True)
        time.sleep(.2)
        GPIO.output(red, False)
        time.sleep(.2)
        GPIO.output(blue, True)
        time.sleep(.2)
        GPIO.output(green, False)
        time.sleep(.2)
        GPIO.output(red, True)
        time.sleep(.2)
        GPIO.output(blue, False)
        GPIO.output(red, False)
    GPIO.output(blue, False)
    GPIO.output(red, False)
    GPIO.output(green, False)
    GPIO.output(buzzer, False)


try:
    if __name__ == '__main__':
        main()
finally:
    GPIO.cleanup()
