import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
conv1 = (1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

proposed1 = (2,3,3,3,3,4,4,4,5,6,7,8,8,9,9,10,10,11,12)
proposed2 = (2,3,3,3,3,3,4,4,4,5,5,5,5,6,7,7,9,9,11)
proposed3 = (2,3,3,3,3,3,4,4,4,4,4,5,5,5,6,6,8,8,10)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed1, color="navy", marker="p", markersize=7, label=r'sequential T-SIC $E_{th}$ = 0.5 mW ')
lns2 = ax1.plot(time, proposed2, color="blue", marker="p", markersize=7, label=r'sequential T-SIC $E_{th}$ = 0.8 mW  ')
lns2 = ax1.plot(time, proposed3, color="lightblue", marker="p", markersize=7, label=r'sequential T-SIC $E_{th}$ = 1.2mW  ')
lns3 = ax1.plot(time, conv1, color="saddlebrown", marker="d", markersize=7,  label=r'conv T-SIC ' )

lns = lns1
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
ax1.set_ylim(0,13)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of superimposed data",fontname="Arial",fontsize=14)
plt.ylabel(r"Total number of iterations",fontname="Arial",fontsize=14)
plt.show()
