import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

button = 13                     # Abalog led
led = 26                        # светодиод
state = False
timeSleep = 1

GPIO.setup( button, GPIO.IN )
GPIO.setup( led, GPIO.OUT )

while True:
    if GPIO.input( button ):    # если есть контакт
        state = not state
        GPIO.output( led, state )
        time.sleep( timeSleep )