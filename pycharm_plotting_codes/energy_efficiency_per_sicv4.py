import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
proposed1= (47.7924,
   41.4510,
   36.1510,
   31.1082,
   26.8768,
   23.3272,
   20.5003,
   18.2762,
   16.5528,
   15.2303,
   14.2295,
   13.4887,
   12.9691,
   12.6479,
   12.4675,
   12.3824,
   12.3556,
   12.3556,
   12.3556,
   12.3556,
   12.3556,
   12.3556,
   12.3556,
   12.3556,)

conv1 = (33.6519,
   30.1141,
   26.8947,
   23.7964,
   21.0084,
   18.5431,
   16.4349,
   14.6675,
   13.2057,
   12.0026,
   11.0098,
   10.1854,
    9.4993,
    8.9318,
    8.4724,
    8.1144,
    7.8523,
    7.6784,
    7.5798,
    7.5380,
    7.5361,
    7.5525,
    7.5799,
    7.6007)


conv3 = (34.8519,
30.6313,
27.2299,
23.9752,
21.1928,
18.7974,
16.8099,
15.1582,
13.7884,
12.6413,
11.6788,
10.8788,
10.2335,
9.7404,
9.3942,
9.1804,
9.074,
9.0417,
9.0493,
9.0692,
9.0692,
9.0692,
9.0692,
9.0692
)

prop3 = (34.6519,
   31.6333,
   28.7938,
   25.9005,
   23.1416,
   20.5593,
   18.2252,
   16.3286,
   14.8012,
   13.6865,
   12.9030,
   12.3783,
   11.9676,
   11.7548,
   11.6119,
   11.5247,
   11.4786,
   11.4604,
   11.4587,
   11.4585,
   11.4620,
   11.4667,
   11.4644,
   11.4761
)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed1, color="black",marker=".", markersize=5, label=r'sequential T-SIC $I_{th}$=0.5 mW ')
lns2 = ax1.plot(time, conv3,color="peru",marker=".",linestyle='dashed', markersize=5,  label=r'conv T-SIC $I_{th}$=0.5 mW' )
lns5 = ax1.plot(time, prop3, color="black",marker="x", markersize=5, label=r'sequential T-SIC $I_{th}$= 1.2 mW')
lns6= ax1.plot(time, conv1,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC $I_{th}$ = 1.2 mW')

lns = lns5
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
ax1.set_ylim(5,50)  # most of the data
ax1.set_xlim(1, 25.0)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of transmitters (K)",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
