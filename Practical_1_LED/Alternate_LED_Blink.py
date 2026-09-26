# ==========================================================
# Program Name : Alternate LED Blink
#
# Description:
# This program blinks LEDs in alternating pairs.
# LEDs 1 and 3 turn ON together while LEDs 2 and 4 remain OFF.
# Then LEDs 2 and 4 turn ON while LEDs 1 and 3 turn OFF.
# The pattern repeats for the number of cycles entered
# by the user.
#
# LEDs Used:
# LED1 - Pin 11
# LED2 - Pin 13
# LED3 - Pin 15
# LED4 - Pin 16
# ==========================================================
import RPi.GPIO as GPIO
import time

numTimes = int(input("Enter total cycles: "))
speed = float(input("Enter delay: "))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

for i in range(numTimes):

    GPIO.output(11, True)
    GPIO.output(15, True)

    GPIO.output(13, False)
    GPIO.output(16, False)

    time.sleep(speed)

    GPIO.output(11, False)
    GPIO.output(15, False)

    GPIO.output(13, True)
    GPIO.output(16, True)

    time.sleep(speed)

GPIO.cleanup()
print("Done")
