#Record an audio, calculates its DFT and plot both.
from audio_handler import Audio_Handler
from signal_processing import Signal_Processing
import matplotlib.pyplot as plt
import numpy as np

audio_filename = "audio_file.wav"
sampling_frequency = 44100
recording_duration = 2

#Recording audio and writing it to an audio file
audio = Audio_Handler(sampling_frequency, recording_duration)
audio_recorded = audio.record()
audio.write(audio_filename)


#Reading recorded audio
audio_data = audio.read(audio_filename)

#Processing DFT
signal = Signal_Processing(0,2,0.1)
fft, psd, freq = signal.fourier_transform(audio_data[1], audio_data[0], 0.1)


#Plotting results
fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot( np.linspace ( 0,recording_duration, len(audio_data[1])),  audio_data[1] )
ax1.set_title("Audio")

ax2 = fig.add_subplot(212)
ax2.plot(freq,psd)
ax2.set_title("DFT")


fig.tight_layout()

plt.show()
