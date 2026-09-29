# GND - 6, VCC - 2, IN1 - 26, IN2 - 24, IN3 - 21, IN4 - 22

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

relay_pin1 = 26
relay_pin2 = 24
relay_pin3 = 21
relay_pin4 = 22

GPIO.setup(relay_pin1, GPIO.OUT)
GPIO.setup(relay_pin2, GPIO.OUT)
GPIO.setup(relay_pin3, GPIO.OUT)
GPIO.setup(relay_pin4, GPIO.OUT)

GPIO.output(relay_pin1, 1)
GPIO.output(relay_pin2, 1)
GPIO.output(relay_pin3, 1)
GPIO.output(relay_pin4, 1)

try:
    while True:
        GPIO.output(relay_pin1, 0)
        sleep(5)
        GPIO.output(relay_pin1, 1)

        GPIO.output(relay_pin2, 0)
        sleep(5)
        GPIO.output(relay_pin2, 1)

        GPIO.output(relay_pin3, 0)
        sleep(5)
        GPIO.output(relay_pin3, 1)

        GPIO.output(relay_pin4, 0)
        sleep(5)
        GPIO.output(relay_pin4, 1)

except KeyboardInterrupt:
    GPIO.cleanup()