import RPi.GPIO as GPIO
import time
import smbus

sleep_time = 0.5

class MCP4725:
    def __init__( self, dynamic_range, address = 0x61, verbose = True ):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()
    
    def set_number( self, number ):
        if not isinstance( number, int ):
            print("На вход можно подвать тольо целые числа")
        if not (0<=number<=4095):
            print("Число за разрядность")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data( 0x61, first_byte, second_byte )

        if self.verbose:
            print(f"Число: {number}, отправленнные по I2C данные: [0x{(self.address<<1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range ):
            print("Лимит напряжения")
        else:
            self.set_number( int(voltage / self.dynamic_range * 4095))

if __name__ == "__main__":
    dac = MCP4725(5)

    try:
        while True:
            voltage = float( input("Enter number: "))
            dac.set_voltage(voltage)
    finally:
        dac.deinit()