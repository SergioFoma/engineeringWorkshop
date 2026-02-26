import RPi.GPIO as GPIO
import time

GPIO.setmode( GPIO.BCM )

pins = [ 16, 20, 21, 25, 26, 17, 27, 22 ]
GPIO.setup( pins, 0 )

dinamic_range = 3.3
sleep_time = 0.5

def voltage_to_number( voltage ):
    if not ( 0.0 <= voltage <= dinamic_range ):
        print(f"Напряжение выходит за динамический диапазон ЦАП( 0.00 - {dynamic_range:.2f}  B)")
        print( "устанавливаем 0.0 В")
        return 0
    
    return int( voltage * 255 / dinamic_range )
1
def number_to_dac(number, pins):
    string= bin(number)[2:].zfill(8)
    int_to_bin = [ int(x) for x in string ]
    time.sleep( sleep_time )
    GPIO.output( pins, int_to_bin )


try:
    while True:
        try:
            voltage = float( input("Введите напряжение в Вольтах: "))
            number = voltage_to_number( voltage )
            number_to_dac( number, pins )
        except ValueError:
            print("Вы ввели не число. Попоробуте еще раз\n")
finally:
    GPIO.output( pins, 0 )
    GPIO.cleanup()