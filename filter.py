import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import sys



def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype = "high", analog = False)
    return b, a

def butter_lowpass(cutoff,fs, order=5):
    nyq=0.5*fs
    normal_cutoff=cutoff/nyq
    b,a=signal.butter(order,normal_cutoff,btype="low", analog=False)
    return b,a

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq=0.5*fs
    low=lowcut/nyq
    high=highcut/nyq
    b,a =signal.butter(order,[low, high],btype='band')
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_lowpass_filter(data,cutoff,fs,order=5):
    b,a=butter_lowpass(cutoff,fs,order=order)
    y=signal.filtfilt(b,a, data)
    return y

def butter_bandpass_filter(data,lowcut, highcut, fs, order=5):
    b,a=butter_bandpass(lowcut, highcut, fs, order=order)
    y= signal.lfilter(b,a,data)
    return y


a=pd.read_csv(sys.argv[1])

time=a['time'].values.tolist()
data=a['data'].values.tolist()

x=np.array(time)
y=np.array(data)


dataset=pd.DataFrame({"data" : y}, index= x)


fs=1/((time[-1]-time[0])/(len(time)-1)) # sample rate # samples per second(Hz)

dt=1/fs #cycle

filtered_data_byhighpass = butter_highpass_filter(dataset.data, 20000, fs)
filtered_data_bylowpass=butter_lowpass_filter(dataset.data, 20000,fs)
filtered_data_bybandpass=butter_bandpass_filter(dataset.data,20000,40000,fs)


n=len(x)
fhat=np.fft.fft(y,n)
fhat_cleaned_byhighpass=np.fft.fft(filtered_data_byhighpass)
fhat_cleaned_bylowpass=np.fft.fft(filtered_data_bylowpass)
fhat_cleaned_bybandpass=np.fft.fft(filtered_data_bybandpass)



PSD=fhat*np.conj(fhat)/n
freq=(1/(dt*n)) * np.arange(n)
L=np.arange(1,np.floor(n/2),dtype='int')



PSDcleaned_byhighpass=fhat_cleaned_byhighpass*np.conj(fhat_cleaned_byhighpass)/n
PSDcleaned_bylowpass=fhat_cleaned_bylowpass*np.conj(fhat_cleaned_bylowpass)/n
PSDcleaned_bybandpass=fhat_cleaned_bybandpass*np.conj(fhat_cleaned_bybandpass)/n





fig,axe = plt.subplots(3,2)
fig.suptitle(sys.argv[1])
# plt.figure(figsize=(9,7),dpi=80)


plt.sca(axe[0,0])
axe[0,0].title.set_text('Noise')
plt.plot(x,y,color='c',LineWidth=1,label='Noisy')
plt.xlim(x[0],x[-1])
plt.legend()

plt.sca(axe[1,0])
axe[1,0].title.set_text('filtered by highpass')
plt.plot(x,filtered_data_byhighpass,color='k', LineWidth=1, label='Filtered')
plt.xlim(x[0],x[-1])
plt.legend()

plt.sca(axe[2,0])
axe[2,0].title.set_text('Noise vs highpass')
plt.plot(freq[L],PSD[L],color='c',LineWidth=2, label='Noisy')
plt.plot(freq[L],PSDcleaned_byhighpass[L],color='k', LineWidth=1.5,label='Filtered')
plt.xlim(0,50e3)
plt.legend()



plt.sca(axe[0,1])
axe[0,1].title.set_text('Noise')
plt.plot(x,y,color='c',LineWidth=1,label='Noisy')
plt.xlim(x[0],x[-1])
plt.legend()

plt.sca(axe[1,1])
axe[1,1].title.set_text('filtered by lowpass')
plt.plot(x,filtered_data_bylowpass,color='k', LineWidth=1, label='Filtered')
plt.xlim(x[0],x[-1])
plt.legend()

plt.sca(axe[2,1])
axe[2,1].title.set_text('Noise vs lowpass')
plt.plot(freq[L],PSD[L],color='c',LineWidth=2, label='Noisy')
plt.plot(freq[L],PSDcleaned_bylowpass[L],color='k', LineWidth=1.5,label='Filtered')
plt.xlim(0,50e3)
plt.legend()




# plt.sca(axe[0,2])
# axe[0,2].title.set_text('Noise')
# plt.plot(x,y,color='c',LineWidth=1,label='Noisy')
# plt.xlim(x[0],x[-1])
# plt.legend()

# plt.sca(axe[1,2])
# axe[1,2].title.set_text('filtered by bandpass')
# plt.plot(x,filtered_data_bybandpass,color='k', LineWidth=1, label='Filtered')
# plt.xlim(x[0],x[-1])
# plt.legend()

# plt.sca(axe[2,2])
# axe[2,2].title.set_text('Noise vs bandpass')
# plt.plot(freq[L],PSD[L],color='c',LineWidth=2, label='Noisy')
# plt.plot(freq[L],PSDcleaned_bybandpass[L],color='k', LineWidth=1.5,label='Filtered')
# plt.xlim(0,50e3)
# plt.legend()










plt.subplots_adjust(left=0.125, bottom=0.1,  right=0.9, top=0.9, wspace=0.2, hspace=0.6)
plt.show()
