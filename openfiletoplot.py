import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt


a=pd.read_csv(sys.argv[1])


# time=a[0].values.tolist()
# data=a[1].values.tolist()



a.plot(x='time',y='data')
plt.show()

#
time=a['time'].values.tolist()
data=a['data'].values.tolist()
#
#
#
# x=np.array(time)
# y=np.array(data)
#
# fs=1/(time[-1]/len(time)) # sample rate
# t=x
# signal = y
# fft = np.fft.fft(signal) / len(signal)
#
# fft_magnitude = abs(fft)
#
#
# length = len(signal)
# f = np.linspace(-(fs / 2), fs / 2, length)
# plt.stem(f, np.fft.fftshift(fft_magnitude))
# plt.ylim(0,20)
# plt.grid()
#
# plt.show()
