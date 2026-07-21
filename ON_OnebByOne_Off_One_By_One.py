import RPi.GPIO as GPIO
import time

numTimes = int(input("Enter total cycles: "))
speed = float(input("Enter delay: "))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

leds = [11, 13, 15, 16]

for led in leds:
    GPIO.setup(led, GPIO.OUT)

for i in range(numTimes):

    # Turn ON one by one
    for led in leds:
        GPIO.output(led, True)
        time.sleep(speed)

    # Turn OFF one by one
    for led in leds:
        GPIO.output(led, False)
        time.sleep(speed)

GPIO.cleanup()
print("Done")
