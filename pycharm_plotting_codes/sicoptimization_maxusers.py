import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (0.5,1.5,2.5,3,3.5,4,4.5,5,6.5,7.5,8,8.5)

proposed = (5,5,4,4,3,3,3,2,2,1,1,0)
rssimcl = (5,5,5,5,5,5,5,5,5,5,5,5)

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="navy",marker="p", markersize=7, label=r'with optimization (5 UEs)')
lns2 = ax1.plot(time, rssimcl ,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'without optimization (5 UEs)')
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
ax1.set_ylim(0,6)  # most of the data
ax1.set_xlim(0.5, 10.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"energy left priority",fontname="Arial",fontsize=14)
plt.ylabel(r"max number of data decoded",fontname="Arial",fontsize=14)
plt.show()
