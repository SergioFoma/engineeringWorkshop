import RPi.GPIO as GPIO
import r2r_dac as r2r
import signal_generator as sg
import mcp4725_driver as mcp
import time

amplitude = 2
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(5)
    
    start_time = time.time()

    while True:
        current_time = time.time() - start_time

        norm_amp = sg.get_sin_wave_amplitude( signal_frequency, current_time )

        dac.set_voltage( norm_amp * amplitude )

        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()