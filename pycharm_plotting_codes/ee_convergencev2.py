import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)

converg1= (2,
9,
11,
12.7,
12.7,
12.7,
12.62493443,
12.62493443,
12.62493443,
12.62493443,
12.62493443,
12.62493443,
12.62493443,
12.62493443)

converg2= (1,
2.3333,
3,
3.6,
3.8,
4.2,
4.4,
4.82,
5.2467,
5.6734,
6.1,
6.1269,
6.1336,
6.1336)

converg3= (1,
3,
4.5,
5.0,
5.4,
5.8,
6.2,
6.5,
6.8,
6.8,
6.8,
6.8,
6.8,
6.845969397)

converg4 = (1.5,
7,
8,
9.0,
9.6,
9.6,
9.6,
9.6,
9.6,
9.6,
9.6,
9.6,
9.6,
9.521669253)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, converg1, color="black",marker=".", markersize=5, label=r'sequential T-SIC $K$=3 ')
#lns2 = ax1.plot(time, converg2, color="black",marker="x", markersize=5, label=r'sequential T-SIC $K$=10 ')
lns4 = ax1.plot(time, converg4,color="black",marker="s", markersize=3,  label=r'sequential T-SIC $K$=8' )
lns3 = ax1.plot(time, converg3,color="black",marker="x", markersize=5,  label=r'sequential T-SIC $K$=20' )
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
ax1.set_ylim(0.1,14)  # most of the data
ax1.set_xlim(0, 15.0)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Number of iterations",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
