import numpy as np
import time

def get_sin_wave_amplitude( freq, time ):
    first = np.sin( 2 * np.pi * freq * time )
    second = first + 1
    third = second / 2

    return third


def wait_for_sampling_period( sampling_frequency ):
    time.sleep( 1 / sampling_frequency )


