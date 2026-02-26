import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

leds = [ 24, 22, 23, 27, 17, 25, 12, 16 ]
GPIO.setup( leds, 0 )

lightTime = 0.2

for led in leds:
    GPIO.output( led, True )
    time.sleep( lightTime )
    GPIO.output( led, False )

for led in reversed( leds ):
    GPIO.output( led, True )
    time.sleep( lightTime )
    GPIO.output( led, False )