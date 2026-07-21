import RPi.GPIO as GPIO
import time

numTimes = int(input("Enter total number of blinks: "))
speed = float(input("Enter delay in seconds: "))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

leds = [11, 13, 15, 16]

for led in leds:
    GPIO.setup(led, GPIO.OUT)

for i in range(numTimes):
    print("Iteration", i + 1)

    for led in leds:
        GPIO.output(led, True)

    time.sleep(speed)

    for led in leds:
        GPIO.output(led, False)

    time.sleep(speed)

GPIO.cleanup()
print("Done")
