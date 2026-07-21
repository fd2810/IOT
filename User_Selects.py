import RPi.GPIO as GPIO
import time

led = int(input("Enter LED number (1-4): "))
numTimes = int(input("Enter number of blinks: "))
speed = float(input("Enter delay: "))

pins = {
    1: 11,
    2: 13,
    3: 15,
    4: 16
}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)

selected = pins[led]

for i in range(numTimes):
    GPIO.output(selected, True)
    time.sleep(speed)
    GPIO.output(selected, False)
    time.sleep(speed)

GPIO.cleanup()
print("Done")
