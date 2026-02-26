import numpy as np
import time

def get_sin_wave_amplitude( freq, time ):
    first = np.arcsin( np.sin( 2 * np.pi * freq * time ) )

    return first / 2


def wait_for_sampling_period( sampling_frequency ):
    time.sleep( 1 / sampling_frequency )


