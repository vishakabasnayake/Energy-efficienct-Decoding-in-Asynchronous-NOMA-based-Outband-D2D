import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7.5,8,8.5,10,12)
conv = (14.0156,
   14.0156,
   14.0156,
   14.0156,
   14.0156,
   14.0156,
   13.7198,
   13.4240,
   13.1283,
   12.8325,
   12.5368,
   10.7416,
    8.9464,
    7.1512,
    5.3560,
    3.5609,
    3.5609,
    3.5609)
proposed = (70.1042,
   69.1042,
   68.1042,
   67.1042,
   65.1042,
   60.1042,
   59.2527,
   50.4012,
   41.5496,
   32.6981,
   23.8466,
   19.9630,
   16.0795,
   12.1959,
    8.3124,
    4.4288,
    4.4288,
    4.4288)


f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="navy",marker="p", markersize=7, label=r'sequential T-SIC')
lns2 = ax1.plot(time, conv ,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC')
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
ax1.set_ylim(-0.1,80)  # most of the data
ax1.set_xlim(0.0, 12.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
#plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total interference in SIC triangle",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
