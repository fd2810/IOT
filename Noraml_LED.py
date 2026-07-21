import RPi.GPIO as GPIO
import time

# Get user input
numTimes = int(input(&quot;Enter total number of times to blink: &quot;))
speed = float(input(&quot;Enter length of each blink (seconds): &quot;))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # Using physical pin numbers

# Setup GPIO pins for output
GPIO.setup(11, GPIO.OUT) # LED1
GPIO.setup(13, GPIO.OUT) # LED2
def Blink(numTimes, speed):

for i in range(numTimes):
  print(&quot;Iteration&quot;, i + 1)
  GPIO.output(11, True) # LED1 ON
  GPIO.output(13, True) # LED2 ON
  time.sleep(speed)
  GPIO.output(11, False) # LED1 OFF
  GPIO.output(13, False) # LED2 OFF
  time.sleep(speed)
Blink(numTimes, speed)
GPIO.cleanup()
print(&quot;Done&quot;)
