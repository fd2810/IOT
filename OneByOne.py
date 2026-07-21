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
    print("Cycle", i + 1)

    for led in leds:
        GPIO.output(led, True)
        time.sleep(speed)
        GPIO.output(led, False)

GPIO.cleanup()
print("Done")
