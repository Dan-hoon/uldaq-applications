# uldaq-applications

These are Python applications based on Measurement Computing(mccdaq.com)'s USB 1808x, a data acquisition product.
USB 1808x is usually used in acquiring vibration data from a surface of a things such as pipes underground.

I built several apps to automate the tasks of recording, refining, and processing data using the Python library provided by Measurement Computing(https://www.mccdaq.com/PDFs/Manuals/UL-Linux/python/index.html)


<br>**daqtofile.py**<br>
input: data acquired by USB1808<br>
output: csv file<br>
<br>

<br>**openfiletoplot.py**<br>
input: csv file (ex: openfiletoplotexinput.csv)<br>
output: time-series graph<br>
<br>

<br>**fftwithfile.py**<br>
input: csv file (ex: optf10000s20000.csv)<br>
output: fourier transformed graph<br>
<br>

<br>**filter.py**<br>
input: csv file (ex: exinputforfilter.csv)<br>
output: Graph showing only the frequency of a particular interval upto the filter used among highpass, lowpass, and bandpass.
<br>

