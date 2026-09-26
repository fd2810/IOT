# ====================================================================
# PRACTICAL - 3
# Controlling Raspberry Pi with Telegram.
# ====================================================================
#
# Step 1: Open Telegram app in your system or mobile
# Open Telegram app in your system or mobile
# Start "BotFather"
#
# Step 2: Open "BotFather"
#
# STEP 3: /start
#
# STEP 4 Create a new Bot
#
# STEP 5:- Obtain access token
#
# STEP 6:- Install "Python Package Index"
# sudo apt-get install python-pip
#
# STEP 7:- Install "telepot"
# (To download telepot create a virtual environment)
#
# 1) Installing the venv module:-
#    sudo apt install python3-venv
#
# 2) Creating a new virtual environment. Myenv is user-defined name
#    python3 -m venv myenv
#
# 3) Activate the Virtual Environment
#    source myenv/bin/activate
#
# 4) It should look like :- (myenv) pi@raspberrypi:- $
#
# 5) Install telepot in virtual machine:-
#    pip install telepot
#
# 6) pip install RPi.GPIO
#
# STEP 8:-
# 1) Paste the bot token here
#    bot = telepot.Bot('your_bot_token')
#
# 2) Run the Code
#    python telegrambot.py
#
# STEP 9:- All set, now time to connect the Pi and LED.
# Connect LED to Pi
# (LED connected to GPIO pin 11 - BOARD mode)
#
# Step 10: Send Command
# Start our Bot
# Send "on" and "off"
# Look at your Pi, you can see the LED on and off when you send "on" and "off" to our bot.
#
# STEP 11:- To deactivate virtual environment
# deactivate
#
# --------------------------------------------------------------------
# Code:
# (This code will be displayed after the command:- nano telegrambot.py)
# --------------------------------------------------------------------

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == 'on':
       bot.sendMessage(chat_id, on(11))
    elif command =='off':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('Bot Token')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
