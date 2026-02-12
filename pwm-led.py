import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

led = 26
status = False 
GPIO.setup( led, GPIO.OUT )

pwm =  GPIO.PWM( led, 200 )             # Создаем шину - устройство упаравления нагрузкой
duty = 0
pwm.start( duty )

timeSleep = 0.05

while True:
    pwm.ChangeDutyCycle( duty )         # управляем яркостью
    time.sleep( timeSleep )

    duty += 1
    if duty > 100:
        duty = 0 