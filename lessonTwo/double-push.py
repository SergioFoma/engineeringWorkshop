import RPi.GPIO as GPIO 
import time 

def dec2bin( value ):
    return [int(element) for element in bin(value)[2:].zfill( 8 )]
def printArray( leds, lightTime ):
    for led in leds:
        GPIO.output( led, True )
    time.sleep( lightTime )
    for led in leds:
        GPIO.output( led, False )
GPIO.setmode( GPIO.BCM )

leds = [ 16, 12, 25, 17, 27, 23, 22, 24 ]
GPIO.setup( leds, 0 )

up = 9
low = 10

GPIO.setup( up, GPIO.IN )
GPIO.setup( low, GPIO.IN )
num = 0                                                   # текущее число
sleep_time = 0.2
lightTime = 0.5

while True:
    if( num < 0 or num > 7 ): num = 0

    if GPIO.input( up ):
        num += 1
        print(num, dec2bin(num))
        time.sleep( sleep_time )
        GPIO.output( leds, dec2bin(num))
    elif GPIO.input( low ):
        printArray( leds, lightTime )


