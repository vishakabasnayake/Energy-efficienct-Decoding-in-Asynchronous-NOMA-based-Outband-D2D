import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

converg1= (2.0000,
    4.5727,
    7.3698,
    9.4906,
   11.0527,
   12.1987,
   12.6299,
   12.6227,
   12.6269,
   12.6252,
   12.6255,
   12.6255,
   12.6255,
   12.6249,
   12.6249
)

converg2= (1.0000,
    2.1454,
    3.0751,
    3.9576,
    4.6802,
    5.2757,
    5.7357,
    6.0845,
    6.3391,
    6.5209,
    6.6490,
    6.7363,
    6.8075,
    6.8460
)

converg3= (1.0000,
    2.3615,
    3.3502,
    4.2886,
    4.9947,
    5.5533,
    5.9616,
    6.2644,
    6.4773,
    6.6242,
    6.7209,
    6.7813,
    6.8239,
    6.8460,
    6.8460)

converg4 = (1.5000,
    3.8449,
    5.4654,
    6.9694,
    8.0032,
    8.7343,
    9.1655,
    9.4076,
    9.5206,
    9.5648,
    9.5731,
    9.5633,
    9.5478,
    9.5217,
    9.5217
)

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
ax1.set_xlim(0, 16.0)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Number of iterations",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
