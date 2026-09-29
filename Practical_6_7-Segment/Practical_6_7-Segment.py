# TM Board Pin     GPIO pin
# -------------------------
# VCC      ----->  Pin 4-5v
# GND      ----->  Pin 14-GND
# D10      ----->  Pin 18-GPIO 24
# CLK      ----->  Pin 16-GPIO-23
#Step 1: Open the terminal and enter the following command.
#pip install RPi.GPIO --break-system-packages
#https://github.com/bhoomikapansare/7Segment.git
import sys
import time
import datetime
import RPi.GPIO as GPIO
import tml1637
GPIO.setmode(GPIO.BCM)  # or GPIO.BOARD depending on your wiring
Display = tml1637.TM1637()
Display.Clear()
Display.SetBrightness(1)
while True:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    currenttime = [int(hour / 10), hour % 10, int(minute / 10), minute % 10]
    Display.Show(currenttime)
    Display.ShowDoublepoint(second % 2)
    time.sleep(1)
    
# Practical no 2 Pi Camera 
#1. sudo raspi-config
#2. sudo reboot
#3. libcamera-hello
#4. for image: libcamera-still -o image.jpg
#5. for video: libcamera-vid -o video.h264 -t 10000

