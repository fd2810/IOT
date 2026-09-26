# ==========================================================
# Program Name : All LED Blink
#
# Description:
# This program controls four LEDs connected to the Raspberry Pi.
# All four LEDs turn ON at the same time, remain ON for the
# specified delay, and then turn OFF together. The process
# repeats for the number of blinks entered by the user.
#
# LEDs Used:
# LED1 - Pin 11
# LED2 - Pin 13
# LED3 - Pin 15
# LED4 - Pin 16
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
