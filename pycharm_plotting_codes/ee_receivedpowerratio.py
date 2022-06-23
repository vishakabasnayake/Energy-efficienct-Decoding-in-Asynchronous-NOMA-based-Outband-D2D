import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (0,
1.111111111,
2.222222222,
3.333333333,
4.444444444,
5.555555556,
6.666666667,
7.777777778,
8.888888889,
10)

conv= (
7.157,
9.88E+00,
1.87E+01,
7.18E+00,
1.11E+01,
1.27E+01,
1.11E+01,
1.63E+01,
7.16E+00,
7.16E+00)

proposed = (
8.015,
14.9455,
23.99,
16.678,
12.7312,
18.8281,
16.3692,
16.8939,
8.015,
8.015)


f, ax1 = plt.subplots()
ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#strongest user
lns1 = ax1.plot(time, proposed, color="black",marker=".", markersize=5, label=r'sequential T-SIC (nearest user)')
lns2 = ax1.plot(time, conv,color="black",marker=".",linestyle='dashed', markersize=5,  label=r'conv T-SIC (nearest user)')

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
ax1.set_ylim(-0.0,25)  # most of the data
ax1.set_xlim(-0.2, 10.2)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(0.2,0.25e-3,'number of transmitters: 10',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"received power ratio",fontname="Arial",fontsize=14)
plt.ylabel(r"bit error rate (BER)",fontname="Arial",fontsize=14)
plt.show()
