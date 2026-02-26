import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

led = 26                    # светодиод
status = False
lightLed = 6
timeSleep = 1

GPIO.setup( led, GPIO.OUT )
GPIO.setup( lightLed, GPIO.IN )

while True:
    if not GPIO.input( lightLed ):
        status = not status
        GPIO.output( led, status )
        time.sleep( timeSleep )