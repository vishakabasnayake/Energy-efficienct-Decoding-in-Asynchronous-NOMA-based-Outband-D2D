import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

conv1= (14.9172351991285,
11.3478347059128,
9.15400738529980,
7.67167770203235,
6.60390513088856,
5.79847705898559,
5.16945233831367,
4.66468249776597,
4.25070752988302,
3.90508050694700,
3.61218471516772,
3.36082126193513,
3.14275103298148,
2.95177802127491,
2.78315329693414,
2.63317603496678,
2.49891959169003,
2.37803919058227,
2.26863420284123)

proposed1 = (14.9172351991285,
14.9172351991285,
13.7499438557905,
12.6249344262444,
11.6556343835349,
10.8319305836033,
10.1283507730902,
9.52166925284191,
8.99330075186768,
8.52879998928745,
8.11695844853108,
7.74901402172834,
7.41804449099229,
7.11851907393784,
6.84596939698607,
6.59674720755046,
6.36784445420309,
6.15675829725003,
5.96138872090470)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="navy",marker="p", markersize=7, label=r'sequential T-SIC')
lns2 = ax1.plot(time, conv,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC')
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
ax1.set_ylim(0.1,20)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of superimposed data",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
