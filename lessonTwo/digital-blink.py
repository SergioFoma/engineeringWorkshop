import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )                # Обращение к GPIO пинам( пина входа / выхода )
led = 26                                # GPIO - пин
GPIO.setup( led, GPIO.OUT )             # настраиваем пин на выход
state = False                           # состояние светододиода
period = 1                              # период мегания


GPIO.output( led, state )
