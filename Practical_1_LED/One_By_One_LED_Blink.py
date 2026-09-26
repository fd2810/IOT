# ==========================================================
# Program Name : One By One LED Blink
#
# Description:
# This program blinks four LEDs one after another.
# Each LED turns ON individually, waits for the specified
# delay, then turns OFF before the next LED starts blinking.
# The sequence repeats for the number of cycles entered
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
    time.sleep(speed)
    GPIO.output(11, False)

    GPIO.output(13, True)
    time.sleep(speed)
    GPIO.output(13, False)

    GPIO.output(15, True)
    time.sleep(speed)
    GPIO.output(15, False)

    GPIO.output(16, True)
    time.sleep(speed)
    GPIO.output(16, False)

GPIO.cleanup()
print("Done")
