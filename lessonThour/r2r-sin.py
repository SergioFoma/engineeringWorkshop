import RPi.GPIO as GPIO
import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = r2r.R2R_DAC( [16, 20, 21, 25, 26, 17, 27, 22], 3.183, True )
    
    while True:
        current_time = time.time()

        norm_amp = sg.get_sin_wave_amplitude( signal_frequency, current_time )

        dac.set_voltage( norm_amp * amplitude )

        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()