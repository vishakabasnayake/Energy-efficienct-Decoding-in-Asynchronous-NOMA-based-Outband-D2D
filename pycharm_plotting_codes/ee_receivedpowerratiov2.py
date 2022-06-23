import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
conv1= (34.6519,
26.84,
21.8665,
18.4377,
15.9362,
14.0327,
12.5368,
11.3306,
10.3377,
9.5063,
8.8,
8.1926,
7.6648,
7.2019,
6.7927,
6.4283,
6.1018,
5.8075,
5.841)

proposed1 = ( 47.7924,
   43.8002,
   39.1860,
   35.2919,
   31.7867,
   28.7657,
   26.6518,
   24.8960,
   23.4058,
   22.1201,
   20.9961,
   19.9830,
   19.0800,
   18.2915,
   17.6251,
   17.0884,
   16.7288,
   16.4213,
   16.3506,
)


conv2=(34.6519,
28.7658,
24.3633,
20.1995,
17.139,
14.4567,
12.7165,
11.1828,
10.1837,
9.2114,
8.6664,
7.9426,
7.5534,
6.9893,
6.7006,
6.3585,
6.2982,
6.2038,
6.221)

prop2=(45.7924,
   41.2150,
   36.7521,
   32.4199,
   28.3483,
   24.6779,
   21.4829,
   18.8007,
   16.6441,
   14.9518,
   13.6480,
   12.6523,
   11.8924,
   11.3076,
   10.8549,
   10.4960,
   10.2176,
    9.9665,
    9.7955)

conv3 = (34.6519,
   28.0677,
   23.6094,
   19.4341,
   16.5526,
   14.3944,
   12.9377,
   11.8237,
   10.9200,
   10.0819,
    9.2739,
    8.5077,
    7.8390,
    7.2738,
    6.8909,
    6.6819,
    6.7315,
    6.8363,
    6.8464)

prop3 = (43.7924,
   38.7125,
   33.6635,
   28.9108,
   24.7056,
   20.8858,
   17.8962,
   15.5923,
   13.8556,
   12.5444,
   11.5482,
   10.7806,
   10.1856,
    9.7262,
    9.3806,
    9.1254,
    8.9524,
    8.8097,
    8.7500
)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns5 = ax1.plot(time, prop3, color="black",marker="d", markersize=3, label=r'sequential T-SIC received ratio = 2')
lns6= ax1.plot(time, conv1,color="peru",marker="d",linestyle='dashed', markersize=3,  label=r'conv T-SIC received ratio = 2')
lns7 = ax1.plot(time, prop2, color="black",marker="x", markersize=5, label=r'sequential T-SIC received ratio = 5')
lns8= ax1.plot(time, conv1,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC received ratio = 5')
lns1 = ax1.plot(time, proposed1, color="black",marker=".", markersize=4, label=r'sequential T-SIC received ratio = 10')
lns2 = ax1.plot(time, conv1,color="peru",marker=".",linestyle='dashed', markersize=5,  label=r'conv T-SIC received ratio = 10' )

lns = lns1
      #+lns2
labs = [l.get_label() for l in lns]

ax1.legend(loc=2, fontsize=10)

font = font_manager.FontProperties(family='Arial', style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_xticks(time)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
ax1.set_ylim(0.1,50)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of transmitters (K)",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
