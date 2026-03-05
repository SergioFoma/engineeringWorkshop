import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False ):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11 ]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0 )
        GPIO.setup( self.comp_gpio, GPIO.IN )

    def deinit(self):
        GPIO.output(self.gpio_bits, 0 )
        GPIO.cleanup()

    def number_ro_dac( self, number ):
        string = bin(number)[2:].zfill(8)
        bits = [ int(x) for x in string ]
        GPIO.output( self.bits_gpio, bits )
    
    def sequential_counting_adc( self ):
        for value in range( 256 ):
            self.number_ro_dac( value )
            time.sleep( 0.01 )
            comparator_value = GPIO.input( self.comparator_pin )
            if comparator_value == 1:
                return value
        return 255
    def get_sc_voltage( self ):
        digital_value = self.sequential_counting_adc()
        max_digital_value = 2**len(self.bits_gpio) - 1
        voltage = ( digital_value / max_digital_value ) * 3.3

        return voltage




if __name__ == "__main__":
    adc = R2R_ADC( 3.3 )

    try:
        while True:
            voltage = adc.get_sc_voltage()
            print( "voltage: ", voltage, " B")
            time.sleep( 0.1 )
    finally:
        adc.deinit()