#Defines a class Audio_Handler that handles signals as
# record an audio, read an audio from the computer
#and write a array as an audio format

import sounddevice 
from scipy.io.wavfile import write as scipy_write
import librosa

import numpy as np
import matplotlib.pyplot as plt



class Audio_Handler:

    def __init__(self, sampling_frequency: int, record_duration: int):
        self.sampling_frequency = sampling_frequency           #hertz
        self.record_duration = record_duration                #seconds

    def record(self) -> list :
        '''Using sounddevice rec method, record an audio with
        duration in seconds from the variable record_duration and 
        sampling frequency from the variable sampling_frequency'''
        print('3,2,1 Recording audio!')
        self.recording = sounddevice.rec(int(self.record_duration * self.sampling_frequency),
				samplerate=self.sampling_frequency, channels=2)
        sounddevice.wait()
        print('End recording')
        return self.recording

    def write(self, audio_filename: str ) -> None :
        '''Uses scipy to write a array as an audio and save the file'''
        print('Writing audio to ', audio_filename)
        scipy_write(audio_filename, self.sampling_frequency, self.recording)

    def read(self, audio_filename : str) -> list:
        '''Read an audio file as a array and return it'''
        print('Reading ', audio_filename, ' ... ')
        audio_data, sr = librosa.load(audio_filename)
        return [sr, audio_data]



