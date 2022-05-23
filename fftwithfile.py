import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sys

# open csv file
a=pd.read_csv(sys.argv[1],index_col=0)

# make each column each list
time=a['time'].values.tolist()
data=a['data'].values.tolist()


# make each column lists NumPy arrays
x=np.array(time)
y=np.array(data)

fs=1/(time[-1]/len(time)) # sample rate: the number of samples of data recorded every second.
t=x
signal = y
fft = np.fft.fft(signal) / len(signal)

fft_magnitude = abs(fft)


length = len(signal)
f = np.linspace(-(fs / 2), fs / 2, length)
plt.stem(f, np.fft.fftshift(fft_magnitude))
plt.ylim(0,1)
plt.xlim(0,50e3)
plt.grid()

plt.show()
