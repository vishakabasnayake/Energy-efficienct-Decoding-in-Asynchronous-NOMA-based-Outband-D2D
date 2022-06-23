import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

proposed = (23.008014,23.008014,22.321487,19.153153,15.730591,14.716412,14.045253,14.007566,14.020746,14.125912,14.206253,14.467701,14.289124,13.983178,13.134173,13.190436,12.998766,12.73296,12.49495)
rssimcl = (8.940862,8.880681,8.058778,8.142592,7.495821,7.348906,7.326544,7.439712,7.282808,7.455035,7.446427,7.265158,7.265158,6.999402,7.442893,7.420541,7.761878,7.686163,6.526735)

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="navy",marker="p", markersize=7, label=r'with optimization')
lns2 = ax1.plot(time, rssimcl ,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'without optimization')
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
ax1.set_ylim(-0.1,30)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of superimposed data",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
