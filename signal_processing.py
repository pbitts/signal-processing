#Define class Signal_Processing that handles techniques to
#analyze and process signals

import numpy as np


class Signal_Processing:

    def __init__(self, start_time : int, end_time : int, dt: float):
        '''start_time in seconds (int)
        end_time in seconds       (int)
        dt in seconds             (float)
        initialize a time array '''

        self.dt = dt
        self.time = np.arange(start_time, end_time, dt)


    def fourier_transform (self, signal, length, f_ratio):
        '''This function does a DFT receiving as parameters a signal
        to be transformed, the lenght to be applied the DFT e the f_ratio 
        (frequency ratio) for better analysis. returns the fft itself,
        the Power density Spectrum and frequencies array. '''

        fft = np.fft.fft(signal, length)
        power_density_spectrum = fft * np.conj(fft) / length
        frequencies =   np.arange(length)
        num_freq_bins = int(len(frequencies) * f_ratio)
        return fft, power_density_spectrum[:num_freq_bins], frequencies[:num_freq_bins]

