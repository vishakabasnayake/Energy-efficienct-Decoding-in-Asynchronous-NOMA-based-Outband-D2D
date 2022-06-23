import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
conv1= (5.09E-05,
1.11E-04,
1.64E-04,
2.10E-04,
2.60E-04,
3.10E-04,
3.57E-04,
4.06E-04,
4.56E-04,
5.07E-04,
5.56E-04,
6.10E-04,
6.61E-04,
7.09E-04,
7.62E-04,
8.21E-04,
8.69E-04,
9.24E-04,
9.73E-04)

proposed1 = (8.23E-06,
1.68E-05,
2.51E-05,
3.57E-05,
4.58E-05,
5.46E-05,
6.39E-05,
7.36E-05,
8.18E-05,
9.01E-05,
9.72E-05,
1.08E-04,
1.18E-04,
1.27E-04,
1.36E-04,
1.49E-04,
1.57E-04,
1.68E-04,
1.75E-04)

proposed2 = (0.0030932621,
0.006351234,
0.0097551189,
0.0130418051,
0.016220197,
0.019469253,
0.0227568875,
0.0259209992,
0.0290255186,
0.0322297626,
0.0353881204,
0.0386547354,
0.0418952724,
0.0450823747,
0.0482760627,
0.0514581928,
0.0548610572,
0.0582940506,
0.0614797898)

f, ax1 = plt.subplots()
ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend

#lns1 = ax1.plot(time, proposed1, color="lightblue",marker="p", markersize=7, label=r'sequential T-SIC $E_{th} = 1.2 mW$  ')
lns1 = ax1.plot(time, proposed1, color="navy",marker="p", markersize=7, label=r'sequential T-SIC')
lns2 = ax1.plot(time, conv1,color="saddlebrown",marker="d", markersize=7,  label=r'conv T-SIC ' )
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
ax1.set_ylim(5e-6,2e-3)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of transmitters (K)",fontname="Arial",fontsize=14)
plt.ylabel(r"Total SIC decoding delay (sec)",fontname="Arial",fontsize=14)
plt.show()
