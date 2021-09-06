import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import auditok
import pandas as pd


spf = wave.open('Voice_record.wav', "r")
voice = pd.read_csv('Voice_activity.csv', index_col=0)



# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")
signal = signal/max(signal)

#voice = np.resize(voice,(1, len(signal)))


# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(np.arange(len(signal))/ 16000,signal,zorder =1)
plt.plot(np.arange(len(voice))*480/ 16000,voice,zorder =2)

plt.show()




