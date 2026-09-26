# ==========================================================
# Program Name : Dual LED Blink
#
# Description:
# This program blinks two LEDs connected to Raspberry Pi
# GPIO pins simultaneously. Both LEDs turn ON together,
# stay ON for the specified delay, then turn OFF together.
# This process repeats for the number of cycles entered
# by the user.
# ==========================================================
import RPi.GPIO as GPIO
import time

# Get user input
numTimes = int(input("Enter total number of blinks: "))
speed = float(input("Enter delay in seconds: "))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Setup LEDs
GPIO.setup(11, GPIO.OUT)   # LED1
GPIO.setup(13, GPIO.OUT)   # LED2
GPIO.setup(15, GPIO.OUT)   # LED3
GPIO.setup(16, GPIO.OUT)   # LED4

def Blink(numTimes, speed):

    for i in range(numTimes):
        print("Iteration", i + 1)

        GPIO.output(11, True)
        GPIO.output(13, True)
        GPIO.output(15, True)
        GPIO.output(16, True)

        time.sleep(speed)

        GPIO.output(11, False)
        GPIO.output(13, False)
        GPIO.output(15, False)
        GPIO.output(16, False)

        time.sleep(speed)

Blink(numTimes, speed)

GPIO.cleanup()
print("Done")
