import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

conv= (
0.0016,
0.0039,
0.0064,
0.0094,
0.0126,
0.0164,
0.0208,
0.0255,
0.031,
0.0373,
0.0439,
0.0501,
0.0556,
0.0601,
0.0641,
0.0673,
0.0726,
0.0776,
0.0877)

proposed = (
0.0013,
0.0028,
0.0045,
0.0063,
0.0081,
0.0102,
0.0126,
0.0151,
0.0182,
0.0218,
0.0256,
0.0293,
0.0327,
0.0353,
0.0375,
0.039,
0.0413,
0.0433,
0.0478)

f, ax1 = plt.subplots()
ax1.set_yscale('log')
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
ax1.set_ylim(-0.1,1e-1)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
#plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of superimposed data",fontname="Arial",fontsize=14)
plt.ylabel(r"Computational complexity order: Big O ",fontname="Arial",fontsize=14)
plt.show()
