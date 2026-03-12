import time
import RPi.GPIO as GPIO
from r2r_adc import R2R_ADC
import adc_plot

compare_time = 0.0001
duration = 3.0
V_REF = 3.3

adc = R2R_ADC( dynamic_range = V_REF , compare_time = compare_time )
voltage_values = []
time_values = []

try:
    start_time = time.time()

    while (time.time() - start_time) < duration:
        current_time = time.time() - start_time
        voltage = adc.get_sar_voltage()

        voltage_values.append(voltage)
        time_values.append(current_time)

    adc_plot.plot_voltage_as_time(time_values, voltage_values, V_REF )
    adc_plot.plot_sampling_period_hist(time_values)
finally:
    adc.deinit()