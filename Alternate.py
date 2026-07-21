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
