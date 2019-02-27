#import processing libraries
import numpy as np
from numpy.fft import fftshift,fft,ifft,fftfreq
import pandas as pd
import scipy.signal as sgn
import scipy.stats as stats
#import visualization libraries
import matplotlib.pyplot as plt

####################READ SIGNAL
df = pd.read_csv("signal1.dat",delim_whitespace=True,header=None)
independent_array = df[0]
dependent_array = df[2]

####################PROCESS SIGNAL

#determine step size in independent variable
step = (independent_array[1]-independent_array[0])

#do fast fourier transform
D_array = fftshift(fft(fftshift(dependent_array)))
####get freq domain
fftx = fftshift(fftfreq(len(dependent_array),step))

#how to calculate the spectrogram array
f,t,spec_array = sgn.spectrogram(dependent_array,fs=step)

#fit a pdf to the data
epdf = stats.norm(*stats.norm.fit(dependent_array))
####get pdf domain
dpdf = np.linspace(epdf.ppf(.00001),epdf.ppf(.99999),100)

####################VISUALIZE
#Plot raw signal
plt.figure(figsize=(16,9),dpi=200)
plt.plot(independent_array,dependent_array,'k-',zorder=1,label="Signal")
plt.plot([min(independent_array),max(independent_array)],[0,0],'k--',alpha=.7,zorder=0,label="Zero Line")
plt.title("Raw Signal")
plt.xlabel("Independent Variable")
plt.ylabel("Dependent Variable")
plt.legend(framealpha=.7,loc=2)
plt.gcf().savefig("raw_signal.png")

#plot power spectrum
plt.figure(figsize=(16,9),dpi=200)
plt.plot(fftx,abs(D_array)**2,'k-',zorder=1)
plt.title("Power Spectrum")
plt.xlabel("Spectral Power")
plt.ylabel("Frequency")
plt.gcf().savefig("raw_spectrum.png")

#plot spectrogram (note this function just calls the scipy module used above internally)
plt.figure(figsize=(16,9),dpi=200)
plt.specgram(dependent_array,Fs=step)
plt.title("Spectrogram")
plt.gcf().savefig("spectrogram.png")

#histogram of independent_array signal with PDF
plt.figure(figsize=(16,9),dpi=200)
plt.hist(dependent_array, normed=True, bins=50)
plt.plot(dpdf,epdf.pdf(dpdf),color="black")
plt.annotate("mean = %.1f\nstd = %.1f\nskewness = %.1f"%(epdf.mean(),epdf.std(),epdf.moment(3)),xy=(0.82,0.85),xycoords="axes fraction",bbox=dict(boxstyle="round", fc="w"))
plt.gcf().savefig("signal_pdf.png")

#display figures
plt.show()
