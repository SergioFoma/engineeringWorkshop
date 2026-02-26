import RPi.GPIO as GPIO
import time

sleep_time = 0.5

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False ):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0 )
    def set_number( self, number ):
        string = bin(number)[2:].zfill(8)
        bits = [ int(x) for x in string]
        GPIO.output( self.gpio_bits, bits )
    def set_voltage( self, voltage ):
        number = int( voltage * 255 / self.dynamic_range )
        self.set_number( number )
        
    def deinit(self):
        GPIO.output(self.gpio_bits, 0 )
        GPIO.cleanup()

if __name__ == "__main__":
    dac = R2R_DAC( [16, 20, 21, 25, 26, 17, 27, 22], 3.183, True )

    try:

        while True:
            try:
                voltage = float( input("Введите напржение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print( "Вы ввели не число. Попробуте еще раз\n")

    finally:
        dac.deinit()