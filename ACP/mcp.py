import matplotlib.pyplot as plt
import time
from mcp3021_driver import MCP3021

adc = MCP3021( dynamic_range = 3.0 )

voltages = []
timestamps = []
duration = 10

try:
    start_time = time.time()

    while( time.time() - start_time) < duration:
        current_time = time.time() - start_time

        v = adc.get_voltage()
        time.sleep(1.0)
         
        voltages.append(v)
        timestamps.append(current_time)

    plt.plot(timestamps, voltages)
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid( True )
    plt.show()


    
    plt.hist( timestamps, bins = 15 )
    plt.show()
finally:
    adc.deinit()
