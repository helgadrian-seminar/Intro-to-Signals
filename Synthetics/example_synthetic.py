#import processing libraries
import numpy as np
import scipy.signal as sgn
#import visualization libraries
import matplotlib.pyplot as plt

#Set Synthetic parameters
size = 1000
d = np.arange(0,size)
s1p = 100
np.random.seed(666)

#Generate Source Signature/s
source1 = np.sin(2*np.pi*(d/s1p))
source2 = np.random.uniform(0,1,size=size)
source3 = np.exp((-d%200)/50)/(np.e**4)

#Combine sources or apply filter/s to source signal
data = sgn.convolve(sgn.convolve(source1,source2),source3)
data = data/max(abs(data))

import scipy.stats as stats
#fit a pdf to the data
epdf = stats.norm(*stats.norm.fit(data))
####get pdf domain
dpdf = np.linspace(epdf.ppf(.01),epdf.ppf(.99),100)

#Visualize
plt.figure(figsize=(16,9),dpi=200)
plt.subplot(221)
plt.plot(source1)#, normed=True, bins=50)
plt.subplot(222)
plt.plot(source2)#, normed=True, bins=50)
plt.subplot(223)
plt.plot(source3)#, normed=True, bins=50)
plt.subplot(224)
plt.plot(data)#, normed=True, bins=50)
plt.gcf().savefig("central_limit_signals.png")

plt.figure(figsize=(16,9),dpi=200)
plt.subplot(221)
plt.hist(source1, normed=True, bins=100)
plt.subplot(222)
plt.hist(source2, normed=True, bins=100)
plt.subplot(223)
plt.hist(source3, normed=True, bins=100)
plt.subplot(224)
plt.hist(data, normed=True, bins=100)
plt.plot(dpdf,epdf.pdf(dpdf),color="black")
plt.annotate("mean = %.4f\nstd = %.4f\nskewness = %.4f"%(epdf.mean(),epdf.std(),epdf.moment(3)),xy=(0.97,0.95),xycoords="axes fraction",bbox=dict(boxstyle="round", fc="w"),ha='right',va='top')
plt.gcf().savefig("central_limit_pdfs.png")

plt.show()
